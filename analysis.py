##  Dervla Candon
##  Programming & Scripting
##  Fisher's Iris Dataset Project

##  Import as required
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

##  dataset stored in repository - raw version required
iris = pd.read_csv("https://raw.githubusercontent.com/dervlac/PandS-Project/master/iris.csv")

## using seaborn to plot all scatterplots in the one figure
## provides the easiest way to compare results
pair_plot = sns.pairplot(iris, hue = 'species')
pair_plot.savefig("pairplot.png")
plt.clf()

## Separating the data by species
setosa = iris[iris.species == 'Iris-setosa']
versicolor = iris[iris.species == 'Iris-versicolor']
virginica = iris[iris.species == 'Iris-virginica']

## plotting histogram of Petal Lengths
sns.distplot(setosa['petal_length'], kde=False,label='Iris Setosa')
sns.distplot(versicolor['petal_length'],kde=False,label='Iris Versicolor')
sns.distplot(virginica['petal_length'],kde=False,label='Iris Virginica')
plt.title("Petal Length")
plt.xlabel("Length in cm")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='best',ncol=3, mode="expand")
plt.savefig("petal_length_histogram.png")
plt.clf()

## plotting histogram of Petal Widths
sns.distplot(setosa['petal_width'], kde=False,label='Iris Setosa')
sns.distplot(versicolor['petal_width'],kde=False,label='Iris Versicolor')
sns.distplot(virginica['petal_width'],kde=False,label='Iris Virginica')
plt.title("Petal Width")
plt.xlabel("Width in cm")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='best',ncol=3, mode="expand")
plt.savefig("petal_width_histogram.png")
plt.clf()

## plotting histogram of Sepal Lengths
sns.distplot(setosa['sepal_length'], kde=False,label='Iris Setosa')
sns.distplot(versicolor['sepal_length'],kde=False,label='Iris Versicolor')
sns.distplot(virginica['sepal_length'],kde=False,label='Iris Virginica')
plt.title("Sepal Length")
plt.xlabel("Length in cm")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='best',ncol=3, mode="expand")
plt.savefig("sepal_length_histogram.png")
plt.clf()

## plotting histogram of Sepal Widths
sns.distplot(setosa['sepal_width'], kde=False,label='Iris Setosa')
sns.distplot(versicolor['sepal_width'],kde=False,label='Iris Versicolor')
sns.distplot(virginica['sepal_width'],kde=False,label='Iris Virginica')
plt.title("sepal Width")
plt.xlabel("Width in cm")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='best',ncol=3, mode="expand")
plt.savefig("sepal_width_histogram.png")
plt.clf()

setosaDescribe = setosa.describe()
versicolorDescribe = versicolor.describe()
virginicaDescribe = virginica.describe()

## Creating a text file to hold summary of variables
f1 = open("iris_setosa.txt","w+")
f1.write("This document contains a summary of the data relating to the species 'Iris Setosa'\n\n")
f1.write("1. Statitical Analysis of Iris Setosa\n\n")
f1.write(setosaDescribe.to_string())
f2 = open("iris_versicolor.txt","w+")
f2.write("This document contains a summary of the data relating to the species 'Iris Versicolor'\n\n")
f2.write("1. Statitical Analysis of Iris Versicolor\n\n")
f2.write(versicolorDescribe.to_string())
f3 = open("iris_virginica.txt","w+")
f3.write("This document contains a summary of the data relating to the species 'Iris Virginica'\n\n")
f3.write("1. Statitical Analysis of Iris Virginica\n\n")
f3.write(virginicaDescribe.to_string())
f1.close()
f2.close()
f3.close()