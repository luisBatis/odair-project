resultado = 1
qDePaisagens = input("teste")

paisagens: list[str | int] = input().split(' ')


paisagens = list(map(int, paisagens))
for i in range(len(paisagens)):
    if i ==0:
        i = 2
    if  paisagens[i] > paisagens[i-1] <  paisagens[i-2] or   paisagens[i] < paisagens[i - 1] > paisagens[i-2]:
       resultado = 1 
    else:
         resultado = 0 
   
    i +=1
print(resultado)
