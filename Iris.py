import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('desktop\iris.csv')
print(df.to_string())
df.describe()

sum_df = df["SepalLengthCm"].sum()
mean_df = df["SepalLengthCm"].mean()
median_df = df["SepalLengthCm"].median()

df.loc[df["Species"] == "Setosa"]

df.plot(kind ="scatter",
          x ='SepalLengthCm',
          y ='PetalLengthCm')
plt.grid()