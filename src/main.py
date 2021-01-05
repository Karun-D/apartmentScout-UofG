"""
------------------------------------------------------------------------
This program scrapes apartment listings from the University of Guelph's
"The Canon" website, and forwards them using an email client based on
the user's preferences. 
------------------------------------------------------------------------
Author: Karunpreet Dhamnait
Email:  kdhamnai@uoguelph.ca
__updated__ = "2020-12-15"
------------------------------------------------------------------------
"""

# Imports
from notification import send_email
import program_features
import time
import sys

def main():
    # Program scrapes website (with delay) until user exits
    while True:
        # Exit statement
        print("{}: Beginning to scrape website. Type ""Ctrl-C"" to exit loop".format(time.ctime()))
       
        # Scrape website and send email
        try:
            send_email()
        # If user exits program via "Ctrl-C"
        except KeyboardInterrupt:
            print("Exiting Program")
            sys.exit(1)
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))
        # Time Delay
        time.sleep(program_features.DELAY)

# Main needs to be called explicitly.
if __name__ == "__main__":                          # If code is the main program, main is called
    main()                                          # If code is imported as a module, main is not called
