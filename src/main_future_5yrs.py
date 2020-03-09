import numpy as np
import pandas as pd
import csv

### setting
prj="futr"                                            # project name (4 letters)
ssp = 'ssp3'

### input file
iso = pd.read_csv("../dat/nat/nationCode.csv")
cor = pd.read_csv("../dat/cor/correlation_data.csv")       # data of correlation b/w AWS and VAP
gdp = pd.read_csv("../dat/gdp/gdp_per_cap_" + ssp + ".csv")     # data of GDP per capita
upp = pd.read_csv("../dat/upp/upp_future.csv")                # data of urban population rate

gdp_value = gdp.values
upp_value = upp.values

print(gdp_value.shape)

### main function
def main():
    out = pd.DataFrame(index=cor["ISO3"])
    out2 = pd.DataFrame(index=cor["ISO3"])

    for yr in range(2020, 2051):
        tmp1 = []
        tmp2 = []
        tmp3 = []
        thr_cor = 0.10
        thr_gdp = 700
        thr_upp = 40
        for i in range(len(cor)):
            if cor["cor"][i] >= thr_cor:
                if gdp[str(yr)][i] <= thr_gdp:
                    if upp[str(yr)][i] <= thr_upp:
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
        out.to_csv('../out/'+prj+'__rslt__' + ssp + '.csv')
        out2.to_csv('../out/'+prj+'__rslt__cnt__' + ssp + '.csv')
    print("\n")

main()