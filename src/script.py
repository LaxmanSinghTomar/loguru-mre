# Some script containing functions
import os

from custom_logger import CustomizeLogger

# Loading Logger
config_path = os.path.join(os.path.dirname(__file__), "../configs/logging_config.json")
logger = CustomizeLogger.make_logger(config_path)


@logger.catch(reraise=True)
def function(a, b):
    try:
        logger.info("Some Sample Steps 1....")
        logger.info("Some Sample Steps 2....")
        logger.info("Some Sample Steps 3....")
        division = a / b
        logger.info(f"Answer: {division}")
        return division
    except:
        logger.info("Can't divide by 0")

"""
@logger.catch(reraise=True)
def function(a, b):
    try:
        logger.info("Some Sample Steps 1....")
        logger.info("Some Sample Steps 2....")
        logger.info("Some Sample Steps 3....")
        division = a / b
        logger.info(f"Answer: {division}")
        return division
    except ZeroDivisionError:
        raise ZeroDivisionError("Not divisible by 0")
"""
"""
@logger.catch(reraise=True)
def function(a, b):
    try:
        logger.info("Some Sample Steps 1....")
        logger.info("Some Sample Steps 2....")
        logger.info("Some Sample Steps 3....")
        division = a / b
        #logger.info(f"Answer: {division}")
        return division
    except Exception as e:
        logger.info(e)
"""

"""
@logger.catch(reraise=True)
def function(a, b):
    division = a / b
    logger.info(f"Answer: {division}")
    return division
"""