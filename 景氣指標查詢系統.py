import requests
import json

"""原網站"""
uurl = "https://index.ndc.gov.tw/n/zh_tw/data/PMI/total#/"
'''資料網站'''
url = "https://index.ndc.gov.tw/n/json/data/PMI/total"

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
datas = requests.post(url,headers=headers).text
da = json.loads(datas)