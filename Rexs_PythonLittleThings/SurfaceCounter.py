length = input("length?: ")
length_float = float(length)
width = input("width?: ")
width_float = float(width)
area = length_float * width_float
show = f"With width {width_float} and length {length_float} of the room, its area is equal to {area}"
print(show)