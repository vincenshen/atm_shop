from atm_shop.atm.core import db_handler
from atm_shop.atm.core import logger
from atm_shop.atm.conf import settings

class TransAction(object):
    '''
    ATM Transaction function Class
    '''
    def __init__(self):
        self.logger = logger.Logger()
        self.acc_db = db_handler.DB_Handle()

    def transaction_api(self, trans_type, amount, account_data , account2_data = None):
        '''
        All Transaction function api.
        :param trans_type:
        :param amount:
        :param account_data: receive source account_data
        :param account2_data: receive destination account_data
        :return:
        '''
        if trans_type in settings.TRANSACTION_TYPE:
            interest = amount * settings.TRANSACTION_TYPE[trans_type]['interest']
            if trans_type == 'transfer':
                return self._transfer(amount, interest, account_data, account2_data)
            if trans_type == 'repay':
                return self._repay(amount, interest, account_data)
            if trans_type == 'cash':
                return self._cash(amount, interest, account_data)
        else:
            print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % trans_type)
            return

    def _transfer(self, amount, interest, account_data, account2_data):
        account_data['balance'] = account_data['balance'] - amount - interest
        account2_data['balance'] = account2_data['balance'] + amount
        self.acc_db.db_api(account_data, 'write')
        self.acc_db.db_api(account2_data, 'write')
        self.logger.logger_api( "from id %d transfer to id %d success, amount %d" %(account_data['id'],
                               account2_data['id'], amount), settings.LOG_TYPES['transaction'])
        return True

    def _repay(self, amount, interest, account_data):
        account_data['balance'] = account_data['balance'] + amount - interest
        self.acc_db.db_api(account_data, 'write')
        self.logger.logger_api("id %d repay success, amount %d" % (account_data['id'], amount), settings.LOG_TYPES['transaction'])
        return True

    def _cash(self, amount, interest, account_data, ):
        account_data['balance'] = account_data['balance'] - amount - interest
        self.acc_db.db_api(account_data, 'write')
        self.logger.logger_api("id %d cash success, amount %d" % (account_data['id'], amount), settings.LOG_TYPES['transaction'])
        return True