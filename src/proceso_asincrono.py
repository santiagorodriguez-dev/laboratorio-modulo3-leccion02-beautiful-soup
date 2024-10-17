# Importamos las librerías que necesitamos

# Librerías de extracción de datos
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore
import sys
from tqdm import tqdm # type: ignore
import asyncio
import requests # type: ignore
import time

sys.path.append("../")
from src import soporte as sp
# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd # type: ignore

async def tratar_datos(url):
        df_productos_paginas = pd.DataFrame()
        status = ''
        print(f"1.Inicio llamada {url}")
        try:
            url_imagen = "https://atrezzovazquez.es/"
            url_no_imagen = "https://atrezzovazquez.es/img/logo.png"
            res = requests.get(url)
            status = res.status_code
            print(f"2. status code: {status}")
            if res.status_code == 200:
                sopa = BeautifulSoup(res.content, "html.parser")
                if (len(sopa)!= 0):
                    elementos = sopa.findAll("div", {"class": "col-md-3 col-sm-4 shop-grid-item"})

                    for e in elementos:
                        df_temp = pd.DataFrame()
                        ele = BeautifulSoup(str(e), "html.parser")
                            
                        nombre = sp.get_data_elemento_text(ele, 'a', 'class', 'title')
                        categoria = sp.get_data_elemento_text(ele, 'a', 'class', 'tag')
                        seccion = sp.get_data_elemento_text(ele, 'div', 'class', 'cat-sec')
                        descripcion = sp.get_data_elemento_text(ele, 'div', 'class', 'article-container style-1')
                        dimensiones = sp.get_data_elemento_text(ele, 'div', 'class', 'price')
                        imagen = sp.get_data_elemento_imagen(ele, 'src', url_imagen, url_no_imagen)

                        df_temp = sp.create_dataframe(nombre, categoria, seccion, descripcion, dimensiones, imagen)
                        df_productos_paginas = pd.concat([df_productos_paginas, df_temp])
        except:
            print(f"4. error en la llamada {url}, status code: {status}")

        print(f"5.fin llamada {url}")
        return df_productos_paginas


async def main():
    start_time = time.time()
    url_base = "https://atrezzovazquez.es/shop.php?search_type=-1&search_terms=&limit=48&page={}"
    
    # Creamos una lista de tareas para realizar solicitudes a 100 páginas
    tareas = []

    for i in range(1, 101):
        url = url_base.format(i)
        tareas.append(tratar_datos(url))

    lista_resultado = await asyncio.gather(*tareas)

    df = pd.DataFrame()

    for i, r in enumerate(lista_resultado, 1):
            df_temp = pd.DataFrame(r)
            df = pd.concat([df, df_temp])
            df.reset_index(drop=True, inplace=True)

    print(f"cantidad {df.shape[0]}")
    print(df.head())

    end_time = time.time()
    print(f"\nEl scrapeo TOTAL duró {end_time - start_time:.2f} segundos.")

# Ejecutar el script de manera asíncrona
if __name__ == "__main__":
    asyncio.run(main())
