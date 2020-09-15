# Allstar - A Implementation of the A\* Pathfinding Algorithm in Python 3

![alt text](demo.png)

### Challenge

The only resource is this Wikipedia Article: https://en.wikipedia.org/wiki/A*_search_algorithm

Using this Video also: https://www.youtube.com/watch?v=-L-WgKMFuhE

### Goal:

Web based GUI where one can draw an obstacle and the program finds the quickest path around it to a predetermined target

(+extra nice visualsation)

### ToDo:

- Sometimes ignores walls (bug)
- Implement animation for good boy points

### DONE:

- implement command line solution
- Change x and y axis
- Fix obstacle problem

### How does A\* work?

A\* selects the path that minimizes

    f(n)=g(n)+h(n)

n is the next node on the path

g(n) is the cost of the path from the start node to n

h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal

A\* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended

The heuristic function is usually implemented using a priority queue (Binary heap)

### My (bad) implementation

Map = 2d array of bits

- 0 = free
- 1 = cant go through

object oriented implementation:

Class Node (n):

- fields:
  - g: g cost of n, distance to start n
  - h: h cost of n, distance to end n
  - f: g+h
