# import the libraries
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# import the dataset
dataset = pd.read_csv('SBIN_data.csv')

dataset

dataset.iloc[7874,5]

# In the data set all the date and time are read as a string object
# so we need to convert the date and time into a datetime data
# to_datetime() converts the date time into date
dataset['Date'] = pd.to_datetime(dataset['Date']).dt.date
dataset['Time'] = pd.to_datetime(dataset['Time'],format='%H:%M:%S').dt.time

dataset

# Create a new column 'Rank' which will store the ranks of each datapoint
dataset['Rank'] = np.nan

print(dataset)

# create the rank of every datapoint
# loop will contine from last row to 1st row and calculate the rank for every minutes of a each day
for i in range (8249,-1,-1):
    vol_list = []                                 # list of volumes for currect day and previous 5 days
    vol_list.append(dataset.iloc[i,5])
    current_row = i

    # check the previous 5 days volume and store into the list
    for j in range (0,5):
        current_row -= 375
        if(current_row >= 0):
            vol_list.append(dataset.iloc[current_row,5])

    # convert the list of volume into a dataframe to rank them according to their volume
    vol_series = pd.Series(vol_list)

    # Calculate rank based on volume
    vol_rank = vol_series.rank(ascending=False, method='min').astype(int)

    # put the rank of the datapoint into rank column
    dataset.iloc[i,7] = vol_rank[0]

dataset

"""# get th rank"""

# now we need fo find the rank of any point of time
# like rank 1 means highest volume
def get_rank(date,time):
    input_date = pd.to_datetime(date)
    input_time = pd.to_datetime(time, format='%H:%M:%S').time()
    # # Filter DataFrame based on the datetime object
    filtered_row = dataset[(dataset['Date'] == input_date) & (dataset['Time'] == input_time)]

    # Extract rank from the filtered row
    if len(filtered_row) > 0:
        return filtered_row.iloc[0]['Rank']
    else:
        return "No data found for the given date and time."

"""# visualize of the rank of the specific time"""

def get_data(date,time):
    # Convert date and time to datetime object
    input_date = pd.to_datetime(date)
    input_time = pd.to_datetime(time, format='%H:%M:%S').time()
    # # Filter DataFrame based on the datetime object
    filtered_row = dataset[(dataset['Date']==input_date) & (dataset['Time']== input_time)]
    index = filtered_row.index[0]

    # add the previous 5 days volume and store into the list
    for i in range (index,-1,-1):
        vol_list_dt = []
        vol_list_dt.append(dataset.iloc[i,5])
        current_row = i
        for j in range (0,5):
            current_row -= 375
            if(current_row >= 0):
                vol_list_dt.append(dataset.iloc[current_row,5])
        return vol_list_dt

date_input = '09-01-2024'
time_input = '15:28:00'

print(get_rank(date_input, time_input))

get_vol = get_data(date_input, time_input)
print(get_vol)

plt.figure(figsize=(10, 6))
plt.bar(range(len(get_vol)), get_vol, color='skyblue')
plt.xlabel('Day',color = 'red')
plt.ylabel('Volume',color ='red')
plt.title('Volume of Data Points')

dataset.to_csv('out.csv')

