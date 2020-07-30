import pandas as pd
import numpy as np

iso = pd.read_csv("../dat/nat/nationCode.csv")
org = pd.read_csv("../dat/war/war_org.csv")

def trans(nam):
    if nam == "Myanmar (Burma)":
        nam = "Myanmar"
    elif nam == "Hyderabad":
        nam = "India"
    elif nam == "Syria":
        nam = "Syrian Arab Republic"
    elif nam == "Russia (Soviet Union)":
        nam = "Russian Federation"
    elif nam == "Iran":
        nam = "Iran, Islamic Republic Of"
    elif nam == "Cambodia (Kampuchea)":
        nam = "Cambodia"
    elif nam == "Yemen (North Yemen)" or nam == "South Yemen":
        nam = "Yemen"
    elif nam == "Vietnam (North Vietnam)" or nam == "South Vietnam":
        nam = "Viet Nam"
    elif nam == "Laos":
        nam = "Lao People's Democratic Republic"
    elif nam == "North Korea":
        nam = "Korea, Democratic People's Republic Of"
    elif nam == "South Korea":
        nam = "Korea, Republic Of"
    elif nam == "Zimbabwe (Rhodesia)":
        nam = "Zimbabwe"
    elif nam == "Serbia (Yugoslavia)":
        nam = "Serbia"
    elif nam == "Tanzania":
        nam = "Tanzania, United Republic Of"
    elif nam == "Madagascar (Malagasy)":
        nam = "Madagascar"
    elif nam == "Moldova":
        nam = "Moldova, Republic Of"
    elif nam == "DR Congo (Zaire)":
        nam = "Congo, The Democratic Republic Of The"
    elif nam == "Bosnia-Herzegovina":
        nam = "Bosnia and Herzegovina"
    elif nam == "Ivory Coast":
        nam = "Cote D'Ivoire"

    return nam

def main():
    dic = {}
    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1960,2020), data=0)

    print(out)
    for j in range(len(org)):
        name = org["location"][j]
        namelist = name.split(", ")
        #print(namelist)
        for nam in namelist:
            flag = False
            nam = trans(nam)
            for i in range(len(iso)): 
                if iso["Country"][i] == nam:
                    if org["year"][j] < 1960:
                        continue
                    #print(iso["ISO3"][i], org["year"][j])
                    out.at[iso["ISO3"][i], org["year"][j]] = 1
                    flag = True
            if not flag:
                print(nam, org["year"][j])
                dic[nam] = 1
    out.to_csv("../dat/war/war.csv")
    print(dic)


# def war_bool():
#     inp = pd.read_csv("../dat/war/war.csv", index_col = "ISO3")
#     out = pd.DataFrame(index=iso["ISO3"])
#     for i in range(len(inp)):
#         for y in inp.columns:
#             if inp.at[iso["ISO3"][i], str(y)] > 0:
#                 out.at[iso["ISO3"][i], str(y)] = 1
#             else:
#                 out.at[iso["ISO3"][i], str(y)] = 0
#     out.to_csv("../dat/war/war_bool.csv")

def war_ma():
    inp = pd.read_csv("../dat/war/war.csv", index_col = "ISO3")
    out = pd.DataFrame(index=iso["ISO3"])
    for i in range(len(inp)):
        cnt = iso["ISO3"][i]
        for y in inp.columns:
            y = int(y)
            if 1961 < y and y < 2018:
                out.at[cnt, str(y)] = (inp.at[cnt, str(y-2)]*1 + inp.at[cnt, str(y-1)]*2 + inp.at[cnt, str(y)]*3 + inp.at[cnt, str(y+1)]*2 + inp.at[cnt, str(y+2)]*1) / 9
            elif y == 1961:
                out.at[cnt, str(y)] = (inp.at[cnt, str(y-1)]*2 + inp.at[cnt, str(y)]*3 + inp.at[cnt, str(y+1)]*2 + inp.at[cnt, str(y+2)]*1) / 8
            elif y == 2018:
                out.at[cnt, str(y)] = (inp.at[cnt, str(y-2)]*1 + inp.at[cnt, str(y-1)]*2 + inp.at[cnt, str(y)]*3+ inp.at[cnt, str(y+1)]*2) / 8
            elif y == 1960:
                out.at[cnt, str(y)] = (inp.at[cnt, str(y)]*3 + inp.at[cnt, str(y+1)]*2 + inp.at[cnt, str(y+2)]*1) / 6
            elif y == 2019:
                out.at[cnt, str(y)] = (inp.at[cnt, str(y-2)]*1 + inp.at[cnt, str(y-1)]*2 + inp.at[cnt, str(y)]*3) / 6
    print(out)
    out.to_csv("../dat/war/war_wma.csv")

#main()
#war_ma()


def prep_war_5yrs(): # average of 5 years
    war = pd.read_csv("../dat/war/war.csv")
    out_sum = pd.DataFrame(index=iso["ISO3"])
    out_max = pd.DataFrame(index=iso["ISO3"])
    for i in range(len(war)):
        for y in range(1961, 2016, 5):
            print(i, y)
            tmp = war.loc[i, str(y):str(y+4)]
            out_sum.loc[iso["ISO3"][i], str(y)] = tmp.sum()
            out_max.loc[iso["ISO3"][i], str(y)] = tmp.max()
    out_sum.to_csv("../dat/war/war_5yrs_sum.csv")
    out_max.to_csv("../dat/war/war_5yrs_max.csv")

#prep_war_5yrs()

def prep_war_prob():
    inp = pd.read_csv("../dat/war/war.csv", index_col = "ISO3")
    out = pd.DataFrame(index=iso["ISO3"])
    n = len(inp.columns)
    tmp = []
    for i in range(len(inp)):
        tmp.append(inp.sum(axis=1)[i]/n)
    out["prob"] = tmp
    print(out)
    out.to_csv("../dat/war/war_prob.csv")

prep_war_prob()