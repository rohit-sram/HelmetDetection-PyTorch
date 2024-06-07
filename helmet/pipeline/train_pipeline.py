import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from helmet.components.data_ingestion import DataIngestion
from helmet.configuration.s3_operations import S3Operation
from helmet.entity.config_entity import DataIngestionConfig
from helmet.entity.artifacts_entity import DataIngestionArtifacts
from helmet.logger import logging
from helmet.exception import HelmetException

class TrainPipeline():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.s3_operations = S3Operation()
     
    # start_data_ingestion()   
    def begin_data_ingestion(self):
        logging.info("Initiated Data Ingestion (TrainPipeline).")
        try:
            logging.info("Collecting data from the Bucket.")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
                s3_operations=S3Operation()
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Training, Test and Validation data acquired.")
            logging.info("Completed Data ingestion (TrainPipeline).")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise HelmetException(e, sys) from e
        
    def run_pipeline(self):
        logging.info("Starting the run_pipeline() function.")
        try:
            data_ingestion_artifact = self.begin_data_ingestion()
            # self.begin_data_ingestion()
            
        except Exception as e:
            raise HelmetException(e, sys) from e