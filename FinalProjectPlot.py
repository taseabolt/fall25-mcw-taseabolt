import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/Users/turra/Desktop/BRFSSData_FinalProject.xlsx"
df = pd.read_excel(file_path, sheet_name="Cleaned data")

grouped_data = df.groupby(["Region", "Year"])["Data_Value"].mean()
grouped_data = grouped_data.round(1)

pivot_table = grouped_data.unstack()
percent_labels = pivot_table.map(lambda x: str(x) + "%")

plt.figure(figsize=(13, 5))
ax = sns.heatmap(pivot_table, annot=percent_labels, fmt="", cmap="magma_r",
    cbar=True)
cbar = ax.collections[0].colorbar
cbar.set_label("Average Obesity Rate (%)", fontsize=11, fontweight="bold")
ax.set_title("Average Obesity Rate by Region and Year", fontsize=14, pad=18)
ax.text(0.5, 1.02, "Regional obesity trends show persistent disparities from 2011 to 2023.", 
    transform=ax.transAxes, ha="center", fontsize=10)

ax.set_xlabel("Year", fontsize=11, fontweight="bold")
ax.set_ylabel("Region", fontsize=11, fontweight="bold")
plt.xticks(rotation=0)
plt.yticks(rotation=0)

plt.subplots_adjust(bottom=0.3)
south_row = list(pivot_table.index).index("South")
num_rows = pivot_table.shape[0]
south_position = 1 - (south_row + 0.5) / num_rows

ax.text(-0.15, -0.30, "Insight: The South consistently shows\n"
    "the highest obesity rates across all years.", transform=ax.transAxes,
    ha="left", fontsize=12, fontweight="bold")

ax.annotate("", xy=(0.0, south_position), xycoords="axes fraction",
    xytext=(-0.15, -0.18), textcoords="axes fraction", arrowprops=dict(
        arrowstyle="->", linewidth=2, color="black"), annotation_clip=False)

plt.show()
