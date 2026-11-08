# Actividad de usuarios de GitHub

Herramienta de línea de comandos que muestra la actividad pública reciente de
un usuario de GitHub. Utiliza únicamente la biblioteca estándar de Python para
consultar la API de GitHub.

## Ejecución

```powershell
python .\main.py <nombre_de_usuario>
```

Por ejemplo:

```powershell
python .\main.py kamranahmedse
```

También puedes indicar las rutas completas del intérprete de Python y del
script:

```powershell
& "C:\Path\To\python.exe" "C:\Path\To\GitHub User Activity\main.py" kamranahmedse
```

La herramienta muestra un resumen por cada evento reciente. Si el usuario no
existe, la API no está disponible o GitHub limita las solicitudes, se mostrará
un mensaje de error y el comando finalizará con un código distinto de cero.