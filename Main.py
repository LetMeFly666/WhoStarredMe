'''
Author: LetMeFly
Date: 2022-09-29 15:16:51
LastEditors: LetMeFly
LastEditTime: 2022-09-29 15:33:59
'''
import os
import time


with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content += "\n\n66666666666666666\n\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)


def execute1commandAfterEcho(command):
    print('*' * 20, command, '*' * 20)
    os.system(command)


execute1commandAfterEcho("git config --global user.email \"814114971@qq.com\"")
execute1commandAfterEcho("git config --global user.name \"LetMeFly666\"")
execute1commandAfterEcho("git add .")
execute1commandAfterEcho("git commit -m \"Updated on {}\"".format(time.strftime("%Y-%m-%d")))
execute1commandAfterEcho("git push")
