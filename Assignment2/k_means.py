import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

data = np.array([[2, 4], [1.7, 2.8], [7, 8], [8.6, 8], [3.4, 1.5], [9, 11]])
plt.scatter(data[:, 0], data[:, 1], s=150)
# plt.show()

# number of clusters
numcluster = 2


def initial_centroids(numcluster, data):
    centroid_min = data.min()
    centroid_max = data.max()
    centroids = []
    for centroid in range(numcluster):
        centroid = np.random.uniform(centroid_min, centroid_max, 2)
        centroids.append(centroid)
    centroids = np.array(centroids)

    return centroids


centroids = initial_centroids(numcluster, data)


def euclidean(a, b):
    distance = np.linalg.norm(a - b)
    return distance
