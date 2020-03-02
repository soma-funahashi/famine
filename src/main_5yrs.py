import numpy as np
import pandas as pd
import csv

### setting
prj="dflt"                                            # project name (4 letters)
yrs=np.arange(1961,2016)                              # year

### input file
iso = pd.read_csv("../dat/nat/nationCode.csv")
cor = pd.read_csv("../dat/cor/correlation_data.csv")       # data of correlation b/w AWS and VAP
gdp = pd.read_csv("../dat/gdp/gdp_per_cap_filled.csv")     # data of GDP per capita
#gdp = pd.read_csv("../dat/gdp/imported_value_per_cap.csv")     # data of GDP per capita
upp = pd.read_csv("../dat/upp/upp_new_filled.csv")                # data of urban population rate

gdp_value = gdp.values
upp_value = upp.values

print(gdp_value.shape)

### main function
def main():
    out = pd.DataFrame(index=cor["ISO3"])
    out2 = pd.DataFrame(index=cor["ISO3"])

    for k in range((2016 - 1961) // 5):
        tmp1 = []
        tmp2 = []
        tmp3 = []
        thr_cor = 0.10
        thr_gdp = 700
        thr_upp = 40
        yr = 1961 + k * 5
        for i in range(len(cor)):
            gdp_ave = np.mean(gdp_value[i][5*k+2 : 5*k+7])
            upp_ave = np.mean(upp_value[i][5*k+1 : 5*k+6])
            if cor["cor"][i] >= thr_cor:
                if gdp_ave <= thr_gdp:
                    if upp_ave <= thr_upp:
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

        print(yr, np.count_nonzero(np.array(tmp1) == 3), tmp3)
        out[str(yr)]=tmp1
        out2[str(yr)]=tmp2
        out.to_csv('../out/'+prj+'__rslt__5yrs.csv')
        out2.to_csv('../out/'+prj+'__rslt__5yrs__cnt.csv')
    print("\n")

main()


# validation
def validation():
    rsl = pd.read_csv('../out/'+prj+'__rslt__5yrs.csv')
    fam = pd.read_csv('../dat/fam/famineData_drought.csv')
    fam_value = fam.values
    for i in range(len(rsl)):
        for y in range(1961, 2016, 5):
            famnum = np.sum(fam_value[i][(y-1961)*5+1:(y-1961)*5+6])
            if rsl[str(y)][i] != 3 and famnum > 0:
                print(y, rsl["ISO3"][i], rsl[str(y)][i], round(cor["cor"][i], 2), round(gdp[str(y)][i], 2), round(upp[str(y)][i], 2))

#validation()


def count():
#   df_obs = pd.read_csv("../dat/fam/famineData.csv")
    df_sim = pd.read_csv("../out/"+prj+"__rslt__5yrs.csv")
    fam = pd.read_csv('../dat/fam/famineData_drought.csv')
    fam_value = fam.values
    cnt_os_11 = 0
    cnt_os_10 = 0
    cnt_os_01 = 0
    cnt_os_00 = 0

    def check(y,rsl):
        return y, rsl["ISO3"][i], rsl[str(y)][i], round(cor["cor"][i], 2), round(gdp[str(y)][i], 2), round(upp[str(y)][i], 2)

    for i in range(len(df_sim)):
        for y in range(1961,2016,5):
            famnum = np.sum(fam_value[i][(y-1961)+1:(y-1961)+6])
            if famnum >= 1 and df_sim[str(y)][i] == 3:
                cnt_os_11 += 1
                #print(fam["ISO3"][i], y)
            elif famnum >= 1 and df_sim[str(y)][i] <= 2:
                cnt_os_10 += 1
                print(check(y,df_sim))
            elif famnum == 0 and df_sim[str(y)][i] == 3:
                cnt_os_01 += 1
            else:
                cnt_os_00 += 1

    print("")
    print("both     :", cnt_os_11)
    print("only obs :", cnt_os_10)
    print("only sim :", cnt_os_01)
    print("neither  :", cnt_os_00)
    print("accuracy     =", (cnt_os_11 + cnt_os_00) / (cnt_os_11 + cnt_os_10 + cnt_os_01 + cnt_os_00) * 100)
    print("threat score =", cnt_os_11 / (cnt_os_11 + cnt_os_10 + cnt_os_01) * 100)
    #df_dif.to_csv("../out/validationResult.csv")

#count()