### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# lists of digimon
r = requests.get("https://wikimon.net/Visual_List_of_Digimon")
soup = BeautifulSoup(r.content, 'html.parser')

dataTarget = soup.find_all('table', class_='')  # table yang tanpa class!
# print(len(dataTarget))                        # 1-1280 data digimon
# print(dataTarget[1:1280])
# print(dataTarget[2].tr.find_next_sibling())
# print(dataTarget[2].tr.find_next_sibling().a.text)

dataDigimonCSV = []
dataDigimonMysql = []

for i in dataTarget[1:1280]:
        # print(i)
        nama = i.tr.find_next_sibling().a
        p = nama.find_parent()
        pp = p.find_parent()
        ppp = pp.find_parent()
        image = ppp.img['src']
        
        # print(nama.text)
        # print('https://wikimon.net'+image)

        data1 = {
                'nama': nama.text,
                'gambar': 'https://wikimon.net'+image
        }
        dataDigimonCSV.append(data1)

        data2 = (nama.text, 'https://wikimon.net'+image)
        dataDigimonMysql.append(data2)

print(dataDigimonCSV)
print(dataDigimonMysql)

# ===========================================
# save as digimon.csv
# ===========================================

import csv

with open('{}.csv'.format('digimon'), 'w', newline = '', encoding="utf-8") as fileku:
        kolom = ['nama', 'gambar']
        tulis = csv.DictWriter(fileku, fieldnames = kolom)
        tulis.writeheader()
        tulis.writerows(dataDigimonCSV)

# ===========================================
# save on mysql database:
#       $ create database digimon;
#       $ use digimon;
#       $ create table digimon(id int auto_increment, nama varchar(255), gambar varchar(255), primary key(id));
# ===========================================

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="lintang",
  passwd="12345",
  database="digimon"
)

mycursor = mydb.cursor()
sql = "INSERT INTO digimon (nama, gambar) VALUES (%s, %s)"

mycursor.executemany(sql, dataDigimonMysql)
mydb.commit()
print(mycursor.rowcount, "Data tersimpan!")