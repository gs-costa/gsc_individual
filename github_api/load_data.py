import json

protocol_lake = "s3a"
bucket_path = "linker-datalake"

class LoadData():
    def __init__(self, spark_df, bq_schema=None, bq_table=None) -> None:
        self.spark_df = spark_df
        self.bq_table = bq_table
        self.bq_schema = bq_schema
        pass

    def upload_bq(self):
        self.spark_df.write.format('bigquery') \
        .option('table', 'wordcount_dataset.wordcount_output') \
        .save()
        return f"Saved table in {self.bq_schema}.{self.bq_table}"
    
    def upload_s3(self, dest_path, partitions=[], mode="overwrite"):
        self.spark_df.write.parquet(
        path=dest_path,
        mode=mode,
        partitionBy=partitions
        )

    
    def write_csv(self, folder):
        dest_path = "./github/" + folder
        self.spark_df.write.options(header=True, delimiter=',')\
            .csv(dest_path, mode='overwrite')
        print(f"csv salvo em {dest_path}")
    
    def save_json(self, folder, json_object):
        dest_path = f"./github/raw/{folder}.json"
        with open(dest_path, 'w') as outfile:
            outfile.write(json.dumps(json_object, indent=4))
        print(f"json salvo em {dest_path}")

