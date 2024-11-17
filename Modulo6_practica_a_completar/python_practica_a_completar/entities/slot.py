from datetime import datetime

class Slot:
    def __init__(self):
        self.id = None
        self.fecha_inicial = None
        self.fecha_final = None

    def asigna_vuelo(self, id, fecha_llegada, fecha_despegue):
        self.id = id
        self.fecha_inicial = datetime.strptime(fecha_llegada, "%d/%m/%Y %H:%M")
        self.fehca_final = datetime.strptime(fecha_despegue, "%d/%m/%Y %H:%M")

    def slot_esta_libre_fecha_determinada(self, fecha_llegada):
        if self.fecha_inicial is None or self.fecha_final is None:
            return 0 # El slot esta libre por que no tiene fechas asignadas
        fecha_llegada = datetime.strptime(fecha_llegada, "%d/%m/%Y %H:%M")
        if fecha_llegada < self.fecha_inicial or fecha_llegada >=self.fecha_final:
            return 0 # el slot estara libre al al esta fuera del rando fecha inicial, fecha final
        else:
            tiempo_restante = self.fecha_final - fecha_llegada
            return tiempo_restante #Devuelve el tiempo restante para que quede libre el slot
 

 