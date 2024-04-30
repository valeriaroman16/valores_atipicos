import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('ventas_totales_sinnulos_1.csv', index_col=0)
#print(df.head())

valores_nulos=df.isnull().sum()
#print(valores_nulos)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes_con_outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
#plt.show()

y=df["ventas_precios_corrientes"]
#print(y)

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr= percentile75 - percentile25
#print(iqr)


#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["ventas_precios_corrientes"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)


#Obtenemos datos limpios
data_clean_iqr= df[(y < Limite_Superior_iqr) & (y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
#plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes_sin_outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

#data_clean_iqr['ventas_precios_corrientes'].to_csv('ventas_precios_corrientes.csv')

#Método aplicando desviación estandar. Encuentro los valores extremos
y=df["ventas_precios_corrientes"]
#print(y)
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()

#print("Limite superior permitido usando des. standar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando des. standar", Limite_Inferior_dev_std)

data_clean_iqr= df[(y < Limite_Superior_dev_std) & (y > Limite_Inferior_dev_std)]
#print(data_clean_iqr)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes_sin_outliers - dev standar')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["ventas_totales_canal_venta"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr

#print()
#print('MÉTODO CUARTILES')
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)

data_clean_iqr= df[(y < Limite_Superior_iqr) & (y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

#Método aplicando desviación estandar. Encuentro los valores extremos
y=df["ventas_totales_canal_venta"]
#print(y)
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()

#print()
#print('MÉTODO DESV. STANDAR')
#print("Limite superior permitido usando des. standar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando des. standar", Limite_Inferior_dev_std)

data_clean_iqr= df[(y < Limite_Superior_dev_std) & (y > Limite_Inferior_dev_std)]
#print(data_clean_iqr)

#data_clean_iqr['ventas_totales_canal_venta'].to_csv('ventas_totales_canal_venta.csv')

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["efectivo"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr

print()
print('MÉTODO CUARTILES')
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

data_clean_iqr= df[(y < Limite_Superior_iqr) & (y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

#Método aplicando desviación estandar. Encuentro los valores extremos
y=df["efectivo"]
#print(y)
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()

print()
print('MÉTODO DESV. STANDAR')
print("Limite superior permitido usando des. standar", Limite_Superior_dev_std)
print("Limite inferior permitido usando des. standar", Limite_Inferior_dev_std)

data_clean_iqr= df[(y < Limite_Superior_dev_std) & (y > Limite_Inferior_dev_std)]
#print(data_clean_iqr)

data_clean_iqr['efectivo'].to_csv('efectivo.csv')