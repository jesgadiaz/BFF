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
$ python bgp.py D:\dataset\squaredIdealBurn7.mtx 231 418 False
```

The output shows a burning sequence and its length. The running time of the initialization phase and the running time of the 'burning greedy permutation' algorithm is showed too.

```
---Compute all shortest paths - running time: 0.18633675575256348 seconds ---
burning sequence: [96, 101, 222, 0, 25, 109, 142, 179, 187, 23]
burning sequence length: 10
---BGP running time: 0.0 seconds ---
```

## Example 2

```
$ python bgp.py D:\dataset\squaredIdealBurn7.mtx 231 418 True
```

The output shows a burning sequence and its length. The running time of the initialization phase and the running time of the 'burning greedy permutation' algorithm is showed too.

```
---Compute all shortest paths - running time: 0.17345452308654785 seconds ---
burning sequence: [30, 142, 226, 101, 166, 63, 205, 51, 112, 0]
burning sequence length: 10
---BGP running time: 1.616149663925171 seconds ---
```
# Preprint

Jesús García Díaz, A 3-2/b(G)-approximation algorithm for the graph burning problem, https://arxiv.org/abs/2011.15019

# Contact

* jesgadiaz@inaoep.mx
