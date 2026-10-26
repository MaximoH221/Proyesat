 

class Satelite:

    def __init__(self, nombre, latitud, longitud, altitud_km):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altitud_km = altitud_km

    def tipo_orbita(self): # Despues exporto desde funciones
        return "LEO"  # Valor temporal de prueba

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
