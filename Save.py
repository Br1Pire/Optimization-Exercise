import pandas as pd
import PSO

lista =  PSO.PSO()

col = ['Dimension', 'Enjambre', 'Iteraciones', 'Mejor Punto', 'Mejor Valor', 'Tiempo Ejecucion', 'Cercania']

df = pd.DataFrame(columns=col)

for x in lista:
    df.loc[len(df)] = x

df.to_markdown('Data.md',index=None)
