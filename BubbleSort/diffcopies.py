###shallow copy

# a = [1,2,3]
# b = a

# a.append(1)
# b.append(3)

# print(b)
# print(a)


##deep copy
import copy

a = [1,2,3] #123456
b = copy.copy(a) #654321

a.append(1)
b.append(3)

print('a: ',a)
print('b: ',b)