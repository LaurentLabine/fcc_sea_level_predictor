import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
#Note to self. Issue with latest pandas version breaks testing.  To solve, set Pandas version to 1.1.5 in 
#pyproject.toml and poetry.lock.  Issue developments trackd at : 
# https://forum.freecodecamp.org/t/sea-level-predictor-errors/437517/10 

data_url = "https://raw.githubusercontent.com/LaurentLabine/fcc_data_analysis_python/main/epa-sea-level.csv"

def draw_plot():
    # Read data from file
  df = pd.read_csv(data_url)

    # Create scatter plot
  fig, ax = plt.subplots(figsize=(10, 6))
  ax.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
  plt.xlabel("Year")
  plt.ylabel("CSIRO Adjusted Sea Level")

    # Create first line of best fit
  res = linregress(df["Year"], df['CSIRO Adjusted Sea Level'])
  line_x = np.arange(df["Year"].min(), 2050)
  line_y = line_y = res.slope*line_x + res.intercept
  plt.plot(line_x,line_y)

    # Create second line of best fit
  df2000 = df[(df.Year >= 2000) ]
  res2 = linregress(df2000.Year, df2000['CSIRO Adjusted Sea Level'])
  line_x = np.arange(2000, 2050)
  line_y = line_y = res2.slope*line_x + res2.intercept
  plt.plot(line_x,line_y)

    # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)') 
  ax.set_title('Rise in Sea Level') 
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()