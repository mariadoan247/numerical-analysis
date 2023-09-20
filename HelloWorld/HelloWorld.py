print('Hello World!')
print('By Maria Doan')

# Storing 5 in Python will take more space in memory than you will think
x = 5

x = 1
print('The value of x is ', x)
print('The type of x ', type(x), '\n')

y = 1.1
print('The value of y is ', y)
print('The type of y ', type(y), '\n')

s = 'Hello World'
print('The value of x is ', s)
print('The type of x ', type(s), '\n')

z = x + y
print('The value of x is ', z)
print('The type of x ', type(z), '\n')

# This does not print
if(0.1+0.1+0.1 == 0.3):
    print("This is always true!!!!")

print('statements before if...')
x = 0.1+0.1+0.1
if x == 0.3:
    print('This is what should happen!')
else:
    print("This is not what happends in floating point arithmetic because ")
    print('0.1+0.1+0.1 = ', x)
print('Statements after if ...')
