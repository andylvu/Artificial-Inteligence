import numpy as np

K = 2
x = np.array([[2, 4], [1.7, 2.8], [7, 8], [8.6, 8], [3.4, 1.5], [9, 11]])


def euclidean(a, b):
    distance = np.linalg.norm(a - b)
    return distance


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
def closestCentroid(x, centroids):
    assignments = []
    for i in x:
        # print(i, 'this is i')
        # distance between one data point and centroids
        distance = []
        for j in centroids:
            # print(j, 'this is j')
            # print((euclidean(i, j)), 'this is distance')
            distance.append(euclidean(i, j))
            # assign each data point to the cluster with closest centroid
        assignments.append(np.argmin(distance))
    # print(assignments)
    return np.array(assignments)


def updateCentroid(x, clusters, K):
    new_centroids = []
    for c in range(K):
        print(c, 'this is c')
        # Update the cluster centroid with the average of all points
        # in this cluster
        cluster_meanx = x[clusters == c][0].mean()
        cluster_meany = x[clusters == c][1].mean()
        print(cluster_meanx, 'this is cluster meanx', c)
        print(cluster_meany, 'this is cluster mean y', c)
        clusterpair = []
        clusterpair.append(cluster_meanx)
        clusterpair.append(cluster_meany)
        new_centroids.append(clusterpair)
    return new_centroids


centroids = initial_centroids(K, x)
print(centroids, "initial centroids")
clusters = closestCentroid(x, centroids)
print(clusters, 'clusters')
new_centroids = updateCentroid(x, clusters, K)
print(new_centroids, 'new centroids')
