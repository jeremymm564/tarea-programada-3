from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw
import os
import xlsxwriter


def procesar_imagenes():
    """
    Procesa todas las imágenes de la carpeta 'imagenes_entrada'.

    La función:
    - Lee imágenes JPG y PNG.
    - Las redimensiona a un máximo de 800x800 píxeles.
    - Las convierte a escala de grises.
    - Agrega una marca de agua.
    - Guarda las imágenes procesadas en la carpeta 'imagenes_salida'.

    Retorna:
        list: Lista con la información necesaria para generar el reporte.
    """

    os.makedirs("imagenes_salida", exist_ok=True)

    datos_reporte = []

    for archivo in os.listdir("imagenes_entrada"):

        if not archivo.lower().endswith((".jpg", ".png")):
            continue

        print(archivo)

        ruta_imagen = os.path.join("imagenes_entrada", archivo)

        imagen = Image.open(ruta_imagen)

        formato = imagen.format

        ancho_original, alto_original = imagen.size

        imagen.thumbnail((800, 800))

        imagen = ImageOps.grayscale(imagen)

        dibujo = ImageDraw.Draw(imagen)

        dibujo.text(
            (imagen.width - 120, imagen.height - 40),
            "agencia de fotos",
            fill=255
        )

        ruta_salida = os.path.join("imagenes_salida", archivo)

        imagen.save(ruta_salida)

        datos_reporte.append([
            archivo,
            formato,
            ancho_original,
            alto_original,
            "Procesada"
        ])

    return datos_reporte


def generar_reporte(datos_reporte):
    """
    Genera un archivo Excel con la información de las imágenes procesadas.

    Parámetros:
        datos_reporte (list): Lista con el nombre, formato,
        dimensiones originales y estado de cada imagen.
    """

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


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    """

    datos = procesar_imagenes()
    print(datos)
    generar_reporte(datos)