height = float(input("height: "))
weight = float(input("weight: "))
z = weight / pow(height, 2)
if z < 18.5:
    result = ("Gain weight")
elif 18.5 < z < 25:
    result = ("Normal weight")
elif 25 < z < 30:
    result = ("start exercising")
elif z > 30:
    result = ("go to the gym every day")
print("index mass", round(z, 2))
print("What to do?:", result)






