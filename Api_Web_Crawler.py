__author__ = 'KittipatDechkul'
import json
from Web_Crawler import Logo_url

url = "https://theinternship.io/"

test = []

for line in Logo_url:
    test.append(url + line)

score_titles = {"companies": [{"logo": t} for t in test]}


if __name__ == '__main__':
    print (json.dumps(score_titles, indent=2))