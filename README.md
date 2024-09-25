# newspapertomp3

**newspapertomp3** es una herramienta de conversión que permite extraer texto de artículos web y convertirlo en archivos de audio. Utiliza el paquete **newspaper3k** para extraer el contenido de los artículos y **Coqui TTS** (Text-to-Speech) para generar los archivos de audio en formato **mp3**.

### Características

- Extrae automáticamente texto de artículos web.
- Convierte el texto extraído en audio utilizando **Coqui TTS**.
- Soporte para idioma español (puede ser extendido a otros idiomas).
- Interfaz gráfica para facilitar la interacción con la herramienta.

### Requisitos

Antes de comenzar, asegúrate de tener instaladas las siguientes dependencias:

- **Python 3.x**
- **newspaper3k**
- **Coqui TTS**
- **NLTK**
- **Tkinter** (para la interfaz gráfica)

Instala todas las dependencias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

Instalación
Clona el repositorio:
```bash
git clone https://github.com/mario-sound/newspapertomp3.git
cd newspapertomp3
```

## Instala las dependencias:
``` bash
pip install -r requirements.txt
```

Configura el entorno NLTK (necesario para tokenización y limpieza del texto):
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Configura Coqui TTS (si no está ya configurado):
Sigue las instrucciones en la documentación oficial de Coqui TTS para configurar y descargar los modelos TTS en español.

Uso
1. Uso desde la línea de comandos
Para convertir un artículo web en un archivo de audio, utiliza el siguiente comando:

```bash
python coqui_tool.py "https://example.com/articulo"
```
Esto descargará el contenido del artículo, lo procesará y generará un archivo de audio en formato mp3 que se guardará en la carpeta output/.


2. Uso con la Interfaz Gráfica
Puedes lanzar la interfaz gráfica utilizando Tkinter para facilitar la conversión sin necesidad de usar la línea de comandos:

```bash
python UI_tool.py
```

La interfaz te permitirá introducir la URL del artículo y seleccionar las configuraciones necesarias para convertir el texto en audio.
Estructura del Proyecto

```text
newspapertomp3/
│
├── __pycache__/
├── audio/               # Contiene varios audios para pruebas.
├── metadata/            # Contiene información de los audios.
├── output/              # Contiene los archivos mp3 generados.
├── TTS/                 # Carpeta de soporte para Coqui TTS.
├── nltk_tool.py         # Procesamiento del texto (limpieza y segmentación).
├── newspaper3k_tool.py  # Herramienta para extraer texto de artículos.
├── coqui_tool.py        # Herramienta para convertir texto a mp3 utilizando Coqui TTS.
├── UI_tool.py           # Interfaz gráfica con Tkinter.
├── README.md            # Este archivo.
└── requirements.txt     # Archivo con las dependencias necesarias.
```

## Funcionalidades en Desarrollo
Mejoras en la interfaz gráfica: Se está trabajando para hacer la interfaz más intuitiva y estética.
Integración con más servicios de TTS: Evaluación de otros motores TTS como Google TTS para comparar la calidad del audio generado.

## Ejemplos
Conversión de un artículo en mp3
```
bash
python coqui_tool.py "https://es.wikipedia.org/wiki/Inteligencia_artificial"
```

El archivo de salida estará en la carpeta output/ con un nombre basado en la fecha y hora de la conversión.

## Contribuciones
Si quieres colaborar con el proyecto, por favor sigue los siguientes pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Haz commit de tus cambios (git commit -m 'Añadir nueva funcionalidad').
Sube la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
## Licencia

MIT License

Copyright (c) 2024 Mario Sánchez Molina

Por la presente se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para tratar en el Software sin restricciones, incluidos, entre otros, los derechos de usar, copiar, modificar, fusionar, publicar, distribuir, y permitir a las personas a quienes se les proporcione el Software que lo hagan, **únicamente para fines personales o educativos**, sujeto a las siguientes condiciones:

**No se permite el uso del Software para fines comerciales sin el permiso expreso del titular del copyright.**

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN CONTRACTUAL, AGRAVIO O DE OTRO TIPO, QUE SURJA DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.
