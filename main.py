from src.Classifier_Model import logger
from src.Classifier_Model.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Classifier_Model.pipeline.base_model_pipeline import PrepareBaseModelTraningPipeline
from src.Classifier_Model.pipeline.training_model_pipeline import PrepareTrainingModelPipeline
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Base Model stage"
try:
    
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<<<<")        
    prepare_base_model = PrepareBaseModelTraningPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>stage{STAGE_NAME} completed <<<<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Model stage"
try:
        logger.info(f"*********************")
        logger.info(f">>>>>stage{STAGE_NAME} started<<<<<<<<")
        obj = PrepareTrainingModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage{STAGE_NAME} completed <<<<<<<<<<\n\nx=============x")
except Exception as e:
        logger.exception(e)
        raise e


