import json,os
from atm_shop.atm.conf import settings

class DB_Handle(object):
    def __init__(self):
        self.conn_params = settings.DATABASE
        self.db_path = r"%s\%s" % (self.conn_params['path'], self.conn_params['name'])

    def db_api(self, account_data, access_type):
        if self.conn_params['engine'] == 'file_storage':
            if access_type == 'read':
               return self._file_db_read(account_data)
            if access_type == 'write':
               return self._file_db_write(account_data)
        if self.conn_params['engine'] == 'mysql':
            pass

    def _file_db_read(self, account_data):
        if os.path.isfile(r'%s\%s.json' %(self.db_path, account_data['id'])):
            with open(r'%s\%s.json' %(self.db_path, account_data['id'])) as f:
                account_data = json.load(f)
            return account_data

    def _file_db_write(self, account_data):
        with open(r'%s\%s.json' % (self.db_path, account_data['id']), 'w') as f:
            json.dump(account_data, f)
        return True

