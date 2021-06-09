import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# DTW algorithm
# with windows
# to limit matching of value
# for example when window=3,it will match 3 value only for one-to-many relationships
def dtw(s, t, window):
    n, m = len(s), len(t)
    w = np.max([window, abs(n - m)])
    dtw_matrix = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        for j in range(m + 1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0

    for i in range(1, n + 1):
        for j in range(np.max([1, i - w]), np.min([m, i + w]) + 1):
            dtw_matrix[i, j] = 0

    for i in range(1, n + 1):
        for j in range(np.max([1, i - w]), np.min([m, i + w]) + 1):
            cost = abs(s[i - 1] - t[j - 1])
            last_min = np.min([dtw_matrix[i - 1, j], dtw_matrix[i, j - 1], dtw_matrix[i - 1, j - 1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix

def dtw_normal(fast, normal):
    fast_len = len(fast)
    normal_len = len(normal)
    dtw_matrix = np.zeros((fast_len + 1, normal_len + 1))

    for i in range(fast_len + 1):
        for j in range(normal_len + 1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0

    for i in range(1, fast_len + 1):
        for j in range(1, normal_len + 1):
            cost = abs(fast[i - 1] - normal[j - 1])

            last_min = np.min([dtw_matrix[i - 1, j], dtw_matrix[i, j - 1], dtw_matrix[i - 1, j - 1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix


#using build in
x = [1,2,3,4,3,4,1,5]
y = [1,3,1,4,5,2,1,4]

distance, path = fastdtw(x,y,dist=euclidean)
print('The distance is '+str(distance))

print('The path is '+str(path))

#using dtw method
distance1 = dtw(x,y,window=8)
print(distance1)