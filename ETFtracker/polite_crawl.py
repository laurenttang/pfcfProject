import requests
import os
from bs4 import BeautifulSoup
import json

# 爬回存放區
resource_path = r'./res_gossiping'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

# 基本禮貌
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
ss = requests.session()
# ss.cookies['over18'] = '1'
url = 'https://mis.twse.com.tw/stock/data/all_etf.txt'
res = ss.get(url, headers = headers)
print(res.text)
# use soup when it is a html
# soup = BeautifulSoup(res.text, 'html.parser')

# use when it is Json res
a=json.loads(res.text)

# Serializing json
json_object = json.dumps(a, indent=4)
print(json_object)
 
# Writing to sample.json
with open(f"{resource_path}/output.json", "w") as outfile:
    outfile.write(json_object)
