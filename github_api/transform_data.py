from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql import functions as F
from pyspark.sql.types import StructField, StructType, IntegerType, \
    StringType, BooleanType, ArrayType
from extract_data import creds

# build spark app alocating 1 gb of ram memory
spark_conf = SparkConf()
spark_conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.2')
spark_conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
spark_conf.set("fs.s3a.endpoint", "s3.amazonaws.com")
spark_conf.set('spark.hadoop.fs.s3a.access.key', creds['aws_access_key_id'])
spark_conf.set('spark.hadoop.fs.s3a.secret.key', creds['aws_secret_access_key'])
spark_conf.set("spark.hadoop.fs.s3a.endpoint", "s3.us-east-1.amazonaws.com")
spark_conf.set('spark.executor.memory', '1g')
spark_context = SparkSession.builder.config(conf=spark_conf).getOrCreate()

# schema for events
schema = StructType([
    StructField('id', StringType(), True),
    StructField('type', StringType(), True),
    StructField('actor', StructType([
        StructField('id', IntegerType(), True),
        StructField('login', StringType(), True),
        StructField('display_login', StringType(), True),
        StructField('gravatar_id', StringType(), True),
        StructField('url', StringType(), True),
        StructField('avatar_url', StringType(), True)
    ])),
    StructField('repo', StructType([
        StructField('id', IntegerType(), True),
        StructField('name', StringType(), True),
        StructField('url', StringType(), True)
    ])),
    StructField('payload', StringType(), True),
    StructField('public', BooleanType(), True),
    StructField('created_at', StringType(), True)
])

class TransformData():
    def __init__(self, json_data, date_start, date_end) -> None:
        """define args"""
        self.json_data = json_data
        self.spark_context = spark_context
        self.date_start = date_start
        self.date_end = date_end
        self.date_col = "created_at"
        pass

    def create_spark_df(self):
        """build pyspark dataframe from json infering schema"""
        return self.spark_context.createDataFrame(
            data=self.json_data, schema=schema)
    
    def filter_created_at(self):
        """use start and end dates to filter dataframe between them"""
        df = self.create_spark_df()
        df = df.filter(df[self.date_col].between(
            self.date_start, self.date_end))
        return df
    
    def build_schema(self, df, df_column):
        """if a column has dictionary as string, 
        this function infer its schema"""
        json_schema = self.spark_context.read.json(
            df.rdd.map(lambda row: row[df_column])).schema
        return json_schema
    
    def spark_flatten(self, df):
        """detect Array or Struct column types, 
        unnested it in another columns"""

        # compute Complex Fields (Lists and Structs) in Schema
        complex_fields = dict([(field.name, field.dataType)
                            for field in df.schema.fields
                            if type(field.dataType) == ArrayType or 
                            type(field.dataType) == StructType])

        while len(complex_fields) != 0:
            col_name = list(complex_fields.keys())[0]

            # if StructType then convert all sub element to columns.
            # i.e. flatten structs
            if (type(complex_fields[col_name]) == StructType):
                expanded = [
                    F.col(col_name + '.' + k).alias(col_name + '_' + k)
                        for k in [n.name for n in complex_fields[col_name]]
                ]
                df = df.select("*", *expanded).drop(col_name)

            # if ArrayType then add the Array Elements as Rows using the explode function
            # i.e. explode Arrays
            elif (type(complex_fields[col_name]) == ArrayType):
                df = df.withColumn(col_name, F.explode_outer(col_name))

            # recompute remaining Complex Fields in Schema
            complex_fields = dict([(field.name, field.dataType)
                                for field in df.schema.fields
                                if type(field.dataType) == ArrayType 
                                or type(field.dataType) == StructType])
        return df
