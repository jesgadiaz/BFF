# Burning Farthest-First algorithm 
# An approximation algorithm for the graph burning problem
This repository contains a Python implementation of the 'burning greedy permutation' algorithm. The approximation factor of this algorithm is 3-2/b(G). 

## Running the algorithm

To execute the 'burning farthest-first' algorithm (bff.py) run the following command on a Terminal.

```
$ python bff.py {instance} {n} {m} {plus}
```

### Where,

|  Parameter |                                          Description                                          |
|----------|---------------------------------------------------------------------------------------------|
| `{instance}` | (string) Instance file path                                    |
| `{n}`    | (integer) Number of vertices  |
| `{m}`    | (integer) Number of edges  |
| `{plus}`    | (string) for bgp set 'False'. For bgp+ set 'True'  |

By setting plus to True, the algorithm is repeated n times and the best solution is returned.

## Example 1

```
$ python bff.py D:\dataset\econ-mahindas.mtx 1258 7513 False
```

The output shows a burning sequence and its length. The running time of the initialization phase and the running time of the 'burning frthest-first' algorithm is showed too.

```
---Compute all shortest paths - running time: 13.222469329833984 seconds ---
burning sequence: [110, 551, 607, 523, 540, 546, 549]
burning sequence length: 7
---BFF running time: 0.15363645553588867 seconds ---
```

## Example 2

```
$ python bff.py D:\dataset\econ-mahindas.mtx 1258 7513 True
```

The output shows a burning sequence and its length. The running time of the initialization phase and the running time of the 'burning farthest-first' algorithm is showed too.

```
---Compute all shortest paths - running time: 14.913883447647095 seconds ---
burning sequence: [989, 554, 555, 50, 51]
burning sequence length: 5
---BFF running time: 210.62542939186096 seconds ---
```
# Preprint

Jesús García Díaz, A simple approximation algorithm for the graph burning problem, https://arxiv.org/abs/2011.15019

# Contact

* jesgadiaz@inaoep.mx
