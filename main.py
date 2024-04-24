import pandas as pd
import os

# Directory where your Excel files are located
directory = './G_MAP_DATA'

# List to store DataFrames
dfs = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):  # Check if the file is an Excel file
        file_path = os.path.join(directory, filename)
        # Read Excel file into DataFrame and append to list
        dfs.append(pd.read_excel(file_path))

# Concatenate all DataFrames in the list
combined_df = pd.concat(dfs, ignore_index=True)

combined_df_no_duplicates = combined_df.drop_duplicates()
# Define the path where you want to save the combined Excel file
output_file = 'combined_data.xlsx'

# Save the combined DataFrame without duplicates to Excel
combined_df_no_duplicates.to_excel(output_file, index=False)
print(combined_df_no_duplicates)

print("Combined data saved to:", output_file)
