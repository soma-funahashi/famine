import numpy as np
import pandas as pd
import csv

### setting
prj="drgt"                                            # project name (4 letters)
yrs=np.arange(1961,2019)                              # year

### input file
iso = pd.read_csv("../dat/nat/nationCode.csv")
df1 = pd.read_csv("../dat/cor/correlation_data.csv")       # data of correlation b/w AWI and AP
df2 = pd.read_csv("../dat/gdp/gdp_per_cap.csv")            # data of GDP per capita
df3 = pd.read_csv("../dat/upp/upp_new.csv")                # data of urban population rate

### main function
def main():
    cnt=iso["ISO3"]
    out=pd.DataFrame(index=df1["ISO3"])

    with open("../out/"+prj+"____name.csv", "w") as f:
        writer=csv.writer(f)

        for k in range(len(yrs)):
            tmp1 = []
            tmp2 = []
            yr   = yrs[k]
            avl  = df2.mean()

            for i in range(len(df1)):
                if df1["cor"][i] >= 0.10:
                    if df2[str(yr)][i] < avl[yr-1961]:
                        if df3[str(yr)][i] <= 30:
                            tmp1.append(3)
                            tmp2.append(cnt[i])
                        else:
                            tmp1.append(2)
                    else:
                        tmp1.append(1)
                else:
                    tmp1.append(0)
            print(yr, np.count_nonzero(np.array(tmp1)==3), tmp2)
            w = [yr] + [np.count_nonzero(np.array(tmp1)==3)] + tmp2
            writer.writerow(w)
            out[str(yr)]=tmp1

        out.to_csv('../out/'+prj+'____rslt.csv')

main()


# validation
def validation():
    rsl = pd.read_csv('../out/'+prj+'____rslt.csv')
#   fam = pd.read_csv('../dat/fam/famineDataNumberRate.csv')
    fam = pd.read_csv('../dat/fam/famineDataNumberRate_drought.csv')
    for i in range(len(rsl)):
        for y in range(1961, 2018):
            if rsl.iloc[i][y-1960] != 3 and float(fam.iloc[i][y-1960]) > 0:
                print(y, rsl["ISO3"][i], rsl.iloc[i][y-1960], round(df1["cor"][i],2), round(df2.iloc[i][y-1960],2), round(df3.iloc[i][y-1960],2))

validation()


def count():
#   df_obs = pd.read_csv("../dat/fam/famineData.csv")
    df_obs = pd.read_csv("../dat/fam/famineData_drought.csv")
    df_sim = pd.read_csv("../out/"+prj+"____rslt.csv")
    cnt_os_11 = 0
    cnt_os_10 = 0
    cnt_os_01 = 0
    cnt_os_00 = 0

    def check(y,rsl):
        return y, rsl["ISO3"][i], rsl.iloc[i][y-1960], round(df1["cor"][i],2), round(df2.iloc[i][y-1960],2), round(df3.iloc[i][y-1960],2)

    for y in range(1961,2019):
        for i in range(len(df_obs)):
            if df_obs[str(y)][i] == 1 and df_sim[str(y)][i] == 3:
                cnt_os_11 += 1
            elif df_obs[str(y)][i] == 1 and df_sim[str(y)][i] == 0:
                cnt_os_10 += 1
                print(check(y,df_sim))
            elif df_obs[str(y)][i] == 0 and df_sim[str(y)][i] == 3:
                cnt_os_01 += 1
            else:
                cnt_os_00 += 1
    print("both     :", cnt_os_11)
    print("only obs :", cnt_os_10)
    print("only sim :", cnt_os_01)
    print("neither  :", cnt_os_00)
    print("accuracy =", (cnt_os_11 + cnt_os_00) / (cnt_os_11 + cnt_os_10 + cnt_os_01 + cnt_os_00))
    #print("threat score  =", cnt_os_11 / (cnt_os_11 + cnt_os_10 + cnt_os_01))
    #df_dif.to_csv("../out/validationResult.csv")

count()