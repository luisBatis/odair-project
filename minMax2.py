def minmax(a):
    _min = a[0]
    _max = a[0]
    for i in range(len(a)):
        if a[i] > _max:
            _max = a[i]
        elif a[i] < _min:
            _min = a[i]
            
    
    
