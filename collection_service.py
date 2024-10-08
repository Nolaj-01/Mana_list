import pandas as pd
import os
import shutil

class Config:
    """Establece la configuración general"""

    def copia_coleccion():
        """Hace una copia en el directorio del programa de la base de datos"""
        
        # Busca el archivo CSV en el escritorio independientemente del sistema operativo PENDIENTE DE ACTUALIZAR EN EL PASO A APLICACION
        directorio_usuario = os.path.expanduser('~')
        if os.name == 'nt': # Para Windows
            escritorio = os.path.join(directorio_usuario, 'Desktop')
        else: # Para macOS o Linux
            escritorio = os.path.join(directorio_usuario, 'Escritorio')

        print("\t---No existe un archivo de colección, sigue las instrucciones para importarlo---")
        print("-Coloca el archivo a importar en el escritorio")
        try:
            orden = input("-A continuación introduce el nombre del archivo (sin extensión): ")
        except FileExistsError:
            print(f"\t**El archivo {orden} no eciste, inténtelo de nuevo**")

        # Copia la colección en la base de datos del programa
        origen = os.path.join(escritorio, orden + '.csv')
        destino = 'coleccion.csv'
        shutil.copy(origen, destino)

    def cargar_coleccion():
        """Carga la colección"""
        ruta = 'coleccion.csv'
        try:
            df = pd.read_csv(ruta) # Intentar cargar el CSV
            return df
        except Exception as e:
            print(f"Error al cargar el archivo {e}")
            return None
        
    def comprobar_csv(ruta):
        """Verificar si la ruta proporcionada es un archivo CSV válido"""
        try:
            pd.read_csv(ruta) # Intentar cargar el CSV para verificar si es válido
            return True
        except Exception:
            return False

    def actualizar_coleccion():
        """Actualiza el archivo de la colección"""
        directorio_usuario = os.path.expanduser('~')
        if os.name == 'nt': # Para Windows
            escritorio = os.path.join(directorio_usuario, 'Desktop')
        else: # Para macOS o Linux
            escritorio = os.path.join(directorio_usuario, 'Escritorio')

        print("Coloca el nuevo archivo de la colección en el escritorio")
        orden = input("Introduce el nombre del nuevo archivo CSV (sin extension): ")

        # Definir origen y destino
        origen = os.path.join(escritorio, orden + '.csv')
        destino = 'coleccion.csv'
        
        # Realizar la copia (sobreescribiendo el archivo actual)
        try:
            shutil.copy(origen, destino)
            print(f"\nColección actualizada con el archivo {origen}.")
        except FileNotFoundError:
            print(f"\nEl archivo {origen} no se encontró. Verifica el nombre.")
        except Exception as e:
            print(f"\nOcurrió un error al intentar actualizar la colección: {e}")

    def cargar_o_pedir_coleccion():
        df = Config.cargar_coleccion()

        if df is not None:
            return df
        else:
            Config.copia_coleccion()
            return Config.cargar_coleccion()