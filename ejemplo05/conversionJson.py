import csv
import json

# Ruta del archivo CSV
csv_file = 'atp_tennis.csv'

# Ruta de salida JSON
json_file = 'datos.json'

# Claves fijas (columnas)
columnas = [
    "Tournament", "Date", "Series", "Court", "Surface", "Round", "Best of",
    "Player_1", "Player_2", "Winner", "Rank_1", "Rank_2", "Pts_1", "Pts_2",
    "Odd_1", "Odd_2", "score"
]

# Lista para almacenar los objetos (registros)
datos = {"docs": []}

# Leer el CSV
with open(csv_file, mode='r', encoding='latin1') as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    # Saltar encabezado si está presente en CSV
    encabezado = next(lector)
    
    # Iterar por cada fila
    for fila in lector:
        fila_dict = {col: fila[i] for i, col in enumerate(columnas)}
        datos["docs"].append(fila_dict)

# Guardar como JSON
with open(json_file, mode='w', encoding='utf-8') as archivo_json:
    json.dump(datos, archivo_json, indent=4, ensure_ascii=False)

print(f"Listo: se procesaron {len(datos['docs'])} registros.")
