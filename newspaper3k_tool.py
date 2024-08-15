import newspaper
import nltk
from urllib.parse import urlparse

# Descargar el paquete 'punkt' para tokenización (necesario para algunas funcionalidades de newspaper3k)
nltk.download('punkt', quiet=True) 

def extract_article(url):
    """
    Extrae información relevante de un artículo en línea.

    Args:
        url (str): La URL del artículo.

    Returns:
        dict: Un diccionario con los datos extraídos: título, autores, fecha de publicación y texto completo.

    Raises:
        ValueError: Si la URL proporcionada no es válida.
        RuntimeError: Si ocurre un error al descargar o analizar el artículo.
    """

    # Verificar si la URL es válida
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]): 
        raise ValueError("La URL proporcionada no es válida.")

    # Crear el objeto de artículo
    article = newspaper.Article(url) 

    # Descargar y analizar el artículo
    try:
        article.download()  # Descargar el contenido HTML de la página
        article.parse()     # Analizar el HTML para extraer la información relevante
    except Exception as e:
        # Capturar cualquier error que pueda ocurrir durante la descarga o análisis
        raise RuntimeError(f"Error al procesar el artículo: {e}") 

    # Extraer datos y devolverlos en un diccionario
    return {
        'titulo': article.title,
        'autores': article.authors,
        'fecha_publicacion': article.publish_date,
        'texto': article.text
    }