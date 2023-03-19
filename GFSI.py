import pandas as pd
import numpy as np
from numpy import nan as NA

def import_GFSI(y):
    raw = pd.read_excel('../GFSI/data/'+str(y)+'_SSA.xlsx', skiprows=6, usecols="B:AI", index_col=0).T
    raw['Year'] = y
    return raw.reset_index(names='Area').set_index(['Area','Year'])
  
gfsi = import_GFSI(2012)

for i in range(2013,2023):
  raw = import_GFSI(i)
  gfsi = pd.concat([gfsi,raw]).sort_index()
  
gfsi = gfsi.rename(columns = {'FOOD SECURITY ENVIRONMENT':'fs', '1) AFFORDABILITY':'afford', '2) AVAILABILITY':'avail', '3) QUALITY AND SAFETY':'qual', '4) SUSTAINABILITY AND ADAPTATION':'adapt'})
gfsi.to_csv("../data/gfsi_all.csv")

gfsi = gfsi.iloc[:,[0,1,13,46,65]]
gfsi.to_csv("../data/gfsi_sum.csv")
  
gfsi_r = gfsi.reset_index()[gfsi.reset_index().Area.isin(['Average (mean)','Average (median)','Maximum','Minimum'])]
gfsi_r['Area'] = gfsi_r['Area'].apply(lambda x: 'SSA '+x)
gfsi_r.to_csv("../data/gfsi_r.csv", index=False)

gfsi.reset_index()[~(gfsi.reset_index().Area.isin(['Average (mean)','Average (median)','Maximum','Minimum','Weight']))].to_csv("../data/gfsi_SSA.csv", index=False)



