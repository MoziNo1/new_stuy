from common.log_handler import logger


class www(object):

    @staticmethod
    def add(a, b):
        try:
            res = a + b
            return res
        except Exception as e:
            logger.exception(e)
        finally:
            pass


c = www.add(1, 111111111111)
logger.info(c)
# log.error(test.add(1, "eqwe"))

