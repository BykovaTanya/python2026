def rectangle_info(width, height):
    square = width*height
    perimeter = 2*(width+height)
    return (square, perimeter)
rect=rectangle_info(3,5)
print(rect)

def is_adult(age):
    adult = "True" if age >= 18 else "False"
    return adult
result=is_adult(23)
print(result)

def safe_div(a, b):
    result = "None" if b == 0 else a / b
    return result
result=safe_div(6,3)
print(result)    
