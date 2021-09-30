# IMPORT LIBRARIES
from pathlib import Path
from google.oauth2 import service_account
import os
from google.cloud import bigquery
from google.oauth2 import service_account
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, StructType, StructField


def bq_sessions():
    my_path = Path().absolute()
    path_key_file_bq = str(my_path)+'\\File_directory_json'
    KEY_FILE_LOCATION = path_key_file_bq
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_FILE_LOCATION
    bigquery_client = bigquery.Client()
        
    return bigquery_client

