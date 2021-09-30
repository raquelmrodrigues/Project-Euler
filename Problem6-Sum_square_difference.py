# The sum of the squares of the first ten natural numbers is 1²+2²+...+10²=385
# The square of the sum of the first ten natural numbers is (1+2+...+10)² = 55² = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.
sum_of_squares = []
square_of_sum = list(range(1, 1000))

for i in range(1, 1000):
    sum_of_squares.append(i^2)
    i++

