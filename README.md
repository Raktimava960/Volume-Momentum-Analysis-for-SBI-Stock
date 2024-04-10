# Volume-Momentum-Analysis-for-SBI-Stock
## Conducting volume rank analysis BY Machine Learning for SBI stock from Jan 1st to Jan 31st comparing daily volume data over the last 5 working days to assess relative volume strength."

 The "Volume Rank Analysis for SBI Stock" project focuses on analyzing the volume data of the SBI (State Bank of India) stock for a specific period (from 1st Jan 2024 till 31st Jan 2024) and ranking the volume based on comparison with the corresponding time for the last 5 working days. The analysis aims to provide insights into the relative volume strength of the stock at specific times of the day compared to previous days.

## Project Overview:
The project involves the following key steps:

**Data Collection:** Obtain SBI stock data including open, high, low, close, and volume for every minute from 9:15 AM to 3:29 PM for each day from 1st Jan 2024 to 31st Jan 2024.

**Data Preprocessing:** Clean the data, ensuring consistency and removing any anomalies or missing values.

**Volume Rank Analysis:** For each minute of trading, calculate the volume rank based on the volume at that specific time compared to the corresponding time for the last 5 working days (excluding weekends and holidays).

**Rank Storage:** Store the volume ranks as a new column named "rank" in the dataframe.

**Visualization (Optional):** Visualize the volume ranks over time to identify trends and patterns in the volume strength of the SBI stock.

Project Implementation:
The project can be implemented using Python programming language along with libraries such as Pandas for data manipulation and analysis, Matplotlib or Seaborn for data visualization, and NumPy for numerical computations.

## Requirements:
Python,
Pandas,
Matplotlib or Seaborn,
NumPy,

## Usage:
* Clone the project repository.
* Ensure that the required Python libraries are installed.
* Run the Python script for data preprocessing and volume rank analysis.
* View the generated output dataframe with volume ranks stored as a new column.
* Optionally, visualize the volume rank trends using Matplotlib or Seaborn.
