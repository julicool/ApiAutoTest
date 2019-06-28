# -*-coding:utf-8-*-
import xlwt
import time
import os


# 这个文件的作用是生成测试报告
def create_excel(my_data):
    title_style = set_style(18, 1)                      # 设置title样式，参数有两个，前一个是单元格颜色，第二个是字体颜色
    fail_style = set_style(2, 1)                        # 设置失败单元格样式
    row_index = 1                                       # 游标一样的作用，每写完一行会+1，引导将当前数据写入到第几行
    run_total = len(my_data)                            # 最后会返回个统计数据，这个是总用例执行数
    run_fault = []                                       # 这个是执行失败用例数，每执行失败一次+1
    run_time = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 开始执行时间，文件保存命名时会用到

    my_excel = xlwt.Workbook()                          # 创建表格
    my_sheet = my_excel.add_sheet('test_result')        # 创建sheet页
    my_sheet.write(0, 0, "name", title_style)           # 设置表头，也就是标题行
    my_sheet.write(0, 1, "result", title_style)
    my_sheet.write(0, 2, "reason", title_style)
    my_sheet.write(0, 3, "response", title_style)
    my_sheet.write(0, 4, "url", title_style)
    my_sheet.write(0, 5, "data", title_style)
    my_sheet.col(0).width = 18*256                      # 设置列宽，指定每列的列宽
    my_sheet.col(1).width = 12*256
    my_sheet.col(2).width = 50*256
    my_sheet.col(3).width = 50*256
    my_sheet.col(4).width = 50*256
    my_sheet.col(5).width = 50*256

    for i in my_data:                                   # 循环写入每条用例执行的结果，一条用例生成一行数据
        my_sheet.write(row_index, 0, i['name'])
        my_sheet.write(row_index, 2, i['reason'])
        my_sheet.write(row_index, 3, i['response'])
        my_sheet.write(row_index, 4, i['url'])
        my_sheet.write(row_index, 5, i['data'])
        if i['result'] == "Error":
            my_sheet.write(row_index, 1, i['result'], fail_style)
            run_fault.append(i['name'] + "  -->  " + i['response'])
        else:
            my_sheet.write(row_index, 1, i['result'])
        row_index += 1

    if run_fault > 0:                                   # 判断Results文件夹是否存在，不存在则创建。主要是用来临时保存测试报告的，
        if not os.path.exists("./Results/"):            # 报告在有执行失败的时候会以邮件附件的形式被发送，邮件发送成功后被删除
            os.mkdir("./Results/")
        my_excel.save("./Results/report-" + run_time +".xls")
    run_result = {"run_total": run_total, "run_fault": len(run_fault), "run_time": run_time, "run_fault_list": run_fault}
    return run_result


def set_style(cell_color=1, font_color=0) :             # cell_color为单元格颜色，font_color为字体颜色
    my_pattern = xlwt.Pattern()                         # 初始化单元格样式
    my_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    my_pattern.pattern_fore_colour = cell_color         # 设置单元格背景颜色
    my_font = xlwt.Font()                               # 初始化字体样式
    my_font.colour_index = font_color                   # 设置字体颜色
    my_style = xlwt.XFStyle()                           # 初始化样式设置
    my_style.pattern = my_pattern                       # 添加单元格样式
    my_style.font = my_font                             # 添加字体样式

    return my_style


'''
style颜色说明
0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 
6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 
19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 
22 = Light Gray, 23 = Dark Gray, the list goes on...
'''