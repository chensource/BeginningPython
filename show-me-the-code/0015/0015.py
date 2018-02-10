# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:chenshi	
# Date:2016-09-06
# Python 3.4

"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中.
"""

import json
import xlwt


def write_text_to_xls(text_file):
    with open(text_file) as f:
        file_content = json.load(f)

    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('student')
    for i in range(len(file_content)):
        sheet.write(i, 0, i+1)
        data = file_content[str(i+1)]
        sheet.write(i, 1, data)
    xls_object.save('city.xls')

if __name__ == '__main__':
    write_text_to_xls('city.txt')