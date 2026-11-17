widgets = int(input("How many widgets?:"))

if widgets >= 100:
    cost = widgets * 0.20   
else:
    cost = widgets * 0.25   

print(cost)