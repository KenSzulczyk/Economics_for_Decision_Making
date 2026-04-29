# The next plot shows the closing index for Hang Seng, the Hong Kong Stock Market. 
# We also plot the 200 day and 50 day moving average. We also indicate a bull market 
# by the green shading, and a bear market by the red shading.

# -----------------------------------------------------------
# HANG SENG INDEX: TIME SERIES PLOT WITH MOVING AVERAGES
# -----------------------------------------------------------

# Import the required libraries
import pandas as pd              # For working with data tables
import matplotlib.pyplot as plt  # For plotting graphs
import seaborn as sns            # For nicer plot styling

# -----------------------------------------------------------
# STEP 1: LOAD THE DATA
# -----------------------------------------------------------

# Read the CSV file into a DataFrame
# (Make sure the file is in the same folder as your script,
# or provide the full file path)
df = pd.read_csv('Hang_Seng_Index.csv')

# -----------------------------------------------------------
# STEP 2: PREPARE THE DATE COLUMN
# -----------------------------------------------------------

# Convert the "New_date" column into a proper datetime format
# This allows Python to treat it as time (not just text)
df['Date'] = pd.to_datetime(df['New_date'])

# -----------------------------------------------------------
# STEP 3: SET THE PLOT STYLE
# -----------------------------------------------------------

# Use a clean background style
sns.set_style('whitegrid')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# -----------------------------------------------------------
# STEP 4: PLOT THE DATA
# -----------------------------------------------------------

# Plot the Hang Seng Index (closing prices)
ax.plot(df['Date'], df['Closing'],
        color='cornflowerblue',
        linewidth=1,
        label='Hang Seng Index')

# Plot the 200-day moving average (long-term trend)
ax.plot(df['Date'], df['MA200'],
        color='green',
        linewidth=1,
        label='200-day Moving Average')

# Plot the 50-day moving average (short-term trend)
ax.plot(df['Date'], df['MA50'],
        color='red',
        linewidth=1,
        label='50-day Moving Average')

# -----------------------------------------------------------
# STEP 5: HIGHLIGHT BULL AND BEAR MARKETS
# -----------------------------------------------------------

# Bear market (shaded in red)
ax.axvspan(pd.Timestamp('2021-08-09'),
           pd.Timestamp('2023-12-31'),
           color='crimson',
           alpha=0.25,
           label='Bear Market')

# Bull market (shaded in green)
ax.axvspan(pd.Timestamp('2016-01-21'),
           pd.Timestamp('2018-07-13'),
           color='green',
           alpha=0.25,
           label='Bull Market')

# -----------------------------------------------------------
# STEP 6: ADD LABELS AND LEGEND
# -----------------------------------------------------------

# Add title and axis labels
ax.set_title('Hang Seng Index with Moving Averages', fontsize=14)
ax.set_xlabel('Date')
ax.set_ylabel('Index Level')

# Show legend
ax.legend()

# -----------------------------------------------------------
# STEP 7: SAVE AND DISPLAY THE PLOT
# -----------------------------------------------------------

# Save the figure BEFORE showing it
plt.savefig('Figure-Time_series_plot.png',
            bbox_inches='tight',
            dpi=600)

# Display the plot on screen
plt.show()
