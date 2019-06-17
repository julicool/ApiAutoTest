from Supports import getexcel
from Supports import getresponse
from Supports import getresult
from Supports import sendmail
from schema import Schema, And
import logging

logging.basicConfig(format='%(asctime)s : %(filename)s - %(levelname)s : %(message)s', level=logging.INFO)

my_data = getexcel.get_data('.\Cases\Topapi.xlsx')
for i in range(len(my_data)) :
    resp = getresponse.cho_met(my_data[i])
    chek = eval(my_data[i]['schema'])
    my_data[i]['response'] = str(resp)

    try :
        resu = Schema(chek, ignore_extra_keys=True).validate(resp)
        my_data[i]['result'] = "Pass"
        my_data[i]['reason'] = ""
    except Exception as e :
        my_data[i]['result'] = "Error"
        my_data[i]['reason'] = str(e)

run_result = getresult.create_excel(my_data)
if run_result['run_failt'] > 0 :
    result = sendmail.send_mail(run_result)
    print(result)
