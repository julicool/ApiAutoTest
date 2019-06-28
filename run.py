# -*-coding:utf-8-*-
from Supports import getexcel
from Supports import getresponse
from Supports import getresult
from Supports import sendmail
from schema import Schema, And
import logging
import os

# 日志配置，有需要可以全局加日志，需要在文件头引入logging模块
logging.basicConfig(format='%(asctime)s : %(filename)s - %(levelname)s : %(message)s', level=logging.INFO)


my_data = getexcel.get_data('./Cases/TopApi.xlsx')                     # 获取Excel中的case数据
for i in range(len(my_data)) :                                         # 循环取出每行case进行执行，将获取的结果格式化为字典
    resp = getresponse.cho_met(my_data[i])                             # 获取执行返回结果json
    chek = eval(my_data[i]['schema'])                                  # 获取校验用的schema数据
    my_data[i]['response'] = str(resp)                                 # 将执行结果放到最终要输出的字典中去

    try :
        resu = Schema(chek, ignore_extra_keys=True).validate(resp)     # 根据schema格式进行结果校验
        my_data[i]['result'] = "Pass"
        my_data[i]['reason'] = ""
    except Exception as e :
        my_data[i]['result'] = "Error"
        my_data[i]['reason'] = str(e)

run_result = getresult.create_excel(my_data)                           # 创建测试报告，获取执行情况
if run_result['run_fault'] > 0 :                                       # 如果失败数大于0，则进行邮件通知。等于0则不发送
    result = sendmail.send_mail(run_result)
    print(result)                                                      # 打印邮件发送结果
os.remove("./Results/report-" + run_result['run_time'] +".xls")        # 执行完成后删除本地测试报告