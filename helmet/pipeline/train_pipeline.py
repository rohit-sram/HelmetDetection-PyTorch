import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from helmet.components.data_ingestion import DataIngestion
from helmet.components.data_transformation import DataTransformation
from helmet.configuration.s3_operations import S3Operation
from helmet.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from helmet.entity.artifacts_entity import DataIngestionArtifacts, DataTransformationArtifacts
from helmet.logger import logging
from helmet.exception import HelmetException

class TrainPipeline():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
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
    
    # start_data_transformation
    def begin_data_transformation(self, data_ingestion_artifact: DataIngestionArtifacts) -> DataIngestionArtifacts:
        logging.info("Initiated Data Transformation (TrainPipeline).")
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=self.data_transformation_config
            )
            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )
            logging.info("Completed Data Transformation (TrainPipeline).")
            
            return data_transformation_artifact
            
        except Exception as e:
            raise HelmetException(e, sys)
        
    def run_pipeline(self):
        logging.info("Starting the run_pipeline() function.")
        try:
            data_ingestion_artifact = self.begin_data_ingestion()
            data_transformation_artifact = self.begin_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact
            )
            logging.info("Pipeline run completed.")
            
        except Exception as e:
            raise HelmetException(e, sys) from e