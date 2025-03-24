# Commodity Price Scraper

## Overview

This Python script scrapes commodity prices for coffee, durian RI6, and pepper from specific websites using Selenium. It retrieves prices based on predefined CSS selectors and class names, and calculates the average price for durian RI6.

## Requirements

Python 3.x

Google Chrome

ChromeDriver

## Installation

Clone this repository or copy the script.

Install the required dependencies using pip:

pip install selenium webdriver-manager

Ensure Google Chrome is installed on your system.

## Usage

Run the script to fetch commodity prices:

python script.py

## Features

Scrapes price data for coffee, durian RI6, and pepper.

Uses Selenium with headless Chrome for automated scraping.

Extracts and calculates the average price for durian RI6 when a price range is provided.

Outputs data in a structured JSON format.

## Output Example

{
    "Commodity": "Durian RI6",
    "Price": 48500
}

## Notes

The script runs in headless mode.

If the website structure changes, the CSS selectors might need updates.

Ensure you have stable internet access while running the script.
