user_age = 26
user_height = 5 + (7/12)
user_complex = 5 + 5j

# Problem 4
# Write a script that prompts the user to enter base and height of the triangle
# and calculate an area of this triangle (area = 0.5 x b x h).

triangle_base = int(input('Enter Base:'))
triangle_height = int(input('Enter Height:'))
triangle_area = int(triangle_base * triangle_height * 0.5)
print('The area of the triangle is ' + str(triangle_area))

# Problem 5:
# Write a script that prompts the user to enter side a, side b, and side c of
# the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a, b, c = int(input('Enter side A: ')), int(input('Enter side B: ')), int(input('Enter side C: '))
triangle_perimeter = sum([a, b, c])
print('The perimeter for the triangle is ' + str(triangle_perimeter))

# Problem 6:
# Get length and width of a rectangle using prompt. Calculate its area
# (area = length x width) and perimeter (perimeter = 2 x (length + width))

rect_length, rect_height = int(input('Enter rectangle length: ')), int(input('Enter rectange height: '))
rect_area = rect_height * rect_length
rect_perimeter = 2 * rect_length * rect_height
print('The area of the rectangle is ' + str(rect_area))
print('The perimeter of the rectangle is ' + str(rect_perimeter))

