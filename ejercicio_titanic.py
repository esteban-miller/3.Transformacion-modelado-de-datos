# =============================================================================
# SESION 4 - EJERCICIOS CLASE GRUPAL
# Integrantes:
# - Esteban Miller
# - Sergio Martin
# - Roberto De Gouveia 
# - Jaquelin Da Costa 
# =============================================================================
import pandas as pd
from unidecode import unidecode
import re

data= pd.read_excel("C:/Users/jaque/Documents/IMMUNE/Modulo3/sesion4/Ejercicio_grupal/Titanic.xlsx")


# =============================================================================
# 1. Ordena el DataFrame del Titanic por la columna 'Age' de forma
# ascendente.
# =============================================================================
data_asc = data.sort_values("Age",ascending=1)

# =============================================================================
# 2. Ordena el DataFrame del Titanic por las columnas 'Pclass' y 'Age' de
# forma ascendente.
# =============================================================================
data_asc2= data.sort_values(["Pclass","Age"],ascending=[1,1])


# =============================================================================
# 3. Crea una nueva columna llamada 'Adult' que sea True si la edad es
# mayor o igual a 18, y False de lo contrario.
# =============================================================================
data['Adult'] = data['Age'] >= 18


# =============================================================================
# 4. Crea una nueva columna llamada 'Family_size' que sea la suma de las
# columnas 'SibSp' y 'Parch’.
# =============================================================================
data['Family_size'] = data['SibSp'] + data['Parch'] 


# =============================================================================
# 5. Filtra el DataFrame para mostrar solo las filas donde 'Fare' esté entre
# 50 y 100, inclusive.
# =============================================================================
databetween= data.loc[data.Fare.between(50,100)]


# =============================================================================
# 6. Crea una nueva columna llamada 'Class_high' que sea True si 'Pclass'
# es 1, y False de lo contrario.
# =============================================================================


# =============================================================================
# 7. Filtra el DataFrame para mostrar solo las filas donde 'Embarked' sea 'C'
# o 'Q'. (Usando ISIN)
# =============================================================================

# =============================================================================
# 8. Rellena los valores faltantes en la columna 'Age' con la media de esa
# columna.
# =============================================================================

# =============================================================================
# 9. Crea una nueva columna llamada 'Has_Cabin' que sea True si 'Cabin'
# no es nulo, y False de lo contrario.
# =============================================================================

# =============================================================================
# 10. Ordena el DataFrame del Titanic por 'Fare' de forma descendente.
# =============================================================================


# =============================================================================
# 11. Crea una nueva columna llamada 'Is_Alone' que sea True si
# 'Family_size' es 0, y False de lo contrario.
# =============================================================================
data["Is_Alone"] = data.Family_size == 0


# =============================================================================
# 12. Filtra el DataFrame para mostrar solo las filas donde 'Age' esté
# entre 20 y 30, inclusive, y 'Pclass' sea 1 o 2. (Usando between
# e ISIN)
# =============================================================================
data12 = data.loc[data.Age.between(20, 30) & data.Pclass.isin([1, 2])]

# =============================================================================
# 13. Crea una nueva columna llamada 'Fare_Category' que sea 'High' si
# 'Fare' es mayor que 50, 'Medium' si está entre 20 y 50, y 'Low' de lo
# contrario.
# =============================================================================
data.loc[data.Fare > 50, "Fare_Category"] = "High"
data.loc[data.Fare.between(20,50), "Fare_Category"]="Medium"
data.loc[data.Fare < 50, "Fare_Category"] = "Low"

# =============================================================================
# 14. Rellena los valores faltantes en la columna 'Embarked' con el valor
# más frecuente.
# =============================================================================
data.Embarked.fillna(data.Embarked.mode()[0], inplace = True)


# =============================================================================
# 15. Crea una nueva columna llamada 'Age_Group' que sea 'Child' si 'Age'
# es menor que 18, 'Adult' si está entre 18 y 60, y 'Senior' de lo
# contrario.
# =============================================================================
data.loc[data.Age < 18, "Age_Group"] = "Child"
data.loc[data.Age.between(18,60), "Age_Group"]="Adult"
data.loc[data.Age > 60, "Age_Group"] = "Senior"

# =============================================================================
# 16. Ordena el DataFrame del Titanic por las columnas 'Pclass' de forma
# descendente y 'Fare' de forma ascendente.
# =============================================================================
data16 = data.sort_values(by=['Pclass', 'Fare'], ascending=[False, True])


# =============================================================================
# 17. Crea una nueva columna llamada 'Is_Female' que sea True si 'Sex' es
# 'female', y False de lo contrario.
# =============================================================================


data['Is_Female'] = data['Sex'] == 'female'


# =============================================================================
# 18. Filtra el DataFrame para mostrar solo las filas donde 'Embarked' no
# sea 'S’.
# =============================================================================

data18 = data[data['Embarked'] != 'S']


# =============================================================================
# 19. Rellena los valores faltantes en la columna 'Cabin' con 'Unknown’.
# =============================================================================

data19 = data['Cabin'] = data['Cabin'].fillna('Unknown').reset_index()

# =============================================================================
# 20. Crea una nueva columna llamada 'Has_SibSp' que sea True si 'SibSp' es
# mayor que 0, y False de lo contrario.
# =============================================================================

data['Has_SibSp'] = data['SibSp'] > 0
data20 = data.reset_index(drop=True)

# =============================================================================
# 21. Filtra el DataFrame para mostrar solo las filas donde 'Age' no esté
# entre 25 y 35, inclusive.
# =============================================================================

data21 = data[~data['Age'].between(25, 35, inclusive='both')]


# =============================================================================
# 22. Crea una nueva columna llamada 'Fare_Normalized' que sea el
# resultado de restar la media de 'Fare' a 'Fare' y dividir entre 'Fare’.
# =============================================================================

data22 = data
data22['Fare_Normalized'] = (data22['Fare'] - data22['Fare'].mean()) / data22['Fare']

# =============================================================================
# 23. Rellena los valores faltantes en la columna 'Embarked' con el valor 'C'
# si 'Pclass' es 1, 'Q' si es 2, y 'S' si es 3.
# =============================================================================

data23 = data
data['Embarked'] = data.apply(lambda row: 'C' if pd.isna(row['Embarked'])\
    and row['Pclass'] == 1 else ('Q' if pd.isna(row['Embarked'])\
      and row['Pclass'] == 2 else ('S' if pd.isna(row['Embarked'])\
        and row['Pclass'] == 3 else row['Embarked'])), axis=1)


# =============================================================================
# Contexto:
# Tienes el dataset del Titanic cargado como data. Se requiere realizar un
# análisis y limpieza de datos de manera exhaustiva utilizando pandas para
# preparar el DataFrame para un análisis más detallado.
# =============================================================================


# =============================================================================
# 1. Comprobación de valores nulos:
# • Realiza una comprobación completa de valores nulos en el
# DataFrame. Crea un DataFrame booleano que indique la
# presencia de valores nulos en el DataFrame.
# • Cuenta el total de valores nulos en cada columna y el total de
# valores nulos en el DataFrame completo.
# =============================================================================
valores_nulos = data.isnull()
total_nulos = data.isnull().sum()
nulos_completo = data.isnull().sum().sum()

# =============================================================================
# 2. Relleno de valores nulos:
# • Rellena los valores nulos en la columna Age con la media de la
# columna.
# • Rellena los valores nulos en la columna Fare con un valor
# constante, como 100.
# • Utiliza la moda para rellenar valores nulos en la columna
# Embarked.
# • Aplica un método de relleno hacia adelante (ffill) en la columna
# Cabin para sustituir los valores nulos.
# • Rellena hacia atrás (bfill) los valores nulos en la columna Cabin.
# =============================================================================
data.Age.fillna(data.Age.mean(), inplace = True)
data.Fare.fillna(100, inplace = True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace = True)
data.Cabin.fillna(method="ffill", inplace = True) 
data.Cabin.fillna(method="bfill", inplace = True)

# =============================================================================
# 3. Limpieza de datos con regex:
# • Limpia todas las columnas de texto (strings) para eliminar
# espacios en blanco no deseados y cualquier carácter especial
# (acentos o diacríticos) utilizando expresiones regulares con regex.
# • Convierte todos los nombres de las columnas a minúsculas y
# elimina espacios al inicio y al final.
# =============================================================================
data_texto = data.select_dtypes(include=[object]).columns

#Eliminar espacios en blanco
for i in data_texto:
    data["i"] = data[i].str.replace(r'^\s+|\s+$', "", regex=True) 

#Eliminar carácteres especiales
data.columns = [unidecode(col) for col in data.columns]


data.columns = data.columns.str.strip().str.lower()

# =============================================================================
# 4. Filtrado avanzado de datos:
# • Extrae solo las filas donde el rango de edad esté entre 18 y 60
# años, y donde el valor de la columna Fare esté por encima del
# percentil 50.

# • Se debe crear una nueva columna llamada "Categoria_Edad" con
# condiciones específicas dentro de una función:
# • Si la edad es menor a 30 años, debe contener el
# valor "Joven".
# • Si la edad está entre 30 y 45 años, debe contener el
# valor "Adulto".
# • Si la edad es mayor a 45 años, debe contener el
# valor "Mayor".
# =============================================================================
databetween= data.loc[(data.age.between(18,60))&(data.fare < data.fare.quantile(0.50))]

data.loc[data.age < 30, "Categoria_Edad"] = "Joven"
data.loc[data.age.between(30,45), "Categoria_Edad"]="Adulto"
data.loc[data.age > 45, "Categoria_Edad"] = "Mayor"


# =============================================================================
# 5. Análisis numérico:
# • Ordena el DataFrame por el valor de la columna Fare en orden
# descendente y elimina duplicados basándote en la combinación
# de las columnas PassengerId y Pclass.
# • Crea una nueva columna llamada "Fare_Rank" que indiuqe el
# rango de cada pasajero basado en su tarifa (Fare) utilizando un
# método de ranking en orden descendente.
# =============================================================================
data_Fare = data.sort_values("fare",ascending=0).drop_duplicates(subset=["passengerid", "pclass"],keep="first")

data["Fare_Rank"] = data.fare.rank(ascending = False) 


# =============================================================================
# 6. Cálculo de puntuación para cada pasajero:
# • Crea una función personalizada llamada calcular_puntuacion.
# Esta función debe tomar como entrada la información de un
# pasajero individual (las columnas Age, Fare, Pclass, y Survived) y
# devolver una puntuación calculada utilizando la siguiente lógica:
# • Si el pasajero sobrevivió (Survived = 1), suma 5
# puntos a la puntuación.
# • Si la edad es mayor o igual a 50, suma 4 puntos.
# • Si la tarifa (Fare) es mayor a 200, suma 3 puntos.
# • Si la clase del pasajero es 1a clase, suma 2 puntos.
# • Si la clase del pasajero es 3a clase, resta 2 puntos.
# 
# • Muestra que pasajero tiene mayor puntuación
# =============================================================================

def calcular_puntuacion(Age, Fare, Pclass, Survived): 
    puntuacion = 0
    if Survived == 1:
        puntuacion = puntuacion + 5
        
    if Age >= 50: 
        puntuacion = puntuacion + 4
    
    if Fare > 200:
       puntuacion = puntuacion + 3
       
    if Pclass == 1:
        puntuacion = puntuacion + 2
    elif Pclass == 3:
      puntuacion = puntuacion - 2
        
    return puntuacion;


data['puntuacion'] = data.apply(
    lambda row: calcular_puntuacion(row['age'], row['fare'], row['pclass'], row['survived']), axis=1)


print(data[['age', 'fare', 'pclass', 'survived', 'puntuacion']])


# =============================================================================
# 7. Pregunta adicional compleja:
# Crear una nueva columna llamada Indice_Sobrevivencia que se
# calcule con las siguientes reglas:
# 1. Puntaje base:
# • Comienza con un puntaje igual al doble de la tarifa (fare * 2).
# 2. Modificaciones al puntaje base (por cada fila):
# • Restar 10 puntos si la edad es mayor de 50.
# • Sumar 15 puntos si el pasajero pertenece a la clase 1.
# • Restar 20 puntos si pertenece a la clase 3.
# • Multiplicar el puntaje por 1.2 si el pasajero es hombre y
# sobrevivió.
# • Dividir el puntaje por 2 si tiene más de 60 años y está en clase 3
# 3. Finalmente, clasificar a los pasajeros en "Alta", "Media" o "Baja"
# probabilidad de sobrevivencia según el valor del Indice_Sobrevivencia:
# • "Alta" si el índice es mayor de 200.
# • "Media" si está entre 100 y 200.
# • "Baja" si es menor de 100.
# =============================================================================

#7.1
data["Indice_Sobrevivencia"] = data["Fare"] * 2

#7.2
for index, row in data.iterrows():

    if row['Age'] > 50:
        data.at[index, 'Indice_Sobrevivencia'] -= 10


    if row['Pclass'] == 1:
        data.at[index, 'Indice_Sobrevivencia'] += 15


    if row['Pclass'] == 3:
        data.at[index, 'Indice_Sobrevivencia'] -= 20


    if row['Sex'] == 'male' and row['Survived'] == 1:
        data.at[index, 'Indice_Sobrevivencia'] *= 1.2


    if row['Age'] > 60 and row['Pclass'] == 3:
        data.at[index, 'Indice_Sobrevivencia'] /= 2


#7.3
def clasificar_probabilidad(sobrevivencia):
    if sobrevivencia > 200:
        return 'Alta'
    elif 100 <= sobrevivencia <= 200:
        return 'Media'
    else:
        return 'Baja'

data['Probabilidad_Sobrevivencia'] = data['Indice_Sobrevivencia'].apply(clasificar_probabilidad)



