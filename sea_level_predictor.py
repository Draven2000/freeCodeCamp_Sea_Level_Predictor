import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Create scatter plot
    '''Use matplotlib to create a scatter plot using the Year column as the x-axis 
    and the CSIRO Adjusted Sea Level column as the y-axis.'''
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label = 'Data')

    # Create first line of best fit
    '''Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
    Plot the line of best fit over the top of the scatter plot. 
    Make the line go through the year 2050 to predict the sea level rise in 2050.'''
    model = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    '''Predicting Y values over time from model '''
    import numpy as np
    X_range = np.linspace(1880, 2050, (2050-1880)+1)
    Y_predict = X_range * model.slope
    plt.plot(X_range, (model.intercept+Y_predict), 'g--', label='Prediction from all data')

    # Create second line of best fit
    '''Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. 
    Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.'''
    df_2000 = df[df['Year'] >= 2000]
    model2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    '''Predicting Y values over time from model '''
    X_range = np.linspace(2000, 2050, (2050-2000)+1)
    Y_predict = X_range * model2000.slope
    plt.plot(X_range, (model2000.intercept+Y_predict), 'r-', label='Prediction from 2000 onwards')
    print()


    # Add labels and title
    '''The x label should be Year, the y label should be Sea Level (inches), 
    and the title should be Rise in Sea Level.'''
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    '''Appears to be a strange quirk of the freeCodeCamp test code running through the function four times
    as the legend shows four sets of the three labels.
    Left the legend code in as it aids the readability of the plot.'''
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()