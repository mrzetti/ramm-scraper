# Scraper for the [RammsteinShop](https://shop.rammstein.de/en)

## Installation

### Required
* [git](https://git-scm.com/downloads)
* [python](https://www.python.org/downloads/)

### Quick start
`git clone https://github.com/mrzetti/ramm-scraper`  
`pip install -r requirements.txt`

## Usage

`python ramm_scraper.py [-h] [--start START] [--end END] [--new]`

	options:
    -h, --help     show this help message and exit

    --start START  Starting id. Default: 0

    --end END      Ending id. Default: 10.000

    --new          Enable scraping new items.

## Info

Creates the directory `RammsteinShop` with subfolders for each 'item' in a given id range.


## TODO:

* add `--new` functionality