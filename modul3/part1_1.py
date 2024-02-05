# If + condition

var1 = int(input('Add number:'))

if var1 == 1:
    print(var1)
else:
    print('number is not 1')

# true-ish

print(bool(''), 'Empty string')
print(bool('0'), '0 string')
print(bool(0), '0 int')
print(bool(-1000), '-1000 int')
print(bool(None), 'None object')

