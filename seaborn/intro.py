# seaborn is a popular library used to build the barchart and other visual
# seaborn is built on top of matplotlib and it is easy to understand

#lets create our first bar chart using seaborn
# here we have to get the school_data.csv
import matplotlib.pyplot  as plt
import seaborn as sns
import pandas as pd

# lets read the school_data.csv
df = pd.read_csv("seaborn/school_data.csv")
value_order = ["NOT ENOUGH DATA", "VERY WEAK", "WEAK", "NEUTRAL", "STRONG", "VERY STRONG"]
# lets plot the barplot using countplot method in seaborn
sns.countplot(df['Supportive Environment'],order=value_order)
plt.xticks(rotation=30)
plt.show()

