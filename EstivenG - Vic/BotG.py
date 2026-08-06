import pandas as pd
import glob

print("=================================== DATAFRAME MEDELLIN =====================================")

df_medellin = pd.read_csv("C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_medellin.csv")
print(df_medellin.head(3))

print("\n")
print("=================================== DATAFRAME BOGOTA =======================================")
print("\n")

df_bogota = pd.read_excel("C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_bogota.xlsx")
print(df_bogota.head(3))


print("\n")
print("================================== DATAFRAME BARRANQUILLA ===================================")
print("\n")

df_barranquilla = pd.read_excel("C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_barranquilla.xlsx")
print(df_barranquilla.head(3))


print("\n")
print("====================================== DATAFRAME CALI ========================================")
print("\n")

df_cali = pd.read_csv("C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_cali.csv")
print(df_cali.head(3))

print("\n")
print("====================================== COLUMNAS BOGOTA =======================================")
print("\n")

print(df_bogota.columns)

print("\n")
print("====================================== COLUMNAS MEDELLIN =======================================")
print("\n")


print(df_medellin.columns)

print("\n")
print("==================================== COLUMNAS BARRANQUILLA =====================================")
print("\n")

print(df_barranquilla.columns)

print("\n")
print("======================================== COLUMNAS CALI =========================================")

print(df_cali.columns)

print("\n")
print("======================================== ARCHIVOS CSV ===========================================")
print("\n")

archivos_csv = glob.glob("C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\*.csv")

print(archivos_csv)

print("\n")
print("======================================== ARCHIVOS XLSX ==========================================")

archivos_xlsx = glob.glob("C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\*.xlsx")

print(archivos_xlsx)

print("\n")

print("========================================= LEER ARCHIVOS ==========================================")

print("\n")

lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)

    print(f"Leidos: {archivo} - {len(df)} filas")
    print("\n")

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_informes.append(df)
    
    print(f"Leidos: {archivo} - {len(df)} filas")
    print("\n")
    
print("========================================= CONSOLIDAR ==========================================")

print("\n")
  
for i, df in enumerate(lista_informes):
    if "Fecha_Venta" in df.columns:
        lista_informes[i] = df.rename(columns={
            "Fecha_Venta": "fecha", "Producto": "producto", 
            "Cant": "cantidad", "Valor_Unitario": "precio_unitario", 
            "Categoria": "categoria", "Vendedor": "vendedor", "Pago": "metodo_pago"
        })
                                    
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(df_consolidado)


print("\n")
print("========================================== LIMPIEZA ==========================================")

# 4a. Eliminar filas duplicadas
filas_antes = len(df_consolidado)
df_consolidado = df_consolidado.drop_duplicates()
print(f"Filas antes: {filas_antes} - despues: {len(df_consolidado)}")

# 4b. Explorar valores nulos ANTES de decidir que hacer
print(df_consolidado.isnull().sum())

# 4c. Rellenar segun el tipo de columna
df_consolidado["cantidad"] = df_consolidado["cantidad"].fillna(0)
df_consolidado["precio_unitario"] = df_consolidado["precio_unitario"].fillna(0)

df_consolidado["producto"] = df_consolidado["producto"].fillna("Desconocido")
df_consolidado["categoria"] = df_consolidado["categoria"].fillna("Desconocido")
df_consolidado["vendedor"] = df_consolidado["vendedor"].fillna("Desconocido")
df_consolidado["metodo_pago"] = df_consolidado["metodo_pago"].fillna("Desconocido")

# Si la columna fecha tiene nulos, rellenamos con la fecha más frecuente
if "fecha" in df_consolidado.columns and df_consolidado["fecha"].isnull().any():
    moda_fecha = df_consolidado["fecha"].mode()
    if len(moda_fecha) > 0:
        df_consolidado["fecha"] = df_consolidado["fecha"].fillna(moda_fecha[0])

print("\n")
print("========================================== NULOS ==========================================")

print("Nulos después de rellenar:")
print(df_consolidado.isnull().sum())


# --------------------------------------------
# PARTE 5: Guardar el resultado
# --------------------------------------------
df_consolidado.to_excel("consolidado_limpio.xlsx", index=False)
print("Archivo guardado")
    
    
    