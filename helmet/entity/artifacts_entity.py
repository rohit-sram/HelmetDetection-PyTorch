from dataclasses import dataclass

@dataclass 
class DataIngestionArtifacts():
    # train_file_path, test_file_path, valid_file_path
    train_path: str
    test_path: str 
    valid_path: str