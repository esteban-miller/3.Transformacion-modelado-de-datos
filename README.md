# Transformación y Modelado de Datos con Python

Este repositorio contiene dos ejercicios completos centrados en la transformación, limpieza y análisis de datos utilizando Python y pandas. Cada uno aborda datasets reales y aplica múltiples técnicas de preprocesamiento para preparar los datos de cara a futuros análisis.

---

## 🚢 Ejercicio 1: Dataset del Titanic

### 📝 Descripción

Este ejercicio se enfoca en la limpieza y transformación del dataset del Titanic. A partir de un archivo Excel, se realizan múltiples operaciones de procesamiento: imputación de valores nulos, creación de nuevas columnas, filtrado, clasificación y análisis exploratorio de variables clave como edad, tarifa, clase, género y más.

### 📂 Archivos incluidos

- `Titanic.xlsx`  
  Dataset original del Titanic.  
- `ejercicio_titanic.py`  
  Script con el desarrollo completo del ejercicio.  
- `Enunciado - Titanic.pdf`  
  Documento con las instrucciones del proyecto.

---

## 🏬 Ejercicio 2: Análisis de Ventas Multilocales

### 📝 Descripción

Este segundo ejercicio analiza las ventas de la cadena "VentasExpress", que opera en cinco ubicaciones: Barcelona, Valencia, Pozuelo, Mallorca y Malasaña. A través de cinco datasets individuales se realiza un análisis integral que abarca comportamiento de ventas, descuentos, productos más vendidos, precios, patrones temporales, y clientes compartidos.

### 📂 Archivos incluidos

- `barcelona.xlsx`  
- `valencia.xlsx`  
- `pozuelo.xlsx`  
- `mallorca.xlsx`  
- `malasaña.xlsx`  
  Conjuntos de datos individuales por ubicación.  
- `Proyecto de Análisis de Ventas Multilocales.pdf`  
  Enunciado oficial con objetivos y preguntas de análisis.  
- `Módulo_3_FINAL.ipynb`  
  Notebook con el desarrollo completo del análisis en Python.

---

## 🔍 Tareas realizadas

- Limpieza avanzada de datos (relleno de nulos, detección de errores, homogenización de campos)
- Creación de columnas derivadas:
  - `is_discounted`
  - `%_descuento`
  - `ganancia_neta`
  - `categoria_venta` (Alta, Media, Baja)
- Análisis temporal por día, mes, año y día de la semana
- Comparación de precios entre ubicaciones
- Agrupaciones y cálculos por producto, cliente, fecha y tienda
- Análisis de descuentos y su impacto en ingresos
- Identificación de productos más vendidos por ubicación y periodo
- Clasificación de clientes por comportamiento y presencia en distintas tiendas
- Visualizaciones de ventas, productos destacados, márgenes y distribución de ingresos

---

## 🛠️ Habilidades aplicadas

- Python (pandas, numpy)
- Limpieza y preprocesamiento de datos
- Análisis exploratorio y agrupaciones (`groupby`, `agg`)
- Filtrado condicional avanzado (`isin`, `between`, condiciones múltiples)
- Creación de columnas calculadas y categorización
- Visualización de datos con gráficos (matplotlib / seaborn)
- Uso de Jupyter Notebook para desarrollo y presentación

---

## 👤 Autor

**Esteban Miller**  
Proyectos realizados como parte de mi formación en análisis de datos.
