import os,sys

BASE_DIR = os.path.normcase(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         os.path.pardir,
                                         os.path.pardir,
                                         os.path.pardir
                                         ))
sys.path.append(BASE_DIR)
from atm_shop.atm.core import main


if __name__ == '__main__':
    main.run()

