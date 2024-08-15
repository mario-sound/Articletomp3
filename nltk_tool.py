import nltk
import newspaper3k_tool as nw3k
from dateutil import tz
import locale

# Configurar la localización a español para formatear la fecha correctamente
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para Linux/MacOS
# locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para Windows

# Descargar recursos necesarios para NLP (si aún no los tienes)
nltk.download('punkt', quiet=True) 
nltk.download('stopwords', quiet=True)

def format_text(url):
    """
    Formatea el texto extraído de un artículo para su conversión a audio.

    Args:
        url (str): La URL del artículo.

    Returns:
        str: El texto formateado, listo para ser convertido a audio.
    """

    try:
        # Obtener los datos del artículo
        data = nw3k.extract_article(url)

        # Lista para acumular el texto formateado
        tomp3 = []

        # Agregar el título si existe
        if data.get('titulo', ''):
            tomp3.append(data['titulo'])

        # Agregar los autores si existen, uniéndolos en una cadena
        if data.get('autores', []):
            tomp3.append(', '.join(data['autores'])) 

        # Limpieza y segmentación del texto del artículo
        if data.get('texto', ''):
            texto_limpio = limpiar_texto(data['texto'])
            parrafos = segmentar_texto(texto_limpio)
            tomp3.extend(parrafos)  # Agregar cada párrafo a la lista

        # Unir la lista en una sola cadena y realizar reemplazos para mejorar la pronunciación
        tomp3 = ' '.join(tomp3)
        tomp3 = tomp3.replace('ń', 'ñ')  # Reemplazar caracteres problemáticos

        # Agregar la fecha de publicación formateada si existe
        if data.get('fecha_publicacion', None):
            fecha_formateada = data['fecha_publicacion'].strftime('%d de %B de %Y, %H:%M %Z')
            tomp3 += f"\n\nArtículo publicado a fecha: {fecha_formateada}"

        return tomp3

    except ValueError as e:
        return f"Error: {e}"  # Manejar errores de URL inválida
    except RuntimeError as e:
        return f"Error al procesar el artículo: {e}"  # Manejar otros errores de extracción

def limpiar_texto(texto):
    """
    Realiza una limpieza básica del texto, eliminando stop words y caracteres no deseados.

    Args:
        texto (str): El texto a limpiar.

    Returns:
        str: El texto limpio.
    """

    # Tokenizar el texto en palabras
    palabras = nltk.word_tokenize(texto)

    # Eliminar stop words en español
    stop_words = set(nltk.corpus.stopwords.words('spanish'))
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]

    # Unir las palabras filtradas en una cadena
    texto_limpio = ' '.join(palabras_filtradas)

    return texto_limpio

def segmentar_texto(texto):
    """
    Segmenta el texto en párrafos.

    Args:
        texto (str): El texto a segmentar.

    Returns:
        list: Una lista de párrafos.
    """

    # Dividir el texto en párrafos utilizando saltos de línea dobles
    parrafos = texto.split('\n\n')

    # Eliminar párrafos vacíos o muy cortos
    parrafos = [parrafo for parrafo in parrafos if parrafo.strip() and len(parrafo) > 20]

    return (parrafos)