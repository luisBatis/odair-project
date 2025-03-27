def minmax(a):
  n = len(a)
  if n % 2 != 0:
    a.append(a[-1])
    b = n -1
  else:
    b = n -1
  _min = a[1]
  _max = a[1]
  if a[0] > a[1]:
    _min, _max = a[0], a[1]
  i = 2
  while i <= b:
    if a[i] > a[i+1]:
      _max = a[i]
    if a[i+1] < _min:
      _min = a[i + 1]
    else: 
      if a[i] < _min:
        _min = a[1]
      if a[i+1] > _max:
       _max = a[i+1]
    i += 2
  print(_min)
  print(_max)
    
