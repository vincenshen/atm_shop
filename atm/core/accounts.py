from atm_shop.atm.core import db_handler

class AccData(object):
    '''
    ATM Account Data function Class
    '''
    def __init__(self):
        self.db = db_handler.DB_Handle()
        self.data = {}

    def acc_data_api(self, account_id, access_type='read'):
        '''
         account_data api method. call db.db_api method to get account_data.
        :param account_id:
        :param access_type: receive read or write
        :return:
        '''
        if account_id is None: return
        self.data['id'] = account_id
        return self.db.db_api(self.data, access_type)