def sequential_search(dlist, item):
  """Thực hiện tìm kiếm tuyến tính trong một danh sách

  Args:
    dlist: Danh sách các phần tử
    item: Phần tử cần tìm

  Returns:
    Chỉ số của phần tử nếu tìm thấy, ngược lại trả về -1
  """

  for i in range(len(dlist)):
    if dlist[i] == item:
      return i
  return -1