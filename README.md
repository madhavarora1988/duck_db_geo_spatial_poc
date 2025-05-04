# DuckDB Geospatial POC: NYC Taxi Data Visualization

This repository is a **proof of concept (POC)** for exploring DuckDB's geospatial features using real-world data. It demonstrates how to use DuckDB's spatial extension to process and visualize geospatial data—in this case, NYC taxi dropoff locations—within a modern Python workflow.

The application creates an interactive heatmap showing the density of taxi dropoffs, with the ability to weight the visualization by either count or total fare amount.

## Features

- Interactive heatmap visualization of taxi dropoff locations
- Option to weight visualization by count or fare amount
- Basic statistics display
- Built with DuckDB Spatial for efficient geospatial data handling
- Interactive visualization using Folium

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application:

```bash
streamlit run nyc_taxi_map.py
```

The application will open in your default web browser. The first run will take a few moments as it downloads and processes the taxi data.

## Data Source

The application uses the NYC Yellow Taxi Trip Data from March 2010. The data is loaded directly from the NYC Taxi & Limousine Commission's public dataset on AWS.

- Official NYC TLC Open Data Portal: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page 