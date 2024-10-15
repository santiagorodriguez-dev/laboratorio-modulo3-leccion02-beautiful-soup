# Importamos las librerías que necesitamos
# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd # type: ignore

def get_data_elemento_text(elemento, p1, p2 ,p3):
    """
    Obtiene el texto de un elemento HTML específico, manejando posibles errores.

    La función busca dentro del elemento proporcionado todas las etiquetas que coinciden con el nombre de etiqueta y el atributo
    especificado, y devuelve el texto del primer elemento encontrado. Si ocurre un error (por ejemplo, si la etiqueta o el atributo
    no se encuentran), la función devuelve una cadena vacía.

    Args:
        elemento (bs4.element.Tag): El elemento HTML que se va a analizar.
        p1 (str): El nombre de la etiqueta HTML a buscar.
        p2 (str): El nombre del atributo del elemento HTML.
        p3 (str): El valor del atributo del elemento HTML.

    Returns:
        str: El texto del primer elemento encontrado, con ajustes de formato. Si no se encuentra o ocurre un error, devuelve una cadena vacía.
    """
    try:
        for v in elemento.findAll(p1, {p2: p3}):
            return v.getText().replace("\xa0\xa0"," ").strip()
    except:
        return ""

def get_data_elemento_imagen(elemento, p1, ruta, no_image):
    """
    Obtiene la URL completa de una imagen a partir de un elemento HTML, con una opción alternativa en caso de error.

    La función busca la primera etiqueta 'img' dentro del elemento proporcionado y obtiene el valor del atributo
    especificado para construir la URL completa utilizando la ruta base. Si ocurre un error (por ejemplo, la etiqueta
    'img' no está presente o el atributo no se encuentra), se devuelve un valor alternativo especificado por el
    parámetro `no_image`.

    Args:
        elemento (bs4.element.Tag): El elemento HTML que contiene la imagen.
        p1 (str): El nombre del atributo de la etiqueta 'img' que contiene la URL parcial.
        ruta (str): La ruta base que se añadirá al valor del atributo para formar la URL completa.
        no_image (str): El valor a devolver en caso de que no se pueda obtener la URL de la imagen.

    Returns:
        str: La URL completa de la imagen si se encuentra el atributo; de lo contrario, el valor especificado por `no_image`.
    """
    try:
        return ruta + elemento.findAll('img')[0].get(p1).strip()
    except:
        return no_image
    

def create_dataframe(nombre,categoria,seccion,descripcion,dimensiones,imagen):
    """
    Crea un DataFrame de pandas con los datos proporcionados.

    Crea un DataFrame con una fila que contiene la información especificada sobre un objeto,
    con columnas correspondientes a nombre, categoría, sección, descripción, dimensiones e imagen.

    Args:
        nombre (str): El nombre del objeto.
        categoria (str): La categoría del objeto.
        seccion (str): La sección a la que pertenece el objeto.
        descripcion (str): La descripción del objeto.
        dimensiones (str): Las dimensiones del objeto.
        imagen (str): La URL de la imagen del objeto.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene los datos proporcionados.
    """

    d = {'': [nombre, categoria, seccion, descripcion, dimensiones, imagen]}
    cols = ['nombre', 'categoria', 'seccion', 'descripcion', 'dimensiones', 'imagen']

    return  pd.DataFrame.from_dict(d, orient='index', columns=cols)