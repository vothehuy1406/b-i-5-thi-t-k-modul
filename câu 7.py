def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i) 
    return (False, -1) 

from sequential_search import Sequential_Search


n = int(input("Nhập số lượng phần tử trong danh sách: "))


dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    dlist.append(value)


item = int(input("Nhập phần tử cần tìm: "))


found, index = Sequential_Search(dlist, item)


if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")
