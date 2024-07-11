import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])



# Clean data
clean_top_days = df['value'] <= df['value'].quantile(0.975)
clean_bottom_days = df['value'] >= df['value'].quantile(0.025)
df = df[clean_bottom_days & clean_top_days]
 

def draw_line_plot():
    fig = plt.figure(figsize=(8, 6))
    # Draw line plot
    plt.plot(df['date'], df['value'] )
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016--12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df['date'].dt.year
    df_bar['month'] = df['date'].dt.month_name()
    #Month-sorting sorts alphabetically by default
    df_bar['month'] = pd.Categorical(df_bar['month'], ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    df_bar.drop('date', axis = 1, inplace=True)
    df_bar = df_bar.groupby([df_bar['year'], df_bar['month']]).mean().reset_index()


    fig, ax = plt.subplots(figsize=(20, 7))

    # Draw bar plot
    sns.barplot(data = df_bar, x='year', y='value', hue='month')
    ax.legend(title='Months')
    ax.set(xlabel='Years', ylabel='Average Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots 
    df_box = df.copy()
    df_box['year'] = df['date'].dt.year
    df_box['month'] = df['date'].dt.month_name()
    #Month-sorting sorts alphabetically by default
    df_box['month'] = pd.Categorical(df_box['month'], ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    df_box.drop('date', axis = 1, inplace=True)
    df_box = df_box.groupby([df_box['year'], df_box['month']]).mean().reset_index()
    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(20, 7))

    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x='year', y='value', hue='year')
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x='month', y='value', hue='month')
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

