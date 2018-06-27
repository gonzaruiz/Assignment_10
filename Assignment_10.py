
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv")

print (df.loc[:, ~df.columns.str.contains('^Unnamed')]) # sacando columna sin nombre

df['Gender'].value_counts().plot(kind='bar') #distribucion de genero
plt.show()

print( df.groupby('Name')[['Count']].agg('sum').sort_values("Count", ascending=False).head(5)) # top 5 nombres

print (df[df.Count==df.median()['Count']]) # meidana

df.groupby(['State','Gender'])[['Count']].agg('sum').plot(kind='bar') #distribucion por genero por estado
plt.show()

