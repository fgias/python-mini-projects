
# Regular Expressions in Python

import re

txt = "The rain in Spain"
txt2 = "The rain in Spain, something else"

print(re.search("^The.*Spain$", txt))
print(re.search("^The.*Spain$", txt2))

x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())



print(re.findall(".ai.", txt))
print(re.findall('Z', txt))

print(re.sub("\s", "9", txt))
print(re.sub("a", "x", txt))