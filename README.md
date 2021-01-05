<!-- PROJECT Title -->
# Apartment Scout (UofG)

<!-- ABOUT THE PROJECT -->
## About The Project

[The Cannon](https://www.thecannon.ca/) is a popular website for students who attend The University of Guelph. One of its main features is the housing page, where students visit to list/search for housing units in Guelph. 

This program web scrapes listings over a defined interval and sends them to the user via email. This program reduces the hassle of finding the ideal living situation by allowing the user to create a filter to narrow the results.

### Built With

* Python
* SQLAlchemy
* BeautifulSoup4
* SMTPLIB

### Prerequisites

1. [Python must be installed](https://www.python.org/downloads/)
2. User must allow [Less Secure Apps](https://myaccount.google.com/lesssecureapps) on Email Account

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Karun-D/apartmentScout-UofG
   ```
2. Enter folder
   ```sh
   cd apartmentScout-UofG
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Edit email account information and filter values in "program_features.py"

<!-- USAGE EXAMPLES -->
## Usage

Enter the following line in terminal
  ```sh
   python main.py
   ```

<!-- ROADMAP -->
## Future Plans

1. Find a practical way to host the program elsewhere (for free) with the ability to disable the program when not in use (Heroku? Docker? (Paid))
