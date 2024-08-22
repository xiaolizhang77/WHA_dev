# -*- coding: gbk -*-
import os


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '|-' * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * level + '|-'
        for f in files:
            print('{}{}'.format(subindent, f))


# 替换成你项目的路径
project_path = "C:\\Users\\98750\\Desktop\\WHA_dev"

list_files(project_path)
