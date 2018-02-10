# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:chenshi
# Date:2016-09-06
# Python 3.4

"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中.
"""

import json
import xlwt

def write_text_to_xls(text_file):
    with open(text_file,'r') as f:
        text_content = json.load(f)
    print(text_content)
    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('numbers')
    for i in range(len(text_content)):
        data = text_content[i]
        for j in range(len(data)):
            sheet.write(i,j,data[j])
    xls_object.save('numbers.xls')


if __name__ == '__main__':
    write_text_to_xls('numbers.txt')