## Librarys & reading CSV ## 
import csv ##Library for CSV files to be read
import pandas as pd ## Library for analyzing Data
import seaborn as sns ##Provides a visualisation libary for our Histo's & Scatters
import matplotlib.pyplot as plt ##Matplot Libary for Graphing

%matplotlib inline
sns.set(style='white', color_codes=True)

df = pd.read_csv('C:/Users/Ryanmc/Desktop/iris.csv') ##Read Data from CSV file
df.head(10) ##Printing out first 10 records of CSV to Make sure all is correct & file loaded in right, head prints first 10 rows

## Summary ##
summary=df.agg(["count",'sum', 'min',"max", "median", "skew"]) ##Summary function prints out a summary of each variable, ignore last bit of display as it is looking at species
print(summary) 
##Writing to File##
df.to_csv(r'C:\Users\Ryanmc\Desktop\MasterFolder\College\pands-project\Summary.txt', header=None, index=None, sep= ' ', mode='a') ##Prints the Dataframe to the Txt file I have saved on my desktop, reference for code: https://www.codegrepper.com/code-examples/python/pandas+to+txt+file

## Histrograms ## 

plt.hist(df["SepalLengthCm"]) ##Matplot function for creating historgrams, I used W3Schools for this part & it was straightforward enough: https://www.w3schools.com/python/matplotlib_histograms.asp
plt.title("Sepal Length Histogram") ##Adding title to histrogram 
plt.savefig('sepallength.png') ##Saves file as PNG: Reference via: https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
plt.figure()
plt.hist(df["SepalWidthCm"])
plt.title("SepalWidthCm Histogram")
plt.savefig('SepalWidthCm.png')
plt.figure()
plt.hist(df["PetalLengthCm"])
plt.title("PetalLengthCm Histogram")
plt.savefig('PetalLengthCm.png')
plt.figure()
plt.hist(df["PetalWidthCm"])
plt.title("PetalWidthCm Histogram")
plt.savefig('PetalWidthCm.png')
plt.show()

## Scatter Plots ##

df.plot(kind ="scatter",
          x ='SepalLengthCm',
          y ='SepalWidthCm',
       ) ##Plotting my Sepal Scatter graph ,Code reference : https://www.w3schools.com/python/matplotlib_plotting.asp
plt.grid() ##Applies grid lines
plt.savefig('SepalScatter.png') ##Saves it as a PNG

df.plot(kind ="scatter",
          x ='PetalLengthCm',
          y ='PetalWidthCm',
       )##Plotting my Petal Scatter graph
plt.grid()##Applies grid lines
plt.savefig('PetalScatter.png') ##Saves it as a PNG

## Extra Analyis ## 

fig = df[df.Species == 'Setosa'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='orange', label='Setosa') ##Creating our sepal plot again but this time  just for setosha which we will make ornage
df[df.Species == 'Versicolor'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='blue', label='Versicolor', ax=fig)##Creating our sepal-Length plot again but this time  just for Versiocolor which we will make blue
df[df.Species == 'Virginica'].plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', color='green', label='Virginica', ax=fig)##Creating our sepal-Length plot again but this time  just for Virgincia which we will make Green

fig.set_xlabel('Sepal Length') ##Setting labels for each axis
fig.set_ylabel('Sepal Width')
fig.set_title('Sepal Length Vs Width')## Title

fig=plt.gcf()
fig.set_size_inches(10, 7) ##Sets size of the grah
plt.show() ##Shows & prints the graph

fig = df[df.Species == 'Setosa'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='orange', label='Setosa') ##Same as previous graph this time for petals 
df[df.Species == 'Versicolor'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='blue', label='Versicolor', ax=fig)
df[df.Species == 'Virginica'].plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='green', label='Virginica', ax=fig)

fig.set_xlabel('Petal Length')
fig.set_ylabel('Petal Width')
fig.set_title('Petal Length Vs Width')

fig=plt.gcf()
fig.set_size_inches(10, 7)
plt.show()