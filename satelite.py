from funciones_base import obtener_posicion, crear_objeto_skyfield
class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""
        self.nombre= nombre
        self.latitud= latitud
        self.longitud= longitud
        self.altitud_km= altitud_km
    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""
        if self.altitud_km <2000:
            return "LEO"
        elif 2000<= self.altitud_km < 34000:
            return "MEO"
        elif 34000<= self.altitud_km <= 37000: 
            return "GEO"
        elif self.altitud_km > 37000: 
            return "HEO"  
    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""
        lon_min, lat_min, lon_max, lat_max = zona
        return (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max)
    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""
        tipo= self.tipo_orbita()
        return f"{self.nombre} | {tipo} | {self.altitud_km} km"

def crear_satelites(registros, momento):
    """
    Devuelve una lista de satelites con su posicion en "momento", descartando satelites caidos
    """
    lista= []
    for registro in registros:
        objeto= crear_objeto_skyfield(registro)
        latitud, longitud, altitud= obtener_posicion(objeto, momento)
        if altitud >= 100: 
            nombre= registro.get("OBJECT_NAME", "Desconocido")
            satelite= Satelite(nombre, latitud, longitud, altitud)
            lista.append(satelite)
    return lista