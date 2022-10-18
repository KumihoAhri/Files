import win32api
import win32file
#Модуль для работы с файлами и папками
import shutil
import os

#Определение информации о дисках
def is_drive_ready(drive_name):
    try:
        win32api.GetVolumeInformation(drive_name) #фукнция извлекает сведения о файловой системе
        return True
    except:
        return False



print("  Информация о логических дисках")
#Получение названий дисков системы

drives = win32api.GetLogicalDriveStrings()  #Извлекает битовую маску
drives = drives.split('\000')[:-1]# разделение дисков
print(drives)
for letter in drives:
    print("Название: ", letter)
    print("Тип: ", win32file.GetDriveType(letter))#определяет и возвращает тип носителя
 
    if is_drive_ready(letter):
        total, used, free = shutil.disk_usage(letter)#Функция disk_usage() модуля shutil возвращает статистику использования диска
        print("Всего: %d ГБ" % (total // (2 ** 30)))
        print("Использовано: %d ГБ" % (used // (2 ** 30)))
        print("Свободно: %d ГБ" % (free // (2 ** 30)))
        t = win32api.GetVolumeInformation(letter) 
        print("Метка:", t[0])
    print("------------------------------")

# Работа с файлом
print("  Работа с файлом")..
my_file = open("Files.txt", "w+") #режим открытия
print(" Для записи строки введите 1, для удаления файла введите 2.")
filecase = input()

match filecase:
    case "1":
        print("Введите строку для записи:")
        string = input()
        my_file.write(string)
        my_file.close()
        my_file = open("Files.txt", "r")
        print("Текст записан в файл")
        print("Содержание файла: ", end="")
        print(my_file.read())
        my_file.close()

    case "2":
        my_file = open("Files.txt", "r")
        print("Содержание файла: ", end="")
        print(my_file.read())
        my_file.close()
        os.remove(my_file.name)
       
    case _:
        print("Введите 1 или 2")
        
# JSON файл
import json

print("  Работа с JSON")

print(" Для записи введите 1, для удаления файла введите 2.")
jsoncase = input()

match jsoncase:
    case "1":
        print("Name = ", end="")
        Name_ = input()
        print("Age = ", end="")
        data = {'Name': Name_, 'Age': input()}
        outfile = open('data.json', 'w+')
        json.dump(data, outfile)
        outfile.close()
        outfile = open('data.json', 'r+')
        print("Текст записан в файл")
        print(outfile.read())
        outfile.close()
        
    case "2":
        outfile = open('data.json', 'w+')
        print(outfile.read())
        outfile.close()
        os.remove(outfile.name)
    case _:
        print("Введите 1 или 2")

# HTML файл

import xml.etree.ElementTree as ET

print("  Работа с XML")


print("Город = ", end="")
par = ET.Element(input())
#Добавляем элементы

print("Name = ", end="")
name1 = ET.SubElement(par,input())
tree = ET.ElementTree(par)
tree.write("HTML.xml")

tree = ET.parse('HTML.xml')
root = tree.getroot()
element = root[0]
print("Age = ", end="")
ET.SubElement(element, input())
print("Текст записан в файл")
print("Содержание файла XML:")
tree.write("HTML.xml")


    
ET.dump(tree)
  

os.remove('HTML.xml')
    
# Zip-архив
import zipfile
print("  ZIP архив")
newzip = zipfile.ZipFile('text.zip', 'w',zipfile.ZIP_DEFLATED)
print("Файл text.txt заархивирован")
newzip.write('text.txt')
newzip.close()

newzip = zipfile.ZipFile('text.zip', 'r',zipfile.ZIP_DEFLATED)

newzip.extractall() #распаковка
print("Содержание ZIP-файла:")
newzip.printdir()
newzip.close()
os.remove('text.zip')
