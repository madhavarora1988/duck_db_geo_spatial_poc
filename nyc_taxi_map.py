import streamlit as st
import duckdb
import folium
from streamlit_folium import folium_static
import pandas as pd

st.set_page_config(layout="wide", page_title="NYC Taxi Visualization")

st.title("NYC Taxi Dropoff Locations")
st.write("This app visualizes NYC taxi dropoff locations using DuckDB Spatial and Folium.")

# Use a file-based DuckDB database
@st.cache_resource
def init_duckdb():
    con = duckdb.connect("nyc_taxi.duckdb")
    duckdb.install_extension("spatial", connection=con)
    duckdb.load_extension("spatial", connection=con)
    return con

# Load and process taxi data
@st.cache_data
def load_taxi_data(_con):
    # Create table if it doesn't exist
    sql = """
    CREATE TABLE IF NOT EXISTS rides AS
    SELECT 
        dropoff_longitude as longitude,
        dropoff_latitude as latitude,
        total_amount,
        ST_Point(dropoff_longitude, dropoff_latitude) as geometry
    FROM 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2010-03.parquet' 
    WHERE
        dropoff_longitude >= -74.6087 AND
        dropoff_latitude >= 40.2738 AND
        dropoff_longitude <= -73.4928 AND
        dropoff_latitude <= 41.1757 AND
        total_amount > 0
    LIMIT 1000000;
    """
    _con.execute(sql)
    return _con.execute("SELECT * FROM rides").df()

# Initialize connection
con = init_duckdb()

# Load data with a loading spinner
with st.spinner("Loading taxi data..."):
    df = load_taxi_data(con)

# Create visualization controls
st.sidebar.header("Visualization Controls")
sample_size = st.sidebar.slider("Sample size", 1000, 10000, 5000)

# Sample the data
df_sample = df.sample(n=min(sample_size, len(df)))

# Create the map centered on NYC
m = folium.Map(
    location=[40.7128, -74.0060],
    zoom_start=11,
    tiles="CartoDB positron"
)

# Add a heatmap layer
folium.plugins.HeatMap(
    data=df_sample[['latitude', 'longitude']].values,
    radius=8,
    max_zoom=13,
).add_to(m)

# Display the map
st.write("### Taxi Dropoff Heatmap")
folium_static(m, width=1200, height=600)

# Display some statistics
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Total Rides",
        f"{len(df):,}"
    )
with col2:
    st.metric(
        "Average Fare",
        f"${df['total_amount'].mean():.2f}"
    ) 