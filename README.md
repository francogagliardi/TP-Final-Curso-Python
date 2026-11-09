# TP Final - Curso Python

El trabajo está dividido en 3 ejercicios. Cada uno se ejecuta por separado y no dependen entre sí.

## Requisitos

- Python 3
- Django 6.1.3 (solo para el ejercicio 3)
- pytest (solo para los tests del ejercicio 3)

```bash
pip install django pytest
```

Si usás el entorno virtual del repo, activalo antes:

```bash
venv\Scripts\activate
```

---

## Ejercicio 1 - Sensores

```bash
cd ejercicio_1_sensores
python main.py
```

Muestra por pantalla los sensores con registros sucios, la versión limpia/estandarizada, los sensores en alerta (más de 25°C) y la temperatura promedio.

---

## Ejercicio 2 - Productos

```bash
cd ejercicio_2_productos
python main.py
```

Prueba el manejo de excepciones con un stock inválido y exporta el catálogo a `catalogo_ecotech.json` (se genera en la misma carpeta).

---

## Ejercicio 3 - Auditoría y panel web

Este es el más completo: tiene los tests del cálculo de emisiones y el panel en Django.

### 3.1 Tests unitarios

```bash
cd ejercicio_3_auditoria_web
python -m pytest sustentabilidad/test_emisiones.py -v
```

Los tests validan:

- El cálculo de emisiones con valores nominales (`consumo * factor`, con factor por defecto 0.4).
- Que se lance `ValueError` si el consumo es negativo.

### 3.2 Levantar el servidor Django

```bash
cd ejercicio_3_auditoria_web
python manage.py runserver
```

En la terminal Django va a mostrar algo así:

```
Starting development server at http://127.0.0.1:8000/
```

Esa URL ya abre el panel directamente. También se puede entrar por `http://127.0.0.1:8000/panel/`, que es la misma vista.

El panel muestra el total de emisiones (18240.0 kg CO2) y las plantas con mayor consumo.

El admin de Django está en `http://127.0.0.1:8000/admin/`, pero pide un usuario creado antes con `python manage.py createsuperuser`.

Para cortar el servidor: `Ctrl + C`.

### Cómo funciona el flujo

`vista_panel_sustentabilidad` (en `sustentabilidad/views.py`) arma una lista de registros de prueba, llama a `obtener_metricas_consumo` (en `sustentabilidad/emisiones.py`) y le pasa el total de emisiones y las plantas de mayor consumo a la plantilla `sustentabilidad/panel.html`.
