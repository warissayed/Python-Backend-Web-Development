import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the medicine's page (update as needed)
url = "https://www.1mg.com/drugs/avastin-100mg-injection-135666"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

def get_text(selector):
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else ""

# Example selectors - these need to be adjusted based on the actual page structure and class names
medicine_info = {
    "Medicine Name": get_text("h1"),
    "Salt Composition": get_text("div.saltComp"),  # Update with correct selector
    "Therapeutic Class": get_text("div.theraputicClass"),  # Update as needed
    "Action Class": get_text("div.actionClass"),  # Update as needed
    "Type": get_text("div.form"),  # Example
    "Uses": get_text("div.uses"),  # Update as needed
    "Side Effects": get_text("div.sideEffects"),  # Update as needed
    "How it Works": get_text("div.howWorks"),  # Update as needed
    # ...add more fields as per actual HTML
}

# Print or save
print(medicine_info)

# Optionally, save to CSV
df = pd.DataFrame([medicine_info])
df.to_csv("medicine_scraped.csv", index=False)
