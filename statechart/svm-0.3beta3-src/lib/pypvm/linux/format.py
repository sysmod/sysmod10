import sys
from string import *
from re import *

in_comment=0
def remove_comment(l):
  global in_comment
  c = search("/\\*.*\\*/", l)
  while c:
    l = l[:c.start()] + l[c.end():]
    c = search("/\\*.*\\*/", l)
  pos = find(l, "//")
  if pos >= 0:
    l = l[:pos]
  if in_comment:
    pos = find(l, "*/")
    if pos >= 0:
      l = l[pos+2:]
      in_comment = 0
    else:
      l = ""
  else:
    pos = find(l, "/*")
    if pos >= 0:
      l = l[:pos]
      in_comment = 1
  return l

f = open(sys.argv[1], "r")
ls = f.readlines()

quotes = 0
for l in ls:
  l = replace(l, "\t", "    ")
  l = rstrip(l)
  lr = remove_comment(l)
  quotes = quotes + count(lr, "\"") - count(lr, "\\\"")
  if quotes % 2:
    l = lr + "\\n\\"
  print l

f.close()
