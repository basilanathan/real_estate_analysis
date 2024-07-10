from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your Apify API token
client = ApifyClient("apify_api_YeBF1m38SFBNjs86QCZ63VS43sJEuD2YThqi")

# Prepare the Actor input
run_input = {
    "searchUrls": [
        {
            "url": "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-124.61572460426518%2C%22east%22%3A-120.37225536598393%2C%22south%22%3A36.71199595991113%2C%22north%22%3A38.74934086729303%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22customRegionId%22%3A%227d43965436X1-CRmxlqyi837u11_1fi65c%22%7D"
        }
    ]
}

# Run the Actor and wait for it to finish
run = client.actor("maxcopell/zillow-scraper").call(run_input=run_input)

# Fetch Actor results from the run's dataset
dataset_items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

# Save results to a CSV file
df = pd.DataFrame(dataset_items)
df.to_csv('zillow_data.csv', index=False)

# Print the URL to access the dataset and the number of items
print(f"💾 Check your data here: https://console.apify.com/storage/datasets/{run['defaultDatasetId']}")
print(f"Number of properties scraped: {len(dataset_items)}")