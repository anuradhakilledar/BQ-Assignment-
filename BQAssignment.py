#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import csv
df=pd.read_excel("C:\\Users\\home\\Documents\\BQ-Assignment.xlsx",header=0)
df
df.columns=['Item_type','Item','Item_Sort_Order','Date','Sales']
str1='Fruit'
df=df.loc[df.Item_type==str1]
df['Date']=df['Date'].dt.strftime('%b %y')
df.pivot_table(df,index=["Item","Item_Sort_Order"],columns=["Date"],aggfunc=sum).sort_values(by="Item_Sort_Order",ascending=True)


# In[ ]:




