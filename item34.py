# list comprehensions
x = [1, 2, 3, 4, 5, 6, 7]
x_compre = [a**2 for a in x]
print(x_compre)
even_squares = [a**2 for a in x if a%2 == 0]
print(even_squares)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)
cond_flat = [[x**2 for x in row] for row in matrix if sum(row)>=10]
print(cond_flat)