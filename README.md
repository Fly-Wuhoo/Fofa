# Fofa
Fofa自动化采集脚本  
需要在fofa_search.py中自定义邮箱地址和key  
运行脚本，输入fofa dork会自动进行数据采集，并将详细结果保存到当前页面下的result.xlsx，将查询到的URL保存在当前目录下的Url.txt中，便于批量使用。  
![图片](https://user-images.githubusercontent.com/56914048/114561769-71084580-9ca0-11eb-8f33-1acf10737ba0.png)

# python3环境下运行报错解决办法：  
fofa库采用python2环境编写，在python3环境下运行会报错，大佬可以根据报错信息进行一步步修改。也可使用手工安装fofa库解决该问题  
Linux环境下将fofa.py放在python3的安装目录下的/Lib/site-packages下，具体路径请根据python3环境进行修改  
kali中python3.8路径为/usr/local/lib/python3.8/dist-packages  

