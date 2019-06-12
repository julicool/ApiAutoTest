import xlwt
import time

def create_excel(my_data):
    title_style = set_style(18, 1)
    fail_style = set_style(2, 1)
    row_index = 1
    my_time = time.strftime('%Y%m%d%H%M%S', time.localtime())

    my_excel = xlwt.Workbook()                          # 创建表格
    my_sheet = my_excel.add_sheet('test_result')        # 创建sheet页
    my_sheet.write(0, 0, "name", title_style)           # 设置表头
    my_sheet.write(0, 1, "result", title_style)
    my_sheet.write(0, 2, "reason", title_style)
    my_sheet.write(0, 3, "response", title_style)
    my_sheet.write(0, 4, "url", title_style)
    my_sheet.write(0, 5, "data", title_style)
    my_sheet.col(0).width = 18*256                      # 设置列宽
    my_sheet.col(1).width = 12*256
    my_sheet.col(2).width = 50*256
    my_sheet.col(3).width = 50*256
    my_sheet.col(4).width = 50*256
    my_sheet.col(5).width = 50*256

    for i in my_data:                                   # 循环写入结果
        my_sheet.write(row_index, 0, i['name'])
        my_sheet.write(row_index, 2, i['reason'])
        my_sheet.write(row_index, 3, i['response'])
        my_sheet.write(row_index, 4, i['url'])
        my_sheet.write(row_index, 5, i['data'])
        if i['result'] == "Error":
            my_sheet.write(row_index, 1, i['result'], fail_style)
        else:
            my_sheet.write(row_index, 1, i['result'])
        row_index += 1

    my_excel.save("./Results/report-" + my_time +".xls")

    return my_time


# 颜色说明 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
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
