import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],s=6)


    # Create first line of best fit
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    df1 = df.append([{'Year': y} for y in range(df['Year'].max() + 1, 2051)])
    
    plt.plot(
    df1['Year'],
    reg1.intercept + reg1.slope * df1['Year'],
    c='r',
    )


    # Create second line of best fit
    df2=df[df['Year']>=2000]
    reg2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])

    df2 = df2.append([{'Year': y} for y in range(df2['Year'].max() + 1, 2051)])
    
    plt.plot(
    df2['Year'],
    reg2.intercept + reg2.slope * df2['Year'],
    c='m',
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()