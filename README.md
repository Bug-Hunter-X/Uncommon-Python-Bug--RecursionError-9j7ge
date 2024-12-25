This repository contains a simple Python function that demonstrates an uncommon bug.  The function `my_function` uses recursion to calculate a sum. However, it lacks a proper base case for the recursion which leads to a stack overflow and a RecursionError for large inputs. The `bugSolution.py` file provides a corrected version of the function with an appropriate base case.