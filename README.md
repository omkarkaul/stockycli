# stockycli

This is the stocky cli. User enters an asset to lookup and stocky scrapes latest data from yahoo finance and displays it to the user. I built it so that I can quickly check up on the post March 23rd 2020, COVID-19 related, Air New Zealand uptick :moneybag: :moneybag: :moneybag:

## Dependencies:

- Pipenv (optional)
- Python 3.6
- BS4
- urllib3
- Click

## How to use:
- Clone the repo to a folder of your choosing
- CD to the chosen directory and build the app by typing the following:
```
python3 setup.py bdist_wheel
```
- Now install the package locally on your machine by typing the following:
```
pip install dist/stockycli-1.0-py3-none-any.whl
```

A _whl_ or _Wheel_ file is the standard built-package format used for Python modules.  

Now, in your terminal, you can use the alias __stockycli__, followed by the __--price__ flag and a valid asset name to search for its price, like so:
```
$ ~ stockycli --price AIR.NZ
$ ~ AIR.NZ's latest price: $1.3100, at close: 5:00PM NZST
```

Please file an issue if you find any, or contact me directly :)

## TODO:
- [x] scrape latest price and time
- [x] encapsulate data retrieval 
- [x] add some custom exceptions
- [x] finish scraper logic
- [x] build actual cli
- [x] more error handling
- [ ] _more_ more error handling
- [ ] continue TDD
- [ ] upload to pypi to bypass the cumbersome build + install process
