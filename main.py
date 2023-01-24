from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv


"""Make a CSV file containing updated major data."""

site = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
site_text = site.text
soup = BeautifulSoup(site_text, 'html.parser')
rows = soup.find_all('tr', class_='data-table__row')

# for each row, get the column data
data = []
for row in rows:
    cols = row.find_all('td')
    major = cols[1].text.split(':')[1]
    degree = cols[2].text.split(':')[1]
    early_career_pay = cols[3].text.split(':')[1]
    mid_career_pay = cols[4].text.split(':')[1]
    meaning = cols[5].text.split(':')[1]
    data.append([major, degree, early_career_pay, mid_career_pay, meaning])


# Turn the data into a csv file
with open('salaries_by_major.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Major', 'degree', 'Starting Salary', 'Mid Career Salary', 'Meaning'])
    writer.writerows(data)