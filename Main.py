'''
Author: LetMeFly
Date: 2022-09-29 15:16:51
LastEditors: LetMeFly
LastEditTime: 2022-09-29 15:19:03
'''
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content += "\n\n66666666666666666\n\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
