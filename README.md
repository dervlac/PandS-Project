# PandS-Project
Repository for Fisher's Iris Project for Programming and Scripting Module

## Introduction
Fisher's Iris data is so-called due to the 1936 paper by the statistician and biologist Ronald Fisher, and his paper titled *The use of multiple measurements in taxonomic problems*. The data was initially collected by Edgar Anderson in the year prior.

## Data
The data set consists of measurements relating to 3 classes of iris; iris setosa, iris versicolor, and iris virginica. For a sample of 50 flowers from each species, measurements were taken of sepal length, sepal width, petal length and petal width. Thus the data set consists of 150 rows, with 5 attributes per row.

## Accuracy
Following the download of the dataset from the source cited below, upon further research I noted that there have been variations in the data set referenced throughout the years. As noted at the data source, these variations relate to samples 35 and 38 of the data set I selected. Following comparison with the data set noted as most probable in the article *Will the real iris data please stand up?* by Bezdek, Keller et al, I have subequently updated the values for samples 35 and 38 to most accurately reflect the original data used by Fisher in his 1936 analysis.

## Pairplot Analysis
It is clear from inspecting the diagonal plots found in the pairplot diagram that the distributions of the measurements for the iris setosa are significantly different to the 2 remaining species, particularly so for the petal attributes, for which there is no overlap of its distributions whatsoever.
This difference is further reaffirmed when inspecting the variaitons of pairplots, where it is noted that the apparent clusters of values relating to the iris setosa. Again, this is most apparent when one or both attributes relating to the petal measurements are being used.
Inspecting the pairplots from the view of rates of change, it appears that both the iris versicolor and iris virginica have measurements which vary at fairly similar rates, with the slopes of their projections appearing to be similar. However, more detailed regression analysis would be required to confirm or disfute this theory. 
Conversely, the rate at which one dimension for the iris setose varies as another dimension increases or decreases does not appear to align either of the remaining species, except for the relationship between petal length and petal width. In these pariplots, if a rough line of best fit were to be drawn for each species, I believe they would have very similar slopes. 
It could be argued that variation in sepal length and width has very little, if any, effect on the petal dimension, as evidenced by the 4 plots in the top right and bottom left of the pairplot diagram. Dots representing the iris setosa in these diagrams appear mostly vertical or horizontal, suggesting that one variable is not dependent on another.

## Histogram Analysis
Through inspection of the histograms relating the petal length and petal width, it is clear that each species has its own distinct meadian and mean value, as corroborated within the 'iris_summary' document. For both the iris versicolor and iris virginica, while the plots are centred at dfferent values, the width and shape of the distribution of their histograms are of a similar nature. In contrast, the histograms for th iris setosa are very narrow, with little deviation from the centre, and as such reach a much higher peak, suggesting that the standard deviation for this species is smaller than the 2 other species.
In contrast to this, the sepal width histogram appears to show similar levels of deviation from the average for all species.

## Summary Corroboration
With the above analysis of the histogram data in mind, I inspected the petal length and width mean, median and standard deviation values for all three species to compare to my hypotheses. 
For all species, the mean and median (50%) values are distinctly different from one another. The standard deviation for petal length is very low for the iris setosa (0.173664) relative to the versicolor and virginica (0.469911, 0.551895). While less defined, this pattern remains for the peta width standard deviation.
In relation to the sepal width distributions, the spread of the values across all species is very similar, with the standard deviations for the iris setosa, iris versicolor, and iris virginica equal to 0.379064, 0.3313798, and 0.322497. 

### Dataset source
``` http://archive.ics.uci.edu/ml/datasets/iris ```
### Document Sources
```
R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems". Annals of Eugenics. 7 (2): 179–188.
J. C. Bezdek, J. M. Keller, R. Krishnapuram, L. I. Kuncheva and N. R. Pal, "Will the real iris data please stand up?," in IEEE Transactions on Fuzzy Systems, vol. 7, no. 3, pp. 368-369, June 1999.
```
