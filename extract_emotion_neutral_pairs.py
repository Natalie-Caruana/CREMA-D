import pandas as pd

# Load the dataset
df = pd.read_csv('finishedResponses.csv')

# Filter for rows where 'clipName' contains "FEA" or "NEU"
filtered_df = df[df['clipName'].str.contains("FEA|NEU", na=False)]

# Extract relevant components
filtered_df['Speaker_ID'] = filtered_df['clipName'].str.extract(r'^(\d+)_')[0]
filtered_df['Specific_Text'] = filtered_df['clipName'].str.extract(r'_(.*?)_')[0]
filtered_df['Emotion'] = filtered_df['clipName'].str.extract(r'_.*?_(.*?)_')[0]

# Split into FEA and NEU subsets
fea_df = filtered_df[filtered_df['clipName'].str.contains("FEA")]
neu_df = filtered_df[filtered_df['clipName'].str.contains("NEU")]

# Merge FEA and NEU on Speaker_ID and Specific_Text
pairs = fea_df.merge(
    neu_df,
    on=['Speaker_ID', 'Specific_Text'],
    suffixes=('_FEA', '_NEU')
)[['clipName_FEA', 'clipName_NEU']]

pairs = pairs.drop_duplicates()

# Save the result or use it further
pairs.to_csv('FEA_NEU_pairs.csv', index=False)

# Display the first few rows of the pairs
print(pairs.head())
