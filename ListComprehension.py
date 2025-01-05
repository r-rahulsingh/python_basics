# Basics 🐣
# Expression: [expression for item in iterable_collection]

# # Create a list of squares
# squares = [x**2 for x in range(6)]
# print(squares) # [0, 1, 4, 9, 16, 25]

# ## list.pop() method removes the last item and returns the list.
# while squares:
#     pop_item = squares.pop()
#     non_pop = squares
#     print(f"Popped:{pop_item},Remaining:{non_pop}")

# ## list.pop(0) method removes the first item and returns the list.
# while squares:
#     popped_item = squares.pop(0)
#     non_popped = squares
#     print(f"Popped:{popped_item},Remaining:{non_popped}")

# # Convert items to uppercase
# words = ['rahul','s','python']
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words) # ['RAHUL', 'S', 'PYTHON']

# Intermediate 🐥
# Adding conditional logic

# # # Filter even numbers
# # evens = [x for x in range(10) if x % 2 == 0]
# # print(evens) # [0, 2, 4, 6, 8]

# # Filter odd numbers
# odds = [x for x in range(10) if x % 2 != 0]
# print(odds) # [1, 3, 5, 7, 9]
# print(odds.pop()) # 9
# print(odds) # [1, 3, 5, 7]
# print(odds.pop(1)) # 3
# print(odds) # [1, 5, 7]

# # Filter words with length > 3
# words = ['cat','camel','hippopotamus']
# lengths = [word for word in words if len(word) > 3]
# print(lengths) # ['camel', 'hippopotamus']

# Advanced 🐔

# # Nested Condition

# # Cartesian product
# pair = [(x,y) for x in [1,2] for y in ['a','b']]
# pairs = [(x**2,y) for x in [2,3] for y in ['a','b']]
# print(pair) # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
# print(pairs) # [(4, 'a'), (4, 'b'), (9, 'a'), (9, 'b')]

# # Replace odd numbers with -1
# result = [x if x % 2 == 0 and x != 0 else -1 for x in range(6) ]
# print(result) # [-1, -1, 2, -1, 4, -1]

# # Flatten a 2D list
# array_2d = [[1,2],[3,4],[5,6]]
# flattened = [num for row in array_2d for num in row]
# print(flattened) # [1, 2, 3, 4, 5, 6]

# # Nested conditionals
# labels = ['even' if x % 2 == 0 else 'odd' for x in range(1,10)]
# print(labels) # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# # Apply a function to elements
# def cube(x):
#     return x**3

# cubes = [cube(x) for x in range(1,10)]
# print(cubes) # [1, 8, 27, 64, 125, 216, 343, 512, 729]

# # # Memory-efficient : Generator Expression
# squares_gen = (x**2 for x in range(20)) # Use parentheses (), no memory overload
# print(next(squares_gen))
# print(next(squares_gen))
# print(next(squares_gen))
# print(next(squares_gen))
# for i in squares_gen:
#     print(next(squares_gen))
# """
# 0
# 1
# 4
# 9
# 25
# 49
# 81
# 121
# 169
# 225
# 289
# 361
# """