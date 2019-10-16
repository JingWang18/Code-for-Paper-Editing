# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:41:22 2019

@author: wang0918.stu
"""

import matplotlib.pyplot as plt

x_axis = ['0', '1e-4', '1e-3', '0.01', '0.1', '1', '10' ,'100']
y_axis = [94.2, 96.4, 96.5, 96.6, 97.5, 97.1, 97, 97.1]

plt.figure(figsize=(24, 6))

plt.subplot(133)
plt.xlabel('Value of $\lambda$')
plt.ylabel('Accuracy')
plt.title('KFEMCD from MNIST to USPS')

plt.plot(x_axis, y_axis)
plt.savefig(r'C:\Users\wang0918.stu\Desktop\ab_KFEMCD.png')
#%%