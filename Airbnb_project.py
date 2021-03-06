# Installing required packages
!pip install pandas
!pip install matplotlib
!pip install seaborn
!pip install plotly
!pip install numpy

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Opening the file
listings = pd.read_csv('/Users/monicahuaytadurand/Documents/Python projects/listings_sf.csv')
listings.describe()
listings.head()

# Checking empty values
listings.isna().sum()

# Let's check the neighbourhoods
listings.neighbourhood.unique()

# Let's create a graph that counts number of listings
group_neighbourhood = listings.groupby(['neighbourhood'], as_index = False)['id'].count()
group_neighbourhood = group_neighbourhood.rename(columns = {'id' : 'Num_bookings'})
group_neighbourhood = group_neighbourhood.sort_values(by = 'Num_bookings', ascending = False)

# Violin Graph
px.violin(
  listings,
  x = 'neighbourhood',
  y = 'price'
)
plt.show()

# Style and size of the plot
sns.set_theme(style = "dark")
plt.rcParams['figure.figsize'] = [8,4]

# Visualization
sns.barplot(data = group_neighbourhood, y = 'neighbourhood', x ='Num_bookings')
plt.show()

# Let's reduce the number: take first 10
group_10 = group_neighbourhood.head(n=10)
sns.barplot(data = group_10, y = 'neighbourhood', x = 'Num_bookings').set_title('Top 10 SF Neighbourhoods')
plt.show()

# Plotting the price per Neighbourhood
civic_center = listings.loc[listings.neighbourhood == 'Downtown/Civic Center'].price
mission = listings.loc[listings.neighbourhood == 'Mission'].price
south_mk = listings.loc[listings.neighbourhood == 'South of Market'].price

plt.figure(figsize = (8,6))
plt.hist(civic_center, bins=100, alpha=0.5, label = 'Civic Center')
plt.hist(mission, bins=100, alpha=0.5, label = 'Mission')
plt.hist(south_mk, bins=100, alpha=0.5, label = 'South of Market')
plt.legend(loc = 'upper right')
plt.show()

# There is an outlier in Civic Center!
civic_center.mean()
civic_center.max()
civic_center[civic_center >= 9999]

# Let's double check those records
listings.loc[(listings.price >= 9999) & (listings.neighbourhood == 'Downtown/Civic Center')]

# Excluding the outliers
civic_center = listings.loc[(listings.neighbourhood == 'Downtown/Civic Center') & (listings.price < 9999)].price

# Showing some statistics about the price
listings[['neighbourhood','price']]
listings.groupby('neighbourhood')['price'].agg([min,max,np.mean])

