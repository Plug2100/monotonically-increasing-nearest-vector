The folder contains the solution to the second task 
"2. Programming Task

Given a vector x containing n numbers, find a vector y, such that the euclidean distance between the two is minimised, subject to the constraint that the values in y are monotonically increasing.

Example 1: Given x=[1,5,7], y should be [1,5,7]

Example 2: Given x=[1,7,3], y should be [1,5,5]

Do you have an idea what the computional complexity of your solution is?"


Content:

Algorithm_explanation.pdf - Description and proof of the solution of the second task.

task_2_solution.py - Implementation of the algorithm from a PDF file Algorithm_explanation.pdf

data/test_vectors.txt - Test vectors for the algorithm.

data/input_vectors.txt - File for your examples.

Vector input format:
Each line is a new vector, vector elements separated by commas (check the first line from data/test_vectors.txt as an example).

venv - Virtual environment for the task.

requirments.txt - Versions requirments.


How to run the solution:
1) Activate venv (if you use Windows) OR create a new one using requirments.txt, then activate it.
2) If you want, input your examples into data/input_vectors.txt .
3) Run the task_2_solution.py .

Computional complexity:
We will discuss the complexity of the algorithm for one vector.
The most computationally complex part is the outer loop and (inner loop + np.mean + slicing) in the _enforce_non_decreasing_vector.
The computational complexity is O(n^2).