import csv
''' откроем файл , прочтем его и запшием в новом файле'''
with open('scientist.txt',encoding='utf8') as file , open('scientist_origin.txt', 'w', encoding='utf8',newline='') as file_new:
    reader = csv.DictReader(file,delimitet='')
    writer_new= csv.DictWriter(file_new,['ScientistName','preparation','date','components'], delimiter='')


