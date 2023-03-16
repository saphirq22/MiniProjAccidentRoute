
import matplotlib.pyplot as plt
import seaborn as sns

from pyDefineDF import *

df = DefineDF(laFranceEntiere)

plt.figure(figsize=(20, 10))
sns.heatmap(df.corr(), annot=True, cbar=False) #
plt.show()


