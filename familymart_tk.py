import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import pandas as pd
import json
import requests
from datetime import date
import time

def connectweb(url):
    header ={}
    header ["Referer"] = "https://www.family.com.tw/"
    return requests.get(url,headers=header).text.replace("([","[").replace("])","]")

cityurl = "https://api.map.com.tw/net/familyShop.aspx?searchType=ShowTownList&type=&city={}&fun=storeTownList&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC"
townurl = "https://api.map.com.tw/net/familyShop.aspx?searchType=ShopList&type=&city={}&area={}&road=&key=6F30E8BF706D653965BDE302661D1241F8BE9EBC"

'''縣市列表'''
cities =["台北市","新北市","基隆市","桃園市","新竹市","新竹縣","苗栗縣",
"雲林縣","嘉義市","嘉義縣","台南市","高雄市","屏東縣",
"澎湖縣","金門縣","連江縣",
"台中市","彰化縣","南投縣",
"宜蘭縣","花蓮縣","台東縣",]



def callallmanu(*args):
    to_shop = connectweb(townurl.format(variable.get(),variable1.get()))
    time.sleep(10)
    to_shop = pd.read_json(to_shop)
    for i in range(len(to_shop)):
        if to_shop["NAME"][i] ==str(variable2.get()):
            text1 = str(to_shop["TEL"][i])#電話
            text2 = str(to_shop["addr"][i])#地址
            text3 = str(to_shop["post"][i])#郵遞區號
            text4 = str(to_shop["SERID"][i])#服務編號
            text5 = str(to_shop["road"][i])#在哪條路
            text6 = str(to_shop["all"][i])#服務項目
        
            # if len(to_shop["all"][i])>20:                
            #     text6 = str(to_shop["all"][i])[0:20]#服務項目
            #     text7 = str(to_shop["all"][i])[20:40]#服務項目
            #     text8 = str(to_shop["all"][i])[40:60]#服務項目
            #1
            text6=text6.replace('LCoffee','咖啡複合店')
            #2
            text6=text6.replace('laundry','自助洗衣')
            #3
            text6=text6.replace('SCoffee','單品咖啡_雙豆販售')
            #4
            text6=text6.replace('SWEETPOTATO','夯番薯')
            #5
            text6=text6.replace('Rpotato','烤馬鈴薯')
            #6
            text6=text6.replace('Meatballs','海瑞貢丸')
            #7
            text6=text6.replace('dessert','現烤點心')
            #8
            text6=text6.replace('oneice','單口味')
            #9
            text6=text6.replace('twoice','雙口味')
            #10
            text6=text6.replace('FreshFruit','鮮水果')
            #11
            text6=text6.replace('TANHOU','天和鮮物')
            #12
            text6=text6.replace('SUNMAI','金色三麥冰箱')
            #13
            text6=text6.replace('intl','國際線專架')
            #14
            text6=text6.replace('costco','好市多專架')
            #15
            text6=text6.replace('leezen','里仁專架')
            #16
            text6=text6.replace('veg','生鮮蔬菜')
            #17
            text6=text6.replace('pet','寵物專架')
            #18
            text6=text6.replace('wash','洗沐清潔專架')
            #19
            text6=text6.replace('kit','廚房調理專架')
            #20
            text6=text6.replace('hada','哈根達斯冰箱')
            #21
            text6=text6.replace('Preorder','隨買跨店取')
            #22
            text6=text6.replace('COFFEEDeliver','咖啡外送')
            #23
            text6=text6.replace('Photo','相片立可得')
            #24
            text6=text6.replace('CS','行動電源租借')
            #25
            text6=text6.replace('Rest','休憩區')
            #26
            text6=text6.replace('Toilet','廁所')
            #27
            text6=text6.replace('None','無')
            #28
            text6=text6.replace('icecream','冰淇淋')
            #29
            text6=text6.replace('Smoothie','冰沙')

    # 電話
    labelTest = tk.Label(text="電話", font=(100))
    labelTest.place(x =400,y=5)
    labelTest01 = tk.Label(text=text1, font=(100), fg='red')
    labelTest01.place(x =400,y=45)    
    # 地址
    labelTest02 = tk.Label(text="地址", font=(100))
    labelTest02.place(x =400,y=85)
    labelTest03 = tk.Label(text=text2, font=(100), fg='red')
    labelTest03.place(x =400,y=125)
    # 郵遞區號
    labelTest04 = tk.Label(text="郵遞區號", font=(100))
    labelTest04.place(x =400,y=165)
    labelTest05 = tk.Label(text=text3, font=(100), fg='red')
    labelTest05.place(x =400,y=205)
    # 服務編號
    labelTest06 = tk.Label(text="服務編號", font=(100))
    labelTest06.place(x =400,y=245)
    labelTest07 = tk.Label(text=text4, font=(100), fg='red')
    labelTest07.place(x =400,y=285)    
    # 服務內容
    labelTest08 = tk.Label(text="服務內容", font=(100))
    labelTest08.place(x =400,y=325)
    labelTest09 = tk.Label(text=text6, font=(100), fg='red',wraplength =300)
    labelTest09.place(x =400,y=365)

def callbackcity(*args):
    #區域(文字)
    labelTest = tk.Label(text="區域", font=(50), fg='red').place(x =5,y=100)
    #讀取資料
    town = connectweb(cityurl.format(variable.get()))
    time.sleep(10)
    town = pd.read_json(town[13:])
    towns = town["town"]
    #選單
    option_1 = tk.OptionMenu(gotsh, variable1, *towns)
    option_1.config(width=20, font=(20))
    option_1.place(x = 30, y = 140)
    #送出鍵
    btn_send_1 = Button(gotsh, text = "send", command =callbacktown)
    btn_send_1.config(width=6, font=(15))
    btn_send_1.place(x = 300, y = 140)


def callbacktown(*args):
    #店家(文字)
    labelTest = tk.Label(text="店家", font=(50), fg='red').place(x =5,y=200)
    #讀取資料
    to_shop = connectweb(townurl.format(variable.get(),variable1.get()))
    time.sleep(10)
    to_shop = pd.read_json(to_shop)
    shop_name = to_shop['NAME']
    #選單
    option_2 = tk.OptionMenu(gotsh, variable2, *shop_name)
    option_2.config(width=20, font=(20))
    option_2.place(x = 30, y = 240)
    
    #送出鍵
    btn_send_1 = Button(gotsh, text = "send", command =callallmanu)
    btn_send_1.config(width=6, font=(15))
    btn_send_1.place(x = 300, y = 240)

#開新視窗
gotsh = tk.Tk()
gotsh.title("歡迎使用全家查詢系統")
gotsh.geometry('800x600')

labelTest = tk.Label(text="城市", font=(50), fg='red').place(x =5,y=5)
#城市
variable = tk.StringVar(gotsh)
#區域
variable1 = tk.StringVar(gotsh)
#店家
variable2 = tk.StringVar(gotsh)

#城市(選單)
option = tk.OptionMenu(gotsh, variable, *cities)
option.config(width=20, font=(20))
option.place(x = 30, y = 40+5)

#城市(送出)
btn_send = Button(gotsh, text = "send", command =callbackcity)
btn_send.config(width=6, font=(15))
btn_send.place(x = 300, y = 40+5)

#關閉
btnExit = Button(gotsh, text = "Exit", command = gotsh.destroy)
btnExit.config(width=20, font=(20))
btnExit.place(x = 15, y = 500)                   


gotsh.mainloop()