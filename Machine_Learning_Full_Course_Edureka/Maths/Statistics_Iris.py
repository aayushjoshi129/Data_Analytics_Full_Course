# Statistics plays a crucial role in various aspects of machine learning, including data analysis, model evaluation, and inference. Here are some key concepts of statistics in machine learning along with their terminologies, definitions, and examples:

# 1. Descriptive Statistics:
#    - Definition: Descriptive statistics summarize and describe the features of a dataset using numerical and graphical methods.
#    - Terminologies:
#      - Mean: Average value of a dataset.
#      - Median: Middle value of a dataset.
#      - Mode: Most frequent value in a dataset.
#      - Variance: Measure of the spread or dispersion of the values in a dataset.
#      - Standard Deviation: Square root of the variance, representing the average deviation from the mean.
#    - Example: Computing the mean, median, and standard deviation of a dataset of exam scores to understand the central tendency and spread of scores.

# 2. Probability Distributions:
#    - Definition: Probability distributions describe the likelihood of different outcomes in a random experiment.
#    - Terminologies:
#      - Normal Distribution: Bell-shaped distribution characterized by its mean and standard deviation.
#      - Bernoulli Distribution: Distribution for binary outcomes (success/failure).
#      - Poisson Distribution: Distribution for counting the number of events occurring in a fixed interval.
#    - Example: Using a normal distribution to model the heights of individuals in a population.

# 3. Hypothesis Testing:
#    - Definition: Hypothesis testing is a statistical method used to make inferences about population parameters based on sample data.
#    - Terminologies:
#      - Null Hypothesis (\(H_0\)): Hypothesis to be tested or compared against an alternative hypothesis.
#      - Alternative Hypothesis (\(H_1\)): Hypothesis that contradicts the null hypothesis.
#      - p-value: Probability of observing the test statistic or more extreme results if the null hypothesis is true.
#      - Type I Error: Incorrectly rejecting the null hypothesis when it is true (false positive).
#      - Type II Error: Failing to reject the null hypothesis when it is false (false negative).
#    - Example: Testing whether a new drug treatment is effective by comparing the treatment group with the control group using a t-test.

# 4. Regression Analysis:
#    - Definition: Regression analysis models the relationship between a dependent variable and one or more independent variables.
#    - Terminologies:
#      - Linear Regression: Regression method that models the relationship between variables using a linear equation.
#      - Coefficients: Parameters of the regression equation representing the relationship between independent and dependent variables.
#      - R-squared: Measure of how well the regression model fits the data.
#    - Example: Predicting house prices based on features such as square footage, number of bedrooms, and location using linear regression.

# 5. Statistical Testing and Inference:
#    - Definition: Statistical inference involves making conclusions or predictions about a population based on sample data.
#    - Terminologies:
#      - Confidence Interval: Range of values within which the true population parameter is likely to lie with a certain level of confidence.
#      - Central Limit Theorem: The theorem states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases.
#    - Example: Estimating the mean height of all adults in a country with a 95% confidence interval based on a sample survey.

# Understanding statistical concepts and methods is essential for effectively analyzing data, evaluating models, and making informed decisions in machine learning applications.



# Certainly! Here are some key statistical formulas along with definitions and examples for both population and sample statistics:

# 1. Population Mean:
#    - Population Formula: \(\mu = \frac{1}{N} \sum_{i=1}^{N} x_i\)
#    - Sample Formula: \(\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i\)
#    - Definition: The average value of all observations in a population or sample, respectively.
#    - Example: Calculating the mean height of all adults in a country based on a census (population) or based on a sample survey (sample).

# 2. Population Variance:
#    - Population Formula: \(\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2\)
#    - Sample Formula: \(s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2\)
#    - Definition: Measure of the spread or dispersion of values around the mean in a population or sample, respectively.
#    - Example: Assessing the variability in test scores among all students in a school (population) or among a sample of students from the school (sample).

# 3. Population Standard Deviation:
#    - Population Formula: \(\sigma = \sqrt{\sigma^2}\)
#    - Sample Formula: \(s = \sqrt{s^2}\)
#    - Definition: Square root of the variance, representing the average deviation from the mean in a population or sample, respectively.
#    - Example: Expressing the variability in monthly temperatures across all cities in a country (population) or across a sample of cities (sample).

# 4. Population Proportion:
#    - Population Formula: \(P = \frac{\text{Number of successes}}{\text{Total population size}}\)
#    - Sample Formula: \(\hat{p} = \frac{\text{Number of successes}}{\text{Sample size}}\)
#    - Definition: Proportion of successes in a population or sample, respectively.
#    - Example: Estimating the proportion of defective items in a factory's entire production (population) or in a sample batch of items (sample).

# 5. Confidence Interval for Population Mean:
#    - Formula: \(\bar{x} \pm Z \frac{\sigma}{\sqrt{N}}\)
#    - Definition: Range of values within which the true population mean is likely to lie with a certain level of confidence.
#    - Example: Estimating the average income of all households in a city with a 95% confidence interval based on a sample survey.

# Understanding these formulas and their applications is essential for conducting statistical analysis, making inferences about populations, and drawing conclusions from sample data in machine learning and data analysis.

import statistics as s
from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

my_data = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 100, 200, 300, 2, 3, 2, 2, 2, 2, 2, 2, 2]

print("The Mean, Median and Mode are:")
print(s.mean(my_data))
print(s.median(my_data))
print(s.mode(my_data))


print("The Variance and Standard Deviation of Data is :")
print(s.pvariance(my_data))
print(s.stdev(my_data))


iris = datasets.load_iris()

data = pd.DataFrame(iris['data'], columns=['Petal Length', 'Petal Width', 'Sepal Length', 'Sepal Width'])

data['Species'] = iris['target']
data['Species'] = data['Species'].apply(lambda x: iris['target_names'][x])

print(data.describe())

sns.pairplot(data)
plt.savefig('./Math_Plots/Statistics_PairPlot.jpg')
plt.show()