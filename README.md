# ProyectoDemoApis

# Para ver este proyecto en funcionamiento visitar este link 

#### Para poder ejectuar este proyecto se debe de tener instalado python, ademas es requerido instalar ciertas librerias y paquetes que son necesarios para el correcto funcionamiento del proyecto. A continuación se listan los comandos para instalar dichas librerias y paquetes. Adicionalmente se debe de tener un entorno virtual:

# Entorno virtual windows: 
* python -m venv env
* .\env\Scripts\activate

# Entorno virtual MacOS:
* python3 -m venv env
* source env/bin/activate

# Instalaciones de paquetes:
* pip install -r requirements.txt


##### Como nota importante, en el archivo settings donde se configura la base de datos, se deben de poner los datos correspondientes a sus credenciales y el nombre del servidor local que tengan en su PC.



    'default': {
        'ENGINE': 'mssql',
        'NAME':'C_CDATABASE',
        'USER': 'NOMBRE_USUARIO_INICIO_SESION_SQL_SERVER',
        'PASSWORD': 'CONTRASEÑA_INICIO_SESION_SQL_SERVER',
        'HOST': 'NOBRE_SERVIDOR_LOCAL',  
        'PORT': '',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        },
