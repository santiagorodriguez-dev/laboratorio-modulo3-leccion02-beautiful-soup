## Contexto

**Descripción:**

SetMagic Productions es una empresa especializada en la provisión de servicios integrales para la realización de rodajes cinematográficos y audiovisuales. Nos dedicamos a facilitar tanto el atrezzo necesario para las producciones como los lugares idóneos para llevar a cabo los rodajes, ya sea en entornos al aire libre o en interiores.

**Servicios Ofrecidos:**

- **Atrezzo Creativo:** Contamos con un extenso catálogo de atrezzo que abarca desde accesorios hasta muebles y objetos temáticos para ambientar cualquier tipo de  escena.

- **Locaciones Únicas:** Nuestra empresa ofrece una amplia selección de locaciones, que incluyen desde escenarios naturales como playas, bosques y montañas, hasta espacios interiores como estudios, casas históricas y edificios emblemáticos.
- **Servicios de Producción:** Además de proporcionar atrezzo y locaciones, también ofrecemos servicios de producción audiovisual, incluyendo equipos de filmación, personal técnico y servicios de postproducción.

**Herramientas y Tecnologías:**

Para recopilar información sobre nuevas locaciones y tendencias en atrezzo, utilizamos herramientas de web scraping como Beautiful Soup y Selenium para extraer datos de sitios web relevantes y redes sociales especializadas en cine y producción audiovisual. También integramos APIs de plataformas de alquiler de locaciones y bases de datos de atrezzo para acceder a información actualizada y detallada.

**Almacenamiento de Datos:** (A trabajar la próxima semana)

La información recopilada mediante web scraping y APIs se almacenará tanto en una base de datos relacional SQL como en una base de datos no relacional MongoDB . Estas base de datos nos permite organizar eficientemente la información sobre locaciones, atrezzo, clientes y proyectos en curso, facilitando su acceso y gestión.

**Objetivo:**

Nuestro objetivo principal es proporcionar a nuestros clientes una experiencia fluida y personalizada en la búsqueda y selección de locaciones y atrezzo para sus proyectos audiovisuales. Utilizando tecnologías avanzadas y una amplia red de contactos en la industria, nos esforzamos por ofrecer soluciones creativas y de alta calidad que satisfagan las necesidades específicas de cada producción.


## Lab: Extracción de Información con Beautiful Soup

En este laboratorio seguirás enriqueciendo la base de datos para ofrecer a tus clientes un servicio más completo y personalizado. Para lograr esto, extraerás información valiosa sobre objetos de atrezzo de una web especializada. Utilizarás técnicas de web scraping con la biblioteca **Beautiful Soup** para obtener y organizar los datos de manera eficiente.

Trabajarás con la siguiente URL: [Atrezzo Vázquez](https://atrezzovazquez.es/shop.php?search_type=-1&search_terms=&limit=48&page=1). Esta página contiene una gran cantidad de objetos de atrezzo que pueden ser de interés para un proyecto de rodaje. Tu tarea será extraer información relevante de los productos listados en las primeras 100 páginas.

1. **Navegación y Extracción de Múltiples Páginas**:

   - La página web contiene varios elementos distribuidos en distintas páginas. Tu objetivo será iterar a través de las 100 primeras páginas y extraer la información deseada.

   - Debes asegurarte de que tu código sea capaz de navegar automáticamente por estas páginas y extraer datos de manera continua.

2. **Verificación del Código de Estado de la Respuesta**:

   - Antes de extraer cualquier información, es fundamental verificar que la solicitud a la página web ha sido exitosa. Un código de estado 200 indica que la página se ha cargado correctamente.

   - Si el código no es 200, debes imprimir un mensaje de error y detener la ejecución de la extracción para evitar problemas posteriores.

3. **Extracción de Información Específica**:

   De cada página, deberás extraer los siguientes detalles de los objetos de atrezzo:

   - **Nombre del Objeto**: El nombre o identificador del objeto.

   - **Categoría**: La categoría en la que se clasifica el objeto (ej.: mobiliario, decorado, utilería, etc.).

   - **Sección**: La sección específica dentro de la categoría.

   - **Descripción**: Una breve descripción del objeto que puede incluir detalles sobre su estilo, material o uso.

   - **Dimensiones**: El tamaño del objeto en formato (largo x ancho x alto).

   - **Enlace a la Imagen**: El link a la imagen del objeto, útil para tener una vista previa visual.

4. **Organización de los Datos en un Diccionario**:

   Una vez extraída la información, deberás organizarla en un diccionario con las siguientes claves:

   - `"nombre"`: Nombres del objeto.

   - `"categoria"`: Categoría a la que pertenece el objeto.

   - `"seccion"`: Sección específica dentro de la categoría.

   - `"descripcion"`: Breve descripción del objeto.

   - `"dimensiones"`: Dimensiones del objeto en el formato adecuado.

   - `"imagen"`: URL de la imagen del objeto.

5. **Almacenamiento de la Información en un DataFrame**:

   Una vez que tengas toda la información organizada en diccionarios, el siguiente paso es convertirla en un DataFrame de Pandas. Este DataFrame te permitirá manipular y analizar los datos con facilidad. Tu DataFrame debería verse similar al ejemplo proporcionado, donde cada fila representa un objeto diferente y cada columna contiene la información extraída:

![Dataframe](https://github.com/Hack-io-Data/Imagenes/blob/main/02-Imagenes/BS/df_atrezzo.png?raw=true)


6.  Consideraciones Adicionales:

- Asegúrate de manejar posibles errores o excepciones durante el scraping, como tiempos de espera agotados, páginas inaccesibles o datos faltantes.

- Recuerda que el scraping debe hacerse de manera respetuosa, evitando sobrecargar el servidor de la página web (puedes usar pausas entre solicitudes).

- Finalmente, asegúrate de almacenar el DataFrame en un archivo CSV para que puedas reutilizar esta información en análisis futuros.
