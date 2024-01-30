a = input()
b = input()
c = input()
car = {
    "brand": a,
    "model": b,
    "year": c
}
print(car["year"])
x = car.values()
d = input()
car["year"] = d
print(x)
car["color"] = "black"
print(car)
car.pop("model")