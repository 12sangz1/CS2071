# Instructions

The `test.in` file is used to pipe the contents of a problem via stdin into the binary executable. You can modify the number of runs timed for the algorithms by modifying NUM_RUNS in the `main` function.

How to run on Unix/OS X:

1. `g++ Assignment.cpp -o Assignment -std=c++0x`
1. `./Assignment < test.in`



# Time Writeup
When timed, the Kruskal algorithm performs considerably better than the Prim algorithm. To account for interference and other random interference, each algorithm was run over the same data set 10,000 times.

For 10,000 runs, Kruskal took `.3205` seconds. For the same number of runs, Prim took `1.8410` seconds. 