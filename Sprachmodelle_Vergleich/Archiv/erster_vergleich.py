import pandas as pd
import matplotlib.pyplot as plt

# Laden der Daten
df_31122024 = pd.read_csv('Dezember/2024-12-31-prices.csv')
df = df_31122024.drop(df_31122024.index[df_31122024.index % 2 == 0]).reset_index(drop=True)
df = df.drop(df.index[df.index % 2 == 0]).reset_index(drop=True)
df = df.drop(df.index[df.index % 2 == 0]).reset_index(drop=True)
df.to_csv('test.csv')
print(df.info())
#print(df_31122024.info())

# Maximaler Wert für e5
#print(df_31122024['e5'].max())

# Anzahl der Spalten, in der dieselchange den Wert 1 hat
#print(len(df_31122024[df_31122024['dieselchange']== 1]))

# Ausgabe der ersten 20 Zeilen des Datensatzes
#print(df_31122024.head(n=20))

# Dastellen von e10 in einem Boxplot
#plt.boxplot(df_31122024['e10'])
#plt.show()

