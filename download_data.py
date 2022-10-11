import requests
import datetime
import os

url_museo = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
url_teatro = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/87ebac9c-774c-4ef2-afa7-044c41ee4190/download/17_teatro.xlsx-datos-abiertos.csv"
url_librerias = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

current_time = datetime.datetime.now()

categories= ["museos","teatros","librerias"]

category1 = "museos"
category2 = "teatros"
category3 = "librerias"

# Using datetime library to automatically set current date
def create_directories(category):
    path= "/home/user/folder_name"
    os.chdir(path)
    new_folder= category
    os.makedirs(new_folder)
    path2= path+"/"+new_folder
    os.chdir(path2)
    new_folder_1= str(current_time.year)+"-"+str(current_time.strftime("%B"))
    os.makedirs(new_folder_1)

def filename(category):
    return "/home/user/folder_name"+"/"+category+"/"+str(current_time.year)+"-"+str(current_time.strftime("%B"))+"/"+category+"-"+str(current_time.day)+"-"+str(current_time.month)+"-"+str(current_time.year)+".csv"


def download(url,filename):
    response = requests.get(url)
    open(f'{filename}', "wb").write(response.content)

for cat in categories:
    create_directories(cat)
    filename(cat)

download(url_museo,filename(category1))
download(url_teatro,filename(category2))
download(url_librerias,filename(category3))
