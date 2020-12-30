# SAP

>Comandos utiles para el uso del ORM

Despues de construir la clase Modelo ejercutar para ver migraciones que se ejecutaran ✔

```python
python manage.py makemigrations
```

Para revisar en consola el sql que se ejecutara podemos usar el siguiente comando 😉

```python
python manage.py sqlmigrate nombre-de-app nombre-de-migracion
```

Crea la tabla ejcutando las migraciones

```python
python manage.py migrate
```

Podemos usar la migracion de Admin para manejar los modelos, primero creamos el super usuario
```python
python manage.py createsuperuser
```
Ahora solo debemos acceder al path /admin
