ATM_Shopping Readme

作者：沈洪斌
博客：http://www.cnblogs.com/vincenshen/

程序介绍：
	实现ATM简单功能，以及购物商城结账调用ATM相关API结算。
	
程序目录结构：
	atm_shop
	│   
	├── readme
	│   
	├── atm #ATM主程目录
	│   ├── __init__.py
	│   │
	│   ├── bin #ATM 执行文件目录
	│   │   ├── __init__.py
	│   │   ├── atm.py  #ATM  主执行程序
	│   │   └── manage.py #ATM 管理端,未实现
	│   │
	│   ├── conf #配置文件
	│   │   ├── __init__.py
	│   │   └── settings.py
	│   │
	│   ├── core #主程序逻辑目录
	│   │   ├── __init__.py
	│   │   ├── accounts.py  #用于从文件里加载和存储账户数据
	│   │   ├── auth.py      #用户认证模块
	│   │   ├── db_handler.py   #数据库连接引擎
	│   │   ├── logger.py       #日志记录模块
	│   │   ├── main.py         #主逻辑交互程序
	│   │   └── transaction.py  #记账\还钱\取钱等所有的与账户金额相关操作
	│   │
	│   ├── db  # 数据存储目录
	│   │   ├── __init__.py
	│   │   ├── account_sample.py 	# 模板的账户数据
	│   │   └── accounts 	#存放各个用户的账户数据 ,一个用户一个文件
	│   │       	├─ 1234.json 	# 示例账户数据文件
	│   │	└─── 1235.json 	# 示例账户数据文件
	│   │
	│   └── log 	# 日志目录
	│       ├── __init__.py
	│       ├── access.log #用户访问和操作的相关日志
	│       └── transactions.log    # 所有的交易日志
	│
	└── shopping_mall 	# 购物商城程序,还未实现
		│
		├── shopping.py  # 购物商城接口登录程序
		└── __init__.py
		

	
使用方法：
	已经初始化了两个测试账户： 
	id:1234 	passwd:abc  
	id:1235 	passwd:abc
	atm.py 为用户接口登录程序
	manage.py 为管理员接口登录程序     ---未实现
	shopping.py 为购物商城接口登录程序  ---未实现

运行条件：
	本程序使用了外部库 prettytable和colorama，运行本程序前需先安装。

	
注意事项：
	本程序使用python3版本编写，不兼容python2版本

版本：
	1.0
	
更新日志：
	v1.0 2017.02.17 
	
