from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap


fig, axes = plt.subplots(10, 10, 
                        figsize=(8, 8), 
                        subplot_kw={"xticks":[], "yticks":[]},
                        gridspec_kw={"hspace":0.1, "wspace": 0.1}
                        )

digits = load_digits()

for i, ax in enumerate(axes.flat): 
    ax.imshow(digits.images[i], cmap="binary")
    ax.text(0.05, 0.05, str(digits.target[i]), transform=ax.transAxes, color="green")

X = digits.data
y = digits.target

model_iso = Isomap(n_components = 2)
model_iso.fit(X)
X_iso = model_iso.transform(X)

plt.figure()
plt.scatter(X_iso[:, 0], X_iso[:, 1], c=y, cmap=plt.cm.get_cmap("Spectral", 10))
plt.colorbar(ticks=range(10))
plt.show()
input()




