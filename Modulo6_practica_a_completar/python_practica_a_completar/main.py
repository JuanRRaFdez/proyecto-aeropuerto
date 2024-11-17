import os
import pandas as pd
from entities.lector import LectorTXT, LectorCSV, LectorJSON
from entities.slot import Slot

def preprocess_data(df_list):
    combined_df = pd.concat(df_list, ignore_index = True)
    return combined_df


if __name__ == '__main__':
    path_1 = os.path.abspath('./data/vuelos_1.txt')
    path_2 = os.path.abspath('./data/vuelos_2.csv')
    path_3 = os.path.abspath('./data/vuelos_3.json')
    
    lector_txt = LectorTXT(path_1)
    df_txt = lector_txt.lee_archivo()
    print("Contenido del archivo TXT:")
    print(df_txt)
    
    lector_csv = LectorCSV(path_2)
    df_csv = lector_csv.lee_archivo()
    print("Contenido del archivo CSV:")
    print(df_csv)
    
    lector_json = LectorJSON(path_3)
    df_json = lector_json.lee_archivo()
    print("Contenido del archivo JSON:")
    print(df_json)
    
    # Preprocesar los datos
    df_list = [df_txt, df_csv, df_json]
    df_final = preprocess_data(df_list)
    print("Datos combinados y preprocesados:")
    print(df_final)
    
    # Ejemplo de asignación de vuelos a slots
    slots = []
    for _, vuelo in df_final.iterrows():
        slot = Slot()
        slot.asigna_vuelo(vuelo["id"], vuelo["fecha_llegada"], vuelo["fecha_llegada"])  # Ejemplo simple, puedes ajustar las fechas según tu lógica
        slots.append(slot)

    # Mostrar información de los slots
    for slot in slots:
        print(slot)









