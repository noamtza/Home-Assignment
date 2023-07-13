# Pulsenmore Home Assignment
## Data Loading And Description
The 'factory_test.csv' table contains test data for 51 devices that were selected as a sample group from the population of devices tested in the factory.
The first assumption is that Xi represents a constant value for each device, and Yi values are centered around the corresponding Xi values. This suggests that Xi could be considered as the expected value, and Yi as the actual value for each device. 
Alternatively, the second assumption is that Xi represents a timeline, while Yi represents the corresponding values obtained at each specific time point.
we remove the missing values from the table in order to analyse the data.

### statistics:

<img width="500" alt="Screenshot 2023-07-13 185321" src="https://github.com/noamtza/Home-Assignment/assets/96843396/857e2b8a-08a0-4af2-82b4-0fb020de0280">


Based on statistical analysis and the close proximity of the means of Y2, Y3, Y4, and Y5 to xi, I will proceed with analyzing the first assumption.

## Data Visualization and Explenation


<img width="839" alt="Screenshot 2023-07-13 183221" src="https://github.com/noamtza/Home-Assignment/assets/96843396/9b7f35ce-8991-4ae6-af6d-f38f78139a55">


In order to check the first assumption, we created four graphs, one for each Y2, Y3, Y4, and Y5, as a function of the index of the device. In each graph, the green line represents the mean of the values of Yi, while the red line represents the expected value. Upon analyzing the graphs, we observe that the mean values of Yi are very close to their corresponding expected values. Additionally, we notice that the dispersion of values in Y2 and Y4 is higher compared to Y3 and Y5.(the std values of Y2 Y3 Y4 and Y5 are also approved that). This observation prompts us to further investigate the Probability Distribution of each Yi.


<img width="955" alt="image" src="https://github.com/noamtza/Home-Assignment/assets/96843396/4dedcc14-9d2e-4d72-8589-df2c8e38ebbc">


we will also show a graph of the absolute relative error of each y2,y3,y4,y5 as a function of y1.

<img width="853" alt="Screenshot 2023-07-13 183845" src="https://github.com/noamtza/Home-Assignment/assets/96843396/4e592569-0aa1-494f-82e4-146fa1b094d8">


Y2 exhibits the highest absolute relative error, followed by Y4 and Y5, and then Y3.

## preprocessing:
As part of the data preprocessing step, missing values were removed from the dataset during the data loading and description phase. This ensures that the data used for analysis is complete and reliable. Furthermore, probability distribution plots were created for the variables y2, y3, y4, and y5. The observed patterns in these plots indicate that the distributions of y2, y3, y4, and y5 closely resemble Gaussian curves, suggesting that they follow a normal distribution. Based on this observation, it is reasonable to assume that y2, y3, y4, and y5 have a normal distribution. 

<img width="459" alt="Screenshot 2023-07-13 194020" src="https://github.com/noamtza/Home-Assignment/assets/96843396/f19142c1-a46e-4e44-9f55-b58cbda94071">

in addition, I have noticed that the majority of values in Y1 lie within the range of 1487-1500. However, I have not observed any significant correlation between Y1 and the other variables. Therefore, I have decided not to consider Y1 during the exploration phase of my analysis.

## data exploration 
as we assumed that Y2, Y3, Y4, and Y5 follow a normal distribution, we calculate the probability density for each new device. This is achieved by utilizing the mean and standard deviation values specific to each variable. By applying the probability density function, we obtain the probabilities for each device, which are then stored in the prob_densities list. These probabilities serve as a measure of how likely the new devices belong to the sample group.

<img width="447" alt="Screenshot 2023-07-13 185410" src="https://github.com/noamtza/Home-Assignment/assets/96843396/4011137f-2e5c-4223-8482-42a3fc5fc143">


## Bonus
the check_device function is implemented to test new devices based on the knowledge of the sample group. It checks if the measurements of a new device fall within the specified ranges based on the mean ± std values. The purpose of the function is to accept a dictionary containing the keys 'Y1', 'X2', 'Y2', 'X3', 'Y3', 'X4', 'Y4', 'X5', and 'Y5', along with their corresponding values for a specific device. 

