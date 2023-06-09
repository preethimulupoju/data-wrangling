import pandas as pd
import seaborn as sns

# 1. Import the dataset using Pandas from the given URL
url = "https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"
covid_df = pd.read_csv(url)

# 2a. Find no. of rows & columns in the dataset
print("Number of rows:", covid_df.shape[0])
print("Number of columns:", covid_df.shape[1])

# 2b. Data types of columns.
print("Data types of columns:\n", covid_df.dtypes)

# 2c. Info & describe of data in dataframe.
print("Dataframe Info:")
covid_df.info()

print("\nDataframe Description:")
covid_df.describe()

# 3a. Find count of unique values in location column.
unique_locations = covid_df["location"].nunique()
print("Number of unique locations:", unique_locations)

# 3b. Find which continent has maximum frequency using values counts.
max_frequency_continent = covid_df["continent"].value_counts().index[0]
print("Continent with maximum frequency:", max_frequency_continent)

# 3c. Find maximum & mean value in 'total_cases'.
max_total_cases = covid_df["total_cases"].max()
mean_total_cases = covid_df["total_cases"].mean()
print("Maximum total cases:", max_total_cases)
print("Mean total cases:", mean_total_cases)

# 3d. Find 25%,50% & 75% quartile value in 'total_deaths'.
quartiles = covid_df["total_deaths"].quantile([0.25, 0.5, 0.75])
print("25% quartile of total deaths:", quartiles[0.25])
print("50% quartile of total deaths:", quartiles[0.5])
print("75% quartile of total deaths:", quartiles[0.75])

# 3e. Find which continent has maximum 'human_development_index'.
max_hdi_continent = covid_df.loc[covid_df["human_development_index"].idxmax()]["continent"]
max_hdi = covid_df["human_development_index"].max()
print("Continent with maximum human development index:", max_hdi_continent)
print("Maximum human development index:", max_hdi)

# 3f. Find which continent has minimum 'gdp_per_capita'.
min_gdp_continent = covid_df.loc[covid_df["gdp_per_capita"].idxmin()]["continent"]
min_gdp = covid_df["gdp_per_capita"].min()
print("Continent with minimum GDP per capita:", min_gdp_continent)
print("Minimum GDP per capita:", min_gdp)

# 4. Filter the dataframe with only this columns
# ['continent','location','date','total_cases','total_deaths','gdp_per_capita', 'human_development_index']
covid_df = covid_df[["continent", "location", "date", "total_cases", "total_deaths", "gdp_per_capita", "human_development_index"]]

# 5a. Remove all duplicates observations
covid_df.drop_duplicates(inplace=True)

# 5b. Find missing values in all columns
print("Missing values in each column:\n", covid_df.isna().sum())

# 5c. Remove all observations where continent column value is missing
covid_df.dropna(subset=["continent"], inplace=True)

# 5d. Fill all missing values with 0
covid_df.fillna(0, inplace=True)

# 6a. Convert date column in datetime format using
import pandas as pd

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv")

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])
# Create a new column 'month' with the month extracted from the date column
df['month'] = df['date'].dt.month
# Find the maximum value in all columns grouped by continent
df_groupby = df.groupby('continent').max().reset_index()
# Create a new feature 'total_deaths_to_total_cases'
df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']
import seaborn as sns

# Plot a histogram of 'gdp_per_capita' column
sns.displot(df_groupby['gdp_per_capita'], kde=False)
# Plot a scatter plot of 'total_cases' and 'gdp_per_capita'
sns.scatterplot(data=df_groupby, x='gdp_per_capita', y='total_cases')
# Plot a pairplot of df_groupby dataset
sns.pairplot(df_groupby)
# Plot a bar plot of 'continent' column with 'total_cases'
sns.catplot(data=df_groupby, x='continent', y='total_cases', kind='bar')
# Save the df_groupby dataframe to a CSV file
df_groupby.to_csv('df_groupby.csv', index=False)