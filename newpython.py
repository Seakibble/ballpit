
print("\n\nHello World!")

newList = []
newList.append(1)
newList.append(5)
newList.append(21)
newList.append(14)

print("\n\n* Playing with arrays")
for y in newList:
    print(y)

print([1, 2, 3] * 3)

sillyString = "This is a silly string."
print("\n\n* Playing with strings")
print(sillyString)
print(sillyString[3:10])
print(sillyString[3:10:1])
print(sillyString[3::2])
print(sillyString[3:10:2])
print(sillyString[::-1])

print("\n\n* Conditionals")
if 5 in newList:
    print("Five is in newList.")
    newList.remove(5)
else:
    print("Five is not in newList.")

if 5 in newList:
    print("Five is in newList.")
else:
    print("Five is not in newList.")

print("\n\n* Counting")
for x in range(1, 11):
    print(x)


print("\n\n* Fibonacci!")
print(0)
fibonacciThis = 1
fibonacciPrevious = 0
while fibonacciThis < 1000:
    print(fibonacciThis)
    temp = fibonacciThis
    fibonacciThis = fibonacciThis + fibonacciPrevious
    fibonacciPrevious = temp


print("\n\n* FizzBuzz!")
for i in range(1, 51):
    out = ''

    def fizzfinder(number, mod, name):
        if number % mod == 0:
            return name
        else:
            return ''

    out += fizzfinder(i, 3, "Fizz")
    out += fizzfinder(i, 5, "Buzz")
    out += fizzfinder(i, 7, "Fuzz")
    out += fizzfinder(i, 9, "Bizz")

    if out != '':
        print(out)
    else:
        print(i)

print("\n\n")
