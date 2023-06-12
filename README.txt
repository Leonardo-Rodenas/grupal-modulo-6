# ABPro - Trabajo Grupal 5

## Aplicación: "Telovendo" 

### Descripción

Nuestra aplicación "Telovendo" es una aplicación web desarrollada en Django que permite a los usuarios registrarse, realizar login/logout e ingresar información sobre 
distintos proveedores susceptibles a colaborar con nuestra empresa. Toda la información es guardada en una base de datos de sqlite3 y administrada por el panel de control de Django.

### Funcionalidades

- Registro de usuarios: Registro simple, mediante nombre de usuario y contraseña (solicita repetir contraseña, si no son ambas iguales el registro no es válido). Validación en nombre de 
  usuario (150 caracteres como máximo. Únicamente usar letras, dígitos y @/./+/-/_ ) y contraseña (valida que la contraseña no posea atributos similares a información provista por el usuario, 
establece un largo mínimo de 8 caracteres, no puede ser una contraseña común, ejemplo 1234, e impide contraseñas completamente numéricas).
- Inicio de sesión de usuarios: Si el registro es exitoso, el usuario puede acceder a una página exclusiva (de otro modo inaccesible) con un saludo personalizado con su nombre de usuario. Si se 
  intenta entrar a esta página sin iniciar sesión, ocurre una redirección automática que redirige al usuario a la página de login
- Cierre de sesión de usuarios: Cierre de sesión una vez iniciada. El botón para realizar esta acción se encuentra en la pagina de saludo personalizado post-login.
- Registro de proveedores: Registro vía web rellenando un formulario con los datos del proveedor
- Vista de los últimos usuarios registrados: Visualización de usuarios registrados sin necesidad de utilizar el panel de control provisto por Django
- Interfaz intuitiva y fácil de usar: Interfaz sencilla, minimalista y con el contenido justo para no sobresaturar ni entorpecer el uso de la aplicación.

### Requisitos del sistema

- Python 3.11.3
- Django 4.2.1
- DBeaver (o cualquier otro cliente de base de datos que maneje sqlite)
- Navegador web de su preferencia.
- Conexión estable de internet
- dependencias necesarias para la aplicación se encuentran en archivo requirements.txt

### Instrucciones de instalación

1. Clona el repositorio de la aplicación desde GitHub:

   git clone https://github.com/Leonardo-Rodenas/grupal-modulo-6

2. Accede al directorio del proyecto:

3. Crea un entorno virtual e instala las dependencias desde requeriments.txt :

   python -m venv (nombre de tu entorno virtual)
   .(nombre de tu entorno virtual)\scripts\activate.bat   <-- Ejecutar dentro del directorio del proyecto
   pip install -r requirements.txt

4. Configura la base de datos:

   - Crea una base de datos en PostgreSQL y actualiza la configuración en el archivo `settings.py`.
   - Si deseas puedes utilzar la base datos por defecto (sqlite3) que trae la aplicación.

5. Aplica las migraciones:

   python manage.py makemigrations
   python manage.py migrate

6. Inicia el servidor local:

   python manage.py runserver

8. Abre tu navegador web y visita `http://localhost:8000` para acceder a la aplicación.

### Contribuciones

¡Se agradecen las contribuciones a "Telovendo"! Si deseas colaborar, sigue estos pasos:

1. Crea un fork del repositorio
2. Crea una rama para tu nueva función o corrección de error: `git checkout -b nombre-rama`
3. Realiza tus modificaciones y asegúrate de escribir pruebas adecuadas.
4. Realiza un commit de tus cambios: `git commit -m "Descripción de los cambios"`
5. Envía tus cambios al repositorio remoto: `git push origin nombre-rama`
6. Abre una solicitud de extracción en GitHub para que revisemos tus cambios.

### Soporte

Si tienes alguna pregunta, problema o sugerencia, no dudes en contactarnos a través de la sección de "Issues" en GitHub o enviando un correo electrónico a soporte@telovendo.com.

¡Gracias por utilizar "Telovendo"!