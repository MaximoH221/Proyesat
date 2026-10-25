import json
grupos= {
        "STARLINK": "Starlink", 
        "ONEWEB": "OneWeb",
        "KUIPER": "Kuiper",
        "QIANFAN": "Qianfan",
        "IRIDIUM": "Iridium",
        "GLOBALSTAR": "Globalstar",
        "NAVSTAR": "GPS",
        "BEIDOU": "BeiDou"
}
def leer_satelites(ruta):
    try: 
        with open(ruta, "r", encoding="utf-8") as archivo:
            registros = json.load(archivo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return []
    return registros

def anio_lanzamiento(registro: dict) -> int:
    ob_id= registro["OBJECT_ID"]
    if len(ob_id) < 4:
        print("Error: OBJECT_ID no tiene el formato esperado")
    anio= ob_id[:4]
    return int(anio)


def grupo(registro: dict) -> str:
    nombre= registro["OBJECT_NAME"]
    if len(nombre) < 1: 
        print("Error: OBJECT_NAME no tiene el formato correcto")
    for prefijo, grupete in grupos.items():
        if nombre.startswith(prefijo):
            return grupete
    return "Otros"
def nombre_satelite(registro: dict) -> dict:
    diccio= {}
    for register in registro: 
        nombres= register["OBJECT_NAME"]
        grupete = grupo(register)
        if grupete not in diccio: 
            diccio[grupete]= []
        diccio[grupete].append(nombres)
    return diccio

def contar_por_grupo(registro):
    cantidad={}
    for register in registro:   
        grupete= grupo(register)
        if grupete not in cantidad:
            cantidad[grupete]=0
        cantidad[grupete]+= 1
    return cantidad 

def lanzamientos_por_anio(registro):
    lanzamientos= {}
    for lanzamiento in registro:
        años= anio_lanzamiento(lanzamiento)
        if años not in lanzamientos:
            lanzamientos[años]= 0
        lanzamientos[años]+= 1
    return lanzamientos

if __name__ == "__main__":
    print("Prueba 1 del codigo")
    archivo= "datos/satelites.json"
    registros= leer_satelites(archivo)
    
    if registros:
        if isinstance(registros, list):
            satelite1= registros[0]
        else:
            satelite1= list(registros.values())[0]
        anio= anio_lanzamiento(satelite1)
        print(f"El primer satelite se lanzo en el año {anio}")
        g= grupo(satelite1)
        print(f"El primer satelite pertenece al grupo {g}")
        conteo= contar_por_grupo(registros)
        print("Resumen de contar por grupo")
        for nombre, cantidad in conteo.items():
            print(f"Hay {cantidad} satelites de {nombre}")
        
        lanzamientos= lanzamientos_por_anio(registros)
        print("Lanzamientos por año, de los primeros 15 años en orden")
        anios_ordenados= sorted(lanzamientos.keys())[:15]
        for a in anios_ordenados:
            print(f"En el Año {a}: hubo {lanzamientos[a]} lanzamientos")
    else: 
        print("-> No se pudo realizar la prueba porque la lista de registros está vacía o el archivo no existe.")