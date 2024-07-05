num = int(input())


a =(num - (num % 10000)) // 10000
b = (num % 10000) // 1000
c = (num % 1000) // 100
d = (num % 100) //  10
e = (num % 10)

print((d ** e) * c / (a - b))