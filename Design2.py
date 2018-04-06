row = int(input("Enter the value of rows:"))
n = row
i = 1

while i <= n:
    x = " " * (row - i)
    y = "*" * i
    print(x + y)
    i += 1
while n >= 0:
    n -= 1
    x = "*" * n
    y = " " * (row - n)
    print(y + x)
