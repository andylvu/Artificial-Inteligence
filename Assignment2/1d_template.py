import numpy as np


def euclidean_distance(a, b):
    # Euclidean distance (l2 norm)
    # 1-d scenario: absolute value
    return abs(a - b)


# Step 1
def closestCentroid(x, centroids):
    assignments = []
    for i in x:
        # distance between one data point and centroids
        distance = []
        for j in centroids:
            distance.append(euclidean_distance(i, j))
            # assign each data point to the cluster with closest centroid
        assignments.append(np.argmin(distance))
    return np.array(assignments)


# Step 2
def updateCentroid(x, clusters, K):
    new_centroids = []
    for c in range(K):
        # Update the cluster centroid with the average of all points
        # in this cluster
        cluster_mean = x[clusters == c].mean()
        new_centroids.append(cluster_mean)
    return new_centroids


# 1-d kmeans
def kmeans(x, K):
    # initialize the centroids of 2 clusters in the range of [0,20)
    centroids = 20 * np.random.rand(K)
    print('Initialized centroids: {}'.format(centroids))
    for i in range(10):
        clusters = closestCentroid(x, centroids)
        centroids = updateCentroid(x, clusters, K)
        print('Iteration: {}, Centroids: {}'.format(i, centroids))


K = 2
x = np.array([0, 2, 10, 12])
kmeans(x, K)
