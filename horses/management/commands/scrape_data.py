from django.core.management.base import BaseCommand
from horses.scrapers.indiana_harness_scraper import IndianaHarnessScraper
from parse_pdf_with_openai import parse_pdf_with_openai
from parse_pdf_with_claude import parse_pdf_with_claude
from save_parsed_data import save_parsed_data

class Command(BaseCommand):
    help = 'Runs the scrapers and populates the database'

    def handle(self, *args, **kwargs):
        url = 'https://indianaharness.com/horsemen/indiana-sire-stakes/calendar'
        scraper = IndianaHarnessScraper(url)
        pdf_path = scraper.run()

        if pdf_path:
            openai_json = parse_pdf_with_openai(pdf_path)
            claude_json = parse_pdf_with_claude(pdf_path)

            if openai_json:
                self.stdout.write(self.style.SUCCESS('Data parsed with OpenAI'))
                save_parsed_data(openai_json)
            if claude_json:
                self.stdout.write(self.style.SUCCESS('Data parsed with Claude'))
                save_parsed_data(claude_json)
        else:
            self.stdout.write(self.style.ERROR('Failed to download PDF.'))
