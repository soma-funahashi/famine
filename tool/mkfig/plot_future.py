import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid', {'grid.linestyle': '--'})
sns.set_context(context = "paper")

yrs = np.arange(2020,2040,1)
ssp1 = [4,3,2,2,2]
ssp2 = [4,4,2,2,2,2,2,2]
ssp3 = [4,4,3,2,2,2,2,2,2,2,2,2,1,1,1]

for i in range(20 - len(ssp1)):
    ssp1.append(0)
for i in range(20 - len(ssp2)):
    ssp2.append(0)
for i in range(20 - len(ssp3)):
    ssp3.append(0)

plt.plot(yrs,ssp1, label = "SSP1")
plt.plot(yrs,ssp2, label = "SSP2")
plt.plot(yrs,ssp3, label = "SSP3")
plt.xticks(yrs, size = 8, rotation = -45)
plt.yticks(np.arange(0, 5, 1))
plt.legend()
plt.title("Famine vulnerable countries in the future", size=12)
plt.savefig("../../fig/plt/future.png", bbox_inches = "tight", dpi = 300)

plt.show()