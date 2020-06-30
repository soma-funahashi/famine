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
    out = pd.DataFrame(index=iso["ISO3"], columns=np.arange(1940,2020), data=0)

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
                    #print(iso["ISO3"][i], org["year"][j])
                    out.at[iso["ISO3"][i], org["year"][j]] += 1
                    flag = True
            if not flag:
                print(nam, org["year"][j])
                dic[nam] = 1
    out.to_csv("../dat/war/war.csv")
    print(dic)


def war_bool():
    inp = pd.read_csv("../dat/war/war.csv", index_col = "ISO3")
    out = pd.DataFrame(index=iso["ISO3"])
    for i in range(len(inp)):
        for y in inp.columns:
            if inp.at[iso["ISO3"][i], str(y)] > 0:
                out.at[iso["ISO3"][i], str(y)] = 1
            else:
                out.at[iso["ISO3"][i], str(y)] = 0
    out.to_csv("../dat/war/war_bool.csv")

war_bool()
