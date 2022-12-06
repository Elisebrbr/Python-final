# Python for Data Analysis
## ESILV S1 2022–2023

Taous Bedouhene - Inès Baazia - Elise Barbier - DIA 1
 
### Final project

### Online Shoppers Purchasing Intention
https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset

The dataset consists of feature vectors belonging to 12,330 sessions.
It was formed so that each session
would belong to a different user in a 1-year period to avoid
any tendency to a specific campaign, special day, user
profile, or period.

The dataset consists of 10 numerical and 8 categorical attributes.
The 'Revenue' attribute can be used as the class label.

## Our objectives 
To analyze the dataset, we had to answer the following questions:
* A code in python:
 - Data pre-processing: encoding, normalization, imputation….
 - Data visualization (use matplotlib, seaborn, bokeh ...): show the link between
the variables and the target.
 - Modeling: use the scikit-learn library to try several algorithms, change the
hyper parameters, do a grid search, compare the results of your models using
graphics
* Transformation of the model into an API of your choice (Django or flask)

## Data Analysis 
We want to predict if the end of a session ends with a purchase. 
The dataset consists of feature vectors belonging to 12,330 sessions with only 15,5% of sessions (1908) ending in purchases (against 84.5% (10,422)).

#### Pre-processing 
For this part, we change some types "object" into 'string', there were nothing to clean and no missing values, we had no imputation to make.

We encoded the categorical values : 'Month', 'VisitorType', 'Weekend' and 'Revenue'.

For  weekend and revenue with binary values, for VisitorType we use a matrix of binary values and for the months we encoded with values between 1 and 12 and then with cos and sin because they are connected cyclically.

For the normalization, we added some variables in our dataset :
* "Moyenne_Administrative": mean of the time spent on the administrative part
* "Moyenne_Informational" : mean of the time spent on the informational part
* "Moyenne_ProductRelated" :  mean of the time spent on the product related part

And we reshaped each variables to keep only the best values.

#### Visualization 

For this part we wanted to analyse firstly everything by month with barplots, then the revenue by type of visitor with pies, with boxenplot,the time spent on product related in relation wit revenue and the exit rates related with revenue and finally, we used stripplot to analyse the bounce rates with the revenue. 

#### Modeling 

The first thing to do is a correlation matrix (heatmap) to see which variables have the higher correlation with our target revenue.
We choose to take the 7 higher values : "Administrative","Administrative_Duration","Informational","Informational_Duration","ProductRelated","ProductRelated_Duration" and "PageValues".

We will only keep thoses columns for the modeling. 

Then, we split the dataset into a train and test sets

We try some models : Support Vector Machine, Naive Bayes, Random Forest Classification, K Nearest Neighbour, Logisitic Regression, Decision Tree Classification, Gradient Boosting Classification, Linear Discriminant Analysis

We calculate the accurancy, the classification report and the confusion matrix for each models.

Then, we do a grid search, we compare the results of ours models and we saw that the best one is the random forest. 

