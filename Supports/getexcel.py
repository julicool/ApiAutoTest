import xlrd


def get_data(path):
    my_excel = xlrd.open_workbook(path)                    # 打开文件
    my_sheets = my_excel.sheets()                          # 获取sheet页列表。
    my_sheet = my_sheets[0]                                # 获取第一个sheet页数据
    my_data = [{} for i in range(my_sheet.nrows)]          # 创建长度等于行数的空数组

    for i in range(my_sheet.nrows):                        # 循环取出每行数据内容
        my_data[i]['name'] = my_sheet.row_values(i)[0]
        my_data[i]['method'] = my_sheet.row_values(i)[1]
        my_data[i]['url'] = my_sheet.row_values(i)[2]
        my_data[i]['data'] = my_sheet.row_values(i)[3]
        my_data[i]['schema'] = my_sheet.row_values(i)[4]

    my_data.pop(0)                                         # 去掉标题行

    return my_data
