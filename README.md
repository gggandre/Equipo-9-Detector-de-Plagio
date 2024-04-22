# Equipo-9-Detector-de-Plagio

Este proyecto es un sistema de detección de plagio diseñado para analizar textos y determinar el grado de similitud entre ellos. Utiliza técnicas básicas de procesamiento de lenguaje natural (NLP) sin depender de bibliotecas de aprendizaje automático avanzadas, ideal para entornos educativos y académicos.

## Estructura del Proyecto

La estructura del proyecto se organiza de la siguiente manera:


![image](https://github.com/gggandre/Equipo-9-Detector-de-Plagio/assets/84719490/3ed64b91-de56-47d4-abc8-616b5ca16910)

## Configuración del Entorno

Antes de ejecutar el proyecto, asegúrate de tener Python instalado en tu sistema. Este proyecto fue desarrollado utilizando Python 3.8.

### Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando en la raíz del proyecto:

bash:
```pip install -r requirements.txt```

## Ejecución de Pruebas
Para ejecutar las pruebas unitarias y asegurar que cada componente funcione correctamente, utiliza el siguiente comando:
```python -m unittest discover -s tests```

## Uso del Sistema
### Ejecutar la Interfaz Gráfica
Para iniciar la interfaz gráfica del sistema de detección de plagio, ejecuta el script main.py ubicado en la carpeta src/. Puedes hacerlo desde la línea de comandos como sigue:
```python main.py```

## Guía Paso a Paso para la Interfaz
1. **Cargar Documentos:** Al iniciar la aplicación, verás un botón Load Documents. Haz clic en este botón para abrir un diálogo donde podrás seleccionar uno o más documentos de texto (.txt) que deseas analizar.
2. **Verificar Plagio:** Una vez cargados los documentos, presiona el botón Check Plagiarism. Esto procesará los documentos y mostrará los resultados de similitud entre cada par de documentos cargados en la interfaz.
3. **Resultados:** Los resultados se mostrarán en el área de texto principal de la interfaz, indicando el porcentaje de similitud entre los documentos.

## Salida de Resultados
Los resultados de las comparaciones también se guardarán automáticamente en archivos en el directorio results/, tanto en formato de texto plano como en Excel, para su revisión posterior.

## Clonar Repositorio
Para obtener una copia local del proyecto y empezar a trabajar con él, sigue estos pasos:

1. Abre una terminal en tu computadora.
2. Asegúrate de tener Git instalado. Puedes verificarlo ejecutando `git --version`. Si no tienes Git instalado, puedes descargarlo e instalarlo desde [Git - Downloads](https://git-scm.com/downloads).
3. Clona el repositorio utilizando el siguiente comando:

bash:
   ```git clone https://github.com/gggandre/Equipo-9-Detector-de-Plagio.git```

## Vídeo demo:
https://github.com/gggandre/Equipo-9-Detector-de-Plagio/assets/84719490/42d6ead5-e046-4010-84f8-f4205e9c2070

