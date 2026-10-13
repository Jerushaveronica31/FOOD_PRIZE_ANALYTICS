import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Creating a Sample Dataset for Regional Street Food & Market Prices (Coimbatore/Pollachi region)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Filtered_Coffee_Price': [20, 20, 22, 22, 25, 25, 25, 28, 28, 30, 30, 30],
    'Street_Snack_Price': [15, 15, 15, 18, 18, 20, 20, 20, 22, 22, 25, 25],
    'Veg_Meal_Price': [70, 75, 75, 80, 80, 85, 90, 90, 95, 100, 100, 100],
    'Fuel_Logistics_Cost': [100, 102, 105, 103, 108, 110, 112, 110, 115, 118, 120, 122]
}

# Converting into a Pandas DataFrame
df = pd.DataFrame(data)

print("--- RAW DATA PREVIEW ---")
print(df.head())

print("\n--- STATISTICAL SUMMARY (INFLATION INSIGHTS) ---")
print(df.describe())

# 2. Data Visualization using Seaborn & Matplotlib
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12, 6))

# Plotting price trends over the months
plt.plot(df['Month'], df['Filtered_Coffee_Price'], marker='o', label='Filter Coffee (₹)', linewidth=2.5)
plt.plot(df['Month'], df['Street_Snack_Price'], marker='s', label='Street Snack (₹)', linewidth=2.5)
plt.plot(df['Month'], df['Veg_Meal_Price'], marker='^', label='Veg Meal (₹)', linewidth=2.5)

plt.title('Regional Street Food & Local Market Price Trends (Coimbatore/Pollachi)', fontsize=14, fontweight='bold', color='#333333')
plt.xlabel('Months of the Year', fontsize=12)
plt.ylabel('Average Price (INR)', fontsize=12)
plt.legend(fontsize=11)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the generated chart as an image for portfolio use
plt.savefig('food_price_trends.png', dpi=300)
print("\n[SUCCESS] Analysis complete! Visualization chart saved as 'food_price_trends.png'.")

# Show the chart window
plt.show()