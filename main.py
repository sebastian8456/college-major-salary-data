from bs4 import BeautifulSoup
import pandas as pd
import requests

"""Make a CSV file containing updated major data."""

site = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
site_text = site.text
soup = BeautifulSoup(site_text, 'html.parser')
rows = soup.find_all('tr', class_='data-table__row')