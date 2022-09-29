'''
Author: LetMeFly
Date: 2022-09-29 15:16:51
LastEditors: LetMeFly
LastEditTime: 2022-09-29 18:30:28
'''
import os
import time
import requests


with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

"""Generate begin"""
# document.querySelector("#repos > ol").querySelectorAll("li")
# https://docs.github.com/cn/rest/activity/starring#list-stargazers
nowPage = 1
allUsers = []
while True:
    try:
        # response = requests.get(f"https://github.com/LetMeFly666/WhoStarredMe/stargazers?page={nowPage}", verify=False)
        # print(response)
        # soup = BeautifulSoup(response.content, 'lxml')
        # repos = soup.find("div", attrs={"id": "repos"})
        # ol = repos.find("ol")
        # for li in ol.find_all("li"):
        #     div = li.find("div")
        #     avatarA = div.find("a")
        #     href = "https://github.com" + avatarA.get("href")
        #     avatarSrc = avatarA.find("img").get("src")
        #     username = li.find("span").find("a").string
        #     allUsers.append(f"<li><img src=\"{avatarSrc}\" style=\"border-radius: 50% !important;\" with=\"96px\" height=\"96px\"><a href=\"{href}\">{username}</a></li>")
        def getHeaders():
            if os.environ.get("GITHUB_TOKEN"):
                headers = {
                    "Authorization": "Bearer " + os.environ.get("GITHUB_TOKEN"),
                }
            else:
                headers = {}
            return headers
        response = requests.get(
            url="https://api.github.com/repos/LetMeFly666/WhoStarredMe/stargazers",
            verify=False,
            params={
                "per_page": 100,
                "page": nowPage
            },
            headers = getHeaders(),
        )
        if not response.json():
            break
        if nowPage > 10000:
            raise ValueError("项目有100万个star了？")
        for thisUser in response.json():
            allUsers.append(f"<li><img src=\"{thisUser['avatar_url']}\" style=\"border-radius: 50% !important;\" with=\"96px\" height=\"96px\"><a href=\"{thisUser['html_url']}\">{thisUser['login']}</a></li>")
        nowPage += 1
    except BaseException as e:
        print(e)
        try:
            print(response)
            print(response.json())
        except:
            pass
        break
# allUsers.reverse()

LetMeFLetMeFly_Anchor1_Begin = "<LetMeFly id=\"LetMeFly_Anchor1_Begin\"></LetMeFly>"
LetMeFLetMeFly_Anchor1_End = "<LetMeFly id=\"LetMeFly_Anchor1_End\"></LetMeFly>"
contentFront, temp = content.split(LetMeFLetMeFly_Anchor1_Begin)
contentBack = temp.split(LetMeFLetMeFly_Anchor1_End)[1]
content = contentFront + LetMeFLetMeFly_Anchor1_Begin + "\n\nUpdated at: " + time.strftime("%Y-%m-%d") + "\n\n<ol>\n"
for thisUser in allUsers:
    content += "    " + thisUser + "\n"
content += "</ol>\n\n" + LetMeFLetMeFly_Anchor1_End
content += contentBack
    
"""Generate End"""

if not os.environ.get("LetMeFly_OnGithub"):
    print(content)
    print("Not on github action")
    exit(0)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)


def execute1commandAfterEcho(command):
    print('*' * 20, command, '*' * 20)
    os.system(command)

"""Commit"""
execute1commandAfterEcho("git config --global user.email \"814114971@qq.com\"")
execute1commandAfterEcho("git config --global user.name \"LetMeFly666\"")
execute1commandAfterEcho("git add .")
execute1commandAfterEcho("git commit -m \"Updated on {}\"".format(time.strftime("%Y-%m-%d")))
execute1commandAfterEcho("git push")
