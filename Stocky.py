import urllib3
from CustomException import *
from bs4 import BeautifulSoup as soup

class Stocky:
    """Class containing central functionality for Stocky CLI"""
    def __init__(self, asset):
        self.url = "https://finance.yahoo.com/quote/"
        self.asset = asset
        self.price_attributes = {
            "element":"span",
            "attrs":{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}
        }
        self.time_attributes = {
            "id":"quote-market-notice"
        }
    
    def check_stock(self):
        try:
           # asset = self.__get_asset_from_user()
            asset = self.asset
                
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
            stock_data = self.__get_stock_data(page_html)
            
            print(f"{asset}'s latest price: ${stock_data['price']}, {stock_data['time']}\n")

    """OLD OLD OLD OLD OLD OLD OLD OLD"""
    def __get_asset_from_user(self):
        asset = None

        while not asset:
            user_query = input('Enter an asset name to search: ')
        
            if user_query != "":
                asset = user_query
            else:
                print('Try again!')
        
        return asset

    def __get_stock_data(self, bs4_html_object):
        price = self.__get_stock_price(bs4_html_object)
        time = self.__get_last_updated_time(bs4_html_object)

        return {
            "price":price,
            "time":time
        }

    def __get_stock_price(self, bs4_html_object):
        try:
            latest_price_element = bs4_html_object.find(self.price_attributes['element'],self.price_attributes['attrs'])

            if not latest_price_element:
                raise BrokenPageException('price')
        except BrokenPageException as e:
            print(f"Error finding the latest {e.arg}!")
            print(e.message)
            exit() # temporary early exit, figure out how to make parent Exception class soft exit or custom exit
        else:
            return latest_price_element.get_text()
    
    def __get_last_updated_time(self, bs4_html_object):
        try:
            current_time_container = bs4_html_object.find(id=self.time_attributes['id'])

            if not current_time_container:
                raise BrokenPageException('time')
        except BrokenPageException as e:
            print(f"Error finding the latest {e.arg}!")
            print(e.message)
            exit() # temporary early exit, figure out how to make parent Exception class soft exit or custom exit
        else:
            market_notice_string = current_time_container.contents[0].get_text()
            return market_notice_string[0].lower() + market_notice_string[1:] # return new string with first letter lowercase
