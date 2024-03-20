import pandas as pd
import random

# Load the dataset
df = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Replace empty values in the 'bmi' column with a random value between 15 and 50
df['bmi'] = df['bmi'].apply(lambda x: random.uniform(15, 50) if pd.isna(x) else x)

# Save the modified dataset back to the .csv file
df.to_csv('healthcare-dataset-stroke-data.csv', index=False)

print("Empty 'bmi' values have been replaced with random values between 15 and 50.")
