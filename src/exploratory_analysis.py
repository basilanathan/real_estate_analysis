# src/exploratory_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from data_cleaning import load_and_clean_data

# Load and clean the data
df = load_and_clean_data('zillow_data.csv')

def plot_distribution(df, output_path):
    # Distribution of Prices
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title('Distribution of Property Prices')
    plt.xlabel('Price (Log Scale)')
    plt.ylabel('Frequency')
    plt.xscale('log')
    plt.savefig(os.path.join(output_path, 'price_distribution.png'))
    plt.show()
    plt.close()

def plot_price_vs_area(df, output_path):
    # Scatter plot of Price vs Area
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='area', y='price', data=df)
    plt.title('Price vs Square Footage')
    plt.xlabel('Square Footage (sqft)')
    plt.ylabel('Price')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig(os.path.join(output_path, 'price_vs_area.png'))
    plt.show()
    plt.close()

def plot_avg_price_by_beds(df, output_path):
    # Average Price by Number of Bedrooms
    avg_price_beds = df.groupby('beds')['price'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='beds', y='price', data=avg_price_beds)
    plt.title('Average Price by Number of Bedrooms')
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Average Price')
    plt.savefig(os.path.join(output_path, 'avg_price_by_beds.png'))
    plt.show()
    plt.close()

def plot_price_distribution_by_city(df, output_path):
    # Price Distribution by City
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='addressCity', y='price', data=df)
    plt.xticks(rotation=90)
    plt.title('Price Distribution by City')
    plt.xlabel('City')
    plt.ylabel('Price')
    plt.yscale('log')
    plt.savefig(os.path.join(output_path, 'price_distribution_by_city.png'))
    plt.show()
    plt.close()

if __name__ == "__main__":
    output_path = 'data/plots'
    os.makedirs(output_path, exist_ok=True)
    
    plot_distribution(df, output_path)
    plot_price_vs_area(df, output_path)
    plot_avg_price_by_beds(df, output_path)
    plot_price_distribution_by_city(df, output_path)