import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

spreadsheet_id = '1ukP0EvXlTKfL7tfQ1KuwDaFI7ue6oSJRhK7gk7Gtg-s'
gid = '1795184240'
url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}'

df = pd.read_csv(url)
print("Dataset berhasil dibaca. Berikut 5 baris pertamanya:")
print(df.head())

df.info()

df['event_timestamp'] = pd.to_datetime(df['event_timestamp'])
df['event_date'] = pd.to_datetime(df['event_date'])

print("Tipe data kolom 'event_timestamp' dan 'event_date' berhasil diubah menjadi datetime.")
df.info()

# Cell was empty, skipping or adding a placeholder if content is strictly needed.
# If there was code here, it would be included.

df_filtered = df[df['event_type'].isin(['search', 'add_to_cart'])]
print("DataFrame berhasil difilter. Berikut 5 baris pertamanya:")
print(df_filtered.head())
print("\nInformasi DataFrame setelah filtering:")
df_filtered.info()

df_sorted = df_filtered.sort_values(by=['user_id', 'event_date', 'event_timestamp'])
print("DataFrame berhasil diurutkan berdasarkan user_id, event_date, dan event_timestamp. Berikut 5 baris pertamanya:")
print(df_sorted.head())

df_sorted['prev_event_type'] = df_sorted.groupby(['user_id', 'event_date'])['event_type'].shift(1)
df_sorted['prev_user_id'] = df_sorted.groupby(['user_id', 'event_date'])['user_id'].shift(1)
df_sorted['prev_event_date'] = df_sorted.groupby(['user_id', 'event_date'])['event_date'].shift(1)

search_add_to_cart_sequences = df_sorted[
    (df_sorted['event_type'] == 'add_to_cart') &
    (df_sorted['prev_event_type'] == 'search') &
    (df_sorted['user_id'] == df_sorted['prev_user_id']) &
    (df_sorted['event_date'] == df_sorted['prev_event_date'])
]

users_with_search_add_to_cart = search_add_to_cart_sequences['user_id'].unique()

print(f"Number of unique users who performed 'search' followed by 'add_to_cart' on the same day: {len(users_with_search_add_to_cart)}")
print("First 10 unique users:")
print(users_with_search_add_to_cart[:10])

display(search_add_to_cart_sequences)

total_unique_users = df_filtered['user_id'].nunique()
percentage_users = (len(users_with_search_add_to_cart) / total_unique_users) * 100

print(f"Total unique users in the filtered dataset: {total_unique_users}")
print(f"Percentage of unique users who performed 'search' followed by 'add_to_cart' on the same day: {percentage_users:.2f}%")

print(f"Total unique users in the filtered dataset: {total_unique_users}")
print(f"Percentage of unique users who performed 'search' followed by 'add_to_cart' on the same day: {percentage_users:.2f}%")

unique_event_types = df['event_type'].unique()
print("Unique event types present in the dataset:")
print(unique_event_types)

all_unique_users = set(df['user_id'].unique())

users_add_to_cart_all = set(df[df['event_type'] == 'add_to_cart']['user_id'].unique())
users_search_all = set(df[df['event_type'] == 'search']['user_id'].unique())
users_login_all = set(df[df['event_type'] == 'login']['user_id'].unique())
users_page_view_all = set(df[df['event_type'] == 'page_view']['user_id'].unique())

assigned_users = set()

# 1. 'Search & Add to Cart (Same Day)'
cat_search_add_to_cart_same_day = set(users_with_search_add_to_cart)
assigned_users.update(cat_search_add_to_cart_same_day)

# 2. 'Add to Cart Only'
cat_add_to_cart_only = users_add_to_cart_all - assigned_users
assigned_users.update(cat_add_to_cart_only)

# 3. 'Search Only'
cat_search_only = users_search_all - assigned_users
assigned_users.update(cat_search_only)

# 4. 'Login Only'
cat_login_only = users_login_all - assigned_users
assigned_users.update(cat_login_only)

# 5. 'Page View Only'
cat_page_view_only = users_page_view_all - assigned_users
assigned_users.update(cat_page_view_only)

# 6. 'Other/No Specific Action'
cat_other = all_unique_users - assigned_users

print(f"Number of unique users in 'Search & Add to Cart (Same Day)': {len(cat_search_add_to_cart_same_day)}")
print(f"Number of unique users in 'Add to Cart Only': {len(cat_add_to_cart_only)}")
print(f"Number of unique users in 'Search Only': {len(cat_search_only)}")
print(f"Number of unique users in 'Login Only': {len(cat_login_only)}")
print(f"Number of unique users in 'Page View Only': {len(cat_page_view_only)}")
print(f"Number of unique users in 'Other/No Specific Action': {len(cat_other)}")

# Verify that all users are accounted for and categories are mutually exclusive
assert len(cat_search_add_to_cart_same_day) + \
       len(cat_add_to_cart_only) + \
       len(cat_search_only) + \
       len(cat_login_only) + \
       len(cat_page_view_only) + \
       len(cat_other) == len(all_unique_users), "Total users do not match!"
print("All categories are mutually exclusive and cover all unique users.")

total_unique_users_all = len(all_unique_users)

category_counts = {
    'Search & Add to Cart (Same Day)': len(cat_search_add_to_cart_same_day),
    'Add to Cart Only': len(cat_add_to_cart_only),
    'Search Only': len(cat_search_only),
    'Login Only': len(cat_login_only),
    'Page View Only': len(cat_page_view_only),
    'Other/No Specific Action': len(cat_other)
}

category_percentages = {
    category: (count / total_unique_users_all) * 100
    for category, count in category_counts.items()
}

print("Percentage of unique users in each category:")
for category, percentage in category_percentages.items():
    print(f"- {category}: {percentage:.2f}%")

# Convert percentages to a Pandas Series for easier plotting
percentages_series = pd.Series(category_percentages)

# Sort the percentages for better visualization (optional, but good practice)
percentages_series = percentages_series.sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(12, 7))
sns.barplot(x=percentages_series.index, y=percentages_series.values, palette='viridis')

# Add labels and title
plt.title('Distribution of Unique Users by Activity Category', fontsize=16)
plt.xlabel('User Category', fontsize=12)
plt.ylabel('Percentage of Unique Users (%)', fontsize=12)
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability

# Add percentage values on top of the bars
for index, value in enumerate(percentages_series.values):
    plt.text(index, value + 0.5, f'{value:.2f}%', ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()

# Convert percentages to a Pandas Series for easier plotting
percentages_series = pd.Series(category_percentages)

# Sort the percentages for better visualization (optional, but good practice)
percentages_series = percentages_series.sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(12, 7))
sns.barplot(x=percentages_series.index, y=percentages_series.values, hue=percentages_series.index, palette='viridis', legend=False)

# Add labels and title
plt.title('Distribution of Unique Users by Activity Category', fontsize=16)
plt.xlabel('User Category', fontsize=12)
plt.ylabel('Percentage of Unique Users (%)', fontsize=12)
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability

# Add percentage values on top of the bars
for index, value in enumerate(percentages_series.values):
    plt.text(index, value + 0.5, f'{value:.2f}%', ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()

df_time_series = df.groupby(['event_date', 'event_type']).size().reset_index(name='event_count')
print("Aggregated time-series data created. Here are the first 5 rows:")
print(df_time_series.head())

unique_event_types_ts = df_time_series['event_type'].unique()

for event_type in unique_event_types_ts:
    df_subset = df_time_series[df_time_series['event_type'] == event_type]

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_subset, x='event_date', y='event_count', marker='o')
    plt.title(f'Daily Trend of {event_type.replace("_", " ").title()} Events', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Event Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

df_search_add_to_cart_daily = search_add_to_cart_sequences.groupby('event_date').size().reset_index(name='sequence_count')
print("Daily count of 'search' followed by 'add_to_cart' sequences created. Here are the first 5 rows:")
print(df_search_add_to_cart_daily.head())

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_search_add_to_cart_daily, x='event_date', y='sequence_count', marker='o')
plt.title('Daily Trend of Search followed by Add to Cart Sequences', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sequence Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
