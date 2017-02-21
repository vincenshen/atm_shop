import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine':'file_storage',   #support mysql, postgresql in the future
    'name':'accounts',
    'path':"%s\db" % BASE_DIR
}

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
    'log_level': 'error'
}

TRANSACTION_TYPE = {
    'repay':{'interest':0},
    'cash':{'interest':0.05},
    'transfer':{'interest':0.05},
    'consume':{'interest':0},
}