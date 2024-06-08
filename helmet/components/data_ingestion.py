import os
import sys
from zipfile import ZipFile
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from helmet.exception import HelmetException
from helmet.logger import logging
from helmet.constants import *
from helmet.configuration.s3_operations import S3Operation
from helmet.entity.config_entity import DataIngestionConfig
from helmet.entity.artifacts_entity import DataIngestionArtifacts

class DataIngestion():
    def __init__(self, data_ingestion_config: DataIngestionConfig, s3_operations: S3Operation):
        self.data_ingestion_config = data_ingestion_config
        self.s3_operations = s3_operations
        
    def get_data_from_s3(self):
        try:
            logging.info("Calling get_data_from_s3() function.")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
            
            self.s3_operations.read_data_from_s3(
                self.data_ingestion_config.ZIP_FILE_NAME,
                self.data_ingestion_config.BUCKET_NAME,
                self.data_ingestion_config.ZIP_FILE_PATH
            )
            # print(
            #     self.data_ingestion_config.ZIP_FILE_NAME, "\n",
            #     self.data_ingestion_config.BUCKET_NAME, "\n",
            #     self.data_ingestion_config.ZIP_FILE_PATH
            # )
            
            logging.info("Completed Data collection.")
        
        except Exception as e:
            raise HelmetException(e, sys) from e
        
    def unzip_and_clean(self):
        logging.info("Unzipping and cleaning data file.")
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)
                
            logging.info("Completed unzipping and cleaning.")
            return (
                self.data_ingestion_config.TRAIN_DATA_ARTIFACT_DIR, 
                self.data_ingestion_config.TEST_DATA_ARTIFACT_DIR,
                self.data_ingestion_config.VALID_DATA_ARTIFACT_DIR
            )
                
        except Exception as e:
            raise HelmetException(e, sys) from e 
        
    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Called initiate_data_ingestion() function.")
        try:
            self.get_data_from_s3()
            logging.info("Collecting data from the S3 bucket.")
            
            # train_file_path, test_file_path, valid_file_path
            train_path, test_path, valid_path = self.unzip_and_clean()
            logging.info("Unzipped data. \n Data split into train, test and validation sets.")
            data_ingestion_artifact = DataIngestionArtifacts(
                train_path=train_path,
                test_path=test_path, 
                valid_path=valid_path
            )
            logging.info("initiate_data_ingestion() function completed.")
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise HelmetException(e, sys) from e