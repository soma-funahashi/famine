import numpy as np
import pandas as pd
import csv

iso = pd.read_csv("../dat/nat/nationCode.csv")
cor = pd.read_csv("../dat/cor/correlation_data.csv")  
gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv")
upp = pd.read_csv("../dat/upp/upp_new_filled.csv") 

### setting
prj="dflt"                                            # project name (4 letters)
yrs=np.arange(1961,2019)                              # year

### main function
def main():
    cnt=iso["ISO3"]
    out=pd.DataFrame(index=gdp["ISO3"])

    thr_cor = 0.1
    thr_gdp = 750
    thr_upp = 50
    
    for k in range(len(yrs)):
        tmp1 = []
        tmp2 = []
        yr   = yrs[k]
        for i in range(len(cor)):
            if cor["cor"][i] >= thr_cor:
                if gdp[str(yr)][i] < thr_gdp:
                    if float(upp[str(yr)][i]) < thr_upp:
                        tmp1.append(3)
                        tmp2.append(cnt[i])
                    else:
                        tmp1.append(2)
                else:
                    tmp1.append(1)
            else:
                tmp1.append(0)
        print(yr, np.count_nonzero(np.array(tmp1)==3), tmp2)
        out[str(yr)]=tmp1

        out.to_csv('../out/'+prj+'____rslt.csv')

main()


# validation
def validation():
    rsl = pd.read_csv('../out/'+prj+'____rslt.csv')
    fam = pd.read_csv('../dat/fam/famineDataNumberRate.csv')
#   fam = pd.read_csv('../dat/fam/famineDataNumberRate_drought.csv')
    for i in range(len(rsl)):
        for y in range(1961, 2018):
            if rsl.iloc[i][y-1960] != 3 and float(fam.iloc[i][y-1960]) > 0:
                print(y, rsl["ISO3"][i], rsl.iloc[i][y-1960], round(cor["cor"][i],2), round(gdp.iloc[i][y-1960],2), round(upp[str(y)][i],2))

validation()


def count():
    df_obs = pd.read_csv("../dat/fam/famineData.csv")
#   df_obs = pd.read_csv("../dat/fam/famineData_drought.csv")
    df_sim = pd.read_csv("../out/"+prj+"____rslt.csv")
    cnt_os_11 = 0
    cnt_os_10 = 0
    cnt_os_01 = 0
    cnt_os_00 = 0

    def check(y,rsl):
        return y, rsl["ISO3"][i], rsl.iloc[i][y-1960], round(cor["cor"][i],2), round(gdp.iloc[i][y-1960],2), round(upp.iloc[i][y-1960],2)

    for y in range(1961,2019):
        for i in range(len(df_obs)):
            if df_obs[str(y)][i] == 1 and df_sim[str(y)][i] == 3:
                cnt_os_11 += 1
            elif df_obs[str(y)][i] == 1 and df_sim[str(y)][i] <= 2:
                cnt_os_10 += 1
                print(check(y,df_sim))
            elif df_obs[str(y)][i] == 0 and df_sim[str(y)][i] == 3:
                cnt_os_01 += 1
            else:
                cnt_os_00 += 1

    recall = cnt_os_11 / (cnt_os_11 + cnt_os_01)
    precision = cnt_os_11 / (cnt_os_11 + cnt_os_10)

    print("both     :", cnt_os_11)
    print("only obs :", cnt_os_10)
    print("only sim :", cnt_os_01)
    print("neither  :", cnt_os_00)
    print("accuracy =", (cnt_os_11 + cnt_os_00) / (cnt_os_11 + cnt_os_10 + cnt_os_01 + cnt_os_00))

    print("precision    =", precision)
    print("F value      =", 2 * precision * recall / (precision + recall))

    #print("threat score  =", cnt_os_11 / (cnt_os_11 + cnt_os_10 + cnt_os_01))
    #df_dif.to_csv("../out/validationResult.csv")

count()