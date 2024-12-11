
def sort_list(arr):
    return sorted(arr)


def find_max(arr):
    return max(arr)

from my_module import sort_list, find_max


n = int(input("Nhập số lượng phần tử trong danh sách: "))


arr = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(value)


min_value = min(arr)
max_value = find_max(arr)


sorted_arr = sort_list(arr)


print(f"Danh sách ban đầu: {arr}")
print(f"Danh sách sau khi sắp xếp: {sorted_arr}")
print(f"Phần tử nhỏ nhất: {min_value}")
print(f"Phần tử lớn nhất: {max_value}")
