from Supports import getexcel
from Supports import getresponse
from schema import Schema

my_data = getexcel.get_data('.\Cases\Topapi.xlsx')
for i in my_data:
    resp = getresponse.cho_met(i)
    chek = eval(i['schema'])

    try:
        resu = Schema(chek, ignore_extra_keys=True).validate(resp)
        print(resu)
    except Exception as e:
        print(e)

