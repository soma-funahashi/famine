import numpy as np
import scipy.stats
import pandas as pd

gdp = pd.read_csv("../dat/fpi/gdp_per_cap_fpi.csv", index_col="ISO3")
upp = pd.read_csv("../dat/upp/upp_new_filled.csv", index_col="ISO3")
cor = pd.read_csv("../dat/cor/correlation_data.csv", index_col="ISO3")
gin = pd.read_csv("../dat/gin/gini_coeff_ave.csv", index_col="ISO3")
sow = pd.read_csv("../dat/sow/soilmois_cropland_kg.csv", index_col="ISO3")

gin = gin.fillna(gin.mean())
sow = sow.fillna(sow.mean())

gdp_st = pd.DataFrame(scipy.stats.zscore(gdp, axis = 1), index=gdp.index, columns=gdp.columns)
upp_st = pd.DataFrame(scipy.stats.zscore(upp, axis = 1), index=upp.index, columns=upp.columns)
cor_st = pd.DataFrame(scipy.stats.zscore(cor, axis = 1), index=cor.index, columns=cor.columns)
gin_st = pd.DataFrame(scipy.stats.zscore(gin, axis = 1), index=gin.index, columns=gin.columns)
sow_st = pd.DataFrame(scipy.stats.zscore(sow, axis = 1), index=sow.index, columns=sow.columns)

print(sow_st)

gdp_st.to_csv("../dat/fpi/gdp_per_cap_fpi_st.csv")
upp_st.to_csv("../dat/upp/upp_new_filled_st.csv")
cor_st.to_csv("../dat/cor/correlation_data_st.csv")
gin_st.to_csv("../dat/gin/gini_coeff_ave_st.csv")
sow_st.to_csv("../dat/sow/soilmois_cropland_kg_st.csv")