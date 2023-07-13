# Pulsenmore Home Assignment
## Data Loading And Description
### The 'factory_test.csv' table contains test data for 51 devices that were selected as a sample group from the population of devices tested in the factory.
### The first assumption is that Xi represents a constant value for each device, and Yi values are centered around the corresponding Xi values. This suggests that Xi could be considered as the expected value, and Yi as the actual value for each device. 
### Alternatively, the second assumption is that Xi represents a timeline, while Yi represents the corresponding values obtained at each specific time point. 
### we remove the missing values from the table in order to analyse the data.

### statistics:

count    51.000000  47.0  47.000000  47.0  47.000000  47.0  47.000000  47.0  47.000000
mean   1504.960784  18.0  17.425957  14.0  13.452340  12.0  11.673830   9.0   8.346383
std      71.384861   0.0   4.275727   0.0   0.123732   0.0   1.226748   0.0   0.295807
min    1487.000000  18.0   7.870000  14.0  13.190000  12.0   9.100000   9.0   7.810000
25%    1493.000000  18.0  14.825000  14.0  13.395000  12.0  10.965000   9.0   8.195000
50%    1495.000000  18.0  18.000000  14.0  13.450000  12.0  11.500000   9.0   8.330000
75%    1497.000000  18.0  20.250000  14.0  13.520000  12.0  12.355000   9.0   8.555000
max    2004.000000  18.0  25.260000  14.0  13.990000  12.0  14.560000   9.0   9.160000

### according of the statistics and that the mean of each of y2,y3,y4,y5 is very close to xi i will analyse the first assumption.

## Data Visualization and Explenation
### !['Yi as a function of the devices index']('./plot.png')
### In order to check the first assumption, we created four graphs, one for each Y2, Y3, Y4, and Y5, as a function of the index of the device. In each graph, the green line represents the mean of the values of Yi, while the red line represents the expected value. Upon analyzing the graphs, we observe that the mean values of Yi are very close to their corresponding expected values. Additionally, we notice that the dispersion of values in Y2 and Y4 is higher compared to Y3 and Y5.(the std values of Y2 Y3 Y4 and Y5 are also approved that). This observation prompts us to further investigate the Probability Distribution of each Yi.
!['f'Probability Distribution of {col}'']('./plot.png')
###we will show also a graph of the absolute relative error of each y2,y3,y4,y5 as a function of y1.
!['f'Probability Distribution of {col}'']('./plot.png')
and we can see that y2 has the bigger absolute relative error and than y4 y5 and than y3.
### preprocessing:
As part of the data preprocessing step, missing values were removed from the dataset during the data loading and description phase. This ensures that the data used for analysis is complete and reliable. Furthermore, probability distribution plots were created for the variables y2, y3, y4, and y5. The observed patterns in these plots indicate that the distributions of y2, y3, y4, and y5 closely resemble Gaussian curves, suggesting that they follow a normal distribution. Based on this observation, it is reasonable to assume that y2, y3, y4, and y5 have a normal distribution. This assumption will guide further analysis and modeling of the data.

## data exploration
In the data exploration phase, we begin by checking if the value of Y1 for each new device falls within the range of Y1 values observed in the sample group. 
as we assumed that Y2, Y3, Y4, and Y5 follow a normal distribution, we calculate the probability density for each new device. This is achieved by utilizing the mean and standard deviation values specific to each variable. By applying the probability density function, we obtain the probabilities for each device, which are then stored in the prob_densities list. These probabilities serve as a measure of how likely the new devices belong to the sample group.
 ID    Y1  X2     Y2  X3     Y3  X4     Y4  X5    Y5  Probability Density
  2  1497  18  18.31  14  13.44  12  11.65   9  8.34             0.134025
  1  1557  18  16.15  14  13.55  12  11.28   9  8.33             0.090686
  3  1495  18  17.48  14  13.39  12  11.52   9  8.03             0.066898

## Bonus
the check_device function is implemented to test new devices based on the knowledge of the sample group. It checks if the measurements of a new device fall within the specified ranges based on the mean ± std values. Additionally, it checks if the first measurement (Y1) falls within the range of 1400 to 2010.

