#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np  
from matplotlib import pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


mean_01=np.asarray([0.,2.])
sigma_01=np.asarray([[1.0,0.0],[0.0,1.0]])
print (mean_01)
print (sigma_01)
mean_02=np.asarray([4.,0.])
sigma_02=np.asarray([[1.0,0.0],[0.0,1.0]])
data_1=np.random.multivariate_normal(mean_01,sigma_01,500)
data_2=np.random.multivariate_normal(mean_02,sigma_02,500)##this function generates a normal distribution
print(data_1.shape,data_2.shape)


# In[38]:


plt.figure(0)
plt.xlim(-7,7)
plt.ylim(-7,7)
plt.grid('on')
plt.scatter(data_1[:,0],data_1[:,1],color="red")
plt.scatter(data_2[:,0],data_2[:,1],color="green")

plt.show()


# In[37]:


labels=np.zeros((1000,1))  ##making a matrix containing 1000 rows and 1 column and which contains 0
labels[500:,:]=1.0 ##making last 500rows 0


# In[42]:


data=np.concatenate([data_1,data_2],axis=0) ##to concatenate along first dimension
print (data.shape)


# In[51]:


im = list(range(1000))
np.random.shuffle(im)
print (im[:10])


# In[57]:


data=data[im]
labels=labels[im]
print (data.shape,labels.shape)


# In[ ]:




