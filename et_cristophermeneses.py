import os
os.system("cls")

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}


def menu():
    os.system("cls")
    
    
    print("*** Menu Principal ***")
    print("1.- Stock marca.")
    print("2.- Busqueda por precio.")
    print("3.- Actualizar precio.")
    print("4.- Salir")

    int(input("Ingrese Opcion: "))



def menu_principal(marca):
    os.system("cls")
    
    if menu == 1:
        input("Ingrese marca a consultar: ")
        print(f"El stock es:{stock} ")
    

def busqueda(stock):
    os.system("cls")
    if menu == 2:
        int(input("Ingrese precio mínimo: "))
        int(input("Ingrese precio máximo: "))
        print(f"Los notebooks entre los precios consultados son: {stock}")


def actualizar_precio():
    os.system("cls")
    if menu == 3:
        input("Ingrese modelo a actualizar: ")
        int(input("Ingrese nuevo precio: "))
        print("¡Precio Actualizado con exito!...")


def salir():
    os.system("cls")
    if menu == 4:
        print("Programa Finalizado...")


    

    

    









menu()
