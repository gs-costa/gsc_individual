import json, os

protocol_lake = "s3a"
bucket_path = "etl-pyspark-processing-talk"

class LoadData():
    def __init__(self, spark_df, bq_schema=None, bq_table=None, partitionby=None) -> None:
        """define args"""
        self.spark_df = spark_df
        self.bq_table = bq_table
        self.bq_schema = bq_schema
        self.partition_by = partitionby
        pass

    def upload_bq(self):
        """upload pyspark df to bigquery"""
        self.spark_df.write.format('bigquery') \
        .option('table', 'wordcount_dataset.wordcount_output') \
        .save()
        return f"Saved table in {self.bq_schema}.{self.bq_table}"
    
    def upload_s3(self, folder, partitions=[], mode="overwrite"):
        """upload pyspark df to S3 as parquet files"""
        dest_path = os.path.join(f"{protocol_lake}://{bucket_path}", "refined", folder) \
            .replace("\\", "/")
        print(f'{folder} will be saved in {dest_path}')
        self.spark_df.write.parquet(
        path=dest_path,
        mode=mode,
        partitionBy=partitions
        )
    
    def write_csv(self, folder):
        """write csv from pyspark df"""
        dest_path = f"./results/refined/{folder}"
        self.spark_df.coalesce(1).write.partitionBy(self.partition_by)\
            .options(header=True, delimiter=',')\
            .csv(dest_path, mode='overwrite')
        print(f"csv salvo em {dest_path}")
    
    def save_json(self, folder, json_object):
        """write json in file"""
        dest_path = f"./results/raw/{folder}.json"
        with open(dest_path, 'w') as outfile:
            outfile.write(json.dumps(json_object, indent=4))
        print(f"json salvo em {dest_path}")

