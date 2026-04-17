from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

print("Starting Daraz scraper...")

# Setup browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

data = []

# Scrape 5 pages
for page in range(1, 6):

    url = f"https://www.daraz.pk/catalog/?q=mobile&page={page}"
    driver.get(url)

    print(f"\nScraping page {page}...")

    # wait for page to load 
    time.sleep(6)

    products = driver.find_elements(By.CSS_SELECTOR, "div.Bm3ON")

    print("Products found:", len(products))

    for p in products:
        try:
            text = p.text.split("\n")

            if len(text) >= 2:
                title = text[0]
                price = text[1]

                data.append({
                    "Title": title,
                    "Price": price,
                    "Page": page
                })

        except:
            continue

# Save data to CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("\nScraping completed ✔")
print(f"Total products collected: {len(data)}")

# wait before closing 
time.sleep(6)

driver.quit()

print("Browser closed ✔")