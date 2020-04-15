class BadAssetException(Exception):
    """Raised when user inputs a bad asset search string"""
    def __init__(self):
        self.message = "Asset wasn't found. Try again!\nTIP: Ensure you're searching the right market if the stock has a market prefix/suffix!\n"

class ServerException(Exception):
    """Raised when 500+ status code is received when making a request"""
    def __init__(self):
        self.message = "Sorry, the server is not available right now!\n Try again later.\n"

class BrokenPageException(Exception):
    """Raised when the Yahoo Finance page has changed in such a way that the scraper is now broken"""
    def __init__(self):
        self.message = "Sorry, it seems like Yahoo Finance has recently changed their page consequently rendering Stocky as currently broken! :(\n Please file an issue on the Stocky github page so we can fix it!"