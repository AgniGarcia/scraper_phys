# scraper_phys
scraper de phys.org


En éste repositorio podrán encontrar dos versiones de desarrollo de scrapping al sitio web https://phys.org/

Una desarrollo utilizando el Framework Scrapy para la extracción de la información

Para correr el código y obtener un formato JSON de los datos extraídos es necesario instalar scrapy en un ambiente virtual donde se ubique el script, y con el comando 'scrapy crawl articles' se generará el archivo que contiene la información de phys.org

Con una iteración recursiva se obtendrá dicha información de las más recientes 8 notas de la página de inicio de https://phys.org/. Cambiando el xpath para abarcar más secciones es posible, para extraer la página en su totalidad.

Altamente recomiendo antes leer https://phys.org/robots.txt para tener claro los permisos de scrapping que otorga el sitio web, aunque una de las grandes ventajas que nos ofrece Scrapy como Framework es que respeta robots.txt en automático, con una serie de configuraciones que podemos encontrar en settings.py
