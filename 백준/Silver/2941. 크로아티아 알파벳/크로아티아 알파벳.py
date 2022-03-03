a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for x in a:
    s = s.replace(x,'*')
print(len(s))