import sequential_search.py
import sys

def main():

 
  n = int(input("Nhập số lượng phần tử: "))
  dlist = []
  for i in range(n):
    x = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    dlist.append(x)

 
  item = int(input("Nhập phần tử cần tìm: "))

 
  result = sequential_search.sequential_search(dlist, item)
  if result != -1:
    print("Phần tử", item, "được tìm thấy tại vị trí", result)
  else:
    print("Không tìm thấy phần tử", item)

if __name__ == "__main__":
  main()
