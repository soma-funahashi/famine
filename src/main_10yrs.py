import numpy as np
import pandas as pd
import csv

### setting
prj="gini"                                            # project name (4 letters)
yrs=np.arange(1960,2019)                              # year (1960 - 2018)

### input file
iso = pd.read_csv("../dat/nat/nationCode.csv")
cor = pd.read_csv("../dat/cor/correlation_data.csv")       # data of correlation b/w AWS and VAP
gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv")        # data of GDP per capita
upp = pd.read_csv("../dat/upp/upp_new_filled.csv")         # data of urban population rate
sow = pd.read_csv("../dat/sow/soilmois_cropland.csv")
gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv")
#sow = pd.read_csv("../dat/sow/drought_flag_15.csv")

gdp_value = gdp.values
upp_value = upp.values
sow_value = sow.values

gin = gin.fillna(gin.mean())

#print(gin)

### main function
def main():
    out = pd.DataFrame(index=cor["ISO3"])
    out2 = pd.DataFrame(index=cor["ISO3"])

    for k in range((2019 - 1960) // 10 + 1):
        tmp1 = []
        tmp2 = []
        tmp3 = []
        yr = 1960 + k * 10
        for i in range(len(cor)):
            thr_cor = 0.15
            thr_gdp = 550
            thr_upp = 35
#           thr_sow = 30
            thr_gin = 30

            gdp_ave = np.min(gdp_value[i][10*k+1 : 10*k+11])
            upp_ave = np.min(upp_value[i][10*k+1 : 10*k+11])
#           sow_ave = np.min(sow_value[i][10*k+1 : 10*k+11])

#            if sow_ave < thr_sow:
            if cor["cor"][i] >= thr_cor:
                if gdp_ave <= thr_gdp:
                    if gin["gin"][i] >= thr_gin:
                        tmp1.append(3)
                        tmp2.append(1)
                        tmp3.append(iso["ISO3"][i])
                    else:
                        tmp1.append(2)
                        tmp2.append(0)
                else:
                    tmp1.append(1)
                    tmp2.append(0)
            else:
                tmp1.append(0)
                tmp2.append(0)
            # else:
            #     tmp1.append(-1)
            #     tmp2.append(0)

        print(yr, np.count_nonzero(np.array(tmp1) == 3), tmp3)
        out[str(yr)]=tmp1
        out2[str(yr)]=tmp2
        out.to_csv('../out/'+prj+'__rslt__10yrs.csv')
        out2.to_csv('../out/'+prj+'__rslt__10yrs__cnt.csv')
    print("\n")

main()


# validation
def validation():
    rsl = pd.read_csv('../out/'+prj+'__rslt__10yrs.csv')
    fam = pd.read_csv('../dat/fam/famineData_drought.csv')
    fam_value = fam.values
    for i in range(len(rsl)):
        for y in range(1960, 2019, 10):
            famnum = np.sum(fam_value[i][(y-1960)*10+1:(y-1960)*10+11])
            if rsl[str(y)][i] != 3 and famnum > 0:
                print(y, rsl["ISO3"][i], rsl[str(y)][i], round(cor["cor"][i], 2), round(gdp[str(y)][i], 2), round(upp[str(y)][i], 2))

validation()


def count():
#   df_obs = pd.read_csv("../dat/fam/famineData.csv")
    df_sim = pd.read_csv("../out/"+prj+"__rslt__10yrs.csv")
    fam = pd.read_csv('../dat/fam/famineData_drought.csv')
    fam_value = fam.values

    drt = sow
    drt_value = drt.values

    cnt_os_11 = 0
    cnt_os_10 = 0
    cnt_os_01 = 0
    cnt_os_00 = 0

    cnt_os_11_d = 0
    cnt_os_10_d = 0
    cnt_os_01_d = 0
    cnt_os_00_d = 0

    thr_drt = 20

    def check(y,rsl):
        return y, rsl["ISO3"][i], rsl[str(y)][i], round(cor["cor"][i], 2), round(gdp[str(y)][i], 2), round(upp[str(y)][i], 2)

    for i in range(len(df_sim)):
        for y in range(1960,2018,10):
            famnum = np.sum(fam_value[i][(y-1960)+1:(y-1960)+11])
            drtnum = np.min(drt_value[i][(y-1960)+1:(y-1960)+11])
            if famnum >= 1 and df_sim[str(y)][i] == 3:
                cnt_os_11 += 1
                if drtnum < thr_drt:
                    cnt_os_11_d += 1
            elif famnum >= 1 and df_sim[str(y)][i] <= 2:
                cnt_os_10 += 1
                print("only obs :", check(y, df_sim))
                if drtnum < thr_drt:
                    cnt_os_10_d += 1
            elif famnum == 0 and df_sim[str(y)][i] == 3:
                cnt_os_01 += 1
                if drtnum < thr_drt:
                    cnt_os_01_d += 1
            else:
                cnt_os_00 += 1
                if drtnum < thr_drt:
                    cnt_os_00_d += 1

    recall = cnt_os_11 / (cnt_os_11 + cnt_os_01)
    precision = cnt_os_11 / (cnt_os_11 + cnt_os_10)

    print("")
    print("both     :", cnt_os_11, "(" + str(cnt_os_11_d) + ")")
    print("only obs :", cnt_os_10, "(" + str(cnt_os_10_d) + ")")
    print("only sim :", cnt_os_01, "(" + str(cnt_os_01_d) + ")")
    print("neither  :", cnt_os_00, "(" + str(cnt_os_00_d) + ")")
    print("accuracy     =", (cnt_os_11 + cnt_os_00) / (cnt_os_11 + cnt_os_10 + cnt_os_01 + cnt_os_00) * 100)
    print("threat score =", cnt_os_11 / (cnt_os_11 + cnt_os_10 + cnt_os_01) * 100)
    print("recall       =", recall)
    print("precision    =", precision)
    print("F value      =", 2 * precision * recall / (precision + recall))
    #df_dif.to_csv("../out/validationResult.csv")

count()