# Comparação de Funções `minmax`



```python
from minMax1 import minmax as m1
from minMax2 import minmax as m2
from minMax3 import minmax as m3

import timeit
import random

tempo = {"m1": [], "m2": [], "m3": []}

def criar_vetor(k):
   lista = list()
   for i in range(k):
      lista.append(random.randint(-16000, 16000))
   return lista

for i in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
   vetor = criar_vetor(i)
   t_m1 = timeit.timeit(lambda: m1(vetor), number=1)
   t_m2 = timeit.timeit(lambda: m2(vetor), number=1)
   t_m3 = timeit.timeit(lambda: m3(vetor), number=1)
   tempo["m1"].append(t_m1)
   tempo["m2"].append(t_m2)
   tempo["m3"].append(t_m3)

print(tempo)
```
![Exemplo de Imagem](grafico.png)

