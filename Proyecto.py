import sqlite3
db=sqlite3.connect("Torneo_Fulbo.sqlite")
cur=db.cursor()

#DEFINICION DE FUNCIONES
def imprimirDic(diccionario):   #Funcion para imprimir diccionarios, lo llamo cada vez que se necesita un menu.
    for clave,entrada in diccionario.items():
        print(clave,"->",entrada)

def funcionSelect (tabla):              #Funcion que lista todo el contenido de una tabla
    buscar="SELECT * FROM "+tabla+";"
    cur.execute(buscar)
    registros=cur.fetchall()
    return registros

def funcionNombreCampos (tabla):        #Funcion que obtiene los nombres de los campos de la base de datos.
    db.row_factory = sqlite3.Row
    cursor = db.execute('select * from '+tabla+';')
    row = cursor.fetchone()
    names = row.keys()
    print (names)
    return names#medio al pedo creo¿?

def funcionBuscar(tabla, campo, valor): #Esta funcion buscaria uno o varios registros especificos 
    valor="'"+valor+"'"                 #dentro de la tabla que se le pasa como parametro. Aun no funciona
    print (tabla, campo, valor)         #DEBUG (borrar luego)
    parametros=(campo,valor)
    buscar="SELECT * FROM "+tabla+" WHERE ? LIKE ?;"
    cur.execute(buscar,parametros)
    registros=cur.fetchall()
    print (len(registros))              #DEBUG
    return registros

#Diccionarios para ahorrar codigo
dicMenu={1:"Listar tabla",2:"Buscar una tabla",3:"Agregar datos a una tabla",4:"Borrar datos"}
dicTablas={1:"Jugadores", 2:"Equipos",3:"Fixture",4:"Arbitros",5:"Tabla_de_posiciones"}

#ACA COMIENZA EL PROGRAMA
imprimirDic(dicMenu)
entrada=input("Ingrese la opcion deseada: ")
if entrada=="1":
    imprimirDic(dicTablas)
    entTabla=int(input("Que tabla desea listar: "))
    registros=funcionSelect(dicTablas[entTabla])
    for registro in registros: 
        print (registro)
elif entrada=="2":
    imprimirDic(dicTablas)
    entTabla=int(input("Que tabla desea buscar: "))
    funcionNombreCampos(dicTablas[entTabla])
    entEncabezado=input("Que desea buscar: ")
    entValor=input("Ingrese el valor a buscar: ")
    #Al Debug
    print (type(entTabla))
    print (type(entEncabezado))
    print (type(entValor))
    resultado=funcionBuscar(dicTablas[entTabla], entEncabezado, entValor)
    print(resultado)
elif entrada=="3":                      #Hay que hacer la opcion de insertar un registro, modificar un registro y de borrar un registro
    imprimirDic(dicTablas)
    entTabla=int(input("Que tabla desea buscar: "))
    funcionNombreCampos(dicTablas[entTabla])






