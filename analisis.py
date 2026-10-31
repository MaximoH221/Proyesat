from catalogo import grupos
from satelite import Satelite


def contar_por_tipo(satelites):
    """devuelve un diccionario {"LEO": n, "MEO": n, "GEO": n, "HEO": n},
    con las cuatro claves siempre presentes ( 0 si no hay satélites de ese tipo)."""

    # Creo el diccionario
    mi_dicc = {"LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}

    for satelite in satelites:
        tipo = satelite.tipo_orbita()

        mi_dicc[tipo] += 1
    return mi_dicc

def mas_bajo(satelites):
    """devuelve el objeto Satelite de menor altitud."""

    # Que revise segun el parametro de altitud:km
    return min(satelites, key=lambda sat: sat.altitud_km)

def mas_alto(satelites):
    """devuelve el objeto Satelite de mayor altitud."""
    return max(satelites, key=lambda sat: sat.altitud_km)

def en_zona(satelites, zona):
    """devuelve una lista de los satélites dentro de la zona 
    (usando el método esta_en_zona)."""

    # Creacion de la variable
    mi_list = []

    for satelite in satelites:
        # El metodo esta_en_zona devuelve un booleano
        if satelite.esta_en_zona(zona):
            mi_list.append(satelite)

    return mi_list

def ordenar_por(satelites, atributo, descendente=False):
    """ función genérica que devuelve una lista nueva ordenada por cualquier atributo
    ("altitud_km", "latitud", "nombre", ...). """
    return sorted(satelites, key=lambda sat: getattr(sat, atributo), reverse= descendente)

def top_n(satelites, n, mas_altos=True):
    """devuelve los n satélites más altos
    (o más bajos), reutilizando ordenar_por"""

    mi_lista = ordenar_por(satelites, "altitud_km", descendente=mas_altos)
    return mi_lista[:n]


def resumen_por_grupo(satelites):
    """Usando grupo de catalogo.py, devuelve un diccionario 
    con un resumen de las altitudes de cada grupo."""
    
    mi_dicc = {}
    
    for sat in satelites:
        prefijo = sat.nombre.split('-')[0].upper()
        nombre_grupo = grupos.get(prefijo, "Otros")
        
        if nombre_grupo not in mi_dicc:
            mi_dicc[nombre_grupo] = [sat.altitud_km]
        else:
            mi_dicc[nombre_grupo].append(sat.altitud_km)
            
    resumen_final = {}
    
    for grupo, lista_altitudes in mi_dicc.items():
        cantidad = len(lista_altitudes)
        minima = min(lista_altitudes)
        maxima = max(lista_altitudes)
        media = sum(lista_altitudes) / cantidad
        
        resumen_final[grupo] = {
            "cantidad": cantidad,
            "minima": round(minima, 2), # Redondeado a 2 decimales por prolijidad
            "media": round(media, 2),
            "maxima": round(maxima, 2)
        }
        
    return resumen_final

def lanzamientos_desde_2015(satelites):
    """
    Devuelve un diccionario con los lanzamientos por año (desde 2015)
    de los satélites que están activos.
    """
    lanzamientos= {}
    for sat in satelites:
        if sat.anio >= 2015:
            if sat.anio not in lanzamientos:
                lanzamientos[sat.anio] = 0
            lanzamientos[sat.anio] += 1
    return lanzamientos 
def resumen_altitudes_por_grupo(satelites):
    """
    Calcula un resumen (cantidad, altitud mínima, máxima y promedio) 
    para cada tipo de órbita de los satélites activos.
    """
    resumen = {}
    for sat in satelites:
        tipo = sat.tipo_orbita()
        if tipo not in resumen:
            resumen[tipo] = {"altitudes": [], "cantidad": 0}
        resumen[tipo]["altitudes"].append(sat.altitud_km)
        resumen[tipo]["cantidad"] += 1
    
    # Procesamos los datos finales para cada grupo
    resultado_final = {}
    for tipo, datos in resumen.items():
        alts = datos["altitudes"]
        resultado_final[tipo] = {
            "Cantidad": datos["cantidad"],
            "Altitud Mínima (km)": round(min(alts), 2),
            "Altitud Máxima (km)": round(max(alts), 2),
            "Altitud Promedio (km)": round(sum(alts) / len(alts), 2)
        }
    return resultado_final