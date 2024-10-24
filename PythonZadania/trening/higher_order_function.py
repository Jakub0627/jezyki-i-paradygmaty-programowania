nums = [3, 4, 5, 6, 7]

def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result

cubed = my_map(lambda x: x**3, nums)

print(cubed)