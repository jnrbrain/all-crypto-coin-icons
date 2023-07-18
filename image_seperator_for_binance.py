import shutil
import json
import requests
import os.path

coin_list=[]
x = requests.get('https://api.binance.com/api/v3/exchangeInfo').json()
for i in x["symbols"]:
    if i["baseAsset"] not in coin_list:
        coin_list.append(i["baseAsset"])
    if i["quoteAsset"] not in coin_list:
        coin_list.append(i["quoteAsset"])

these_coins_should_be_added=[]
if os.path.isdir('./binance/')==False:
    os.mkdir("binance")
else:
    print("There is no directory")

print("Wait for copying")
for i in coin_list:
    path = './icons/'+i+'.png'
    check_file = os.path.isfile(path)
    if check_file==False:
        these_coins_should_be_added.append(i)
    else:
        shutil.copy('icons/'+i+'.png', 'binance/'+i+'.png')
print("Downloaded!\n")
print("New icons should be downloaded= "+str(these_coins_should_be_added))