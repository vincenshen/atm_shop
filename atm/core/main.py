from atm_shop.atm.core import accounts
from atm_shop.atm.core import auth
from atm_shop.atm.core import transaction
from atm_shop.atm.conf import settings
from prettytable import PrettyTable
from colorama import init, Fore

init()

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

def auth_decorator(func):
    '''
    authentication decorator
    :param func: receive Class
    :return: Class AuthClass
    '''
    class AuthClass(object):
        '''
        add authentication function use auth api
        '''
        def __init__(self, *args, **kwargs):
            self.auth = auth.AuthAccount()
            self.func = func(*args, **kwargs)
            if user_data['is_authenticated'] == False:
                self.auth.auth_api(user_data)
        def __getattr__(self, item):
            return getattr(self.func, item)
    return AuthClass

@auth_decorator
class ATM(object):
    '''
    ATM major function Class
    '''
    def __init__(self):
        '''
        init accounts.Account Class and transaction.TransAction Class
        '''

        self.accounts = accounts.AccData()
        self.transaction = transaction.TransAction()
        self.user_data = user_data

    def query(self):
        '''
        def query user account information method, call accounts api method to implement.
        :return:
        '''
        self.user_data['account_data'] = self.accounts.acc_data_api(user_data['account_id'])
        x = PrettyTable()
        x.field_names = [Fore.GREEN + i + Fore.RESET for i in self.user_data['account_data'].keys()]
        x.add_row([Fore.RED + str(i) + Fore.RESET for i in self.user_data['account_data'].values()])
        print(x)

    def transfer(self):
        '''
        def transfer method, call transaction api method to implement.
        :return:
        '''

        dest_user_id = input("input transfer destination account id:").strip()
        trans_amount = input("input transfer amount:").strip()
        if (dest_user_id.isdigit() and trans_amount.isdigit()):
            dest_user_id = int(dest_user_id)
            trans_amount = float(trans_amount)
        else:
            return

        dest_account_data = self.accounts.acc_data_api(dest_user_id)
        if dest_account_data is None:
            print("\033[31;1mDestination account id non-existent\033[0m")
            return

        if trans_amount >= self.user_data['account_data']['balance']:
            print("\033[31;1mtransfer to %d failure, Balance is insufficient\033[0m" %self.user_data['account_id'])
            return

        if self.transaction.transaction_api('transfer',trans_amount,self.user_data['account_data'], dest_account_data):
            print("\033[31;1mTransfer success, balance is %d\033[0m" % self.user_data['account_data']['balance'])

    def repay(self):
        '''
        def repay method, call transaction api method to implement.
        :return:
        '''

        repay_amount = input("Input repay amount:").strip()
        if repay_amount.isdigit() and len(repay_amount) >0:
            repay_amount = float(repay_amount)
        else:
            return

        if self.transaction.transaction_api('repay',  repay_amount, self.user_data['account_data']):
            print("\033[31;1mRepay Success, balance is %d !\033[0m" % self.user_data['account_data']['balance'])

    def cash(self):
        '''
        def cash method, call transaction api method to implement.
        :return:
        '''

        cash_amount = input("Input cash amount:").strip()
        if cash_amount.isdigit() and len(cash_amount) >0:
            repay_amount = float(cash_amount)
        else:
            return
        interest = cash_amount * settings.TRANSACTION_TYPE['cash']['interest']
        if (cash_amount+interest) >= self.user_data['account_data']['balance']:
            print("\033[31;1mYou balance is insufficient!\033[0m")

        if self.transaction.transaction_api('cash', cash_amount, self.user_data['account_data']):
            print("\033[31;1mCash Success, balance is %d\033[0m" % self.user_data['account_data']['balance'])

    def record(self):
        pass

def run():
    print("---  init account:1234, password:abc  ---")
    atm_func = ATM()
    menu = """
    -----------------------------
        欢迎登录宇宙无敌银行
        1、查询账户信息
        2、转账
        3、还款
        4、取现
        5、查询消费流水
        6、退出
    -----------------------------
    """
    ch = {
        "1":atm_func.query,
        "2":atm_func.transfer,
        "3":atm_func.repay,
        "4":atm_func.cash,
        "5":atm_func.record,
        "6":exit
    }

    while True:
        print(menu)
        choice = input("input a choice:")
        if choice in ch:
            ch[choice]()

if __name__ == '__main__':
    run()
