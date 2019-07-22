-------------
# 描述 #
-------------
转换中文名为对应的威妥玛表达式或查询国内城市的邮政码表达式。

# 使用示例 #
	$ python  waderomanizer.py
	  转换人名或查找地名[0,1]: 0
	  请输入姓名: 习近平
	  Hsi chin p'ing

	$ python  waderomanizer.py
	  转换人名或查找地名[0,1]: 0
	  请输入姓名: 诸葛亮
	  Chu ko liang

	$ python  waderomanizer.py
	  转换人名或查找地名[0,1]:1
	  请输入地名(输入0显示所有地区注音表): 北京
	  Peking

	$ python  waderomanizer.py
	  转换人名或查找地名[0,1]: 1
	  请输入地名(输入0显示所有地区注音表): 四川 
	  Szechwan

# 要求 #
需要安装pypinyin，且python的版本为3，2没测试过，应该能用。

$ sudo pip3 install pypinyin
