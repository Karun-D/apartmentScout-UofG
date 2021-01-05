"""
------------------------------------------------------------------------
Notification Module
------------------------------------------------------------------------
Purpose: used to initalize email with listings to be sent
------------------------------------------------------------------------
"""

# Imports
from web_scraper import store_listings
from web_scraper import filter_listings
import program_features
import smtplib

def send_email():
    print("Creating email")

    # Setup email server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # EHLO - Command sent from email server to identify itself 
    server.ehlo()
    # STARTTLS - Command used to inform the email server to upgrade to a secure connection (using TLS)
    server.starttls()
    server.ehlo()

    # User's email account
    server.login(program_features.EMAIL_USER_SEND, program_features.EMAIL_PASS)

    # Create Email using listings from the database
    subject = "New Apartment Listings"
    body = "\n\n".join(store_listings())      
    msg = "Subject: {}\n\n{}".format(subject, body)

    # If there are new listings, send the email
    if len(body) > 0: 
        print("Sending email")
        server.sendmail(
            program_features.EMAIL_USER_SEND,                          # E-mail Address (From)
            program_features.EMAIL_USER_RECEIVE,                          # E-mail Address (To)
            msg
        )
        print("EMAIL HAS BEEN SENT")
    # If there are no new listings, print to console
    else:
        print("No new listings")
