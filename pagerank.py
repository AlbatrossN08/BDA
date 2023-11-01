import numpy as np

# Sample web graph as an adjacency matrix
adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
], dtype=float)

# Initialize the PageRank values for each page
num_pages = len(adjacency_matrix)
pagerank = np.ones(num_pages) / num_pages

# Damping factor (probability to follow links)
damping_factor = 0.85

# Number of iterations for PageRank computation
num_iterations = 10

# Simulate MapReduce for PageRank
for _ in range(num_iterations):
    new_pagerank = np.zeros(num_pages)

    # Map: Distribute the PageRank value through links
    for i in range(num_pages):
        for j in range(num_pages):
            if adjacency_matrix[j, i] == 1:
                new_pagerank[i] += pagerank[j] / np.sum(adjacency_matrix[j])

    # Reduce: Combine PageRank values
    pagerank = damping_factor * new_pagerank + (1 - damping_factor) / num_pages

# Print the final PageRank values
for i, pr in enumerate(pagerank):
    print(f"Page {i + 1}: {pr:.4f}")
