# -----------------------------------------------------------
# HOMEWORK 3: CUBIC COST FUNCTION ESTIMATION
# -----------------------------------------------------------
# This program:
# 1. Loads production and cost data
# 2. Creates polynomial terms (Q^2 and Q^3)
# 3. Displays descriptive statistics
# 4. Examines correlation among polynomial terms
# 5. Estimates a cubic cost function
# 6. Plots Total Cost vs Quantity with fitted curve
# -----------------------------------------------------------

# -----------------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Regression library
from statsmodels.formula.api import ols

# -----------------------------------------------------------
# STEP 2: LOAD THE DATA
# -----------------------------------------------------------

df = pd.read_csv('Cubic_cost_function.csv')

# Preview the data
print(df.head())

# -----------------------------------------------------------
# STEP 3: CREATE POLYNOMIAL TERMS
# -----------------------------------------------------------
# These allow us to estimate a cubic cost function

df['Q_squared'] = df['Quantity'] ** 2
df['Q_cubed'] = df['Quantity'] ** 3

# -----------------------------------------------------------
# STEP 4: DESCRIPTIVE STATISTICS (ONLY Q AND COSTS)
# -----------------------------------------------------------

stats = df[['Quantity', 'Total_Cost']]

desc_stats = stats.describe().T
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

desc_stats = desc_stats.round(3)

print('\n----- DESCRIPTIVE STATISTICS (Q & COSTS) -----')
print(desc_stats)

# -----------------------------------------------------------
# STEP 5: CORRELATION MATRIX (Total_Cost, Q, Q^2, AND Q^3 ONLY)
# -----------------------------------------------------------

poly_vars = df[['Total_Cost','Quantity','Q_squared', 'Q_cubed']]

corr_poly = poly_vars.corr()

print('\n----- CORRELATION MATRIX (Total_Cost, Q, Q^2, Q^3) -----')
print(corr_poly)

# Optional heatmap (nice visual)
plt.figure(figsize=(6, 5))
sns.heatmap(corr_poly, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation: Total_Cost, Q, Q^2 and Q^3')
plt.show()

# -----------------------------------------------------------
# STEP 6: ESTIMATE THE CUBIC COST FUNCTION
# -----------------------------------------------------------
# Cost = β0 + β1*Q + β2*Q^2 + β3*Q^3

model = ols('Total_Cost ~ Quantity + Q_squared + Q_cubed', data=df).fit()

print('\n----- CUBIC COST FUNCTION RESULTS -----')
print(model.summary())

# -----------------------------------------------------------
# STEP 7: PLOT TOTAL COST VS QUANTITY
# -----------------------------------------------------------

# Generate predicted costs
df['Costs_pred'] = model.predict(df[['Quantity', 'Q_squared', 'Q_cubed']])

# Sort values for smooth curve
df_sorted = df.sort_values(by='Quantity')

# Create the plot
plt.figure(figsize=(10, 6))

# Scatter plot (actual data)
plt.scatter(df['Quantity'], df['Total_Cost'],
            color='cornflowerblue',
            label='Actual Costs')

# Fitted curve
plt.plot(df_sorted['Quantity'], df_sorted['Costs_pred'],
         color='crimson',
         linewidth=2,
         label='Fitted Cubic Cost Function')

# Labels and title
plt.xlabel('Quantity Produced')
plt.ylabel('Total Cost')
plt.title('Total Cost vs Quantity (Cubic Cost Function)')

# Legend and grid
plt.legend()
plt.grid()

# Show plot
plt.show()
