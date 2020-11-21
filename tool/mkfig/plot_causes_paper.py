import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

sns.set_style('whitegrid')

dat = pd.read_csv("../../dat/fam/causes.csv")
val = dat.values

years = np.arange(1840, 2020, 10)

dat2 = pd.read_csv("../../dat/fam/tmp.csv")
cat = dat2.columns
cat = np.array(cat)
cat = cat[3:]

lc = [1,1,1,2,2,2,3,3,4,4]
#lab = ["1840 - 1859", "1860 - 1879", "1880 - 1899", "1900 - 1919", "1920 - 1939", "1940 - 1959", "1960 - 1979", "1980 - 1999", "2000 - 2019"]
xlab = ["1860–\n1879", "1880–\n1899", "1900–\n1919", "1920–\n1939", "1940–\n1959", "1960–\n1979", "1980–\n1999", "2000–\n2019"]
lab = ["Environmental trigger", "Social trigger", "Domestic response", "International response"]
x_position = np.arange(len(xlab))


def bar_acc_20yrs(ax):
    years20 = np.arange(1860, 2020, 20)
    tmp = np.zeros(len(years20)*4).reshape(len(years20),4)
    for i in range(len(cat)):
        for j in range(len(years20)):
            tmp[j][lc[i]-1] += val[2*j+2][i] + val[2*j+3][i]
    for i in range(4):
        for j in range(len(years20)):
            tmp[j][i] /= (val[2*j+2][10] + val[2*j+3][10])
    tmp = tmp.T
    ax.bar(x_position, tmp[0], width=0.5, label=lab[0], color = "limegreen", hatch='||')
    ax.bar(x_position, tmp[1], bottom=tmp[0], width=0.5, label=lab[1], color = "darkorange", hatch='xx')
    ax.bar(x_position, tmp[2], bottom=tmp[0]+tmp[1], width=0.5, label=lab[2], color = "gold", hatch='..')
    ax.bar(x_position, tmp[3], bottom=tmp[0]+tmp[1]+tmp[2], width=0.5, label=lab[3], color = "deepskyblue", hatch='//')
    plt.xticks(x_position, xlab, size=10, rotation=0)
    plt.axes(ax)
    plt.legend(loc=2, fontsize=10)
    plt.ylim([0, 6])
    plt.xticks(x_position, xlab, size=10, rotation=0)
    plt.yticks(size=10)
    plt.title("1.a", fontsize=10, loc="left", fontweight='bold')



def bar_kind_acc_20yrs(axes_2a, axes_2b, axes_2c, axes_2d):
    years20 = np.arange(1860, 2020, 20)
    dat = [[],[],[],[]]
    for i in range(10):
        tmp = []
        for j in range(len(years20)):
            tmp.append((val[2*j+2][i] + val[2*j+3][i])/ (val[2*j+2][10] + val[2*j+3][10]))
        tmp = np.array(tmp)
        dat[lc[i]-1].append(tmp)
    dat = np.array(dat)
    print(dat)
    print(val)

    axes_2a.bar(x_position, dat[0][0], label="Drought", color="limegreen")
    axes_2a.bar(x_position, dat[0][1], label="Flood", color="limegreen", hatch='xxx', bottom=dat[0][0])
    axes_2a.bar(x_position, dat[0][2], label="Other climatorological factors", color="limegreen", hatch='//', bottom=dat[0][0]+dat[0][1])

    axes_2b.bar(x_position, dat[1][0], label="War or conflict", color="darkorange")
    axes_2b.bar(x_position, dat[1][1], label="Price rise", color="darkorange", hatch='xxx', bottom=dat[1][0])
    axes_2b.bar(x_position, dat[1][2], label="Imperfect infrastructure", color="darkorange", hatch='//', bottom=dat[1][0]+dat[1][1])
    
    axes_2c.bar(x_position, dat[2][0], label="Political regime", color="gold")
    axes_2c.bar(x_position, dat[2][1], label="Government reaction, food policy", color="gold", hatch='xxx', bottom=dat[2][0])
    
    axes_2d.bar(x_position, dat[3][0], label="Insufficient or delayed aid", color="deepskyblue")
    axes_2d.bar(x_position, dat[3][1], label="Embargo on food aid, Blockade", color="deepskyblue", hatch='xxx', bottom=dat[3][0])

    axs = [axes_2a, axes_2b, axes_2c, axes_2d]
    s = "bcde"
    for i in range(4):
        plt.axes(axs[i])
        plt.legend(loc=2, fontsize=8)
        plt.ylim([0, 3])
        plt.yticks(size=10)
        plt.xticks(x_position, xlab, size=8, rotation=0)
        plt.title("1."+str(s[i]), fontsize=10, loc="left", fontweight='bold')


def main():
    figure = plt.figure(figsize=(9, 9))
    gs_master = GridSpec(nrows=2, ncols=2, height_ratios=[1, 1.5], hspace=0.25)
    gs_1 = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[0, 0:2])
    axes_1 = figure.add_subplot(gs_1[:, :])
    gs_2 = GridSpecFromSubplotSpec(nrows=2, ncols=2, subplot_spec=gs_master[1, 0:2], hspace=0.5)
    axes_2a = figure.add_subplot(gs_2[0, 0])
    axes_2b = figure.add_subplot(gs_2[0, 1])

    axes_2c = figure.add_subplot(gs_2[1, 0])
    axes_2d = figure.add_subplot(gs_2[1, 1])

    bar_acc_20yrs(axes_1)
    bar_kind_acc_20yrs(axes_2a, axes_2b, axes_2c, axes_2d)
    plt.savefig("../../fig/plt/plot_causes_paper.png", dpi=300, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()