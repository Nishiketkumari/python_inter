import numpy as np
from scipy import stats


array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
mean_1d = np.mean(array_1d)
median_1d = np.median(array_1d)
mode_1d = stats.mode(array_1d, keepdims=True).mode[0]
std_dev_1d = np.std(array_1d)


mean_2d = np.mean(array_2d)
median_2d = np.median(array_2d)
mode_2d = stats.mode(array_2d, axis=None, keepdims=True).mode[0]
std_dev_2d = np.std(array_2d)


mean_3d = np.mean(array_3d)
median_3d = np.median(array_3d)
mode_3d = stats.mode(array_3d, axis=None, keepdims=True).mode[0]
std_dev_3d = np.std(array_3d)


print("1D Array Statistics:")
print(f"Mean: {mean_1d}, Median: {median_1d}, Mode: {mode_1d}, Standard Deviation: {std_dev_1d}")

print("\n2D Array Statistics:")
print(f"Mean: {mean_2d}, Median: {median_2d}, Mode: {mode_2d}, Standard Deviation: {std_dev_2d}")

print("\n3D Array Statistics:")
print(f"Mean: {mean_3d}, Median: {median_3d}, Mode: {mode_3d}, Standard Deviation: {std_dev_3d}")
