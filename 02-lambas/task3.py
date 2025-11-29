import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel(r"students\students_info.xlsx")
results_list = pd.read_html(r"students\results_ejudge.html")
results = results_list[0].rename(columns={'User': 'login'})

merged_data = students.merge(results, on='login')

tasks = ['A','B','C','D','E','F','G','H']
merged_data['solved_count'] = (merged_data[tasks] > 0).sum(axis=1)

avg_faculty = merged_data.groupby('group_faculty')['solved_count'].mean()
avg_out = merged_data.groupby('group_out')['solved_count'].mean()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
plt.suptitle("average marks per")
avg_faculty.plot(kind='bar', ax=ax1)
avg_out.plot(kind='bar', ax=ax2)

plt.tight_layout()
plt.show()

filtered = merged_data[(merged_data['G'] > 10) | (merged_data['H'] > 10)]

result = filtered.groupby(['group_faculty', 'group_out']).size().reset_index(name='count')

print("strong students come from _ to _:")
for _, row in result.iterrows():
    print(f"{row['group_faculty']} -> {row['group_out']} : {row['count']} person")
