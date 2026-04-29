# Homework 2

# When we write papers, we often summarize the descriptive statistics for the data that we use. 
# We can easily do this in Python. We need to create a matrix or data frame with just the information we need. 
# We also create a visuallly pleasing correlation matrix of our variables.
# The variables are:
# 
# •	Coffee Price: dollars per pound
# •	Sugar Price: dollars per pound
# •	Tea Price: dollars per pound
# •	Family Income: annual family salary in U.S. dollars
# •	Coffee consumption: cups annually per person
# 

# -----------------------------------------------------------
# HOMEWORK 2: MULTIPLE LINEAR REGRESSION ANALYSIS
# -----------------------------------------------------------
# This program:
# 1. Loads economic data
# 2. Creates per capita variables
# 3. Computes descriptive statistics
# 4. Visualizes correlations using a heatmap
# 5. Estimates a multiple linear regression model
# 6. Estimates a log-log (elasticity) regression model
# -----------------------------------------------------------

# -----------------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# -----------------------------------------------------------

import pandas as pd              # Data manipulation
import numpy as np               # Numerical operations
import matplotlib.pyplot as plt  # Plotting
import seaborn as sns            # Advanced visualization

# Library for regression models
from statsmodels.formula.api import ols

# -----------------------------------------------------------
# STEP 2: LOAD THE DATA
# -----------------------------------------------------------

# Read the Excel file into a Pandas DataFrame
# Make sure the file is in the same folder as your script
df = pd.read_csv('Coffee_demand.csv')

# Display the first five observations
df.head()


# We display the descriptive statistics first.

# -----------------------------------------------------------
# STEP 3: SELECT VARIABLES FOR ANALYSIS
# -----------------------------------------------------------

# These are the key variables used in the analysis
X = df[['Coffee_consumption', 'Coffee_price', 'Sugar_price', 'Tea_price', 'Annual_income']]

# -----------------------------------------------------------
# STEP 4: DESCRIPTIVE STATISTICS (TABLE FORMAT)
# -----------------------------------------------------------
# This creates a clean summary table for all variables

# Use Pandas describe() and extend it
desc_stats = X.describe().T   # Transpose so variables are rows

# Add additional statistics
desc_stats['skewness'] = X.skew()

# Rename columns for clarity
desc_stats.rename(columns={
    'count': 'Count',
    'mean': 'Mean',
    'std': 'Std Dev',
    'min': 'Min',
    '25%': '25%',
    '50%': 'Median',
    '75%': '75%',
    'max': 'Max'
}, inplace=True)

# Round values for readability
desc_stats = desc_stats.round(3)

# Display the table
print('\n----- DESCRIPTIVE STATISTICS TABLE -----')
print(desc_stats)

# We display the correlation matrix next

# -----------------------------------------------------------
# STEP 5: CORRELATION MATRIX
# -----------------------------------------------------------
# Correlation measures the strength of relationships between variables

corr = X.corr()

# Create a mask to hide the upper triangle of the matrix
# (This avoids showing duplicate information)
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True

# Set up the plot
fig, ax = plt.subplots(figsize=(11, 9))

# Create a color palette
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap
sns.heatmap(
    corr,
    mask=mask,
    cmap=cmap,
    annot=True,        # Show numbers in each cell
    vmax=1, vmin=-1,   # Correlation ranges from -1 to 1
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.85}
)

# Title for clarity
plt.title('Correlation Matrix')

# Save the figure (high resolution)
plt.savefig('Figure-Correlation.png', bbox_inches='tight', dpi=600)

# Show the plot
plt.show()


# We estimate the simple linear regression for coffee demand

# -----------------------------------------------------------
# STEP 6: MULTIPLE LINEAR REGRESSION (LEVELS)
# -----------------------------------------------------------
# This model estimates how prices and income affect coffee demand

# Define and estimate the model
Model_01 = ols(
    'Coffee_consumption ~ Coffee_price + Sugar_price + Tea_price + Annual_income',
    data=df
).fit()

# Display results
print('\n----- REGRESSION RESULTS: LEVEL MODEL -----')
print(Model_01.summary())

# We take the natural logarithm of all the variables. Then we estimate the non-linear demand function.
# The parameter estimates become the elasticities.

# -----------------------------------------------------------
# STEP 8: LOG TRANSFORMATION
# -----------------------------------------------------------
# Taking logs helps:
# - Interpret coefficients as elasticities
# - Reduce skewness in data
# - Improve model fit

df['ln_Coffee_consumption'] = np.log(df['Coffee_consumption'])
df['ln_Coffee_price'] = np.log(df['Coffee_price'])
df['ln_Sugar_price'] = np.log(df['Sugar_price'])
df['ln_Tea_price'] = np.log(df['Tea_price'])
df['ln_Annual_income'] = np.log(df['Annual_income'])


# -----------------------------------------------------------
# STEP 9: LOG-LOG REGRESSION MODEL
# -----------------------------------------------------------
# In this model, coefficients represent percentage changes
# (i.e., elasticities)

Model_02 = ols(
    'ln_Coffee_consumption ~ ln_Coffee_price + ln_Sugar_price + ln_Tea_price + ln_Annual_income',
    data=df
).fit()

# Display results
print('\n----- REGRESSION RESULTS: LOG-LOG MODEL -----')
print(Model_02.summary())

# -----------------------------------------------------------
# END OF PROGRAM
# -----------------------------------------------------------
