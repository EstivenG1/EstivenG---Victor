import pandas as pd
import glob
import matplotlib.pyplot as plt


# ============================================================
#                    BOT DE VENTAS
#       CONSOLIDACIÓN, LIMPIEZA Y ANÁLISIS
# ============================================================


# ============================================================
# 1. LECTURA INDIVIDUAL DE LOS ARCHIVOS
# ============================================================

print("\n")
print("============================================================")
print("                 LECTURA DE ARCHIVOS")
print("============================================================")


# -------------------------
# DATAFRAME MEDELLÍN
# -------------------------

print("\n--- DATAFRAME MEDELLÍN ---")

df_medellin = pd.read_csv(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_medellin.csv"
)

print(df_medellin.head(3))


# -------------------------
# DATAFRAME BOGOTÁ
# -------------------------

print("\n--- DATAFRAME BOGOTÁ ---")

df_bogota = pd.read_excel(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_bogota.xlsx"
)

print(df_bogota.head(3))


# -------------------------
# DATAFRAME BARRANQUILLA
# -------------------------

print("\n--- DATAFRAME BARRANQUILLA ---")

df_barranquilla = pd.read_excel(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_barranquilla.xlsx"
)

print(df_barranquilla.head(3))


# -------------------------
# DATAFRAME CALI
# -------------------------

print("\n--- DATAFRAME CALI ---")

df_cali = pd.read_csv(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\sucursal_cali.csv"
)

print(df_cali.head(3))


# ============================================================
# 2. MOSTRAR COLUMNAS DE CADA DATAFRAME
# ============================================================

print("\n")
print("============================================================")
print("                    COLUMNAS")
print("============================================================")


print("\nColumnas Bogotá:")
print(df_bogota.columns)


print("\nColumnas Medellín:")
print(df_medellin.columns)


print("\nColumnas Barranquilla:")
print(df_barranquilla.columns)


print("\nColumnas Cali:")
print(df_cali.columns)


# ============================================================
# 3. BUSCAR ARCHIVOS CSV Y XLSX
# ============================================================

print("\n")
print("============================================================")
print("              ARCHIVOS EN LA CARPETA")
print("============================================================")


# -------------------------
# ARCHIVOS CSV
# -------------------------

print("\n--- ARCHIVOS CSV ---")

archivos_csv = glob.glob(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\*.csv"
)

print(archivos_csv)


# -------------------------
# ARCHIVOS XLSX
# -------------------------

print("\n--- ARCHIVOS XLSX ---")

archivos_xlsx = glob.glob(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\*.xlsx"
)

print(archivos_xlsx)


# ============================================================
# 4. LEER TODOS LOS ARCHIVOS
# ============================================================

print("\n")
print("============================================================")
print("                 LECTURA DE ARCHIVOS")
print("============================================================")


lista_informes = []


# -------------------------
# LEER ARCHIVOS CSV
# -------------------------

for archivo in archivos_csv:

    df = pd.read_csv(archivo)

    lista_informes.append(df)

    print(
        "Leído:",
        archivo,
        "| Filas:",
        len(df)
    )


# -------------------------
# LEER ARCHIVOS XLSX
# -------------------------

for archivo in archivos_xlsx:

    df = pd.read_excel(archivo)

    lista_informes.append(df)

    print(
        "Leído:",
        archivo,
        "| Filas:",
        len(df)
    )


# ============================================================
# 5. NORMALIZAR LOS NOMBRES DE LAS COLUMNAS
# ============================================================

print("\n")
print("============================================================")
print("              NORMALIZACIÓN DE COLUMNAS")
print("============================================================")


for i, df in enumerate(lista_informes):

    if "Fecha_Venta" in df.columns:

        lista_informes[i] = df.rename(
            columns={
                "Fecha_Venta": "fecha",
                "Producto": "producto",
                "Cant": "cantidad",
                "Valor_Unitario": "precio_unitario",
                "Categoria": "categoria",
                "Vendedor": "vendedor",
                "Pago": "metodo_pago"
            }
        )


print("\nColumnas normalizadas correctamente.")


# ============================================================
# 6. CONSOLIDAR LOS DATAFRAMES
# ============================================================

print("\n")
print("============================================================")
print("                   CONSOLIDACIÓN")
print("============================================================")


df_consolidado = pd.concat(
    lista_informes,
    ignore_index=True
)


print("\nCantidad de archivos:")
print(len(lista_informes))


print("\nCantidad de registros:")
print(len(df_consolidado))


# ============================================================
# 7. LIMPIEZA DE DATOS
# ============================================================

print("\n")
print("============================================================")
print("                    LIMPIEZA")
print("============================================================")


# -------------------------
# ELIMINAR FILAS DUPLICADAS
# -------------------------

print("\n--- ELIMINACIÓN DE DUPLICADOS ---")

filas_antes = len(df_consolidado)

df_consolidado = df_consolidado.drop_duplicates()

filas_despues = len(df_consolidado)


print("Filas antes:", filas_antes)
print("Filas después:", filas_despues)

print(
    "Duplicados eliminados:",
    filas_antes - filas_despues
)


# -------------------------
# MOSTRAR VALORES NULOS
# -------------------------

print("\n--- VALORES NULOS ANTES DE LIMPIAR ---")

print(
    df_consolidado.isnull().sum()
)


# -------------------------
# RELLENAR VALORES NULOS
# -------------------------

print("\n--- RELLENANDO VALORES NULOS ---")

df_consolidado["producto"] = (
    df_consolidado["producto"].fillna("Desconocido")
)

df_consolidado["categoria"] = (
    df_consolidado["categoria"].fillna("Desconocido")
)

df_consolidado["vendedor"] = (
    df_consolidado["vendedor"].fillna("Desconocido")
)

df_consolidado["metodo_pago"] = (
    df_consolidado["metodo_pago"].fillna("Desconocido")
)

df_consolidado["cantidad"] = (
    df_consolidado["cantidad"].fillna(0)
)

df_consolidado["precio_unitario"] = (
    df_consolidado["precio_unitario"].fillna(0)
)

df_consolidado["fecha"] = (
    df_consolidado["fecha"].fillna("2024-01-01")
)


# -------------------------
# VERIFICAR VALORES NULOS
# -------------------------

print("\n--- VALORES NULOS DESPUÉS DE LIMPIAR ---")

print(
    df_consolidado.isnull().sum()
)


# ============================================================
# 8. GUARDAR RESULTADO CONSOLIDADO
# ============================================================

print("\n")
print("============================================================")
print("               GUARDAR ARCHIVO CONSOLIDADO")
print("============================================================")


df_consolidado.to_excel(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\consolidado_limpio.xlsx",
    index=False
)


print("\nArchivo guardado correctamente:")
print("consolidado_limpio.xlsx")


# ============================================================
#              ANÁLISIS DE NEGOCIO
# ============================================================

print("\n")
print("============================================================")
print("                 ANÁLISIS DE NEGOCIO")
print("============================================================")


# ============================================================
# 9. CALCULAR TOTAL DE CADA VENTA
# ============================================================

print("\n")
print("============================================================")
print("                 CÁLCULO DE VENTAS")
print("============================================================")


# Precio unitario x cantidad
df_consolidado["venta_total"] = (
    df_consolidado["precio_unitario"]
    * df_consolidado["cantidad"]
)


print("\nTotal de venta calculado correctamente.")


# ============================================================
# 10. PREGUNTA 1
# ¿CUÁNTO VENDIÓ CADA CATEGORÍA EN TOTAL?
# ============================================================

print("\n")
print("============================================================")
print("          PREGUNTA 1: VENTAS POR CATEGORÍA")
print("============================================================")


ventas_categoria = (
    df_consolidado
    .groupby("categoria")["venta_total"]
    .sum()
    .sort_values(ascending=False)
)


print("\nVentas por categoría:")
print(ventas_categoria)


# -------------------------
# GRÁFICO DE CATEGORÍAS
# -------------------------

plt.figure(figsize=(8, 5))

ventas_categoria.plot(
    kind="bar",
    title="Ventas por Categoría",
    color="steelblue"
)

plt.ticklabel_format(
    style="plain",
    axis="y"
)

plt.ylabel("Ventas totales ($)")
plt.xlabel("Categoría")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\grafico_categoria.png",
    dpi=150
)

plt.show()


print("\nGráfico generado: grafico_categoria.png")


# ============================================================
# 11. PREGUNTA 2
# ¿QUÉ PORCENTAJE DE LAS VENTAS REPRESENTA CADA VENDEDOR?
# ============================================================

print("\n")
print("============================================================")
print("          PREGUNTA 2: VENTAS POR VENDEDOR")
print("============================================================")


ventas_vendedor = (
    df_consolidado
    .groupby("vendedor")["venta_total"]
    .sum()
    .sort_values(ascending=False)
)


print("\nVentas por vendedor:")
print(ventas_vendedor)


# -------------------------
# CALCULAR PORCENTAJES
# -------------------------

porcentaje_vendedor = (
    ventas_vendedor / ventas_vendedor.sum()
) * 100


print("\nPorcentaje de ventas por vendedor:")
print(porcentaje_vendedor.round(2))


# -------------------------
# GRÁFICO DE VENDEDORES
# -------------------------

plt.figure(figsize=(8, 6))

ventas_vendedor.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    title="Porcentaje de Ventas por Vendedor"
)

plt.ylabel("")

plt.tight_layout()

plt.savefig(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\grafico_vendedor.png",
    dpi=150
)

plt.show()


print("\nGráfico generado: grafico_vendedor.png")


# ============================================================
# 12. PREGUNTA 3
# ¿CUÁL ES EL PRODUCTO QUE MÁS SE VENDE?
# ============================================================

print("\n")
print("============================================================")
print("          PREGUNTA 3: PRODUCTO MÁS VENDIDO")
print("============================================================")


producto_mas_vendido = (
    df_consolidado["producto"].value_counts()
)


print("\nCantidad de ventas por producto:")
print(producto_mas_vendido)


print(
    "\nEl producto que MÁS se vende es:",
    producto_mas_vendido.idxmax()
)

print(
    "Cantidad de transacciones:",
    producto_mas_vendido.max()
)


# ============================================================
# 13. PREGUNTA 4
# ¿CÓMO SE DISTRIBUYEN LAS VENTAS SEGÚN EL MÉTODO DE PAGO?
# ============================================================

print("\n")
print("============================================================")
print("          PREGUNTA 4: VENTAS POR MÉTODO DE PAGO")
print("============================================================")


ventas_metodo = (
    df_consolidado
    .groupby("metodo_pago")["venta_total"]
    .sum()
    .sort_values(ascending=False)
)


print("\nVentas por método de pago:")
print(ventas_metodo)


# -------------------------
# GRÁFICO DE MÉTODO DE PAGO
# -------------------------

plt.figure(figsize=(8, 5))

ventas_metodo.plot(
    kind="bar",
    title="Ventas por Método de Pago",
    color="teal"
)

plt.ticklabel_format(
    style="plain",
    axis="y"
)

plt.ylabel("Ventas totales ($)")
plt.xlabel("Método de pago")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\grafico_metodo_pago.png",
    dpi=150
)

plt.show()


print("\nGráfico generado: grafico_metodo_pago.png")


# ============================================================
# 14. PREGUNTA 5 - RETO OPCIONAL
# ¿CUÁL ES EL DÍA DE LA SEMANA CON MÁS VENTAS?
# ============================================================

print("\n")
print("============================================================")
print("          PREGUNTA 5 - RETO OPCIONAL")
print("============================================================")


# -------------------------
# CONVERTIR FECHA
# -------------------------

print("\nConvirtiendo fechas...")

df_consolidado["fecha"] = pd.to_datetime(
    df_consolidado["fecha"],
    dayfirst=True,
    errors="coerce"
)


# -------------------------
# OBTENER DÍA DE LA SEMANA
# -------------------------

df_consolidado["dia_semana"] = (
    df_consolidado["fecha"].dt.day_name()
)


# -------------------------
# TRADUCIR DÍAS AL ESPAÑOL
# -------------------------

mapa_dias = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}


df_consolidado["dia_semana_es"] = (
    df_consolidado["dia_semana"].map(mapa_dias)
)


# -------------------------
# ORDENAR LOS DÍAS
# -------------------------

orden_dias = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]


ventas_dia = (
    df_consolidado
    .groupby("dia_semana_es")["venta_total"]
    .sum()
    .reindex(orden_dias)
)


print("\nVentas por día de la semana:")
print(ventas_dia)


print(
    "\nEl día con MÁS ventas es:",
    ventas_dia.idxmax()
)

print(
    "Total vendido: $",
    f"{ventas_dia.max():,.0f}"
)


# -------------------------
# GRÁFICO POR DÍA
# -------------------------

plt.figure(figsize=(9, 5))

ventas_dia.plot(
    kind="bar",
    title="Ventas por Día de la Semana",
    color="coral"
)

plt.ticklabel_format(
    style="plain",
    axis="y"
)

plt.ylabel("Ventas totales ($)")
plt.xlabel("Día de la Semana")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "C:\\Users\\ADSO\\Documents\\EstivenG-Vixtor\\EstivenG - Vic\\grafico_dia_semana.png",
    dpi=150
)

plt.show()


print("\nGráfico generado: grafico_dia_semana.png")


# ============================================================
# 15. FINAL DEL PROGRAMA
# ============================================================

print("\n")
print("============================================================")
print("                 ANÁLISIS COMPLETADO")
print("============================================================")


print("\nArchivos generados:")

print("  - consolidado_limpio.xlsx")
print("  - grafico_categoria.png")
print("  - grafico_vendedor.png")
print("  - grafico_metodo_pago.png")
print("  - grafico_dia_semana.png")


print("\n============================================================")
print("                 FIN DEL PROGRAMA")
print("============================================================")