import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CSV File Load Panrom
df = pd.read_csv('student_expenses.csv')

# Plot overall style set panrom
sns.set_theme(style="whitegrid")

# -------------------------------------------------------------
# CHART 1: Hosteller vs Day Scholar Average Spend (Bar Chart)
# -------------------------------------------------------------
plt.figure(figsize=(7, 4))
ax = sns.barplot(
    data=df, 
    x='hosteller_or_day_scholar', 
    y='daily_canteen_spend', 
    estimator='mean',
    palette='Blues_d',
    errorbar=None
)

plt.title('Average Daily Canteen Spend: Hosteller vs Day Scholar', fontsize=12, fontweight='bold')
plt.xlabel('Student Type', fontsize=10)
plt.ylabel('Average Spend (₹)', fontsize=10)

# Bar top-la values print panna
for p in ax.patches:
    ax.annotate(f'₹{p.get_height():.1f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 5), 
                textcoords='offset points', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('spend_comparison_barchart.png') # Graph Image-a Save Pannum
plt.show() # Display chart window

# -------------------------------------------------------------
# CHART 2: Food Category Breakdown (Pie Chart)
# -------------------------------------------------------------
plt.figure(figsize=(6, 6))
category_counts = df['primary_expense_category'].value_counts()

plt.pie(
    category_counts, 
    labels=category_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#ff9999','#66b3ff','#99ff99']
)

plt.title('Primary Expense Category Distribution', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('category_piechart.png') # Image-a Save Pannum
plt.show()