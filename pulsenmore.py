import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('factory_test_data.csv')
data = data.replace('[]', np.nan)
data[['Y2', 'X2', 'Y3', 'X3', 'Y4', 'X4', 'Y5', 'X5']] = data[['Y2', 'X2', 'Y3', 'X3', 'Y4', 'X4', 'Y5', 'X5']].apply(pd.to_numeric, errors='coerce')
statistics=data.describe(include='all')
print(statistics)
mean_y1 = statistics.loc['mean', 'Y1']
mean_y2 = statistics.loc['mean', 'Y2']
mean_y3 = statistics.loc['mean', 'Y3']
mean_y4 = statistics.loc['mean', 'Y4']
mean_y5 = statistics.loc['mean', 'Y5']
std_y1 = statistics.loc['std', 'Y1']
std_y2 = statistics.loc['std', 'Y2']
std_y3 = statistics.loc['std', 'Y3']
std_y4 = statistics.loc['std', 'Y4']
std_y5 = statistics.loc['std', 'Y5']

# Create scatter plots for Yi as a function of the devices index
fig, axs = plt.subplots(4, 1, figsize=(8, 16), sharex=True, gridspec_kw={'hspace': 0.5})
for i, col in enumerate(['Y2', 'Y3', 'Y4', 'Y5']):
    x_var = 'X' + str(i + 2)
    x_values = data[x_var]
    y_values = data[col]
    meanyi=statistics.loc['mean', col]
    axs[i].scatter(range(len(y_values)), y_values)
    for x in x_values:
        axs[i].axhline(y=x, color='r', linestyle='--')
    
    # Plot horizontal line for the mean value
    if i == 0:
        axs[i].axhline(y=mean_y2, color='g', linestyle='-')
    elif i == 1:
        axs[i].axhline(y=mean_y3, color='g', linestyle='-')
    elif i == 2:
        axs[i].axhline(y=mean_y4, color='g', linestyle='-')
    elif i == 3:
        axs[i].axhline(y=mean_y5, color='g', linestyle='-')
    
    axs[i].set_xlabel('Device Index')
    axs[i].set_ylabel(col)
    axs[i].set_ylim(meanyi-8, meanyi+8)
    axs[0].text(0.01, 0.90, f"the expected value",
            transform=axs[0].transAxes, fontsize=8, color='r')
    axs[0].text(0.01, 0.8, f"the mean value",
            transform=axs[0].transAxes, fontsize=8, color='g')
plt.suptitle('Yi as a function of the devices index',y=1)
plt.show()
plt.savefig('./plot.png')

# Create a plot for y1 as a function of of the devices index
x_values = range(len(data))
plt.plot(x_values, data['Y1'], marker='o')
plt.xlabel('Device Index')
plt.ylabel('Y1 Values')
plt.title('Y1 Values for 51 Devices')
plt.show()
fig, axs = plt.subplots(1, 5, figsize=(15, 3))

#plot the histogram of yi
axs[0].hist(data['Y1'], bins=10)
axs[0].set_xlabel('Y1')
axs[0].set_ylabel('frequency')
axs[0].set_title('Histogram of Y1')

axs[1].hist(data['Y2'], bins=10)
axs[1].set_xlabel('Y2')
axs[1].set_ylabel('frequency')
axs[1].set_title('Histogram of Y2')

axs[2].hist(data['Y3'], bins=10)
axs[2].set_xlabel('Y3')
axs[2].set_ylabel('frequency')
axs[2].set_title('Histogram of Y3')

axs[3].hist(data['Y4'], bins=10)
axs[3].set_xlabel('Y4')
axs[3].set_ylabel('frequency')
axs[3].set_title('Histogram of Y4')

axs[4].hist(data['Y5'], bins=10, density=True)
axs[4].set_xlabel('Y5')
axs[4].set_ylabel('frequency')
axs[4].set_title('Histogram of Y5')

plt.tight_layout()
plt.show()
plt.savefig('./plot.png')

# Calculate the absolute relative error for each combination
absolute_error_2 = abs((data['X2'] - data['Y2']) / data['X2'])
absolute_error_3 = abs((data['X3'] - data['Y3']) / data['X3'])
absolute_error_4 = abs((data['X4'] - data['Y4']) / data['X4'])
absolute_error_5 = abs((data['X5'] - data['Y5']) / data['X5'])

# Plot the graphs 
fig, axs = plt.subplots(4, 1, figsize=(8, 16), sharex=True, gridspec_kw={'hspace': 0.5})

axs[0].plot(data['Y1'], absolute_error_2, 'o')
axs[0].set_xlabel('Y1')
axs[0].set_ylabel('|(X2 - Y2) / X2|')
axs[0].set_title('Absolute Relative Error vs. Y1')
axs[0].set_xlim(1480, 1520)
axs[0].set_ylim(0, 0.5)

axs[1].plot(data['Y1'], absolute_error_3, 'o')
axs[1].set_xlabel('Y1')
axs[1].set_ylabel('|(X3 - Y3) / X3|')
axs[1].set_title('Absolute Relative Error vs. Y1')
axs[1].set_xlim(1480, 1520)
axs[1].set_ylim(0, 0.5)

axs[2].plot(data['Y1'], absolute_error_4, 'o')
axs[2].set_xlabel('Y1')
axs[2].set_ylabel('|(X4 - Y4) / X4|')
axs[2].set_title('Absolute Relative Error vs. Y1')
axs[2].set_xlim(1480, 1520)
axs[2].set_ylim(0,0.5)

axs[3].plot(data['Y1'], absolute_error_5, 'o')
axs[3].set_xlabel('Y1')
axs[3].set_ylabel('|(X5 - Y5) / X5|')
axs[3].set_title('Absolute Relative Error vs. Y1')
axs[3].set_xlim(1480, 1520)
axs[3].set_ylim(0,0.5)
plt.show()

# Calculate the mean of the absolute relative errors
mean_absolute_error_2 = np.mean(absolute_error_2)
mean_absolute_error_3 = np.mean(absolute_error_3)
mean_absolute_error_4 = np.mean(absolute_error_4)
mean_absolute_error_5 = np.mean(absolute_error_5)

print("Mean Absolute Relative Error (x2-y2)/x2:", mean_absolute_error_2)
print("Mean Absolute Relative Error (x3-y3)/x3:", mean_absolute_error_3)
print("Mean Absolute Relative Error (x4-y4)/x4:", mean_absolute_error_4)
print("Mean Absolute Relative Error (x5-y5)/x5:", mean_absolute_error_5)


# Calculate the minimum absolute relative error
min_relative_error_2 = np.min(abs((data['X2'] - data['Y2']) / data['X2']))
min_relative_error_3 = np.min(abs((data['X3'] - data['Y3']) / data['X3']))
min_relative_error_4 = np.min(abs((data['X4'] - data['Y4']) / data['X4']))
min_relative_error_5 = np.min(abs((data['X5'] - data['Y5']) / data['X5']))


# Calculate the maximum absolute relative error
max_relative_error_2= np.max(abs((data['X2'] - data['Y2']) / data['X2']))
max_relative_error_3 = np.max(abs((data['X3'] - data['Y3']) / data['X3']))
max_relative_error_4 = np.max(abs((data['X4'] - data['Y4']) / data['X4']))
max_relative_error_5 = np.max(abs((data['X5'] - data['Y5']) / data['X5']))

print("Minimum Relative Error (x2-y2)/x2:", min_relative_error_2)
print("Minimum Relative Error (y3-x3)/y3:", min_relative_error_3)
print("Minimum Relative Error (y4-x4)/y4:", min_relative_error_4)
print("Minimum Relative Error (y5-x5)/y5:", min_relative_error_5 )

print("Maximum Relative Error (y1-x1)/y1:", max_relative_error_2)
print("Maximum Relative Error (y2-x2)/y2:", max_relative_error_3)
print("Maximum Relative Error (y3-x3)/y3:", max_relative_error_4)
print("Maximum Relative Error (y4-x4)/y4:", max_relative_error_5)

existing_data = pd.read_csv('factory_test_data.csv')
new_data = pd.read_csv('new_devices.csv')
combined_data = pd.concat([existing_data, new_data])
columns_of_interest = ['Y2', 'Y3', 'Y4', 'Y5']
existing_data[columns_of_interest] = existing_data[columns_of_interest].apply(pd.to_numeric, errors='coerce')

# Calculate the probability densities for each new device using the specific mean values
prob_densities = []
for i, row in new_data.iterrows():
    prob_density = 1.0
    for col in columns_of_interest:
        value = row[col]  # Access the value in the current column and row
        std = std_y2
        mean = mean_y2  # Assuming you have calculated the mean values somewhere
        if col == 'Y3':
            std = std_y3
            mean = mean_y3
        elif col == 'Y4':
            std = std_y4
            mean = mean_y4
        elif col == 'Y5':
            std = std_y5
            mean = mean_y5
        prob_density *= (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-0.5 * ((value - mean) / std) ** 2)
    prob_densities.append(prob_density)

new_data['Probability Density'] = prob_densities

# Rank the new devices based on their probability densities
new_data_ranked = new_data.sort_values(by='Probability Density', ascending=False)

print("Ranked Devices based on Probability Density:")
print(new_data_ranked)


def check_device(new_device):
    """
    Checks if the measurements of a new device fall within the specified ranges based on mean ± std values,
    and if the first measurement (Y1) falls within the range of 1400 to 2010.

    Parameters:
        new_device (dict): Dictionary containing the measurements of the new device.

    Returns:
        bool: True if all measurements are within the ranges, False otherwise.
    """
    mean_values = {'Y1': mean_y1, 'Y2': mean_y2, 'Y3': mean_y3, 'Y4': mean_y4, 'Y5': mean_y5}
    std_values = {'Y1': std_y1, 'Y2': std_y2, 'Y3': std_y3, 'Y4': std_y4, 'Y5': std_y5}

    for key in new_device.keys():
        mean = mean_values.get(key)
        std = std_values.get(key)
        measurement = new_device[key]

        if key == 'Y1':
            if measurement < 1400 or measurement > 2010:
                return False
        else:
            if mean is not None and std is not None:
                lower_bound = mean - std
                upper_bound = mean + std

                if measurement < lower_bound or measurement > upper_bound:
                    return False
            else:
                return False

    return True
