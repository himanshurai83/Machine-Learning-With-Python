import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Python Practice/Matplotlib/Project/deliveries.csv")
# print(df.head())
# print(df.isna().sum())
cleaned_df = df.dropna(axis=True)
cleaned_df = cleaned_df.drop_duplicates()
pd.set_option('display.max_columns', None)
# print(cleaned_df.head(30))
# print(cleaned_df.shape)
# print("Tail")
# print(cleaned_df.tail(10))

grouped_runs = cleaned_df[(cleaned_df['batting_team'] == "Sunrisers Hyderabad") & (cleaned_df['match_id'] == 1)] \
    .groupby("over")['total_runs'].sum()
select_srh = cleaned_df[(cleaned_df['batting_team'] ==
                         "Sunrisers Hyderabad") & (cleaned_df['match_id'] == 1)]
srh_total_runs = select_srh['total_runs'].sum()
# print(grouped_runs.index)
# print(grouped_runs.values)

fig, ax = plt.subplots(2, figsize=(10, 8))
ax[0].bar(grouped_runs.index, grouped_runs.values, color='orange')
ax[0].set_title("Sunrisers Hyderabad Over / Runs")
ax[0].set_xlabel("Overs")
ax[0].set_ylabel("Runs")
ax[0].set_xticks(grouped_runs.index)
ax[0].set_yticks(grouped_runs.values)
ax[0].text(
    x=8, y=23, s=f"SRH Total Runs : {srh_total_runs}", fontsize=12, color="red")
# plt.show()

rcb_bowler_runs_concede = cleaned_df[(cleaned_df['bowling_team'] ==
                                      "Royal Challengers Bangalore") & (cleaned_df['match_id'] == 1)].groupby("bowler")['total_runs'].sum()

# print(rcb_bowler_runs_concede.index)
# print(rcb_bowler_runs_concede.values)

# ax[1].bar(rcb_bowler_runs_concede.index,
#           rcb_bowler_runs_concede.values, color="red")
# ax[1].set_title("RCB Bowler Runs")
# ax[1].set_xlabel("Bowler Name")
# ax[1].set_ylabel("Runs")

# plt.show()
# print(cleaned_df)

# print(select_srh.head())
srh_batsman_runs = select_srh.groupby("batsman")['total_runs'].sum()
print(srh_batsman_runs.index)
print(srh_batsman_runs.values)
colors = plt.cm.tab10(np.arange(len(srh_batsman_runs)))
ax[1].bar(srh_batsman_runs.index, srh_batsman_runs.values,
          color=colors)
ax[1].set_title("Batsman Contribution")
ax[1].set_xlabel("Batsman Name")
ax[1].set_ylabel("Batsman Runs")
plt.show()

# srh_batsman_partnership = select_srh.groupby(
#     ["batsman", "non_striker"])['total_runs'].sum()
# print(srh_batsman_partnership)
