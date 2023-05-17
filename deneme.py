def hesapla(x, y, x1, y1, x2, y2):
    oran1 = (x - x1) / (x1 - x2)
    oran2 = (y - y1) / (y1 - y2)
    return oran1, oran2

# mesela
x = 5
x1 = 10
x2 = 2
y = 6
y1 = 3
y2 = 7

oran1, oran2 = hesapla(x, y, x1, y1, x2, y2)
print("x oranı:", oran1)
print("y oranı:", oran2)
    
