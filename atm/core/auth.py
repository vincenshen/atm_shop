from atm_shop.atm.core import accounts
from atm_shop.atm.core import logger
from atm_shop.atm.conf import settings

class AuthAccount(object):
    '''
    ATM Authentication API Class
    '''

    def __init__(self):
        '''
        init logger.Logger Class and accounts.Account Class
        '''
        self.logger = logger.Logger()
        self.account = accounts.AccData()
        self.count = 0

    def auth_api(self, user_data):
        '''
        authentication api method. call _auth_account method to use account api.
        :param user_data: receive
        :return:
        '''

        while self.count < 3:
            self.account_id = int(input("input your account id:").strip())
            self.account_pwd = input("input your account password:").strip()
            account_data = self._auth_account(self.account_id)

            if account_data is None:
                print('Account ID non-existent')
                self.count += 1
                continue
            if (self.account_id == account_data['id']) and (self.account_pwd == account_data['password']):
                user_data['account_id'] = self.account_id
                user_data['is_authenticated'] = True
                user_data['account_data'] = account_data
                self.logger.logger_api("id %s - authentication success" %self.account_id, settings.LOG_TYPES['access'])
                return
            else:
                self.logger.logger_api("id %s - authentication failure" %self.account_id, settings.LOG_TYPES['access'],
                                       settings.LOG_TYPES['log_level'])
                self.count += 1
        else:
            print("account [%s] too many login attempts" % self.account_id)
            exit()

    def _auth_account(self, account_id):
        '''
        call account api method to return account_data.
        :param account_id:
        :return:
        '''
        return self.account.acc_data_api(account_id)