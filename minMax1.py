def minmax(a):
  _max = a[0]
  _min = a[0]
  for i in range(len(a)):
    if a[i] > _max:
      _max = a[i]
    if a[i] < _min:
      _min = a [i]

  print(_max)
  print(_min)
