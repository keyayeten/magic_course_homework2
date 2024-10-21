numbers = 1.1, 1.2, 3.1, 5, 10.01
num = [i - int(i) for i in numbers]
print(max(num) - min(num))
