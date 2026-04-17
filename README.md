# Project Name: Daraz Mobile Phones Web Scraper
###  GitHub Repository
https://github.com/ray0123321/daraz-scraper
### 1. Project Overview
* **Target Website:** https://www.daraz.pk
* **Data Fields Extracted:** Product Title, Price, Page Number
* **Tools Used:** Python, Selenium, Pandas, Webdriver Manager

This project is a web scraping tool that extracts mobile phone product data from Daraz search results. It collects multiple pages of products and stores them in a structured CSV format for analysis.

### 2. Setup Instructions
1. Clone this repo: `git clone https://github.com/ray0123321/daraz-scraper.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`

### 3. Challenges & Solutions
One major challenge was handling dynamic content loading on the Daraz website. The product listings do not load instantly, so the scraper required the use of time delays (`time.sleep()`) to ensure that all elements were fully loaded before extraction.

Another challenge was implementing pagination to scrape multiple pages of results. This was solved by using a loop that dynamically changes the page number in the URL.

Additionally, identifying the correct HTML structure was difficult due to frequently changing class names. This was resolved by inspecting the page source using browser developer tools and selecting stable CSS selectors.