import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, ax = plt.subplots(1,1)
mu,sg = 0,1
def draw_lognorm():
    X = stats.norm(loc=mu, scale=sg)
    Y = stats.lognorm( s=sg,scale=np.exp(mu))
    y = Y.rvs(size=10000)
    x = np.linspace(*X.interval(0.999))
    ax.plot(x, X.pdf(x), label='X (pdf)')
    ax.hist(np.log(y), density=True, bins=x, label='(Y) histogram')
    ax.legend()
    plt.show()

draw_lognorm()
