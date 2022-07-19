import logging
from src.utils import save_json
import time
from src import logger
from src.constants import *
from src.components import StageClass


STAGE = "Stage name" ## <<< change stage name 

# init logger
logger()



def main():
    obj = StageClass()


if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e