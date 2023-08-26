#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


import pandas as pd

file_path = "C:\\Users\\Vijay\\OneDrive\\Desktop\\Nanda\\several csv files\\Diwali Sales Data.csv"
try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Specify the encoding
except UnicodeDecodeError:
    print("Error: Unable to read the file due to encoding issues.")


# In[4]:


df.shape


# In[5]:


df.sample(10)


# In[6]:


df.info()


# In[7]:


#droping unwanted columns

df.drop(["Status","unnamed1"], axis=1, inplace = True)


# In[8]:


df


# In[9]:


df.info()


# In[10]:


pd.isnull(df)


# In[11]:


pd.isnull(df).sum()


# In[12]:


df.shape


# In[13]:


df.dropna(inplace = True)


# In[14]:


pd.isnull(df).sum()


# In[15]:


df["Amount"] = df["Amount"].astype("int")


# In[16]:


df.columns


# # EDA

# In[17]:


ax = sns.countplot(x = "Gender" , data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(by="Amount",ascending = False)


# In[19]:


sales_gender = df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(by="Amount",ascending = False)

sns.barplot(x = "Gender",y = "Amount", data =sales_gender )


# # AGE

# In[20]:


df.columns


# In[25]:


ax = sns.countplot(data = df,x = 'Age Group',hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[27]:


sales_age = df.groupby(['Age Group'],as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending=False)
sns.barplot(x = 'Age Group',y = "Amount", data = sales_age )


# From above graphs we can see that most of the buyers are of age group b/w 25-35 years Female

# # State

# In[36]:


sales_state = df.groupby(["State"],as_index = False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(10)


sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data = sales_state, x = "State",y="Orders" )


# In[35]:


sales_state = df.groupby(["State"],as_index = False)["Amount"].sum().sort_values(by = "Amount",ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state,x ="State",y="Amount" )


# from above graph we can see that most of the orders & total sales/amount are from uttar pradesh,Maharashtra and Karnataka.

# # Marital Status

# In[39]:


ax = sns.countplot(data =df,x= "Marital_Status")

sns.set(rc={'figure.figsize':(10,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[50]:


sales_marital_status = df.groupby(["Marital_Status","Gender"],as_index=False)["Amount"].sum().sort_values(by = "Amount",ascending =False)

sns.set(rc={"figure.figsize":(7,5)})
sns.barplot(data =sales_marital_status,x="Marital_Status",y="Amount",hue = "Gender")


# From above graphs we can see that most of the buyers are married(women)

# # Occupation 

# In[49]:


ax = sns.countplot(data = df,x = "Occupation")

sns.set(rc={"figure.figsize":(25,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


sales_Occupation = df.groupby(["Occupation"],as_index =False)["Amount"].sum().sort_values(by ="Amount",ascending =False)

sns.set(rc={"figure.figsize":(20,5)})

sns.barplot(data = sales_Occupation,x="Occupation",y="Amount")


# From above graph we can see that most of the buyers are working in IT,Healthcare and Aviation sectors

# In[56]:


df.columns


# # Product category 

# In[75]:


ax = sns.countplot(data = df,x ="Product_Category")

sns.set(rc = {"figure.figsize":(10,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[82]:


sales_Product_category = df.groupby(["Product_Category"],as_index =False)["Amount"].sum().sort_values(by ="Amount",ascending =False).head(10)

sns.set(rc={"figure.figsize":(25,5)})
sns.barplot(data =sales_Product_category,x = "Product_Category",y="Amount" )


# from above graph we can see that most of the sold products are food,Clothing and Electronics.

# In[84]:


sales_product = df.groupby(["Product_ID"],as_index = False)["Orders"].sum().sort_values(by = "Orders",ascending = False).head(10)

sns.set(rc={"figure.figsize":(15,5)})

sns.barplot(data =sales_product,x = "Product_ID",y="Orders" )


# In[87]:


fig1,ax1 = plt.subplots(figsize=(12,7))
df.groupby("Product_ID")["Orders"].sum().nlargest(10).sort_values(ascending =False).plot(kind="bar")


# # Conclusion:

# Married women age group 26-35 years from UP,Maharashtra,Karnataka working in IT,Healthcare,Aviation are more likely to buy products from Food,Clothing and Electronics category.
# 
# Most selling product ID = P00265242

# In[ ]:




