import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import json
import os
import sys


sUrl ="https://www.ytn.co.kr/news/list_breaking.php"

sHead = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
oRes = requests.get(sUrl, headers=sHead)
oRes.encoding = "utf-8"

soup = BeautifulSoup(oRes.text, "html.parser")

lstNews = []
lstDate = []

for i in range(1, 31) :
  # oNews = soup.select("#zone1 > div > ul > li:nth-child("+str(i)+") > p.newstit > a")
  oNews = soup.select("#zone1 > div > ul > li:nth-child("+str(i)+") > p.newstit")
  oDate = soup.select("#zone1 > div > ul > li:nth-child("+str(i)+") > p.date ")
  lstNews.append(oNews[0].text)
  lstDate.append(oDate[0].text)

dfData = pd.DataFrame({"Date":lstDate, "News":lstNews})

suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
fileName = suffix + '.csv'

dfData.to_csv(fileName)
# dfData.to_csv("DfData.csv")
