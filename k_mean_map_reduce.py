import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt
# Generate some sample data
np.random.seed(0)
data = np.random.rand(100, 2)

# Define the number of clusters (K)
K = 3

# Initialize cluster centroids randomly
centroids = data[np.random.choice(data.shape[0], K, replace=False)]

def map_point_to_closest_centroid(point):
    # Calculate the distance from the point to all centroids
    distances = np.linalg.norm(centroids - point, axis=1)
    # Find the index of the closest centroid
    closest_centroid = np.argmin(distances)
    return closest_centroid, point

def reduce_cluster_points(cluster_points):
    cluster_points = np.array(cluster_points)
    # Update the centroid as the mean of all data points in the cluster
    new_centroid = np.mean(cluster_points, axis=0)
    return new_centroid

def kmeans_map_reduce(data, centroids, num_iterations):
    for _ in range(num_iterations):
        # Map: Assign each data point to the closest centroid
        with Pool() as pool:
            mapped_data = pool.map(map_point_to_closest_centroid, data)

        # Reduce: Update the centroids based on the assigned data points
        new_centroids = []
        for i in range(K):
            cluster_points = [point for cluster, point in mapped_data if cluster == i]
            new_centroid = reduce_cluster_points(cluster_points)
            new_centroids.append(new_centroid)

        centroids = np.array(new_centroids)

    return centroids

# Run K-means for a number of iterations
new_centroids = kmeans_map_reduce(data, centroids, num_iterations=10)

print("Final Centroids:")
print(new_centroids)

# Run K-means for a number of iterations
new_centroids = kmeans_map_reduce(data, centroids, num_iterations=10)

# Extract cluster assignments
cluster_assignments = [map_point_to_closest_centroid(point)[0] for point in data]

# Plot the data points for each cluster separately
for i in range(K):
    cluster_points = np.array([data[j] for j in range(len(data)) if cluster_assignments[j] == i])
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i+1}', alpha=0.5)

# Plot the centroids
plt.scatter(new_centroids[:, 0], new_centroids[:, 1], marker='x', s=100, c='k', label='Centroids')

plt.legend()
plt.title('K-means Clustering')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
