import os
from gtts import gTTS
import subprocess
import newspaper3k_tool as nw3k
from datetime import datetime
import logging

# Configurar el registro de errores
logging.basicConfig(filename='gtts_errors.log', level=logging.ERROR)

# Ruta donde se guardarán los archivos de audio generados
save_path = ''

if not save_path.endswith(os.path.sep):
    save_path += os.path.sep

# Generar un nombre de archivo único basado en la fecha y hora actual
audio_filename = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'

def convert_text_to_mp3(text, audio_filename=f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.mp3', speedup_audio_filename=f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_speedup.mp3', speed_factor=1.2, lang='es', save_path=''):
    """
    Convierte texto a un archivo MP3 y crea una versión acelerada.

    Args:
        text (str): El texto a convertir.
        audio_filename (str, optional): Nombre del archivo MP3 normal. Por defecto, se genera un nombre basado en la fecha y hora.
        speedup_audio_filename (str, optional): Nombre del archivo MP3 acelerado.
        speed_factor (float, optional): Factor de aceleración de la velocidad. Por defecto, 1.2.
        lang (str, optional): Idioma para la conversión de texto a voz. Por defecto, 'es' (español).

    Raises:
        ValueError: Si el texto está vacío.
    """

    # Verificar si el texto no está vacío
    if not text.strip():
        raise ValueError("El texto está vacío, no se puede generar el archivo de audio.")

   # Asegurarse de que los nombres de archivo sean únicos
    audio_filename = ensure_unique_filename(os.path.join(save_path, audio_filename))
    speedup_audio_filename = ensure_unique_filename(os.path.join(save_path, speedup_audio_filename))

    try:
        # Generar el audio normal
        generate_audio(text, audio_filename, lang)

        # Acelerar el audio
        speed_up_audio(audio_filename, speedup_audio_filename, speed_factor)

    except Exception as e:
        # Registrar el error en el archivo de registro
        logging.error(f"Error al generar o modificar el archivo de audio: {e}")
        raise  # Volver a lanzar la excepción para que el programa principal pueda manejarla si es necesario

def ensure_unique_filename(filename):
    """
    Asegura que el nombre de archivo sea único, añadiendo un sufijo numérico si es necesario.

    Args:
        filename (str): El nombre de archivo original.

    Returns:
        str: El nombre de archivo único.
    """
    base_name, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_name}_{counter:02d}{extension}"
        counter += 1
    return filename

def generate_audio(text, filename, lang='es'):
    """
    Genera un archivo de audio MP3 a partir de texto.

    Args:
        text (str): El texto a convertir.
        filename (str): Nombre del archivo MP3 de salida.
        lang (str, optional): Idioma para la conversión de texto a voz. Por defecto, 'es' (español).
    """
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    print(f"Archivo de audio guardado exitosamente como '{filename}'.")

def speed_up_audio(input_filename, output_filename, speed_factor):
    """
    Acelera un archivo de audio MP3 utilizando ffmpeg.

    Args:
        input_filename (str): Nombre del archivo MP3 de entrada.
        output_filename (str): Nombre del archivo MP3 de salida acelerado.
        speed_factor (float): Factor de aceleración de la velocidad.
    """
    command = [
        'ffmpeg', '-i', input_filename,
        '-filter:a', f'atempo={speed_factor}',
        output_filename
    ]
    subprocess.run(command, check=True)
    print(f"Archivo de audio con velocidad ajustada guardado como '{output_filename}'.")