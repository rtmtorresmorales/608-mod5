#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Project Part 2 7.14.2 Ramon Torres Sept 17 2022


# In[36]:


import pandas as pd


# In[37]:


grades_dict = {'Wally':[87,96,70], 'Eva': [100,87,90], 'Sam' :[94, 77, 90], 'Katie': [100,81,82], 'Bob' : [83,65, 85]}


# In[38]:


grades = pd.DataFrame(grades_dict)


# In[39]:


grades


# In[40]:


print(grades)


# In[41]:


grades.index = ['Test1', 'Test2', 'Test3']


# In[42]:


grades


# In[43]:


print(grades)


# In[44]:


grades['Eva']


# In[45]:


print(grades.Eva)


# In[46]:


grades['Wally']


# In[47]:


print(grades.Wally)


# In[48]:


grades.describe()


# In[49]:


print(grades.describe())


# In[50]:


#"C:\Users\ratorres\Seriesofnumbers.py"pd.set_option("precision", 2)


# In[51]:


pd.set_option("display.precision",2)


# In[52]:


grades.describe()


# In[53]:


print(grades.describe())


# In[54]:


grades.mean()


# In[55]:


print(grades.mean())


# In[56]:


grades.sort_index(ascending=False)


# In[57]:


print(grades.sort_index(ascending=False))


# In[58]:


grades.sort_index(axis=1)


# In[ ]:




