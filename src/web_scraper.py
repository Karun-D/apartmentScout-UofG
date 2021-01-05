"""
------------------------------------------------------------------------
Webscraper Module
------------------------------------------------------------------------
Purpose: used to scrape listings of housing units from thecanon.ca
(UofG student website)
------------------------------------------------------------------------
"""

# Imports
import requests
import datetime

from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker

from database import get_engine
from database import DatabaseListing
from listings import WebListing
import program_features

# Create database session using apartment_listings.db connection
Session = sessionmaker(bind=get_engine())
session = Session()

def scrape_listings():
    """
    -------------------------------------------------------
    Scrapes listings from the canon.ca
    -------------------------------------------------------
    """
    scraped_listings = []                                       # Used to store apartment listings
    links = []                                                  # Used to store links to apartment listings (seperate tag)

    # Download "The Canon" website
    URL = "https://www.thecannon.ca/classifieds/housing"
    headers = program_features.HEADERS
    page = requests.get(URL, headers=headers)

    # Parse document
    soup = BeautifulSoup(page.content, "html.parser")
    page_listings = list(soup.find_all('td'))                   # Find all listing information, and store as list

    # Used to find URL parameters for each apartment listing
    for link in soup.find_all("a"):
        # URL Format Example: "<a href="/page.php?cid=347306&amp;id=26&amp;t=housing">1219 Gordon St, Guelph</a>"
        if link.has_attr('href') and ("t=housing" in link.attrs['href']):
            links.append("https://www.thecannon.ca" + link.attrs['href'])

    # Iterate list  
    for i, listing in enumerate(page_listings, 1):
        # Group every 10 elements into a listing object
        if i % 10 == 0:
            index = int(i / 10) - 1                                     # Calculate index of link that matches the current listing 

            # Append listing object to array
            scraped_listings.append(
                # Create listing object
                WebListing(
                    page_listings[i - 10].get_text().strip(),           # Date post was created
                    page_listings[i - 9].get_text().strip(),            # Date apartment is available
                    page_listings[i - 8].get_text().strip(),            # Offering type
                    page_listings[i - 7].get_text().strip(),            # Housing type
                    page_listings[i - 6].get_text().strip(),            # Address 
                    page_listings[i - 5].get_text().strip(),            # Price
                    page_listings[i - 4].get_text().strip(),            # Distance 
                    page_listings[i - 3].get_text().strip(),            # Sublet permission
                    page_listings[i - 2].get_text().strip(),            # Number of rooms
                    page_listings[i - 1].get_text().strip(),            # Features
                    links[index][38:44],                                # Listing ID (stored in link)
                    links[index]                                        # Listing Link
                )
            )

    return scraped_listings                                             # Return listings array

def store_listings():
    """
    -------------------------------------------------------
    - Stores listings from scraper to database
    - Ensures listings aren't duplicated 
    -------------------------------------------------------
    """

    scraped_listings = scrape_listings()                                # Used to store scraped listings
    valid_listings = []                                                 # Used to store valid listings (after filtering)
    num_valid_listings = 1                                              # Counts the number of valid listings for output

    for listing in scraped_listings:
        # If the Listing ID of the current listing does not exist in the database...
        if session.query(DatabaseListing).filter_by(listing_id=listing.listing_id).first() is None:
            # Safe-guard distance variable (decimal)
            if listing.distance == "n/a":
                listing.distance = 0.0
            else:
                listing.distance = listing.distance[:-2]

            # Create listing object for database
            listing = DatabaseListing(
                created=listing.created,
                available=listing.available,
                listing_type=listing.listing_type,
                room_type=listing.room_type,
                address=listing.address,
                distance=listing.distance,
                sublet=listing.sublet,
                rooms=int(listing.rooms),
                features=listing.features,
                price=listing.price,
                listing_id=int(listing.listing_id),
                link=listing.link
            )

            # Save listing to database
            session.add(listing)
            session.commit()
            

            if (program_features.FILTER == True) and (filter_listings(listing) == False):
                print ("Listing #{} does not match filter".format(num_valid_listings))
            else:
                # Save valid listing (with ASCII encoding for Email server)
                valid_listings.append("""Date Posted: {} | Available: {} | {} | Type: {}
                Address: {}
                Price: {} | Distance: {} | Sublet: {} | Rooms: {}
                Features: {}
                {}""".format(listing.created, listing.available,
                            listing.listing_type, listing.room_type,
                            listing.address, listing.price,
                            (str(listing.distance) + " km"),
                            listing.sublet, listing.rooms,
                            str(listing.features.encode('utf-8')), listing.link))

                # Output success statement 
                print("Listing #{} loaded".format(num_valid_listings))
                    
            # Increment valid listings counter
            num_valid_listings += 1
            
        # If the Listing ID of the current listing exists in the database...
        else:
            print("Listing already loaded")

    return valid_listings                                               # Return valid listings array

def filter_listings(listing):
    """
    -------------------------------------------------------
    Returns valid listings based on user's preferences
    -------------------------------------------------------
    """

    MIN_PRICE = program_features.MIN_PRICE
    MAX_PRICE = program_features.MAX_PRICE

    MAX_DISTANCE = program_features.MAX_DISTANCE

    MIN_NUM_ROOMS = program_features.MIN_NUM_ROOMS
    MAX_NUM_ROOMS = program_features.MAX_NUM_ROOMS

    if (float(listing.price[1:4]) < MIN_PRICE) or (float(listing.price[1:4]) > MAX_PRICE):
        print ("Listing price = {}".format(listing.price[1:4], ))
        return False
    elif (float(listing.distance) > MAX_DISTANCE):
        print ("Listing distance = {}".format(float(listing.distance)))
        return False
    elif (int(listing.rooms) < MIN_NUM_ROOMS) or (int(listing.rooms) > MAX_NUM_ROOMS) :
        print ("Listing rooms = {}".format(int(listing.rooms)))
        return False
    else:
        return True

