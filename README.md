# Cab Fare and Weather Data Analysis

This project involves the analysis of taxi ride and weather data to explore the relationship between weather conditions and cab fare patterns. The primary objective is to merge cab and weather datasets, optimize memory usage, and perform exploratory data analysis, including the calculation of trip durations.

## Datasets

1. **Cab Fare Dataset (`test_cab_fare.csv`)**:
   - This dataset contains information about cab rides, including:
     - Pickup and dropoff locations (longitude, latitude)
     - Passenger count
     - Pickup datetime
     - Fare-related data
     
2. **Weather Data (`Weather Data.csv`)**:
   - This dataset includes weather information at different timestamps, with details such as:
     - Temperature
     - Humidity
     - Wind speed
     - Visibility

## Key Steps in Analysis

- **Memory Optimization**: Reduced memory usage by adjusting data types for both datasets.
- **Data Merging**: Merged cab fare and weather datasets using the `datetime` column.
- **Handling Missing Values**: Replaced missing numerical values with column medians.
- **Exploratory Data Analysis (EDA)**:
  - Visualized the passenger count distribution and pickup locations.
  - Calculated and visualized trip durations by subtracting `pickup_datetime` from `dropoff_datetime`.
  
## Files Included

- **`test_cab_fare.csv`**: The cab fare dataset used for analysis.
- **`Weather Data.csv`**: The weather dataset used for analysis.
- **`main.csv`**: The processed and cleaned dataset after merging the two datasets and handling missing values.
