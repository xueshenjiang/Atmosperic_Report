# %%
#in this script, we are going to demonstrate the statistical feature of gusts in Beijing in November and their following effects, using the data from 2016-2023
#the data set is recorded by automated recording devices
#the data set is stored in my local drive in the file of "D:\电子版作业\大气探测原理\期末大作业\Nov", which consists of 8×30 files, corresponding to every day's record in October during 8 years
#each of 8×30 files is named as "20xx11dd", where "xx" means the year and "dd" means the day
#within each of 8×30 files, there are 5 txt files, in a sequence of "PAAVG1M_20xx11dd", "RHAVG1M_20xx11dd", "TAAVG1M_20xx11dd", "WDAVG2M_20xx11dd", "WSAVG2M_20xx11dd"
#indicating the average pressure, relative humidity, air temperature, wind direction, and wind speed in each time interval on the day of 20xx11dd, and xx and dd are variables
#the first three types of each day's data all have 5760 rows, and the last two types of each day's data have 28800 rows, and all the related quantities are at the end of each row

#Now let's start extracting, analyzing and visualizing the data!

#first, we need to import the necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Task 0: We build a 3×10×8 array to store each day's average wind speed
#the first and second dimension compose 30 days in October each year(like November 16 is in (1, 5)), the third dimension compose 8 years from 2016 to 2023

# Create a 3x10x8 array to store each day's average wind speed
wind_speed_array = np.zeros((3, 10, 8))

#loop to extract each day's average wind speed
for year in range(2016, 2024):
    for day in range(1, 31):
        # Construct the file name
        file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{year}11{day:02d}/WSAVG2M_{year}{11}{day:02d}.txt"

        # Read the data from the file, which is a txt file
        with open(file_name, 'r') as f:
            data = f.read()

        # Check if the file is empty
        if data:
        # Convert the data to a DataFrame
            data = pd.read_csv(file_name, header=None, sep="\t")

        # Check if the DataFrame has more than one column
            if len(data.columns) > 1:
        # Use only the last column
                data = data.iloc[:, -1]
        else:
            print(f"The file {file_name} is empty.")

        data = pd.to_numeric(data, errors='coerce')
        
        # Print the shape of the DataFrame
        print(f"The shape of the DataFrame is {data.shape}")

        #print data to check if the data is read correctly
        print(data)

        
        # Calculate the average wind speed for each day
        avg_wind_speed = data.mean()

        # Store the average wind speed in the array
        wind_speed_array[(day-1)//10, (day-1)%10, year - 2016] = avg_wind_speed


# %%
# Print the array in the form of 3×10 table for each of 8 years
for year in range(2016, 2024):
    print(f"Year {year}")
    print(wind_speed_array[:, :, year - 2016])
    


# %%
#Task 1: Define some specific scopes as criteria to classify the days as gusty or not
#create 4 1D arrays with flexible lengths as groups to contain the days in each scope

#Group 1: greatly gusty days, with average wind speed greater than 3m/s
group_1 = []  
# Iterate through the wind_speed_array to classify the days
for year in range(2016, 2024):
    for day in range(1, 31):
        avg_wind_speed = wind_speed_array[(day-1)//10, (day-1)%10, year - 2016]
        
        # Classify the day based on average wind speed
        if avg_wind_speed > 3:
            group_1.append((year, day))

# Print the days in group 1
print("Group 1: greatly gusty days, with average wind speed greater than 3m/s")
# print day number in group 1
print(len(group_1))


#Group 2: gusty days, with average wind speed greater than 2m/s and less than 3m/s
group_2 = []

# Iterate through the wind_speed_array to classify the days
for year in range(2016, 2024):
    for day in range(1, 31):
        avg_wind_speed = wind_speed_array[(day-1)//10, (day-1)%10, year - 2016]
        
        # Classify the day based on average wind speed
        if avg_wind_speed > 2 and avg_wind_speed < 3:
            group_2.append((year, day))

# Print the days in group 2
print("Group 2: gusty days, with average wind speed greater than 2m/s and less than 3m/s")
# print day number in group 2
print(len(group_2))

#Group 3: slightly gusty days, with average wind speed greater than 1m/s and less than 2m/s
group_3 = []

# Iterate through the wind_speed_array to classify the days
for year in range(2016, 2024):
    for day in range(1, 31):
        avg_wind_speed = wind_speed_array[(day-1)//10, (day-1)%10, year - 2016]
        
        # Classify the day based on average wind speed
        if avg_wind_speed > 1 and avg_wind_speed < 2:
            group_3.append((year, day))

# Print the days in group 3
print("Group 3: slightly gusty days, with average wind speed greater than 1m/s and less than 2m/s")
# print day number in group 3
print(len(group_3))

#Group 4: non-gusty days, with average wind speed less than 1m/s
group_4 = []

# Iterate through the wind_speed_array to classify the days
for year in range(2016, 2024):
    for day in range(1, 31):
        avg_wind_speed = wind_speed_array[(day-1)//10, (day-1)%10, year - 2016]
        
        # Classify the day based on average wind speed
        if avg_wind_speed < 1:
            group_4.append((year, day))

# Print the days in group 4
print("Group 4: non-gusty days, with average wind speed less than 1m/s")
# print day number in group 4
print(len(group_4))


# %%
#Task 2: Make a form about how many days each year can be classified into each group
#the form can be made as a 8×4 array, with each row representing a year and each column representing a group
#the elements in the array are the number of days in each group in each year

# Create a 8×4 array to store the number of days in each group in each year
group_array = np.zeros((8, 4))
# Iterate through the wind_speed_array to classify the days
for year in range(2016, 2024):
    for day in range(1, 31):
        avg_wind_speed = wind_speed_array[(day-1)//10, (day-1)%10, year - 2016]
        
        # Classify the day based on average wind speed
        if avg_wind_speed > 3:
            group_array[year - 2016, 3] += 1
        elif avg_wind_speed > 2 and avg_wind_speed < 3:
            group_array[year - 2016, 2] += 1
        elif avg_wind_speed > 1 and avg_wind_speed < 2:
            group_array[year - 2016, 1] += 1
        elif avg_wind_speed < 1:
            group_array[year - 2016, 0] += 1

# Print the array in the form of 8×4 table
print("The number of days in each group in each year")
#print(group_array)

#Additional task: translate the array into latex a table
#first, we need to import the package of tabulate
from tabulate import tabulate
#then, we can translate the array into latex a table
#print(tabulate(group_array, tablefmt="latex"))


# %%
#Task 3: Make heatmaps showing the frequencies of each group through 8 years on 3×10 arrays representing the date distrubution
#first, we need to import the package of seaborn
import seaborn as sns

#then, we can make the heatmaps using the previously obtained group_x, x=1,2,3,4
#first, we make the heatmap for group 1
#we need to create a 3×10 array to store the frequencies of group 1 through 8 years
group_1_array = np.zeros((3, 10))

#take a look back to the group_1, we can find that the first element of each tuple is the year, and the second element of each tuple is the day
#we can use a loop to extract the frequencies of group 1 through 8 years

for day in range(1, 31):
    for i in range(len(group_1)):
        if  group_1[i][1] == day:
            group_1_array[(day-1)//10, (day-1)%10] += 1

#then, we can make the heatmap for group 1, using cmap with red as the major color
# x and y ticks both +1 to their original values without impacting the heatmap
# optimizing each grid's size to 3:1, using shrink
# no side bar
#sns.heatmap(group_1_array, cmap="Reds", xticklabels=range(1, 11), yticklabels=range(1, 4), annot=True, fmt=".0f", cbar=False, square=True, linewidths=3, linecolor="white", annot_kws={"size": 15}, cbar_kws={"shrink": 0.1})

#first, we make the heatmap for group 2
#we need to create a 3×10 array to store the frequencies of group 2 through 8 years
group_2_array = np.zeros((3, 10))

#take a look back to the group_2, we can find that the first element of each tuple is the year, and the second element of each tuple is the day
#we can use a loop to extract the frequencies of group 2 through 8 years

for day in range(1, 31):
    for i in range(len(group_2)):
        if  group_2[i][1] == day:
            group_2_array[(day-1)//10, (day-1)%10] += 1

# make heatmap for group 2, using cmap with orange as the major color
# x and y ticks both +1 to their original values without impacting the heatmap
# optimizing each grid's size to 3:1, using shrink
# no side bar
#sns.heatmap(group_2_array, cmap="Oranges", xticklabels=range(1, 11), yticklabels=range(1, 4), annot=True, fmt=".0f", cbar=False, square=True, linewidths=3, linecolor="white", annot_kws={"size": 15}, cbar_kws={"shrink": 0.1})

#first, we make the heatmap for group 3
#we need to create a 3×10 array to store the frequencies of group 3 through 8 years
group_3_array = np.zeros((3, 10))

#take a look back to the group_3, we can find that the first element of each tuple is the year, and the second element of each tuple is the day
#we can use a loop to extract the frequencies of group 3 through 8 years
for day in range(1, 31):
    for i in range(len(group_3)):
        if group_3[i][1] == day:
            group_3_array[(day-1)//10, (day-1)%10] += 1

# make heatmap for group 3, using cmap with blue as the major color
# x and y ticks both +1 to their original values without impacting the heatmap
# optimizing each grid's size to 3:1, using shrink
# no side bar
#sns.heatmap(group_3_array, cmap="Blues", xticklabels=range(1, 11), yticklabels=range(1, 4), annot=True, fmt=".0f", cbar=False, square=True, linewidths=3, linecolor="white", annot_kws={"size": 15}, cbar_kws={"shrink": 0.1})

#first, we make the heatmap for group 4
#we need to create a 3×10 array to store the frequencies of group 4 through 8 years
group_4_array = np.zeros((3, 10))

#take a look back to the group_4, we can find that the first element of each tuple is the year, and the second element of each tuple is the day
#we can use a loop to extract the frequencies of group 4 through 8 years
for day in range(1, 31):
    for i in range(len(group_4)):
        if group_4[i][1] == day:
            group_4_array[(day-1)//10, (day-1)%10] += 1

# make heatmap for group 4, using cmap with green as the major color
# x and y ticks both +1 to their original values without impacting the heatmap
# optimizing each grid's size to 3:1, using shrink
# no side bar
#sns.heatmap(group_4_array, cmap="Greens", xticklabels=range(1, 11), yticklabels=range(1, 4), annot=True, fmt=".0f", cbar=False, square=True, linewidths=3, linecolor="white", annot_kws={"size": 15}, cbar_kws={"shrink": 0.1})


#next, we make heatmap for group 1+2, which means the days with average wind speed greater than 2m/s
#we need to create a 3×10 array to store the frequencies of group 1+2 through 8 years
group_12_array = np.zeros((3, 10))

group_12_array = group_1_array + group_2_array

#make heatmap for group 1+2, using cmap with red as the major color
# x and y ticks both +1 to their original values without impacting the heatmap
# optimizing each grid's size to 3:1, using shrink
# no side bar
sns.heatmap(group_12_array, cmap="Reds", xticklabels=range(1, 11), yticklabels=range(1, 4), annot=True, fmt=".0f", cbar=False, square=True, linewidths=3, linecolor="white", annot_kws={"size": 15}, cbar_kws={"shrink": 0.1})

# %%
#The following tasks focus on Nov 9th, 22nd, 28th and their corresponding proximate days in 8 years

#Task 4: Acquire the maximum wind speed during 5-day periods centered on these 3 dates for each year and visualize them

#first, we need to create a 3×8 array to store the maximum wind speed during 5-day periods centered on these 3 dates for each year
#the first dimension represents the 3 dates, the second dimension represents the 8 years
#the elements in the array are the maximum wind speed during 5-day periods centered on these 3 dates for each year\
max_wind_speed_array = np.zeros((3, 8))
#now, we need to fill in the values in the array
for i in range(3):
    for j in range(8):
        #the first date is Nov 9th, which is 20xx1109
        if i == 0:
            #we need to create a 5×1 array to store the wind speed during 5-day periods centered on Nov 9th for each year
            wind_speed_array_5 = np.zeros((5, 1))
            #we need to fill in the values in the 5×1 array
            for k in range(5):
                #the file name is "201611dd", where dd is the day
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{7+k:02d}/WSAVG2M_{2016+j}{11}{7+k:02d}.txt"
                # Read the data from the file, which is a txt file
                with open(file_name, 'r') as f:
                    data = f.read()

                # Check if the file is empty
                if data:
                # Convert the data to a DataFrame
                    data = pd.read_csv(file_name, header=None, sep="\t")

                # Check if the DataFrame has more than one column
                    if len(data.columns) > 1:
                # Use only the last column
                        data = data.iloc[:, -1]
                else:
                    print(f"The file {file_name} is empty.")

                data = pd.to_numeric(data, errors='coerce')
                #print(data)
                # Calculate the maximum wind speed during 5-day periods centered on Nov 9th for each year
                max_wind_speed = data.max()
                #print(max_wind_speed)
                # Store the maximum wind speed during 5-day periods centered on Nov 9th for each year in the array
                wind_speed_array_5[k, 0] = max_wind_speed
                
            #print(wind_speed_array_5)
            #print(np.max(wind_speed_array_5))
            #put max values in wind_speed_array_5 into max_wind_speed_array
            max_wind_speed_array[i, j] = np.max(wind_speed_array_5)
        #the second date is Nov 22nd, which is 20xx1122
        elif i == 1:
            #we need to create a 5×1 array to store the wind speed during 5-day periods centered on Nov 22nd for each year
            wind_speed_array_5 = np.zeros((5, 1))
            #we need to fill in the values in the 5×1 array
            for k in range(5):
                #the file name is "201611dd", where dd is the day
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{20+k:02d}/WSAVG2M_{2016+j}{11}{20+k:02d}.txt"
                # Read the data from the file, which is a txt file
                with open(file_name, 'r') as f:
                    data = f.read()

                # Check if the file is empty
                if data:
                # Convert the data to a DataFrame
                    data = pd.read_csv(file_name, header=None, sep="\t")

                # Check if the DataFrame has more than one column
                    if len(data.columns) > 1:
                # Use only the last column
                        data = data.iloc[:, -1]
                else:
                    print(f"The file {file_name} is empty.")

                data = pd.to_numeric(data, errors='coerce')
                #print(data)
                # Calculate the maximum wind speed during 5-day periods centered on Nov 22nd for each year
                max_wind_speed = data.max()
                #print(max_wind_speed)
                # Store the maximum wind speed during 5-day periods centered on Nov 22nd for each year in the array
                wind_speed_array_5[k, 0] = max_wind_speed
                
            #print(wind_speed_array_5)
            #print(np.max(wind_speed_array_5))
            #put max values in wind_speed_array_5 into max_wind_speed_array
            max_wind_speed_array[i, j] = np.max(wind_speed_array_5)
        #the third date is Nov 28th, which is 20xx1128
        else:
            #we need to create a 5×1 array to store the wind speed during 5-day periods centered on Nov 28th for each year
            wind_speed_array_5 = np.zeros((5, 1))
            #we need to fill in the values in the 5×1 array
            for k in range(5):
                #the file name is "201611dd", where dd is the day
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{26+k:02d}/WSAVG2M_{2016+j}{11}{26+k:02d}.txt"
                # Read the data from the file, which is a txt file
                with open(file_name, 'r') as f:
                    data = f.read()

                # Check if the file is empty
                if data:
                # Convert the data to a DataFrame
                    data = pd.read_csv(file_name, header=None, sep="\t")

                # Check if the DataFrame has more than one column
                    if len(data.columns) > 1:
                # Use only the last column
                        data = data.iloc[:, -1]
                else:
                    print(f"The file {file_name} is empty.")

                data = pd.to_numeric(data, errors='coerce')
                #print(data)
                # Calculate the maximum wind speed during 5-day periods centered on Nov 28th for each year
                max_wind_speed = data.max()
                #print(max_wind_speed)
                # Store the maximum wind speed during 5-day periods centered on Nov 28th for each year in the array
                wind_speed_array_5[k, 0] = max_wind_speed
                
            #print(wind_speed_array_5)
            #print(np.max(wind_speed_array_5))
            #put max values in wind_speed_array_5 into max_wind_speed_array
            max_wind_speed_array[i, j] = np.max(wind_speed_array_5)

print(max_wind_speed_array)
        

# %%
# let's visualize the maximum wind speed during 5-day periods centered on these 3 dates for each year
# generally, we want a column graph, with 8 groups of bars, each group has 3 bars, representing 3 dates
import matplotlib.pyplot as plt
import numpy as np

# Assuming you have the maximum wind speed data stored in the `max_wind_speed_array` variable

# Define the dates for each group of bars
dates = ['Nov 9', 'Nov 22', 'Nov 28']

# Define the years for each group of bars
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

# Set the width of each bar
bar_width = 0.2

# Set the positions of the bars on the x-axis
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Plot the bars for each group of dates, using soft colors
plt.bar(r1, max_wind_speed_array[0,:], color='b', width=bar_width, edgecolor='white', label=dates[0])
plt.bar(r2, max_wind_speed_array[1,:], color='g', width=bar_width, edgecolor='white', label=dates[1])
plt.bar(r3, max_wind_speed_array[2,:], color='r', width=bar_width, edgecolor='white', label=dates[2])

# Add x-axis labels and tick labels
plt.xlabel('Year')
plt.ylabel('Max Wind Speed(m/s)')
plt.xticks([r + bar_width for r in range(len(years))], years)

# Add a legend
plt.legend()

# Show the plot
plt.show()

# %%
#Task 5: Acquire the total duration of wind speed surpassing 3m/s for each 5-day period centered on these 3 dates for each year and visualize them
#note that for one day's data, we use the ratio of number of wind speed surpassing 3m/s to the total number of data points and multiply it by 24 to get the total duration of wind speed surpassing 3m/s for that day
#first, we need to create a 3×8 array to store the total duration of wind speed surpassing 3m/s for each 5-day period centered on these 3 dates for each year
#the first dimension represents the 3 dates, the second dimension represents the 8 years
#the elements in the array are the total duration of wind speed surpassing 3m/s for each 5-day period centered on these 3 dates for each year
total_duration_array = np.zeros((3, 8))
#now, we need to fill in the values in the array

for i in range(3):
    for j in range(8):
        #the first date is Nov 9th, which is 20xx1109
        if i == 0:
            #we need to create a 5×1 array to store the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 9th for each year
            duration_array_5 = np.zeros((5, 1))
            #we need to fill in the values in the 5×1 array
            for k in range(5):
                #the file name is "201611dd", where dd is the day
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{7+k:02d}/WSAVG2M_{2016+j}{11}{7+k:02d}.txt"
                # Read the data from the file, which is a txt file
                with open(file_name, 'r') as f:
                    data = f.read()

                # Check if the file is empty
                if data:
                # Convert the data to a DataFrame
                    data = pd.read_csv(file_name, header=None, sep="\t")

                # Check if the DataFrame has more than one column
                    if len(data.columns) > 1:
                # Use only the last column
                        data = data.iloc[:, -1]
                else:
                    print(f"The file {file_name} is empty.")

                data = pd.to_numeric(data, errors='coerce')
                #print(data)
                # Calculate the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 9th for each year
                total_duration = len(data[data>2])/len(data)*24
                #print(total_duration)
                # Store the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 9th for each year in the array
                duration_array_5[k, 0] = total_duration
                #sum the durations of 5 days
            total_duration_array[i, j] = np.sum(duration_array_5)
        #the second date is Nov 22nd, which is 20xx1122
        elif i == 1:
            #we need to create a 5×1 array to store the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 22nd for each year
            duration_array_5 = np.zeros((5, 1))
            #we need to fill in the values in the 5×1 array
            for k in range(5):
                #the file name is "201611dd", where dd is the day
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{20+k:02d}/WSAVG2M_{2016+j}{11}{20+k:02d}.txt"
                # Read the data from the file, which is a txt file
                with open(file_name, 'r') as f:
                    data = f.read()

                # Check if the file is empty
                if data:
                # Convert the data to a DataFrame
                    data = pd.read_csv(file_name, header=None, sep="\t")

                # Check if the DataFrame has more than one column
                    if len(data.columns) > 1:
                # Use only the last column
                        data = data.iloc[:, -1]
                else:
                    print(f"The file {file_name} is empty.")

                data = pd.to_numeric(data, errors='coerce')
                #print(data)
                # Calculate the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 22nd for each year
                total_duration = len(data[data>2])/len(data)*24
                #print(total_duration)
                # Store the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 22nd for each year in the array
                duration_array_5[k, 0] = total_duration
                #sum the durations of 5 days
            total_duration_array[i, j] = np.sum(duration_array_5)
        #the third date is Nov 28th, which is 20xx1128
        else:
            #we need to create a 5×1 array to store the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 28th for each year
            duration_array_5 = np.zeros((5, 1))
            #we need to fill in the values in the 5×1 array
            for k in range(5):
                #the file name is "201611dd", where dd is the day
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{26+k:02d}/WSAVG2M_{2016+j}{11}{26+k:02d}.txt"
                # Read the data from the file, which is a txt file
                with open(file_name, 'r') as f:
                    data = f.read()

                # Check if the file is empty
                if data:
                # Convert the data to a DataFrame
                    data = pd.read_csv(file_name, header=None, sep="\t")

                # Check if the DataFrame has more than one column
                    if len(data.columns) > 1:
                # Use only the last column
                        data = data.iloc[:, -1]
                else:
                    print(f"The file {file_name} is empty.")

                data = pd.to_numeric(data, errors='coerce')
                #print(data)
                # Calculate the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 28th for each year
                total_duration = len(data[data>2])/len(data)*24
                #print(total_duration)
                # Store the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 28th for each year in the array
                duration_array_5[k, 0] = total_duration
                #sum the durations of 5 days
            total_duration_array[i, j] = np.sum(duration_array_5)

print(total_duration_array)

# %%
#let's plot the total duration of wind speed surpassing 3m/s for each 5-day period centered on Nov 9th for each year
# generally, we want a column graph, with 8 groups of bars, each group has 3 bars, representing 3 dates
import matplotlib.pyplot as plt

# Assuming you have the total duration data stored in the `total_duration_array` variable

# Define the dates for each group of bars
dates = ['Nov 9', 'Nov 22', 'Nov 28']

# Define the years for each group of bars
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

# Set the width of each bar
bar_width = 0.2

# Set the positions of the bars on the x-axis
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
# Create a bar plot
plt.bar(r1, total_duration_array[0,:], color='b', width=bar_width, edgecolor='white', label=dates[0])
plt.bar(r2, total_duration_array[1,:], color='g', width=bar_width, edgecolor='white', label=dates[1])
plt.bar(r3, total_duration_array[2,:], color='r', width=bar_width, edgecolor='white', label=dates[2])

# Add x-axis labels and tick labels
plt.xlabel('Year')
plt.ylabel('Total Duration(h)')
plt.xticks([r + bar_width for r in range(len(years))], years)
# Add a legend
plt.legend()

# Show the plot
plt.show()

# %%
#Task 5:Independently plot the wind rose maps for each of Nov 9th, 22nd, 28th for each year
# Assuming you have the wind rose data stored in the `wind_rose_data` variable
#import some packages
from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

#create wind rose map for each of Nov 9th, 22nd, 28th for each year while extracting the data from the txt files
#start looping
for i in range(3):
    for j in range(8):
        #the first date is Nov 9th, which is 20xx1109
        if i == 0:
            #the file name is "201611dd", where dd is the day, extract both the wind speed and wind direction data
            file_name_speed = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{9:02d}/WSAVG2M_{2016+j}{11}{9:02d}.txt"
            file_name_direction = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{9:02d}/WDAVG2M_{2016+j}{11}{9:02d}.txt"
            # Read the speed data from the file, which is a txt file
            with open(file_name_speed, 'r') as fs:
                data_speed = fs.read()

            # Check if the file is empty
            if data_speed:
            # Convert the data to a DataFrame
                data_speed = pd.read_csv(file_name_speed, header=None, sep="\t")

            # Check if the DataFrame has more than one column
                if len(data_speed.columns) > 1:
            # Use only the last column
                    data_speed = data_speed.iloc[:, -1]
            else:
                print(f"The file {file_name_speed} is empty.")

            data_speed = pd.to_numeric(data_speed, errors='coerce')
            # Read the direction data from the file, which is a txt file
            with open(file_name_direction, 'r') as fd:
                data_direction = fd.read()

            # Check if the file is empty
            if data_direction:
            # Convert the data to a DataFrame
                data_direction = pd.read_csv(file_name_direction, header=None, sep="\t")

            # Check if the DataFrame has more than one column
                if len(data_direction.columns) > 1:
            # Use only the last column
                    data_direction = data_direction.iloc[:, -1]
            else:
                print(f"The file {file_name_direction} is empty.")

            data_direction = pd.to_numeric(data_direction, errors='coerce')
            #compare the length of the two data sets, if not equal, extract the shorter amount of data from both data sets
            if len(data_speed) != len(data_direction):
                if len(data_speed) > len(data_direction):
                    data_speed = data_speed[:len(data_direction)]
                else:
                    data_direction = data_direction[:len(data_speed)]
            #plot the wind rose map
            #wind_rose = WindroseAxes.from_ax()
            #wind_rose.contourf(data_direction, data_speed, bins=np.arange(0, max(data_speed), 1), cmap=cm.hot)
            #wind_rose.set_legend()

        #the second date is Nov 22nd, which is 20xx1122
        elif i == 1:
            #the file name is "201611dd", where dd is the day, extract both the wind speed and wind direction data
            file_name_speed = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{22:02d}/WSAVG2M_{2016+j}{11}{22:02d}.txt"
            file_name_direction = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{22:02d}/WDAVG2M_{2016+j}{11}{22:02d}.txt"
            # Read the speed data from the file, which is a txt file
            with open(file_name_speed, 'r') as fs:
                data_speed = fs.read()

            # Check if the file is empty
            if data_speed:
            # Convert the data to a DataFrame
                data_speed = pd.read_csv(file_name_speed, header=None, sep="\t")

            # Check if the DataFrame has more than one column
                if len(data_speed.columns) > 1:
            # Use only the last column
                    data_speed = data_speed.iloc[:, -1]
            else:
                print(f"The file {file_name_speed} is empty.")

            data_speed = pd.to_numeric(data_speed, errors='coerce')
            # Read the direction data from the file, which is a txt file
            with open(file_name_direction, 'r') as fd:
                data_direction = fd.read()

            # Check if the file is empty
            if data_direction:
            # Convert the data to a DataFrame
                data_direction = pd.read_csv(file_name_direction, header=None, sep="\t")

            # Check if the DataFrame has more than one column
                if len(data_direction.columns) > 1:
            # Use only the last column
                    data_direction = data_direction.iloc[:, -1]
            else:
                print(f"The file {file_name_direction} is empty.")

            data_direction = pd.to_numeric(data_direction, errors='coerce')
            #compare the length of the two data sets, if not equal, extract the shorter amount of data from both data sets
            if len(data_speed) != len(data_direction):
                if len(data_speed) > len(data_direction):
                    data_speed = data_speed[:len(data_direction)]
                else:
                    data_direction = data_direction[:len(data_speed)]
            #plot the wind rose map
            #wind_rose = WindroseAxes.from_ax()
            #wind_rose.contourf(data_direction, data_speed, bins=np.arange(0, max(data_speed), 1), cmap=cm.hot)
            #wind_rose.set_legend()
        #the third date is Nov 28th, which is 20xx1128
        else:
            #the file name is "201611dd", where dd is the day, extract both the wind speed and wind direction data
            file_name_speed = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{28:02d}/WSAVG2M_{2016+j}{11}{28:02d}.txt"
            file_name_direction = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{28:02d}/WDAVG2M_{2016+j}{11}{28:02d}.txt"
            # Read the speed data from the file, which is a txt file
            with open(file_name_speed, 'r') as fs:
                data_speed = fs.read()

            # Check if the file is empty
            if data_speed:
            # Convert the data to a DataFrame
                data_speed = pd.read_csv(file_name_speed, header=None, sep="\t")

            # Check if the DataFrame has more than one column
                if len(data_speed.columns) > 1:
            # Use only the last column
                    data_speed = data_speed.iloc[:, -1]
            else:
                print(f"The file {file_name_speed} is empty.")

            data_speed = pd.to_numeric(data_speed, errors='coerce')
            # Read the direction data from the file, which is a txt file
            with open(file_name_direction, 'r') as fd:
                data_direction = fd.read()

            # Check if the file is empty
            if data_direction:
            # Convert the data to a DataFrame
                data_direction = pd.read_csv(file_name_direction, header=None, sep="\t")

            # Check if the DataFrame has more than one column
                if len(data_direction.columns) > 1:
            # Use only the last column
                    data_direction = data_direction.iloc[:, -1]
            else:
                print(f"The file {file_name_direction} is empty.")

            data_direction = pd.to_numeric(data_direction, errors='coerce')
            #compare the length of the two data sets, if not equal, extract the shorter amount of data from both data sets
            if len(data_speed) != len(data_direction):
                if len(data_speed) > len(data_direction):
                    data_speed = data_speed[:len(data_direction)]
                else:
                    data_direction = data_direction[:len(data_speed)]
            # plot the wind rose map
            wind_rose = WindroseAxes.from_ax()
            wind_rose.contourf(data_direction, data_speed, bins=np.arange(0, max(data_speed), 1), cmap=cm.hot)
            wind_rose.set_legend()

# %%
#Task 5: Acquire the mean temperature changes over 8 years of the day of Nov 9th, 22nd, 28th and the mean changes between their corresponding proximate days
#Compare such changes with those of Nov 4th, which is gust-free, and finally visualize them
#So together we have 8 years of 4 periods centered on Nov 4th, 9th, 22nd, 28th, with each period covering 3 days

#first, we need to create two 4×8 arrays to store the daily-mean temperature contrast between the next and previous day and the daily-mean temperature contrast between the two next and previous days of the day of Nov 4th, 9th, 22nd, 28th for each year
#for the first array, the first dimension represents the 4 dates, the second dimension represents the 8 years, storing the daily-mean temperature contrast between the next and previous day of the day of Nov 4th, 9th, 22nd, 28th for each year
#for the second array, the first dimension represents the 4 dates, the second dimension represents the 8 years, storing the daily-mean temperature contrast between the two next and previous days of the day of Nov 4th, 9th, 22nd, 28th for each year
#begin creating the first array
daily_mean_array = np.zeros((4, 8))
#begin creating the second array
daily_mean_array_2 = np.zeros((4, 8))

#now we need to iterate through the 8 years for 4 dates
for i in range(4):
    for j in range(8):
        #the first date is Nov 4th, which is 20xx1104
        if i == 0:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{2:02d}/TAAVG1M_{2016+j}{11}{2:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{3:02d}/TAAVG1M_{2016+j}{11}{3:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{4:02d}/TAAVG1M_{2016+j}{11}{4:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{5:02d}/TAAVG1M_{2016+j}{11}{5:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{6:02d}/TAAVG1M_{2016+j}{11}{6:02d}.txt"
        elif i == 1:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{7:02d}/TAAVG1M_{2016+j}{11}{7:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{8:02d}/TAAVG1M_{2016+j}{11}{8:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{9:02d}/TAAVG1M_{2016+j}{11}{9:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}1110/TAAVG1M_{2016+j}11{10:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}1111/TAAVG1M_{2016+j}11{11:02d}.txt"
        elif i == 2:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{20:02d}/TAAVG1M_{2016+j}{11}{20:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}1121/TAAVG1M_{2016+j}11{21:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}1122/TAAVG1M_{2016+j}11{22:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}1123/TAAVG1M_{2016+j}11{23:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}1124/TAAVG1M_{2016+j}11{24:02d}.txt"
        else:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}11{26:02d}/TAAVG1M_{2016+j}{11}{26:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}{11}{27:02d}/TAAVG1M_{2016+j}{11}{27:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}{11}{28:02d}/TAAVG1M_{2016+j}{11}{28:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}{11}{29:02d}/TAAVG1M_{2016+j}{11}{29:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+j}{11}{30:02d}/TAAVG1M_{2016+j}{11}{30:02d}.txt"
        # Read the data from the file, which is a txt file
        with open(file_name_n2, 'r') as f_2:
            data_2 = f_2.read()
        with open(file_name_n1, 'r') as f_1:
            data_1 = f_1.read()
        with open(file_name_0, 'r') as f0:
            data0 = f0.read()
        with open(file_name_1, 'r') as f1:
            data1 = f1.read()
        with open(file_name_2, 'r') as f2:
            data2 = f2.read()

        # Check if the file is empty
        if data_2:
        # Convert the data to a DataFrame
            data_2 = pd.read_csv(file_name_n2, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data_2.columns) > 1:
        # Use only the last column
                data_2 = data_2.iloc[:, -1]
        else:
            print(f"The file {file_name_n2} is empty.")

        data_2 = pd.to_numeric(data_2, errors='coerce')

        # Check if the file is empty
        if data_1:
        # Convert the data to a DataFrame
            data_1 = pd.read_csv(file_name_n1, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data_1.columns) > 1:
        # Use only the last column
                data_1 = data_1.iloc[:, -1]
        else:
            print(f"The file {file_name_n1} is empty.")

        data_1 = pd.to_numeric(data_1, errors='coerce')


        # Check if the file is empty
        if data0:
        # Convert the data to a DataFrame
            data0 = pd.read_csv(file_name_0, header=None, sep="\t")

        # Check if the DataFrame has more than one column
            if len(data0.columns) > 1:
        # Use only the last column
                data0 = data0.iloc[:, -1]
        else:
            print(f"The file {file_name_0} is empty.")

        data0 = pd.to_numeric(data0, errors='coerce')

        # Check if the file is empty
        if data1:
        # Convert the data to a DataFrame
            data1 = pd.read_csv(file_name_1, header=None, sep="\t")

        # Check if the DataFrame has more than one column
            if len(data1.columns) > 1:
        # Use only the last column
                data1 = data1.iloc[:, -1]
        else:
            print(f"The file {file_name_1} is empty.")

        data1 = pd.to_numeric(data1, errors='coerce')

        # Check if the file is empty
        if data2:
        # Convert the data to a DataFrame
            data2 = pd.read_csv(file_name_2, header=None, sep="\t")

        # Check if the DataFrame has more than one column
            if len(data2.columns) > 1:
        # Use only the last column
                data2 = data2.iloc[:, -1]
        else:
            print(f"The file {file_name_2} is empty.")

        data2 = pd.to_numeric(data2, errors='coerce')

        # Calculate the daily-mean temperature contrast between the next and previous day for each year
        mean_contrast_1 = data1.mean() - data_1.mean()
        # Store the daily-mean temperature contrast between the next and previous day for each year in the array
        daily_mean_array[i, j] = mean_contrast_1
        # Calculate the daily-mean temperature contrast between the two next and previous days for each year
        mean_contrast_2 = (data1.mean() + data2.mean())/2 - (data_1.mean() + data_2.mean())/2
        # Store the daily-mean temperature contrast between the two next and previous days for each year in the array
        daily_mean_array_2[i, j] = mean_contrast_2

print(daily_mean_array)
print(daily_mean_array_2)

# %%
#Now visulize the daily-mean temperature contrast between the next and previous day of the day of Nov 4th, 9th, 22nd, 28th
#Description: use line chart, with 4 lines; the red one indicating Nov 4th, and different degrees of blue indicating Nov 9th, 22nd, 28th

#let's begin plotting the line chart
import matplotlib.pyplot as plt

#plot the line chart
plt.plot(daily_mean_array[0,:], color='red', label='Nov 4th')
plt.plot(daily_mean_array[1,:], color='lightblue', label='Nov 9th')
plt.plot(daily_mean_array[2,:], color='skyblue', label='Nov 22nd')
plt.plot(daily_mean_array[3,:], color='blue', label='Nov 28th')

# Add x-axis labels and tick labels
plt.xlabel('Year')
plt.ylabel('Daily-mean temperature contrast(1 day)/K')
plt.xticks(range(8),range(2016, 2024, 1))
# Add a dash reference line at y=0, black and dashed
plt.axhline(y=0, color='black', linestyle='--')
# Add a legend
plt.legend()
# Show the plot
plt.show()

#plot the line chart
plt.plot(daily_mean_array_2[0,:], color='red', label='Nov 4th')
plt.plot(daily_mean_array_2[1,:], color='lightblue', label='Nov 9th')
plt.plot(daily_mean_array_2[2,:], color='skyblue', label='Nov 22nd')
plt.plot(daily_mean_array_2[3,:], color='blue', label='Nov 28th')

# Add x-axis labels and tick labels
plt.xlabel('Year')
plt.ylabel('Daily-mean temperature contrast(2 days)/K')
plt.xticks(range(8),range(2016, 2024, 1))
# Add a dash reference line at y=0, black and dashed
plt.axhline(y=0, color='black', linestyle='--')
# Add a legend
plt.legend()
# Show the plot
plt.show()

# %%
#Task 6: Do the same contrasting and visualization for pressure
#Compare such changes with those of Nov 4th, which is gust-free, and finally visualize them
#So together we have 8 years of 4 periods centered on Nov 4th, 9th, 22nd, 28th, with each period covering 3 days

#first, we need to create two 4×8 arrays to store the daily-mean pressure contrast between the next and previous day and the daily-mean pressure contrast between the two next and previous days of the day of Nov 4th, 9th, 22nd, 28th for each year
#for the first array, the first dimension represents the 4 dates, the second dimension represents the 8 years, storing the daily-mean pressure contrast between the next and previous day of the day of Nov 4th, 9th, 22nd, 28th for each year
#for the second array, the first dimension represents the 4 dates, the second dimension represents the 8 years, storing the daily-mean pressure contrast between the two next and previous days of the day of Nov 4th, 9th, 22nd, 28th for each year
#begin creating the first array
daily_mean_array = np.zeros((4, 8))
#begin creating the second array
daily_mean_array_2 = np.zeros((4, 8))

#now we need to iterate through the 8 years for 4 dates
for i in range(4):
    for j in range(8):
        #the first date is Nov 4th, which is 20xx1104
        if i == 0:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{2:02d}/PAAVG1M_{2016 + j}{11}{2:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{3:02d}/PAAVG1M_{2016 + j}{11}{3:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{4:02d}/PAAVG1M_{2016 + j}{11}{4:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{5:02d}/PAAVG1M_{2016 + j}{11}{5:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{6:02d}/PAAVG1M_{2016 + j}{11}{6:02d}.txt"
        elif i == 1:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{7:02d}/PAAVG1M_{2016 + j}{11}{7:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{8:02d}/PAAVG1M_{2016 + j}{11}{8:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{9:02d}/PAAVG1M_{2016 + j}{11}{9:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}1110/PAAVG1M_{2016 + j}11{10:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}1111/PAAVG1M_{2016 + j}11{11:02d}.txt"
        elif i == 2:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{20:02d}/PAAVG1M_{2016 + j}{11}{20:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}1121/PAAVG1M_{2016 + j}11{21:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}1122/PAAVG1M_{2016 + j}11{22:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}1123/PAAVG1M_{2016 + j}11{23:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}1124/PAAVG1M_{2016 + j}11{24:02d}.txt"
        else:
            file_name_n2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}11{26:02d}/PAAVG1M_{2016 + j}{11}{26:02d}.txt"
            file_name_n1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}{11}{27:02d}/PAAVG1M_{2016 + j}{11}{27:02d}.txt"
            file_name_0 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}{11}{28:02d}/PAAVG1M_{2016 + j}{11}{28:02d}.txt"
            file_name_1 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}{11}{29:02d}/PAAVG1M_{2016 + j}{11}{29:02d}.txt"
            file_name_2 = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016 + j}{11}{30:02d}/PAAVG1M_{2016 + j}{11}{30:02d}.txt"
        # Read the data from the file, which is a txt file
        with open(file_name_n2, 'r') as f_2:
            data_2 = f_2.read()
        with open(file_name_n1, 'r') as f_1:
            data_1 = f_1.read()
        with open(file_name_0, 'r') as f0:
            data0 = f0.read()
        with open(file_name_1, 'r') as f1:
            data1 = f1.read()
        with open(file_name_2, 'r') as f2:
            data2 = f2.read()

        # Check if the file is empty
        if data_2:
        # Convert the data to a DataFrame
            data_2 = pd.read_csv(file_name_n2, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data_2.columns) > 1:
        # Use only the last column
                data_2 = data_2.iloc[:, -1]
        else:
            print(f"The file {file_name_n2} is empty.")

        if data_1:
            data_1 = pd.read_csv(file_name_n1, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data_1.columns) > 1:
        # Use only the last column
                data_1 = data_1.iloc[:, -1]
        else:
            print(f"The file {file_name_n1} is empty.")

        if data0:
            data0 = pd.read_csv(file_name_0, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data0.columns) > 1:
                # Use only the last column
                data0 = data0.iloc[:, -1]
        else:
            print(f"The file {file_name_0} is empty.")

        if data1:
            data1 = pd.read_csv(file_name_1, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data1.columns) > 1:
                # Use only the last column
                data1 = data1.iloc[:, -1]
        else:
            print(f"The file {file_name_1} is empty.")

        if data2:
            data2 = pd.read_csv(file_name_2, header=None, sep="\t")
        # Check if the DataFrame has more than one column
            if len(data2.columns) > 1:
                # Use only the last column
                data2 = data2.iloc[:, -1]
        else:
            print(f"The file {file_name_2} is empty.")

        # Calculate the daily-mean pressure contrast between the next and previous day for each year
        mean_contrast_1 = data1.mean() - data_1.mean()
        # Store the daily-mean pressure contrast between the next and previous day for each year in the array
        daily_mean_array[i, j] = mean_contrast_1
        # Calculate the daily-mean pressure contrast between the two next and previous days for each year
        mean_contrast_2 = (data1.mean() + data2.mean())/2 - (data_1.mean() + data_2.mean())/2
        # Store the daily-mean pressure contrast between the two next and previous days for each year in the array
        daily_mean_array_2[i, j] = mean_contrast_2

print(daily_mean_array)
print(daily_mean_array_2)
        

# %%
# Now visulize the daily-mean pressure contrast between the next and previous day of the day of Nov 4th, 9th, 22nd, 28th
# Description: use line chart, with 4 lines; the red one indicating Nov 4th, and different degrees of blue indicating Nov 9th, 22nd, 28th

# let's begin plotting the line chart
import matplotlib.pyplot as plt

# plot the line chart
plt.plot(daily_mean_array[0, :], color='red', label='Nov 4th')
plt.plot(daily_mean_array[1, :], color='lightblue', label='Nov 9th')
plt.plot(daily_mean_array[2, :], color='skyblue', label='Nov 22nd')
plt.plot(daily_mean_array[3, :], color='blue', label='Nov 28th')

# Add x-axis labels and tick labels
plt.xlabel('Year')
plt.ylabel('Daily-mean pressure contrast(1 day)/hPa')
plt.xticks(range(8), range(2016, 2024, 1))
# Add a dash reference line at y=0, black and dashed
plt.axhline(y=0, color='black', linestyle='--')
# Add a legend
plt.legend()
# Show the plot
plt.show()

# plot the line chart
plt.plot(daily_mean_array_2[0, :], color='red', label='Nov 4th')
plt.plot(daily_mean_array_2[1, :], color='lightblue', label='Nov 9th')
plt.plot(daily_mean_array_2[2, :], color='skyblue', label='Nov 22nd')
plt.plot(daily_mean_array_2[3, :], color='blue', label='Nov 28th')

# Add x-axis labels and tick labels
plt.xlabel('Year')
plt.ylabel('Daily-mean pressure contrast(2 days)/hPa')
plt.xticks(range(8), range(2016, 2024, 1))
# Add a dash reference line at y=0, black and dashed
plt.axhline(y=0, color='black', linestyle='--')
# Add a legend
plt.legend()
# Show the plot
plt.show()


# %%
#Task 7: Acquire the Relative Humidity changes for 4 5-day periods centered on Nov 4th, 9th, 22nd, 28th averaged over 8 years and visualize them
# We create a 4×5 array to store the relative humidity changes for 4 5-day periods centered on Nov 4th, 9th, 22nd, 28th averaged over 8 years
# The first dimension represents the 4 dates, the second dimension represents the 5-day periods
# each element in the array represents the relative humidity for a day in a specified period averaged over 8 years

#begin creating the array
daily_mean_array = np.zeros((4, 5))

#now we need to iterate through the 8 years for 4 dates
for i in range(4):
    for j in range(5):
        # create a 8×1 array to store the daily-mean relative humidity for a day in a specified period for 8 years
        daily_mean_array_2 = np.zeros((8, 1))
        #the first date is Nov 4th, which is 20xx1104
        for k in range(8):
            if i == 0:
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+k}11{2+j:02d}/RHAVG1M_{2016+k}{11}{2+j:02d}.txt"
            elif i == 1:
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+k}11{7+j:02d}/RHAVG1M_{2016+k}{11}{7+j:02d}.txt"
            elif i == 2:
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+k}11{20+j:02d}/RHAVG1M_{2016+k}{11}{20+j:02d}.txt"
            else:
                file_name = f"D:/电子版作业/大气探测原理/期末大作业/Nov/{2016+k}11{26+j:02d}/RHAVG1M_{2016+k}{11}{26+j:02d}.txt"
            # Read the data from the file, which is a txt file
            with open(file_name, 'r') as f:
                data = f.read()
            # Check if the file is empty
            if data:
            # Convert the data to a DataFrame
                data = pd.read_csv(file_name, header=None, sep="\t")
            # Check if the DataFrame has more than one column
                if len(data.columns) > 1:
            # Use only the last column
                    data = data.iloc[:, -1]
            else:
                print(f"The file {file_name} is empty.")

            data = pd.to_numeric(data, errors='coerce')
            # Store the daily-mean relative humidity for a day in a specified period for 8 years in the array
            daily_mean_array_2[k, 0] = data.mean()
        # Calculate the daily-mean relative humidity for a day in a specified period averaged over 8 years
        RH_mean = daily_mean_array_2.mean()
        # Store the daily-mean relative humidity for a day in a specified period averaged over 8 years in the array
        daily_mean_array[i, j] = RH_mean

print(daily_mean_array)

# %%
# Visualize the relative humidity changes for 4 5-day periods centered on Nov 4th, 9th, 22nd, 28th averaged over 8 years
# use plot chart, with 4 lines; the red one indicating Nov 4th, and different degrees of blue indicating Nov 9th, 22nd, 28th
import matplotlib.pyplot as plt
plt.plot(daily_mean_array[0,:], color='red', label='Nov 4th')
plt.plot(daily_mean_array[1,:], color='lightblue',label='Nov 9th')
plt.plot(daily_mean_array[2,:], color='skyblue',label='Nov 22nd')
plt.plot(daily_mean_array[3,:], color='blue',label='Nov 28th')
plt.xlabel('5-day period')
plt.ylabel('Daily-mean relative humidity')
plt.xticks(range(5),range(-2, 3, 1))
plt.legend()
plt.show()



