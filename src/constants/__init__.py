from src.utils import *
from pathlib import Path
from src import logger

logger()

# GLOBAL CONSTANTS
CONFIG_FILE_PATH = Path(f"configs/config.yaml")
PARAMS_FILE_PATH = "params.yaml"
ARTIFACTS_DIR_PATH = "artifacts"
METRICS_DIR_PATH = "metrics"

# YAML data
CONFIG_DATA = read_yaml(CONFIG_FILE_PATH)
PARAMS_DATA = read_yaml(PARAMS_FILE_PATH)

# CONFIG 
ARTIFACTS = CONFIG_DATA["artifacts"]

# params
TRAINING_PARAMS = PARAMS_DATA["training"]
TRAINING_BATCH_SIZE = TRAINING_PARAMS["batch_size"]
TRAINING_EPOCHS = TRAINING_PARAMS["epochs"]
TRAINING_LEARNING_RATE = TRAINING_PARAMS["learning_rate"]
TRAINING_MOMENTUM = TRAINING_PARAMS["momentum"]

# Data
SOURCE_DATA = CONFIG_DATA["source_data"]
TRAIN_DATA_URL = SOURCE_DATA["train_data_URL"]
TEST_DATA_URL = SOURCE_DATA["test_data_URL"]
DATA_DIR_PATH = Path(f"{ARTIFACTS_DIR_PATH}/data")
TRAIN_DATA_PATH = Path(f"""{DATA_DIR_PATH}/{ARTIFACTS["train_data"]}""")
TEST_DATA_PATH = Path(f"""{DATA_DIR_PATH}/{ARTIFACTS["test_data"]}""")

# Featurization
FEATURIZATION_DIR_PATH = Path(f"{ARTIFACTS_DIR_PATH}/featurization")
NORMALIZE_TRAIN_DATA_PATH = Path(f"""{FEATURIZATION_DIR_PATH}/{ARTIFACTS["norm_train_data"]}""")
NORMALIZE_TEST_DATA_PATH = Path(f"""{FEATURIZATION_DIR_PATH}/{ARTIFACTS["norm_test_data"]}""")
NORM_PARAMS_FILE_PATH = Path(f"""{FEATURIZATION_DIR_PATH}/{ARTIFACTS["norm_params"]}""")

# Training
TRAINING_DIR_PATH = Path(f"{ARTIFACTS_DIR_PATH}/training")
MODEL_PATH = Path(f"""{TRAINING_DIR_PATH}/{ARTIFACTS["model"]}""")

# Metrics
METRICS_CONFIG = CONFIG_DATA["metrics"]
TRAIN_METRICS_FILE_PATH = Path(f"""{METRICS_DIR_PATH}/{METRICS_CONFIG["train_metrics"]}""")


# Eval
EVAL_DIR_PATH = Path(f"{ARTIFACTS_DIR_PATH}/eval")
EVAL_METRICS_FILE_PATH = Path(f"""{METRICS_DIR_PATH}/{METRICS_CONFIG["eval_metrics"]}""")


# Create all directories
_LIST_OF_DIRS = [
    ARTIFACTS_DIR_PATH, 
    FEATURIZATION_DIR_PATH, 
    TRAINING_DIR_PATH,
    METRICS_DIR_PATH, 
    DATA_DIR_PATH, 
    EVAL_DIR_PATH
]
create_directories(_LIST_OF_DIRS)