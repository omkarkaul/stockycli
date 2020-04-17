import click
from Stocky import *

@click.command()
@click.option('--price', default='', help = "This flag allows you to query an asset for its price!")
def cli(price):
    if price == '':
        print("Try the '--price' flag, followed by a valid asset name!")
    else:
        stocky = Stocky(price)
        stocky.check_stock()

