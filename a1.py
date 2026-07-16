basket1 = {"apple","banana","orange","mango","apple","grape","banana"}
basket2 = {"mango","kiwi","banana","papaya","grape"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

basket1.add("pear")
print("Basket 1 after adding pear:", basket1)

common_fruits = basket1.intersection(basket2)

print("Fruits in both baskets:", common_fruits)

union=basket1.union(basket2)
print("All fruits in baskets:", union)

diff=basket1.difference(basket2)
print("Difference fruits in baskets:", diff)

sym=basket1.symmetric_difference(basket2)
print("Symmetric difference fruits in baskets:", sym)