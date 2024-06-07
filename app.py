import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from helmet.logger import logging
from helmet.exception import HelmetException
from helmet.pipeline.train_pipeline import TrainPipeline

try:
    logging.info("Beginning Training Pipeline")
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
    print("success!!")
    # logging.info("Training pipeline completed.")
    
except Exception as e:
    raise HelmetException(e, sys)