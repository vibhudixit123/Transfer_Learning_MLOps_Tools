from src.Classifier_Model.config.configuration import ConfigurationManager
from src.Classifier_Model.components.base_model import PrepareBaseModel
from src.Classifier_Model import logger

STAGE_NAME = "Base Model stage"

class PrepareBaseModelTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f"*********************")
        logger.info(f">>>>>stage{STAGE_NAME} started<<<<<<<<")
        obj = PrepareBaseModelTraningPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage{STAGE_NAME} completed <<<<<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e