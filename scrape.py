import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL
base_url = "https://pratham.org/"

# Define specific paths for each section
paths = {
    "About Us": "https://pratham.org/about/",
    "Programs": "https://pratham.org/programs/#",
    "Job Opportunities": "https://pratham.org/get%20involved/#",
    "Resources": "https://pratham.org/resources/#",
    "Contact": "https://pratham.org/contact/"
}

# Function to extract text from a section
def extract_section_text(section_soup):
    texts = section_soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return "\n".join([text.get_text(strip=True) for text in texts])

# Create a dictionary to hold the scraped data
scraped_data = {}

# Scrape each section based on the specific paths
for section_name, path in paths.items():
    url = base_url + path
    response = requests.get(url)
    if response.status_code == 200:
        section_soup = BeautifulSoup(response.content, "html.parser")
        scraped_data[section_name] = extract_section_text(section_soup)
    else:
        scraped_data[section_name] = f"Failed to retrieve {section_name}"

# Convert the scraped data to a DataFrame and save to CSV
df = pd.DataFrame.from_dict(scraped_data, orient='index', columns=["Content"])
df.to_csv("pratham_scraped_data.csv")

print("Data scraped and saved to pratham_scraped_data.csv")
