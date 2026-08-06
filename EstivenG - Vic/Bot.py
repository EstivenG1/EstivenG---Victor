import pandas as pd 
import glob

# Exploracion de ls datos y diferentes tipos de archivos
# .csv y .xlsx

print("========================================= DATAFRAME MEDELLIN ===============================================")
print("\n")

df_medellin = pd.read_csv("EstivenG - Vic/sucursal_medellin.csv")
print(df_medellin.head(3))  # Muestra las primeras 3 filas del DataFrame


print("========================================= DATAFRAME BOGOTA =================================================")
print("\n")

df_bogota = pd.read_excel("EstivenG - Vic/sucursal_bogota.xlsx")
print(df_bogota.head(3)) # Muestra las primeras 3 filas del DataFrame


print("========================================= DATAFRAME CALI ===================================================")
print("\n")

df_cali = pd.read_csv("EstivenG - Vic/sucursal_cali.csv")
print(df_cali.head(3)) # Muestra las primeras 3 filas del DataFrame


print("========================================= DATAFRAME BARRANQUILLA ===========================================")
print("\n")

df_barranquilla = pd.read_excel("EstivenG - Vic/sucursal_barranquilla.xlsx")
print(df_barranquilla.head(3)) # Muestra las primeras 3 filas del DataFrame


print("\n")
print("\n")
print("\n")


print("========================================= COLUMNA DATAFRAME BOGOTA ========================================")
print(df_bogota.columns)
print("\n")

print("========================================= COLUMNA DATAFRAME MEDELLIN ======================================")
print(df_medellin.columns)
print("\n")

print("========================================= COLUMNA DATAFRAME CALI ==========================================")
print(df_cali.columns)
print("\n")

print("========================================= COLUMNA DATAFRAME BARRANQUILLA ==================================")
print(df_barranquilla.columns)
print("\n")




#Agrupar archivos por tipo .csv y .xlsx

archivos_csv = glob.glob("*.csv")
archivos_xlsx = glob.glob("*.xlsx")

print("========================================= ARCHIVOS CSV ===================================================")
print(archivos_csv)
print("\n")
print("========================================= ARCHIVOS XLSX ===================================================")
print(archivos_xlsx)
print("\n")


# UNIFICAR COLUMNAS DE LOS DATAFRAMES
LISTA_INFORMES = []



for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    LISTA_INFORMES.append(df)
    print(f"Leidos: {archivo} - {len(df)} filas")
    

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    LISTA_INFORMES.append(df)
    print(f"Leidos: {archivo} - {len(df)} filas")



# UNIFICAR LOS DATAFRAMES EN UNO SOLO

df_unificado = pd.concat(LISTA_INFORMES, ignore_index=True)
print(df_unificado.head(3))



for i, df in enumerate(LISTA_INFORMES):
    if "fecha_Venta" in df.columns:
        LISTA_INFORMES[i] = df.rename(columns={
            "Fecha_Venta": "fecha",
            "Producto": "producto",
            "categoria": "categoria",
            "Cantidad": "cantidad",
            "Valor_Unitario": "precio_unitario",
            "Vendedor": "vendedor",
            "Pago": "metodo_pago"
        })


df_consolidado = pd.concat(LISTA_INFORMES, ignore_index=True)
print(df_consolidado)



