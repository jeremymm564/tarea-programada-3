from PIL import Image
import os
from PIL import ImageOps
from PIL import ImageDraw
import xlsxwriter


#creamos la carpeta donde se guardan las imagenes procesadas
os.makedirs("imagenes_salida", exist_ok=True)

datos_reporte = []


#recorremos todos los archivos de la carpeta de entrada
for archivo in os.listdir("imagenes_entrada"):
    

    if not archivo.lower().endswith((".jpg", ".png")):
        continue
    print(archivo)

    ruta_imagen = os.path.join("imagenes_entrada", archivo)

    imagen = Image.open(ruta_imagen)

    formato = imagen.format

    ancho_original, alto_original = imagen.size

# reducimos la imagen a un maximo de 800x800 manteniendo la proporcion
    imagen.thumbnail((800, 800))
# convertimos la imagen a escala de grises
    imagen = ImageOps.grayscale(imagen)

# creamos un dbujo marca de agua
    dibujo = ImageDraw.Draw(imagen)

# agregamos una marca de agua en la esquina inferior derecha
    dibujo.text(
    (imagen.width - 120, imagen.height - 40),
    "agencia de fotos",
    fill=255)
    # guardamos la imagen procesada en la carpeta de salida
    ruta_salida = os.path.join("imagenes_salida", archivo)

    imagen.save(ruta_salida)
    
    datos_reporte.append([
        archivo,
        formato,
        ancho_original,
        alto_original,
        "Procesada"
    ])
print(datos_reporte)


#creamos el archivo para excel
workbook = xlsxwriter.Workbook("reporte_imagenes.xlsx")
worksheet = workbook.add_worksheet()

encabezados = [
    "Nombre del archivo",
    "Formato",
    "Ancho original",
    "Alto original",
    "Estado"
]

for columna, encabezado in enumerate(encabezados):
    worksheet.write(0, columna, encabezado)

for fila, datos in enumerate(datos_reporte, start=1):

    for columna, valor in enumerate(datos):

        worksheet.write(fila, columna, valor)

workbook.close()

print("Reporte Excel generado correctamente.")