import pandas as pd
import matplotlib.pyplot as plt

# 1. Atrinkite visus įrašus, kurių pardavimai viršija 500 vienetų.
# 2. Konvertuokite 'Data' stulpelį į datetime formatą ir apskaičiuokite pardavimus pagal mėnesius.
# 3. Apskaičiuokite vidutinius pardavimus kiekvienam produktui.
# 4. Sukurkite naują stulpelį, kuriame būtų pardavimo kaina už vienetą (Pardavimai / Kiekis).
# 5. Sukurkite grafiką, vaizduojantį produkto (pasirinkite bet kurį) pardavimus per laiką.
file_name='prekybos_duomenys.csv'
df=pd.read_csv(file_name)

selected=df[(df['Pardavimai']>500)] #1

df['Data']=pd.to_datetime(df['Data'])
df['Month']=df['Data'].dt.month
df['Year']=df['Data'].dt.year
sales=df.groupby(['Year', 'Month'])['Pardavimai'].sum().reset_index() #2

average=df.groupby(['Produktas'])['Pardavimai'].mean() #3

df['Unit']=df['Pardavimai'] / df['Kiekis'] #4

nuqdata=df[df['Produktas']=='NUQ']

plt.figure(figsize=(12, 8))
plt.plot(nuqdata['Data'], nuqdata['Pardavimai'], label='NUQ', marker='o')
plt.title('NUQ Sales across time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show() #5








