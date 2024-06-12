import os
import torch
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
# MAC_OS_EXT = os.path.join("__MACOSX", "data")
MAC_OS_EXT = os.path.join("data")

# Data Ingestion Constants
ARTIFACTS_DIR = os.path.join("artifacts")
# ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'helmet-det'
ZIP_FILE_NAME = 'data.zip'
ANNOTATIONS_COCO_JSON_FILE = "_annotations.coco.json"
# ANNOTATIONS_COCO_JSON_FILE_MACOS = ".__annotations.coco.json"

INPUT_SIZE = 416
HORIZONTAL_FLIP = 0.3
VERTICAL_FLIP = 0.3
RANDOM_BRIGHTNESS_CONTRAST = 0.1
COLOR_JITTER = 0.1
BBOX_FORMAT = 'coco'

RAW_FILE_NAME = 'helmet'

# Data ingestion constants 
DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'
DATA_INGESTION_TRAIN_DIR = 'train'
DATA_INGESTION_TEST_DIR = 'test'
DATA_INGESTION_VALID_DIR = 'valid'

# Data Transformation constants
DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
DATA_TRANSFORMATION_TRAIN_DIR = "Train"
DATA_TRANSFORMATION_TEST_DIR = "Test"
DATA_TRANSFORMATION_TRAIN_FILE_NAME = "train.pkl"
DATA_TRANSFORMATION_TEST_FILE_NAME = "test.pkl"
DATA_TRANSFORMATION_TRAIN_SPLIT = "train"
DATA_TRANSFORMATION_TEST_SPLIT = "test"

# Model Training Constants 
TRAINED_MODEL_DIR = 'TrainedModel'
TRAINED_MODEL_NAME = 'model.pt'
TRAINED_BATCH_SIZE = 2
TRAINED_SHUFFLE = False
TRAINED_NUM_WORKERS = 1
EPOCH = 1
# EPOCH = 10

has_gpu = torch.cuda.is_available()
has_mps = torch.backends.mps.is_built()
DEVICE = "mps" if has_mps else "cuda" if torch.cuda.is_available() else "cpu"

# AWS CONSTANTS
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"