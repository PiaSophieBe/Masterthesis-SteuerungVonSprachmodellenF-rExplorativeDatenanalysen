import pandas as pd
from langchain_community.llms import Ollama
from pandasai import SmartDataframe

df_31122024 = pd.read_csv('2024-12-31-prices.csv')
print(df_31122024.head())

llm = Ollama(model = "codellama")
df = SmartDataframe(df_31122024, config= {"llm":llm})
print(df.chat("Was ist der Maximalwert in Spalte 'e5'?"))
print(df.chat("Beschreibe kurz die wichtigsten Merkmale in dem Datensatz."))
print(df.chat("Bitte gib mir für die folgenden Aufgaben den entsprechenden Python-Code, damit sie gelöst werden können: Ausgabe der ersten 20 Zeilen., Erstellen eines Boxplots für die Spalte 'e10'."))
