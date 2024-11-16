items = ["apple", "banana", "orange", "apple", "mango"]


# method 1

# items_dict = {}
# for elem in items:
#     if elem in items_dict:
#         print(elem)
#         break
#     else: items_dict[elem]=1




# method 2

# for elem in items:
#     if items.count(elem) >1:
#         print("Not unique: ",elem)
#         break



#method 3

# unique_item = set()


# for item in items:
#     if item in unique_item:
#         print("Not unique: ", item)
#         break
#     unique_item.add(item)