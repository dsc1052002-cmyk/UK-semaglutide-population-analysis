import pandas as pd

# Load the clinical market dataset
df = pd.read_csv('data/uk_semaglutide_demographics.csv')

# Calculate total estimated semaglutide users in the UK
total_users = df['estimated_users_2026'].sum()
print(f"Total Estimated UK Semaglutide Users (2026): {total_users:,}\n")

# Calculate percentage market share for each brand
df['market_share_pct'] = (df['estimated_users_2026'] / total_users) * 100

# Display the final scannable table
summary_table = df[['brand_name', 'primary_indication', 'estimated_users_2026', 'market_share_pct']]
print(summary_table.to_string(index=False))
