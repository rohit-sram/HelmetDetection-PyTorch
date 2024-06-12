from dataclasses import dataclass

@dataclass 
class DataIngestionArtifacts():
    # train_file_path, test_file_path, valid_file_path
    train_path: str
    test_path: str 
    valid_path: str
    
@dataclass
class DataTransformationArtifacts():
    transformed_train_object: str
    transformed_test_object: str
    number_of_classes: int
    
@dataclass
class ModelTrainerArtifacts():
    trained_model_path: str