import requests
from bs4 import BeautifulSoup
import os

class IndianaHarnessScraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def parse_pdf_link(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        # Locate the PDF link for the race data
        link = soup.find('a', href=True, text='Conditions')
        if link and link['href'].endswith('.pdf'):
            return link['href']
        return None

    def download_pdf(self, pdf_url, save_path):
        response = requests.get(pdf_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return save_path
        return None

    def run(self):
        html = self.fetch_data()
        if html:
            pdf_url = self.parse_pdf_link(html)
            if pdf_url:
                pdf_path = self.download_pdf(pdf_url, 'race_calendar.pdf')
                if pdf_path:
                    return pdf_path
        return None

if __name__ == "__main__":
    url = 'https://indianaharness.com/horsemen/indiana-sire-stakes/calendar'
    scraper = IndianaHarnessScraper(url)
    pdf_path = scraper.run()
    if pdf_path:
        print(f"PDF downloaded: {pdf_path}")
    else:
        print("Failed to download PDF.")
