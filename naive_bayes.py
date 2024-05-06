from sklearn.dataseats import make_blobs
from sklearn.naive

X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)


model = GaussianNB()
model.fit(X,y)

plt.scatter(X[:,0], X[:,1], c=y, s=50, cmap='RdBu')
plt.scatter(Xnew[:0])

rng = np.random.RandomState(0)
Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
ynew = model.predict(Xnew)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=20,
cmap='RdBu', alpha=0.1)
plt.show()

plt.show()