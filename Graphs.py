import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------------------------------------
# 1.  data
mu, sigma = 0, 1
x = np.linspace(-3, 3, 400)
y = norm.pdf(x, loc=mu, scale=sigma)

# -------------------------------------------------
# 2.  figure / axes
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, color='red', lw=2, label=r'$H_0$ distribution')
ax.set_title(r'distribution graph')
#ax.set_xticks([0, 0.3, 0.5, 0.7, 0.8, 1])
#ax.set_xticklabels(['0', 'lo', '0.5', 'hi', 'T', '1'])
ax.set_ylim(0, None)
fig.tight_layout()

plt.show()