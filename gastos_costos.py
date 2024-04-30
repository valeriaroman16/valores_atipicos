import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_excel('gastos_costos_20_23.xlsx', index_col=0)
#print(df.head())

print(df.isnull().sum())
#print(valores_nulos)

df['IMPORTE'] = df['IMPORTE'].fillna(0)

valores_nulos=df.isnull().sum()
#print(valores_nulos)

#IMPORTE
#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["IMPORTE"]

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
y=df["IMPORTE"]
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

#TOTAL_MX
y=df["TOTAL MX"]

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
y=df["TOTAL MX"]
#print(y)
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()

#print()
#print('MÉTODO DESV. STANDAR')
#print("Limite superior permitido usando des. standar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando des. standar", Limite_Inferior_dev_std)

data_clean_iqr= df[(y < Limite_Superior_dev_std) & (y > Limite_Inferior_dev_std)]
#print(data_clean_iqr)

#df.to_csv('columna_TOTAL_MX.csv')

#TOTAL SAT
y=df["TOTAL SAT"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr

data_clean_iqr= df[(y < Limite_Superior_iqr) & (y > Limite_Inferior_iqr)]
#print(data_clean_iqr)

#print()
#print('MÉTODO CUARTILES')
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)

#Método aplicando desviación estandar. Encuentro los valores extremos
y=df["TOTAL SAT"]
#print(y)
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()

#print()
#print('MÉTODO DESV. STANDAR')
#print("Limite superior permitido usando des. standar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando des. standar", Limite_Inferior_dev_std)

data_clean_iqr= df[(y < Limite_Superior_dev_std) & (y > Limite_Inferior_dev_std)]
#print(data_clean_iqr)

#df.to_csv('columna_TOTAL_SAT.csv')