import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

plt.style.use("/home/ventsi/Work/mpl-supermongo/supermongo.mplstyle")

def norm_plot(x, mu, std, **kwargs):
    """
    Easily plot a normal (Gaussian) distribution with given values.
    Keyword arguments are passed to the plt.fill_between() function.
    """
    y = ss.norm.pdf(x, mu, std)
    
    plt.fill_between(x, 0, y, **kwargs)
    plt.plot(x, y, linestyle="None")

x = np.linspace(-5, 5, 5000)

norm_plot(x, 0, 1, alpha=0.65)
norm_plot(x, -2, 1.5, alpha=0.65)
norm_plot(x, 2, 2.25, alpha=0.65)

plt.xlim(-5, 5)
plt.ylim(0, 0.42)

# Legend:
legend_elements = [Patch(facecolor="tab:orange", alpha=0.65, label=r"$\sigma$ = 1.50 / $\mu$ = -2"), Patch(facecolor="tab:blue", alpha=0.65, label=r"$\sigma$ = 1.00 / $\mu$ = 0"), Patch(facecolor="tab:green", alpha=0.65, label=r"$\sigma$ = 2.25 / $\mu$ = 2")]
plt.legend(handles=legend_elements)

# plt.savefig("gauss.png")
plt.show()
