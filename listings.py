"""
------------------------------------------------------------------------
WebListing Module
------------------------------------------------------------------------
"""

class WebListing:
    """
    Defines an object for a single food: name, origin, vegetarian, calories.
    """
    def __init__(self, created, available, listing_type, room_type, address, distance, sublet, rooms, features, price, listing_id, link):
        """
        -------------------------------------------------------
        Initialize a listing object
        -------------------------------------------------------
        Parameters:
            created - date listing was created
            available - date the housing unit is available
            listing_type - if the unit is "offered" or "wanted" 
            room_type - type of housing unit (house, apartment, room)
            address - address of listing
            distance - distance from UofG
            sublet - if the unit allows subletting
            rooms - number of rooms in unit
            features - features of housing unit
            price - monthly cost to rent unit
            link - URL to listing
        Returns:
            A new Food object (Food)
        -------------------------------------------------------
        """
        self.created = created
        self.available = available
        self.listing_type = listing_type
        self.room_type = room_type
        self.address = address
        self.distance = distance
        self.sublet = sublet
        self.rooms = rooms
        self.features = features
        self.price = price
        self.listing_id = listing_id
        self.link = link
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string for listing
        Use: s = str(f)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of listing (str)
        -------------------------------------------------------
        """

        string = """Date Posted: {} | Available: {} | {} | Type: {}
Address: {}
Price: {} | Distance: {} | Sublet: {} | Rooms: {}
Features: {}
{}""".format(self.created.encode('utf-8'), self.available.encode('utf-8'), self.listing_type.encode('utf-8'),
             self.room_type.encode('utf-8'), self.address.encode('utf-8'), self.price.encode('utf-8'),
             self.distance, self.sublet.encode('utf-8'), self.rooms, self.features.encode('utf-8'), self.link.encode('utf-8'))

        return string

    """
    format(listing.created.encode('utf-8'), listing.available.encode('utf-8'),
           listing.listing_type.encode('utf-8'), listing.room_type.encode('utf-8'),
           listing.address.encode('utf-8'), listing.price.encode('utf-8'),
           listing.distance,
           listing.sublet.encode('utf-8'), listing.rooms,
           listing.features.encode('utf-8'), listing.link.encode('utf-8')))
    """

