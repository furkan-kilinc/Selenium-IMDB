# IMDB Movie Scraper

## Overview
This project is an educational tool designed for practicing web scraping techniques with Selenium. It scrapes data from Oscar-nominated comedy movies on IMDB and exports the information to an Excel file.

## Disclaimer
This project is created for educational purposes only to demonstrate web scraping techniques. Please respect IMDB's terms of service when using this code.

## Features
- Automatically navigates to IMDB's advanced search
- Filters for comedy movies that received Oscar nominations
- Extracts comprehensive movie data including:
  - Movie title
  - Release year
  - Duration
  - IMDB rating
  - Number of votes
  - Metascore (if available)
  - Movie description
- Exports all data to an Excel file

## Requirements
- Python 3.x
- Chrome browser
- ChromeDriver

## Installation
1. Clone this repository
2. Install required packages using the requirements.txt file:
   ```
   pip install -r requirements.txt
   ```
3. Make sure you have Chrome browser installed

## Usage
Simply run the script:
```
python imdb_movies.py
```

The script will:
1. Open Chrome and navigate to IMDB
2. Perform an advanced search for Oscar-nominated comedy movies
3. Scrape data from the search results
4. Save the data to 'filmler.xlsx' in the current directory

## Project Structure
- `imdb_movies.py` - Main script for web scraping
- `requirements.txt` - List of Python dependencies
- `README.md` - Project documentation
- `movie_data/` - Directory where movie data is stored
  - `movies.xlsx` - Excel file with scraped movie data

