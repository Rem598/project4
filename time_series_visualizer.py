import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
def load_data():
    # Load data from the CSV file and set the index to the date column
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    return df

# Clean the data
def clean_data(df):
    # Filter out the top 2.5% and bottom 2.5% of page views
    lower_limit = df['value'].quantile(0.025)
    upper_limit = df['value'].quantile(0.975)
    return df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

# Draw line plot
def draw_line_plot():
    df = load_data()
    df = clean_data(df)

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=2)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

# Draw bar plot
def draw_bar_plot():
    df = load_data()
    df = clean_data(df)

    # Create a new dataframe with average daily page views for each month grouped by year
    df['year'] = df.index.year
    df['month'] = df.index.month_name()

    avg_page_views = df.groupby(['year', 'month'])['value'].mean().unstack()
    avg_page_views = avg_page_views.reindex(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], axis=1)

    plt.figure(figsize=(12, 6))
    avg_page_views.plot(kind='bar', ax=plt.gca())
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

# Draw box plots
def draw_box_plot():
    df = load_data()
    df = clean_data(df)

    df['year'] = df.index.year
    df['month'] = df.index.month

    plt.figure(figsize=(14, 6))

    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()
