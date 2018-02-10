import os
import sys


def get_word(target_file):
    L = []
    with open(target_file, 'r', encoding='gbk', errors='ignore') as f:
        for line in f.readlines():
            if line is not None:
                L.append(line.strip('\n'))
        return L


if __name__ == '__main__':
    argv = sys.argv[1:]
    L = []
    if not argv:
        print(
            'Next at least 1 parameter.Try to excute \'python 0012.py $dir_path \'')
    else:
        for dir_path in sys.argv[1:]:
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                if os.path.splitext(file_path)[1] == '.txt':
                    L += get_word(file_path)

    words = input('请输入:')

    for item_word in L:
        if item_word in words:
            words = words.replace(item_word, '*' * len(item_word))

    print(words)
