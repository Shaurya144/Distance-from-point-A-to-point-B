# A satellite is orbitting around Earth and we need to caculate distance between two points on its flight path (equal distance apart both ways)
# First we need to find out the straight line distance between point A and B ( Diameter )
Straight_line_distance = int(input("What is the straight line distance from point A to B in miles: "))

# Convert  miles to Kilometres (1 mile = 1.6)
Distance_in_Kilometres = Straight_line_distance * 1.6 # This is the Diameter

# Calculate the distance along the flight path(circumference = 2 x pi x radius)
Circumference = Distance_in_Kilometres * 3.142
Flight_path = Circumference // 2

print("The Distance from point A to point B along the flight path for this satelite is " + str(Flight_path) + " kilometres.")
