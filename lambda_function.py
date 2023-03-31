# Lambda functions

## Filtering data:

```
list(filter(lambda x: x > 100, [-5, 200, 300, -10, 10, 1000]))
```

## Data transformation

```
list(map(lambda x: x ** 2, [11, 22, 33, 44,55])
```
## Data aggregation
     
```
from functools import reducedef 
doSum(x1,x2):   
  return x1+x2
x = reduce(doSum, [100, 122, 33, 4, 5, 6])
```
