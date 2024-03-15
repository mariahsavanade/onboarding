import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

nombre_archivo_original = 'cars.csv'
nombre_modificado = 'archivomodificado.csv'
 
with open(nombre_archivo_original, 'r') as archivo_original:
    lineas = archivo_original.readlines()
 
lineas_modificadas = []
for linea in lineas:
    linea = linea.strip('"\n\'')
    linea = linea.rstrip(',')
    linea = linea.replace('""', '"')
    linea = linea.replace('",,', ',,')
    linea = linea.rstrip('"\n')
    lineas_modificadas.append(linea + '\n')
    
 
with open(nombre_modificado, 'w', encoding='utf-8') as archivo_modificado:
    archivo_modificado.writelines(lineas_modificadas)
 
# Cargar el archivo modificado en un DataFrame
df = pd.read_csv(nombre_modificado)
 
# Leer los tipos de cada columna
print(df.dtypes)

# Quitamos las columnas irrelevantes: Market Category y Popularity
df.drop(['Popularity', 'Market Category'], axis='columns')
df.to_csv('archivo_modificado.csv', index=False)

# Renombramos alguna columna que no sea muy intuitiva: MSRP -> Precio
df = df.rename({'MSRP':'Precio'},axis='columns')

# Lo guardamos
df.to_csv('archivo_modificado_1.csv', index=False)

# Valores duplicados y nulos
print(df.duplicated().sum())
print(df.isnull().sum())

df['Engine Fuel Type'] = df['Engine Fuel Type'].fillna('Desconocido')
df['Number of Doors'] = df['Number of Doors'].fillna(value=5.0)
df['Engine Cylinders'] = df['Engine Cylinders'].fillna(df['Engine Cylinders'].mean())
df.replace(np.nan,'0',inplace=True)
#print(df.isnull().sum())

# Lo guardamos
df.to_csv('archivo_modificado_2.csv', index=False)
print(df)

# Detectamos Outliers

# Con Histogramas
#df.hist()
#plt.show()

# Con BoxPlots
#for columna in df.columns:
#    if df[columna].dtype in ['int64', 'float64']:
#        df.boxplot(column=columna)
 #       plt.show()

# Enfrentar datos

plt.scatter(df[['Year']],df[['Engine Cylinders']])
plt.xlabel('Year')
plt.ylabel('Engine Cylinders')
plt.show()

plt.scatter(df[['Year']],df[['Precio']])
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

# Finalmente, lo guardamos
df.to_csv('archivo_modificado_Final.csv', index=False)
print(df)