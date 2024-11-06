color_list = ["red", "green", "blue", "yellow"]
print("First Element:", color_list[0])
print("Last Element:", color_list[-1])
slice_list = color_list[1:3]
print("Slice List", slice_list)


num_list = [4, 6, 4, 2, 9, 4, 1]
print("Original List:", num_list)
num_list.append(5)
print("After Append:", num_list)
num_list.remove(4)
print("After Remove:", num_list)
count = num_list.count(4)
print("Count of 4:", count)
index = num_list.index(9)
print("Index of 9:", index)


fruit_list = ["apple", "banana", "cherry"]
print("Original List:", fruit_list)
fruit_list[1] = "orange"
print("Modified List:", fruit_list)
fruit_list.pop()
print("Updated List:", fruit_list)