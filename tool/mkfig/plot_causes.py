import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

dat = pd.read_csv("../../dat/fam/causes.csv")
val = dat.values

years = np.arange(1840, 2020, 10)

dat2 = pd.read_csv("../../dat/fam/tmp.csv")
cat = dat2.columns
cat = np.array(cat)
cat = cat[3:]

lc = [1,1,1,1,2,2,2,3,3,4,4,4]
#lab = ["1840 - 1859", "1860 - 1879", "1880 - 1899", "1900 - 1919", "1920 - 1939", "1940 - 1959", "1960 - 1979", "1980 - 1999", "2000 - 2019"]
xlab = ["1860 -\n1879", "1880 -\n1899", "1900 -\n1919", "1920 -\n1939", "1940 -\n1959", "1960 -\n1979", "1980 -\n1999", "2000 -\n2019"]
lab = ["Environmental trigger", "Social trigger", "Domestic response", "International response"]

def plot_all():
    for i in range(len(cat)):
        tmp = []
        for j in range(len(years)):
            tmp.append(val[j][i])
        plt.plot(years, tmp, label = cat[i])
    plt.show()


def plot_20yrs():
    years20 = np.arange(1860, 2020, 20)
    tmp = np.zeros(len(years20)*4).reshape(len(years20),4)

    for i in range(len(cat)):
        for j in range(len(years20)):
            tmp[j][lc[i]-1] += val[2*j+2][i] + val[2*j+3][i]

    print(tmp)
    tmp = tmp.T
    plt.plot(years20, tmp[0], label = lab[0], color = "limegreen")
    plt.plot(years20, tmp[1], label = lab[1], color = "darkorange")
    plt.plot(years20, tmp[2], label = lab[2], color = "gold")
    plt.plot(years20, tmp[3], label = lab[3], color = "deepskyblue")

    plt.legend(fontsize = 10)
    plt.xticks(years20, xlab, size=10, rotation=0)
    plt.title("Causes of the previous famine", size = 12)
    plt.savefig("../../fig/plt/causes.png", bbox_inches = "tight", dpi = 300)
    plt.show()

#plot_20yrs()


def bar_20yrs():
    years20 = np.arange(1860, 2020, 20)
    tmp = np.zeros(len(years20)*4).reshape(len(years20),4)

    for i in range(len(cat)):
        for j in range(len(years20)):
            tmp[j][lc[i]-1] += val[2*j+2][i] + val[2*j+3][i]

    for i in range(4):
        for j in range(len(years20)):
            tmp[j][i] /= (val[2*j+2][11] + val[2*j+3][11])

    tmp = tmp.T

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_position = np.arange(len(xlab))
    ax.bar(x_position - 0.24, tmp[0], width=0.16, label=lab[0], color = "limegreen")
    ax.bar(x_position - 0.08, tmp[1], width=0.16, label=lab[1], color = "darkorange")
    ax.bar(x_position + 0.08, tmp[2], width=0.16, label=lab[2], color = "gold")
    ax.bar(x_position + 0.24, tmp[3], width=0.16, label=lab[3], color = "deepskyblue")
    plt.xticks(x_position, xlab, size=10, rotation=0)
    plt.legend(fontsize=10)
    plt.title("Average number of factors in each famine", size=12)
    plt.savefig("../../fig/plt/ratio.png", bbox_inches = "tight", dpi = 300)
    plt.show()

bar_20yrs()