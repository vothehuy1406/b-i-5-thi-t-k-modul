import numpy as np


student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])


sorted_indices = np.lexsort((student_id, student_height))


print("Chỉ số:")
print(sorted_indices)


print("\nDữ liệu sắp xếp:")
for index in sorted_indices:
    print(student_id[index], student_height[index])
