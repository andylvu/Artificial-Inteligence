import numpy as np
import matplotlib.pyplot as plt

# k is the number of clusters, x is the data points
K = 2
x = np.array([[2, 4], [1.7, 2.8], [7, 8], [8.6, 8], [3.4, 1.5], [9, 11]])
plt.scatter(x[:, 0], x[:, 1], s=150)


# new distance function that uses numpy to find
# the euclidean distance for 2 objects instead of 1d
def euclidean(a, b):
    distance = np.linalg.norm(a - b)
    return distance


# new function to create intial centroids
# uses min max to best deteremine random values within the range of data
def initial_centroids(numcluster, data):
    centroid_min = data.min()
    centroid_max = data.max()
    centroids = []
    for centroid in range(numcluster):
        centroid = np.random.uniform(centroid_min, centroid_max, 2)
        centroids.append(centroid)
    centroids = np.array(centroids)

    return centroids


# Step 1
# finds the closest centroids from each datapoint by comparing
# euclidean distances, after that it sets the assignment to which
# corresponding centroid the point is supposed to be
def closestCentroid(x, centroids):
    assignments = []
    for i in x:
        # distance between one data point and centroids
        distance = []
        for j in centroids:
            distance.append(euclidean(i, j))
            # assign each data point to the cluster with closest centroid
        assignments.append(np.argmin(distance))
    return np.array(assignments)


# Step 2
# updates the centroids based off of the average mean of current points
# the average of the current points are then assigned as the new centroids
def updateCentroid(x, clusters, K):
    new_centroids = []
    for c in range(K):
        # Update the cluster centroid with the average of all points
        # in this cluster
        cluster_meanx = x[clusters == c][0].mean()
        cluster_meany = x[clusters == c][1].mean()
        # print(cluster_meanx, 'this is cluster meanx', c)
        # print(cluster_meany, 'this is cluster mean y', c)
        clusterpair = []
        clusterpair.append(cluster_meanx)
        clusterpair.append(cluster_meany)
        new_centroids.append(clusterpair)
    return new_centroids


# 2-d kmeans
def kmeans(x, K):
    # initialize the centroids of 2 clusters in the range of [0,20)
    centroids = initial_centroids(K, x)
    print('Initialized centroids: {}'.format(centroids))
    for i in range(10):
        clusters = closestCentroid(x, centroids)
        centroids = updateCentroid(x, clusters, K)
        print('Iteration: {}, Centroids: {}'.format(i, centroids))
        if i == 9:
            print(centroids)
            print(centroids[0])
            X.append(centroids[0][0])
            X.append(centroids[1][0])
            y.append(centroids[0][1])
            y.append(centroids[1][1])


X = []
y = []
kmeans(x, K)
plt.scatter(X, y)
plt.show()
