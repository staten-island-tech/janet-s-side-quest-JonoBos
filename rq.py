temperatures = ["Label", 32, 50, 77, 104]
celc= list(map(lambda f: (f-32)*5/9,temperatures[2:]))
print (celc)