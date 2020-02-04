#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import matplotlib.pyplot as plt
import csv
get_ipython().run_line_magic('matplotlib', 'inline')

pData = []
with open('Price.csv', 'r') as pri:
    pData = list(csv.reader(pri, delimiter='\t'))

pData = np.array(pData, dtype=np.float)

pData = []
with open('Size.csv', 'r') as siz:
    sData = list(csv.reader(siz, delimiter='\t'))
    
sData = np.array(sData, dtype=np.int)

size = []
for i in range(np.shape(sData)[0]):
    if 0.0 < sData[:][i][1]:
        size.append(sData[:][i][1]) 
    
plt.plot(price)
plt.xlabel('Iteration')
plt.ylabel('Price')
plt.savefig('Price.pdf')
plt.show()

plt.plot(size)
plt.xlabel('Iteration')
plt.ylabel('Size')
plt.savefig('Size.pdf')
plt.show()

# fig, (ax1, ax2) = plt.subplots(2)
# ax1.plot(price)
# ax2.plot(size)
# multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
# plt.show()


# In[ ]:




