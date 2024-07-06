
# Cross-Stake 
Cross-Stake is a Django-based web application that indexes the dates for staking horses and creates a database of horses and their respective series. The application automates the indexing of staking information from various horse racing associations across the country, stores this information in a database, and provides notifications for upcoming staking deadlines. Additionally, the application supports payment processing and receipt generation for stakes.

## Features
Indexes staking information from multiple horse racing associations
Stores horse and owner information in a database
Provides notifications for upcoming staking deadlines
Generates receipts for stakes
Supports payment processing
Scrapes and parses PDF documents containing race information
Integrates with OpenAI and Claude 3.5 Sonnet for parsing PDF data

## Project Structure
plaintext
Copy code
cross_stake/
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── cross_stake/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── horses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── scrapers/
│   │   ├── __init__.py
│   │   ├── indiana_harness_scraper.py
│   ├── analysis.py
│   └── management/
│       ├── __init__.py
│       └── commands/
│           ├── __init__.py
│           ├── check_db.py
│           ├── scrape_data.py
│           └── analyze_data.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── add_horse.html
└── static/
    └── style.css

## Getting Started
Prerequisites
Docker
Docker Compose
Python 3.9+
pip
Installation

## Clone the repository:

bash
Copy code
git clone https://github.com/millerjes37/Cross-Stake.git
cd Cross-Stake
Build the Docker image:

bash
Copy code
docker-compose build
Start the Docker containers:

bash
Copy code
docker-compose up -d
Run database migrations:

bash
Copy code
docker-compose exec web python manage.py migrate
Create a superuser:

bash
Copy code
docker-compose exec web python manage.py createsuperuser
Access the application:

Open your web browser and go to http://localhost:8000.

Usage
Scraping Data
To scrape data from the Indiana Harness website and populate the database:

Run the scraper:

bash
Copy code
docker-compose exec web python manage.py scrape_data
This command will download the PDF from the Indiana Harness website, send it to OpenAI and Claude 3.5 Sonnet for parsing, validate the parsed data, and save it to the database.

API Integration
OpenAI
Set up OpenAI API key:

bash
Copy code
export OPENAI_API_KEY='your-openai-api-key'
Claude 3.5 Sonnet
Set up Claude API key:

bash
Copy code
export CLAUDE_API_KEY='your-claude-api-key'
Directory Structure
cross_stake/: Main project directory containing settings, URLs, and WSGI configuration.
horses/: Django app directory containing models, views, and additional scripts for scraping and analysis.
scrapers/: Directory for scraper modules.
management/commands/: Custom Django management commands.
templates/: Directory for HTML templates.
static/: Directory for static files like CSS.
Adding Horses and Owners
Owners and trainers can create and edit profiles on the website where they can manage payments, add horses, view receipts/stake confirmations, and see upcoming deadlines. Horse registration requires logging in.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request
Contact
If you have any questions, feel free to open an issue or contact the repository owner at millerjes37@gmail.com.
This Program will:
1. Index race information for all horse races by scraping data from association websites.
2. Allow for owner registration for selected series.
3. Allow for Owners to discriminate series on a horse by horse basis.
4. Allow for simplified payment and receipt of staking confirmations.
