import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("iris.csv")

# Preview the data
print(df.head())

# Basic cleaning (drop missing values if any)
df = df.dropna()

# Summary statistics
summary_stats = df.describe()
print(summary_stats)

# Save summary statistics to a CSV (optional but nice)
summary_stats.to_csv("summary_statistics.csv")

# Create a visualization
plt.figure()
plt.hist(df["sepal.length"], bins=10)
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")

# Save the plot
plt.savefig("sepal_length_histogram.png")
plt.close()
