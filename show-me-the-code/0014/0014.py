# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:chenshi 
# Date:2016-09-06
# Python 3.4

"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。
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
        for j in range(len(data)):
            sheet.write(i, j+1, data[j])
    xls_object.save('student.xls')

if __name__ == '__main__':
    write_text_to_xls('student.txt')