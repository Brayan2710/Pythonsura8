from cgitb import text
from distutils import text_file
import pandas as pd

## Cargar los datos. 
dataframe=pd.read_csv('./empleados.csv')
#print(dataframe)

# Cargar todos los datos
#print(dataframe.to_string())

# Cargar los primero registros en un banco de datos
#print(dataframe.head())

# Cargar los ultimos n registros de un banco de datos 
#print(dataframe.tail(50))

# Obtener informacion de los datos cargados 
#print(dataframe.info())
#print(dataframe.describe())

#acceder a datos o regostros especificos
#print(dataframe["nombres"].head())
#print(dataframe["salario"].tail(20))

# Voy acceder registros por su indice 
#print(dataframe.iloc[20:30])
#print(dataframe.loc[[10,20,30,40]])
#print(dataframe.loc[[1,5,10],["nombres"]])

'''
Almacenar datos en una tabla 
tabla=(dataframe.loc[[1,5,10],["nombres"]])

html=tabla.to_html()
text_file=open("index.html","w")
text_file.write(html)
text_file.close()
'''
# filtros con condiciones logicas 
print(dataframe[(dataframe["salario"]>5500000) &(dataframe["cargo"]=="analista2")].head(10))
