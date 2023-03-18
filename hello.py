def cylinder_volume(radius, height):
    volume = (3.14) * radius**2 * height
    return volume

prompt = input('Enter the radius and height of the cylinder: ')
print("The volume of the cylinder is:", {cylinder_volume})
print("This doesn't do anything.")