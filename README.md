# Gestión de Datos de Países 

**Trabajo Práctico Integrador (TPI) — Programación 1 - UTN**


---

## Descripción

Aplicación de consola en Python que permite gestionar un dataset de países cargado desde un archivo CSV. Implementa filtros, búsquedas, ordenamientos y estadísticas utilizando listas, diccionarios y funciones.

---

## Integrantes

Fabricio Emanuel Diaz Cornejo
Tomas Agostino D’Inca Ponte
---

## Requisitos

- Archivo `paises.csv` en el mismo directorio que `main.py`

---

## Cómo ejecutar

```bash
python main.py
```

---

## Estructura del proyecto

```
tpi_paises/
├── main.py        # Código principal
├── paises.csv     
└── README.md      
```

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Mostrar todos los países |
| 2 | Agregar un nuevo país |
| 3 | Actualizar población y/o superficie |
| 4 | Buscar por nombre (parcial o exacto) |
| 5 | Filtrar por continente, rango de población o superficie |
| 6 | Ordenar por nombre, población o superficie (asc/desc) |
| 7 | Estadísticas generales |
| 8 | Guardar cambios en el CSV |
| 0 | Salir (con opción de guardar) |

---

## Estructura del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

---

## Ejemplos de uso

### Buscar un país
```
Seleccione una opción: 4
Ingrese el nombre o parte del nombre: arg

  Resultados para 'arg'
  ──────────────────────────────────────────────────────────────────────
  Nombre                              | Población       | Superficie   | Continente
  ──────────────────────────────────────────────────────────────────────
  • Argentina                         |      45,376,763 |    2,780,400 km² | América
  Total: 1 país/es
```

### Filtrar por continente
```
Seleccione una opción: 5
  1. Por continente
Opción: 1
Continente: Europa

  Países en 'Europa'  → muestra todos los países europeos del dataset
```

### Estadísticas
```
Seleccione una opción: 7

  ESTADÍSTICAS GENERALES
  Población más alta : China (1,412,600,000)
  Población más baja : Nueva Zelanda (5,122,600)
  Promedio de población  : 93,123,456
  Promedio de superficie : 1,234,567 km²

  Países por continente:
    África                   : 7
    América                  : 11
    América del Norte        : 2
    Asia                     : 11
    Europa                   : 10
    Oceanía                  : 3
```

---

## Video 

>  _https://youtu.be/-fRVQhQROjc_


---
