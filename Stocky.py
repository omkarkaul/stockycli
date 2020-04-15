import urllib3
from CustomException import *
from bs4 import BeautifulSoup as soup

class Stocky:
    """Class containing central functionality for Stocky CLI"""
    def __init__(self, url):
        self.url = url
    
    def check_stock(self):
        try:
            asset = self.__get_asset_from_user()
                
            http = urllib3.PoolManager()
            client = http.urlopen('GET', self.url+asset, redirect=False)

            if client.status >= 500:
                raise ServerException()
            elif client.status != 200:
                raise BadAssetException()

        except BadAssetException as e:
            print(e.message)
            self.check_stock()
        except ServerException as e:
            print(e.message)
            exit()
        else:
            page_html = soup(client.data, 'html.parser')
            print(page_html.prettify())
            

    def __get_asset_from_user(self):
        asset = None

        while not asset:
            user_query = input('Enter an asset name to search: ')
        
            if user_query != "":
                asset = user_query
            else:
                print('Try again!')
        
        return asset