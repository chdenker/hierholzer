# hierholzer
# A basic implementation of the algorithm of Hierholzer

The algorithm of Hierholzer (see [wikipedia article](https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm)) is an algorithm for finding Euler tours in an undirected graph where every vertex has even degree.

Euler tours are closed trails which contain each edge of the graph exactly once.

This implementation uses a custom graph data structure and graphs are defined using strings representing an adjacency list.
A simple example would be the graph "a:b,d; b:a,c; c:b,d; d:a,c;;" for which the algorithm
finds the Euler tour "adcba".

Tours are stored using lists. A possible improvement would be to use doubly linked lists which allow O(1) insertion.
