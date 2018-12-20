import re
a = input()
if re.fullmatch(r"^([A-Za-z0-9-!@#$]{8})$", a):
    print('Valid')
else:
    print('Not Valid')

print(a)
