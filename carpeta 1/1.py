H = float(input("porfavor ingrese la altura al que se tirara la pelota : "))

# variables
r = 0
d = H/5

#procesing
while(d <= H):
    H = H - 0.10*H
    r = r + 1
print("el numero de veces que reboto la pelota fueron : ",r)
print("la altura que quedo la pelota fue: ",H)