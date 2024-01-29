import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ToyotaCorolla.csv')

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rowa', 500)
pd.set_option('display.width', 2000)
print(df)
