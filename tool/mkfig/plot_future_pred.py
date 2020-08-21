import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")
sns.set(style="ticks")

def read_data(ssp, rcp):
    out = pd.read_csv("../../out/logisticRegression_all_future_"+ssp+"_rcp"+rcp+".csv", index_col="ISO3")
    return out

out_ssp1_rcp2p6 = read_data("ssp1", "2p6")
out_ssp1_rcp4p5 = read_data("ssp1", "4p5")
out_ssp1_rcp6p0 = read_data("ssp1", "6p0")
out_ssp1_rcp8p5 = read_data("ssp1", "8p5")

out_ssp2_rcp2p6 = read_data("ssp2", "2p6")
out_ssp2_rcp4p5 = read_data("ssp2", "4p5")
out_ssp2_rcp6p0 = read_data("ssp2", "6p0")
out_ssp2_rcp8p5 = read_data("ssp2", "8p5")

out_ssp3_rcp2p6 = read_data("ssp3", "2p6")
out_ssp3_rcp4p5 = read_data("ssp3", "4p5")
out_ssp3_rcp6p0 = read_data("ssp3", "6p0")
out_ssp3_rcp8p5 = read_data("ssp3", "8p5")

t1 = 0.01
t2 = 0.025
t3 = 0.05

def calc(inp):
    out = np.zeros(120).reshape(4,30)
    for i in range(len(inp)):
        for yr in range(2021, 2051):
            if inp.iat[i, yr - 2021] < t1:
                out[0][yr - 2021] += 1
            elif inp.iat[i, yr - 2021] < t2:
                out[1][yr - 2021] += 1
            elif inp.iat[i, yr - 2021] < t3:
                out[2][yr - 2021] += 1
            else:
                out[3][yr - 2021] += 1
    return out

cnt_ssp1_rcp2p6 = calc(out_ssp1_rcp2p6)
cnt_ssp1_rcp4p5 = calc(out_ssp1_rcp4p5)
cnt_ssp1_rcp6p0 = calc(out_ssp1_rcp6p0)
cnt_ssp1_rcp8p5 = calc(out_ssp1_rcp8p5)

cnt_ssp2_rcp2p6 = calc(out_ssp2_rcp2p6)
cnt_ssp2_rcp4p5 = calc(out_ssp2_rcp4p5)
cnt_ssp2_rcp6p0 = calc(out_ssp2_rcp6p0)
cnt_ssp2_rcp8p5 = calc(out_ssp2_rcp8p5)

cnt_ssp3_rcp2p6 = calc(out_ssp3_rcp2p6)
cnt_ssp3_rcp4p5 = calc(out_ssp3_rcp4p5)
cnt_ssp3_rcp6p0 = calc(out_ssp3_rcp6p0)
cnt_ssp3_rcp8p5 = calc(out_ssp3_rcp8p5)


print(cnt_ssp1_rcp2p6)
print(cnt_ssp1_rcp4p5)

fig, ax = plt.subplots(1, 3, figsize=(12,4))

ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[0].set_ylim(0,35)
ax[1].set_ylim(0,35)
ax[2].set_ylim(0,35)

yr = np.arange(2021, 2051).astype(int)
lw = 0.0

def plot_fill_1(p, c, lab):
    ax[0].plot(yr, cnt_ssp1_rcp2p6[p], color = c, linewidth = lw)
    ax[0].plot(yr, cnt_ssp1_rcp4p5[p], color = c, linewidth = lw)
    ax[0].plot(yr, cnt_ssp1_rcp6p0[p], color = c, linewidth = lw)
    ax[0].plot(yr, cnt_ssp1_rcp8p5[p], color = c, linewidth = lw)
    ax[0].fill_between(yr, cnt_ssp1_rcp2p6[p], cnt_ssp1_rcp4p5[p], facecolor = c, edgecolor = c, label = lab)
    ax[0].fill_between(yr, cnt_ssp1_rcp4p5[p], cnt_ssp1_rcp6p0[p], facecolor = c, edgecolor = c)
    ax[0].fill_between(yr, cnt_ssp1_rcp6p0[p], cnt_ssp1_rcp8p5[p], facecolor = c, edgecolor = c)

def plot_fill_2(p, c, lab):
    ax[1].plot(yr, cnt_ssp2_rcp2p6[p], color = c, linewidth = lw)
    ax[1].plot(yr, cnt_ssp2_rcp4p5[p], color = c, linewidth = lw)
    ax[1].plot(yr, cnt_ssp2_rcp6p0[p], color = c, linewidth = lw)
    ax[1].plot(yr, cnt_ssp2_rcp8p5[p], color = c, linewidth = lw)
    ax[1].fill_between(yr, cnt_ssp2_rcp2p6[p], cnt_ssp2_rcp4p5[p], facecolor = c, edgecolor = c, label = lab)
    ax[1].fill_between(yr, cnt_ssp2_rcp4p5[p], cnt_ssp2_rcp6p0[p], facecolor = c, edgecolor = c)
    ax[1].fill_between(yr, cnt_ssp2_rcp6p0[p], cnt_ssp2_rcp8p5[p], facecolor = c, edgecolor = c)

def plot_fill_3(p, c, lab):
    ax[2].plot(yr, cnt_ssp3_rcp2p6[p], color = c, linewidth = lw)
    ax[2].plot(yr, cnt_ssp3_rcp4p5[p], color = c, linewidth = lw)
    ax[2].plot(yr, cnt_ssp3_rcp6p0[p], color = c, linewidth = lw)
    ax[2].plot(yr, cnt_ssp3_rcp8p5[p], color = c, linewidth = lw)
    ax[2].fill_between(yr, cnt_ssp3_rcp2p6[p], cnt_ssp3_rcp4p5[p], facecolor = c, edgecolor = c, label = lab)
    ax[2].fill_between(yr, cnt_ssp3_rcp4p5[p], cnt_ssp3_rcp6p0[p], facecolor = c, edgecolor = c)
    ax[2].fill_between(yr, cnt_ssp3_rcp6p0[p], cnt_ssp3_rcp8p5[p], facecolor = c, edgecolor = c)


plot_fill_1(1, "#CBE6F3", "Prob. 0.010~0.025")
plot_fill_1(2, "#6EB7DB", "Prob. 0.025~0.050")
plot_fill_1(3, "#007AB7", "Prob. 0.050~1.000")

plot_fill_2(1, "#C6EDDB", "Prob. 0.010~0.025")
plot_fill_2(2, "#64C99B", "Prob. 0.025~0.050")
plot_fill_2(3, "#009250", "Prob. 0.050~1.000")

plot_fill_3(1, "#F9DFD5", "Prob. 0.010~0.025")
plot_fill_3(2, "#EDA184", "Prob. 0.025~0.050")
plot_fill_3(3, "#DA5019", "Prob. 0.050~1.000")

ax[0].set_title("SSP1")
ax[1].set_title("SSP2")
ax[2].set_title("SSP3")

ax[0].legend(fontsize=9, loc="upper right")
ax[1].legend(fontsize=9, loc="upper right")
ax[2].legend(fontsize=9, loc="upper right")

plt.savefig("../../fig/plt/future_prediction.png", dpi=300, bbox_inches="tight")

plt.show()