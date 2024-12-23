import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams.update({"figure.max_open_warning": 0})
sns.set_theme(style="darkgrid")

df = pd.read_csv("SIMD.csv", sep=",", header=0, names=["CFLAG", "Requests/sec"])
# print(df.to_string())

plt.figure(figsize=(7, 6))
res = sns.barplot(data=df, x="CFLAG", y="Requests/sec", edgecolor="black")
# numbers in bars
# for i in res.containers: res.bar_label(i, fontsize=11, padding=-25)
# numbers in bottom of bars and at an angle
for p in res.patches:
    height = p.get_height()
    if height > 0:
        res.annotate(f'{p.get_height():.1f}',
                    (p.get_x() + p.get_width() / 2., p.get_height()/5),
                    ha='center', va='bottom',
                    fontsize=10, color='black',
                    xytext=(0, 5),
                    textcoords='offset points',
                    rotation=45,
                    rotation_mode='anchor')
plt.xlabel("Method of optimisation")
plt.ylabel("Requests/sec")
plt.title("Requests/sec for every optimisation method")
plt.savefig("graph.png")
