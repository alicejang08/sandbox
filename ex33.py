n = raw_input("Enter simple number less than 10 \n")
i = 0
numbers = []

while i < n:
    print "At the top i is %d" %i
# method append() takes a single item and adds to the end of the list
    numbers.append(i)

    i = i + 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" %i


print "The numbers: "

for num in numbers:
    print num
