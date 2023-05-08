import os
import shutil

fromDir = "C:/Users/Admin/Downloads"
toDir = "C:/Users/Admin/Pictures/c102"

lista = os.listdir(fromDir)
#print(lista)

for nomes in lista:
    name, extension = os.path.splitext(nomes)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        originalPath = fromDir + "/" + nomes
        path2 = toDir + "/" + "imagens102"
        path3 = toDir + "/" + "imagens102" + nomes
        if os.path.exists(path2):
            print("Movendo " + nomes + "...")
            shutil.move(originalPath, path3)
        else :
            os.makedirs(path2)
            print("Movendo " + nomes + "...")
            shutil.move(originalPath, path3)
