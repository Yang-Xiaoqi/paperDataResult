import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.ndimage import uniform_filter1d

with open('results/sc2/6h_vs_8z/Code_seq/2026-04-04_08-57-09_Code_seq_sc2_6h_vs_8z.json', 'r') as f:
    data = json.load(f)

x = np.array(data['return_mean_T'])
y = np.array(data['battle_won_mean'])


sort_idx = np.argsort(x)
x = x[sort_idx]
y = y[sort_idx]


x_smooth = np.linspace(x.min(), x.max(), 1000)  
spl = make_interp_spline(x, y, k=3)  
y_smooth = spl(x_smooth)


plt.figure(figsize=(10,5))
plt.plot(x_smooth, y_smooth, label='battle_won_mean')
# plt.scatter(x, y, s=10, color='gray', alpha=0.3, label='original points')  # 原始点可选显示
plt.xlabel('Step')
plt.ylabel('Battle Won Mean')
plt.title('6h_vs_8z')
plt.ylim(0, 1)  
plt.legend()
plt.grid(True)
plt.show()
