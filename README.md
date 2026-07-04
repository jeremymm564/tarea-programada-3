# Generador de Catálogos e Informes de Imágenes

## Descripción

Este proyecto fue desarrollado en Python para automatizar el procesamiento de imágenes.

El programa realiza las siguientes funciones:

- Lee imágenes en formato JPG y PNG desde una carpeta de entrada.
- Redimensiona cada imagen a un tamaño máximo de 800x800 píxeles manteniendo la relación de aspecto.
- Convierte las imágenes a escala de grises.
- Agrega una marca de agua en la esquina inferior derecha.
- Guarda las imágenes procesadas en una carpeta de salida.
- Genera un archivo Excel (`reporte_imagenes.xlsx`) con la información de las imágenes procesadas.

## Requisitos

- Python 3
- Pillow
- XlsxWriter

## Instalación

Instale las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecute el programa con:

```bash
python main.py
```

## Autor

Jeremy Montoya Martinez