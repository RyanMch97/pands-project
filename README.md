# pands-project
Iris Dataset Research - 09/04/2022

My research on the Iris Dataset begin by simplying downloading & researching the Iris Dataset online.
From downloading it & viewing it in MS Excel we can see the variables presented.
The 4 variables measured by Dr. Fisher when creating this dataset was the following: sepal's Length, Sepal's Width, Petal Length & Sepal Width.
He measured these 4 variables across the following Setoasha, Versicolor & Virginica.

Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica

Two of the main Reasons for the majority of people starting out using this Dataset when it comes to the Data Analytics is the following.

1- Small dataset, overall it only contains 750 Datapoints in total. Allows for easier analysis rather than starting out on a more complez dataset where plotting chart's etc may prove more diffucult to beginners
2- Use of Real world Data on a non complex subject. The adfvantage of using Real world data on a simple object like Floweres allows us to better visualise & undertand what the differences are in each Flower that was measured.

Code Explantions 

## Librarys & reading CSV ## 
first part is to load data using Pandas Library 
iris = pd.read_csv('C:/Users/Ryanmc/Desktop/iris.csv')
then use head function to visualize data
iris.head(10)

I think I could have placed the Iris dataset in my Pands project folder but for some reason I could not get it to work.
For the project I added to Desktop & it worked for me there

## Summary ##
Using the .agg commmand that I found online here: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html
Once I passed the agg function with the attributes I wanted, mean , min etc I got the summary needed for part of the project.
Ideally I would try to stop the function from applying to the species column but it still displayed what I wanted overall

## Writing to File ##
Used the following website for code refernence on this: https://www.codegrepper.com/code-examples/python/pandas+to+txt+file
I used the to_csv function rather than the to_txt function for some reason did not work. 

## Histrogram ## 
Used both of these for code reference : https://www.codegrepper.com/code-examples/python/pandas+to+txt+file & https://www.w3schools.com/python/matplotlib_histograms.asp
For this section as required it was a straightforward histrogram of each variable, saved it then also with the the plt.save function

## Scatter Plots ##
Based off the following page which I used for code reference:https://www.w3schools.com/python/matplotlib_plotting.asp
I build out the following function using my dataframe

df.plot(kind ="scatter",
          x ='SepalLengthCm',
          y ='SepalWidthCm',
       ) ##Plotting my Sepal Scatter graph ,Code reference : https://www.w3schools.com/python/matplotlib_plotting.asp
plt.grid() ##Applies grid lines
plt.savefig('SepalScatter.png')

Plot is used for creating the graph with my function setting X axis as Sepal Length & Y axis as Sepal Width which was straight forward.
Plt.grid just added grid lines & savefig saved it to my Pands-Project directory 

Once I had the above done for Sepal I did the same for Petals too.

## Extra Analyis ## 
For the extra Analsis section I wanted to compare by species as well, from the previous scatter section we coudl make basic assumptions about Sepals & petals but we could not make any reasonable assumptions in regards to the 3 different specieis which we had not looked at. to start off I couldn't really find anything online that made sense until I found this code for reference: https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html, this page basically shows how a AirQuality dataset could be filtered by ParisAirQuality.
For My Iris dataset I applied the exact same execpt for plotting by Species instaed, as outlined below.

fig = df[df.Species == 'Setosa'].plot

Once I had that figured out I just needed to add my scatter plot again but this time extra colors to make it better visually
plot(kind='scatter', x='PetalLengthCm', y='PetalWidthCm', color='orange', label='Setosa'), once created for all three I set up my label titles.

fig.set_xlabel('Petal Length')
fig.set_ylabel('Petal Width')
fig.set_title('Petal Length Vs Width')

Finally then I set up the size of my grpah & use plot.show to display. Once I had it working for Sepal I applied the exact same for Petals too.
Conclusions we can draw from this are the following

1- Setosha by far has the smallest Petal sizes 
2- Virginica is the largest judging by the length of both the sepals & Petals wehich we got from our scatter plot