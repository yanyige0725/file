# the 1st naon url-web=https://ks.wjx.top/vm/eKqDIRA.aspx
l = [1,3,5,8]
num = ""
for i in range(4):
  num += l[i]
  l.pop(i)
  for i in range(3):
    num += l[i]
    l.pop(i)
    for i in range(2):
      num+=l[i]
      l.pop(i)
      num+=l[0]
      l = [3,5,8]
    l = [1,3,5,8]
