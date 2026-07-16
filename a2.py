import array as arr
fruit_counts = arr.array('i', [6,3,5,2,4])
print("Fruits counts array:",fruit_counts)

fruit_counts.insert(1,7)
fruit_counts.append(6)
print("Fruits counts after adding items:", fruit_counts)

count_of_4 = fruit_counts.count(4)
print("Count of 4 in fruits counts array:", count_of_4)

fruit_counts.reverse()
print("reversed fruit counts array:", fruit_counts)