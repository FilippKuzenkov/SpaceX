import pandas as pd

# Provided data
data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(df)

# Select and print the 'rocket' column
print("\n'rocket' column:")
print(df["rocket"])

# Filter the DataFrame for rockets with more than 5 launches
filtered_df = df[df['launches'] > 5]
print("\nRockets with more than 5 launches:")
print(filtered_df)

# Add a new column for 'success_rate'
# Assuming success_rate is calculated as (successful_launches / total_launches) * 100
# For demonstration, let's assume some hypothetical successful launches data
successful_launches = [2, 95, 2]
df['success_rate'] = [(s / l) * 100 for s, l in zip(successful_launches, df['launches'])]

print("\nDataFrame with 'success_rate' column:")
print(df)
