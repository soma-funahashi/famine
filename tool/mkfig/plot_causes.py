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

lc = [1,1,1,2,2,2,3,3,4,4]
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
            tmp[j][lc[i]-1] += (val[2*j+2][i] + val[2*j+3][i])/ (val[2*j+2][10] + val[2*j+3][10])

    print(tmp)
    tmp = tmp.T
    plt.plot(years20, tmp[0], label = lab[0], zorder=4, color = "limegreen", marker='o')
    plt.plot(years20, tmp[1], label = lab[1], zorder=3, color = "darkorange", marker='s')
    plt.plot(years20, tmp[2], label = lab[2], zorder=2, color = "gold", marker='^')
    plt.plot(years20, tmp[3], label = lab[3], zorder=1, color = "deepskyblue", marker='v')

    plt.legend(fontsize = 10)
    plt.xticks(years20, xlab, size=10, rotation=0)
    plt.title("Causes of the previous famine", size = 12)
    plt.savefig("../../fig/plt/ratio.png", bbox_inches = "tight", dpi = 300)
    plt.show()


def bar_acc_20yrs():
    years20 = np.arange(1860, 2020, 20)
    tmp = np.zeros(len(years20)*4).reshape(len(years20),4)

    for i in range(len(cat)):
        for j in range(len(years20)):
            tmp[j][lc[i]-1] += val[2*j+2][i] + val[2*j+3][i]

    for i in range(4):
        for j in range(len(years20)):
            tmp[j][i] /= (val[2*j+2][10] + val[2*j+3][10])

    tmp = tmp.T

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_position = np.arange(len(xlab))
    ax.bar(x_position, tmp[0], width=0.5, label=lab[0], color = "limegreen", hatch='||')
    ax.bar(x_position, tmp[1], bottom=tmp[0], width=0.5, label=lab[1], color = "darkorange", hatch='xx')
    ax.bar(x_position, tmp[2], bottom=tmp[0]+tmp[1], width=0.5, label=lab[2], color = "gold", hatch='..')
    ax.bar(x_position, tmp[3], bottom=tmp[0]+tmp[1]+tmp[2], width=0.5, label=lab[3], color = "deepskyblue", hatch='//')
    plt.xticks(x_position, xlab, size=10, rotation=0)
    plt.legend(fontsize=10)
    plt.title("Average number of factors in each famine", size=12)
    plt.savefig("../../fig/plt/ratio_acc.png", bbox_inches = "tight", dpi = 300)
    plt.show()


def bar_kind_acc_20yrs():
    years20 = np.arange(1860, 2020, 20)
    x_position = np.arange(len(xlab))

    dat = [[],[],[],[]]

    for i in range(10):
        tmp = []
        for j in range(len(years20)):
            tmp.append((val[2*j+2][i] + val[2*j+3][i])/ (val[2*j+2][10] + val[2*j+3][10]))
            #tmp.append(val[2*j+2][i] + val[2*j+3][i])

        tmp = np.array(tmp)
        dat[lc[i]-1].append(tmp)

    dat = np.array(dat)
    print(dat)

    dat = np.array(dat)

    print(val)

    fig, ax = plt.subplots(2, 2, figsize=(10, 8))

    print(dat[0][0] + dat[0][1])

    ax[0,0].bar(x_position, dat[0][0], label="Drought", color="limegreen")
    ax[0,0].bar(x_position, dat[0][1], label="Flood", color="limegreen", hatch='xxx', bottom=dat[0][0])
    ax[0,0].bar(x_position, dat[0][2], label="Other climatorological factors", color="limegreen", hatch='//', bottom=dat[0][0]+dat[0][1])

    ax[0, 1].bar(x_position, dat[1][0], label="War or conflict", color="darkorange")
    ax[0, 1].bar(x_position, dat[1][1], label="Price rise", color="darkorange", hatch='xxx', bottom=dat[1][0])
    ax[0, 1].bar(x_position, dat[1][2], label="Imperfect infrastructure", color="darkorange", hatch='//', bottom=dat[1][0]+dat[1][1])
    
    ax[1, 0].bar(x_position, dat[2][0], label="Political regime", color="gold")
    ax[1, 0].bar(x_position, dat[2][1], label="Government reaction, food policy", color="gold", hatch='xxx', bottom=dat[2][0])
    
    ax[1, 1].bar(x_position, dat[3][0], label="Insufficient or delayed aid", color="deepskyblue")
    ax[1, 1].bar(x_position, dat[3][1], label="Embargo on food aid, Blockade", color="deepskyblue", hatch='xxx', bottom=dat[3][0])


    axs = plt.gcf().get_axes()

    # 軸毎にループ
    for ax in axs:
        plt.axes(ax)
        plt.legend(loc=2, fontsize=10)
        plt.ylim([0, 2.5])
        plt.xticks(x_position, xlab, size=10, rotation=0)

    # 図の調整
    plt.tight_layout()

    plt.savefig("../../fig/plt/ratio_kind_acc.png", bbox_inches = "tight", dpi = 300)
    plt.show()


#bar_kind_acc_20yrs()
plot_20yrs()
#bar_acc_20yrs()