from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

s = Service(r"C:\My Projects\Laptops Web Scraping\msedgedriver.exe")
driver = webdriver.Edge(service=s)

base_url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
  
try:
  
    for page in range(1, 42):
        url = base_url + str(page)
        driver.get(url)
        time.sleep(2)
        
        with open(f'laptops.html', 'a', encoding='utf-8') as f:
            f.write(driver.page_source)
        
finally:
    driver.quit()
