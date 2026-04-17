import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import uniform_filter1d  


with open('results/sc2/6h_vs_8z/Code_seq/2026-04-04_08-57-09_Code_seq_sc2_6h_vs_8z.json', 'r') as f:
    data = json.load(f)


x = np.array(data['return_mean_T'])
y = np.array(data['test_battle_won_mean'])


sort_idx = np.argsort(x)
x = x[sort_idx]
y = y[sort_idx]


window_peak = 20  
y_peak = np.maximum.reduceat(y, np.arange(0, len(y), window_peak))
x_peak = x[np.arange(0, len(x), window_peak)]


y_smooth = uniform_filter1d(y_peak, size=5)  


plt.figure(figsize=(10,5))
plt.plot(x_peak, y_smooth, label='battle_won_mean ', color='orange')
# plt.scatter(x, y, s=10, alpha=0.3, label='original', color='gray')
plt.xlabel('Step')
plt.ylabel('Battle Won Mean')
plt.title('6h_vs_8z')
plt.ylim(0, 1) 
plt.legend()
plt.grid(True)
plt.show()