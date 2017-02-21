import logging
import os


class Logger(object):
    '''
    Logger API Class
    '''
    def __init__(self):
        self.logger = logging.getLogger('amt_logger')

    def logger_api(self, message, LOG_TYPE, log_level="info"):
        '''
        logger api method. call _info_log or _error_log method to output log.
        :param message: receive log content
        :param LOG_TYPE: receive access or transaction type
        :param log_level: receive log level, default is info
        :return:
        '''

        log_path = "%s/log/%s" % (os.path.abspath('..'), LOG_TYPE)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_path)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        if log_level == "info":
            self._info_log(message)
        if log_level == "error":
            self._error_log(message)

    def _info_log(self,message):
        '''
        output info log
        :param message:
        :return:
        '''
        self.logger.info(message)

    def _error_log(self,message):
        '''
        output error log
        :param message:
        :return:
        '''
        self.logger.error(message)


