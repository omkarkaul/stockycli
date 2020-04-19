from setuptools import setup

setup(
    name="stockycli",
    version="1.0",
    py_modules=["stockycli", "Stocky", "CustomException"],
    include_package_data=True,
    install_requires = [
        "click",
        "beautifulsoup4",
        "urllib3",
    ],
    entry_points = """
        [console_scripts]
        stockycli=stockycli:cli
    """,
    )
