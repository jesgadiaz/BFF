# Approximation algorithm for the graph burning problem
This repository contains a Python implementation of the 'burning greedy permutation' algorithm. The approximation factor of this algorithm is 3-2/b(G). 

## Running the algorithm

To execute the 'burning greedy permutation' algorithm (bgp.py) run the following command on a Terminal.

```
$ python bgp.py {instance} {n} {m} {plus}
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
$ python bgp.py D:\dataset\line49nodes.mtx 49 48 False
```

The output shows a burning sequence and its length. The running time of the initialization phase (Floyd Warshall algorithm) and the running time of the 'burning greedy permutation' algorithm is showed too.

```
---Floyd-Warshall running time: 0.10785794258117676 seconds ---
burning sequence: [17, 48, 0, 32, 8, 40, 24, 4, 12]
burning sequence length: 9
---BGP running time: 0.0 seconds ---
```

## Example 2

```
$ python bgp.py D:\dataset\line49nodes.mtx 49 48 True
```

The output shows a burning sequence and its length. The running time of the initialization phase (Floyd Warshall algorithm) and the running time of the 'burning greedy permutation' algorithm is showed too.

```
---Floyd-Warshall running time: 0.10028624534606934 seconds ---
burning sequence: [39, 0, 19, 29, 9, 48, 14, 24]
burning sequence length: 8
---BGP running time: 0.03125739097595215 seconds ---
```

# Contact

* jesgadiaz@inaoep.mx
