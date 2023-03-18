#%%
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["HDFC", "SBI", "IDFC", "AXIS"]
myexplode = [0.2, 0.5, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.legend(title ="This is the title")
plt.show() 
# %%
