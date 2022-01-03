# Viktor
from os import walk

lista_archivos = []

for (dirpath, dirnames, filenames) in walk("C:\\Users\\Vikto\\Desktop\\Openbootcamp"):
    lista_archivos.append(filenames)
        
if len(lista_archivos) == 0:
    print("No hay ficheros dentro de la dirección indicada, revisala.")
else:
    for file in lista_archivos[:]:
        print(f"{file}\n")



 
