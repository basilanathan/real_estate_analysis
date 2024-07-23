import pandas as pd
import os

def load_and_clean_data(file_path):
    """
    Load data from a CSV file and clean relevant columns.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df = pd.read_csv(file_path)
    print("Columns in the dataset:", df.columns)

    # Cleaning 'price' column
    def clean_price(x):
        if 'K' in x:
            return float(x.replace('K', '')) * 1000
        elif 'M' in x:
            return float(x.replace('M', '')) * 1000000
        else:
            return float(x.replace('+', ''))

    if 'price' in df.columns:
        df['price'] = df['price'].replace(r'[\$,]', '', regex=True)
        df['price'] = df['price'].apply(clean_price)

    # Cleaning 'size' column if it exists
    if 'size' in df.columns:
        df['size'] = df['size'].replace(r'[\, sqft]', '', regex=True).astype(float)

    # Cleaning 'beds' column if it exists
    if 'beds' in df.columns:
        df['beds'] = df['beds'].replace(' beds', '', regex=True).astype(float)

    # Cleaning 'baths' column if it exists
    if 'baths' in df.columns:
        df['baths'] = df['baths'].replace(' baths', '', regex=True).astype(float)

    # Cleaning 'zip_code' column if it exists
    if 'zip_code' in df.columns:
        df['zip_code'] = df['zip_code'].astype(str).str.zfill(5)

    return df

if __name__ == "__main__":
    # Ensure the input file path is correct
    input_path = 'zillow_data.csv'  # Adjust the path if needed
    output_path = os.path.join('data', 'processed', 'cleaned_zillow_data.csv')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = load_and_clean_data(input_path)

    # Save the cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")