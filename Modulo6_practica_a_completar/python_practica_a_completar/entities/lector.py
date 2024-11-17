import csv
import json
import pandas as pd
#Creamos la clase Padre LECTOR.
class Lector:
    def __init__(self, path: str):  
        self.path = path
    # definimos una funcion para comprobar que la extension de los archivos esta permitida.
    # si no lo esta da error, si esta permitida no hace nada
    def _comprueba_extension(self, extension):
        if not self.path.endswith(extension):
            raise ValueError(f"El archivo debe tener la extension {extension}")
    # empezamos a leer los archivos, lo primero que hacemos es pasarle _comprueba_extension
    # para saber si tiene un formato permitido
    def lee_archivo(self):
        self._comprueba_extension(".txt", ".csv", ".json")

        if self.path.endswith(".txt"):
            return self._lee_txt()
        elif self.path.endswith(".csv"):
            return self._lee_csv()
        elif self.path.endswith(".json"):
            return self._lee_json()
    # definimos funciones para poder leer cada uno de las extensiones permitidas, txt, csv y json
    def _lee_txt(self):
        with open (self.path, "r", encoding="utf-8") as txtfile:
            return txtfile.read()
    
    def _lee_csv(self):
        with open (self.path, "r", newline = " ", encoding = "utf-8") as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]
    
    def _lee_json(self):
        with open (self.path, "r", encoding = "utf-8") as jsonfile:
            return json.load(jsonfile)
    # este metodo convierte informacion recivida en forma de diccionarios a archivos CSV.
    @staticmethod
    def convierte_dict_a_csv(data: dict, output_path: str):
        with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data.keys())
            writer.writerow(data.values())


class LectorCSV(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        self._comprueba_extension(".csv")
        df = pd.read_csv(self.path)
        return df


class LectorJSON(Lector):
    def __init__(self, path: str):
        super().__init__(path)
    
    def lee_archivo(self):
        self._comprueba_extension(".json")
        with open(self.path, "r", encoding = "utf-8") as jsonfile:
            return json.load(jsonfile)



class LectorTXT(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        self._comprueba_extension(".txt")
        with open(self.path, "r", encoding = "utf-8") as txtfile:
            return txtfile.read()



lector_csv = LectorCSV('/home/cornaco/Documentos/Proyecto aeropuerto/Modulo6_practica_a_completar/python_practica_a_completar/data/vuelos_2.csv')
contenido_csv = lector_csv.lee_archivo()
print(contenido_csv)


print ("____________________________________")


lector_json = LectorJSON('/home/cornaco/Documentos/Proyecto aeropuerto/Modulo6_practica_a_completar/python_practica_a_completar/data/vuelos_3.json')
contenido_json = lector_json.lee_archivo()
print(contenido_json)


print ("_________________________________")

lector_txt = LectorTXT('/home/cornaco/Documentos/Proyecto aeropuerto/Modulo6_practica_a_completar/python_practica_a_completar/data/vuelos_1.txt')
contenido_txt = lector_txt.lee_archivo()
print(contenido_txt)



datos = {
    'Nombre': 'María',
    'Edad': 25,
    'Ciudad': 'Madrid'
}

# Convertir el diccionario en un archivo CSV
Lector.convierte_dict_a_csv(datos, 'datos_usuario.csv')
