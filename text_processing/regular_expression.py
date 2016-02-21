import re

s = ('xxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxya')
a = filter((lambda s: re.match(r"xxx", s)), s)
print(*a)   # xxx
# re.match function looks fro matches only at the start of its input
# To find strings anywhere in the input, use re.search

b = filter((lambda s: re.search(r"xxx", s)), s)
print(*b)  # xxx, abcxxxabc, axxxxa

c = filter((lambda s: re.search(r"x.x", s)), s)
print(*c)  # xxx, abcxxxabc, xyx, x.x, axxxxa

d = filter((lambda s: re.search(r"x\.x", s)), s)
print(*d)  # x.x

e = filter((lambda s: re.search(r"x.*x", s)), s)
print(*e)  # xxx, abcxxxabc, xyx, x.x, axxxxa, axxya
# "*" matches zero or more occurrences of a character between two x's
# To make sure something is between the x's, use a plus instead, which matches one or more characters
f = filter((lambda s: re.search(r"x.+x", s)), s)
print(*f)  # xxx, abcxxxabc, xyx, x.x, axxxxa

#Match anything with 'c' in it
g = filter((lambda s: re.search(r"c+", s)),s)
print(*g)   # abcxxxabc, abc

# Match anything without a 'c' in it, have to use ^ and $ to refer to the beginning and end
i = filter((lambda s: re.search(r"^[^c]*$", s)), s)
print(*i)  # xxx, xyx, x.x, axa, axxxxa, axxya


































