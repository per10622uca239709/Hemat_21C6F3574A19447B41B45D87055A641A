"""
write a function called linear_search_product that takes the list of products and target product
name as input.the  function should perform a linear search to find the target product in the list and 
return a list of indices of all occurrences of the product if found,or an empty list if the product is not 
fount .
"""


def linearsearchproduct(productlist,targetproduct):
  indices = []

for index,product in enumerate(productlist):
  if product == targetproduct:
    indices.append(index)

return indices


# example usage:
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linersearchproduct(products,target)
print(result)