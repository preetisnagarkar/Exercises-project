N = 10
sum = 0
count = 0
while count < N:
    number = float(input(""))
    sum = sum + number
    count = count + 1
    average = float(sum)/N
    print("n = %d, sum = %f" % (N, sum))
    print("average= %f" % average)
