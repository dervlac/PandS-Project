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