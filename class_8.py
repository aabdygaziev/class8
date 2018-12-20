
import re
a = input()
name = re.fullmatch(r"^([A-Z][a-z]+(\s[A-Z][a-z]){0,2})|(([A-Z][a-z]+\s){1}(uulu|kyzy){1}(\s[A-Z][a-z]+){1})$", a)
print(name)

