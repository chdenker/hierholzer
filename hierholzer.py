# Algorithm of Hierholzer for finding Euler tours in an undirected graph
#
# Input: undirected graph G, connected, all vertices have even degree
# Output: An Euler tour in G, i.e. a closed trail which contains each
#           edge of G exactly once
# NOTE: The behavior is undefined if the provided graph does not
#       fulfill the specified properties.

# Overview (copied from Wikipedia):
# - Choose any starting vertex v, and follow a trail of edges from that
#   vertex until returning to v. It is not possible to get stuck at any
#   vertex other than v, because the even degree of all vertices ensures
#   that, when the trail enters another vertex w there must be an unused
#   edge leaving w. The tour formed this way is a closed tour, but may
#   not cover all the vertices and edges of the initial graph.
# - As long as there exists a vertex u that belongs to the current tour
#   but that has adjacent edges not part of the tour, start another trail
#   from u, following unused edges until returning to u, and join the tour
#   formed in this way to the previous tour.
# - Since we assume the original graph is connected, repeating the previous
#   step will exhaust all edges of the graph.

from graph import *

import copy

def hierholzer_tour(adj_list, start_vertex: str) -> list:
    next_vertex = adj_list[start_vertex].pop() # pick an adjacent vertex of start_vertex, remove the edge
    adj_list[next_vertex].remove(start_vertex) # remove opposite edge (as we have an undirected graph)
    tour = [start_vertex, next_vertex]
    while next_vertex != start_vertex:
        current_vertex = next_vertex
        next_vertex = adj_list[current_vertex].pop()
        adj_list[next_vertex].remove(current_vertex)
        tour.append(next_vertex)
    return tour

def hierholzer(g: Graph) -> list:
    adj_list = copy.deepcopy(g.adj_list)
    vertices = g.vertices

    # Find an initial tour (not necessarily containing all edges yet)
    tour = hierholzer_tour(adj_list, vertices[0])
    print("hierholzer: initial tour = ", "".join(tour))

    # If our tour does not contain all edges yet, find additional tours and
    # join them with the original tour.
    for (v_index, v) in enumerate(tour):
        # Check if v has incident edges
        if len(adj_list[v]) != 0:
            # If yes, find a tour starting from v and insert it into original tour
            v_tour = hierholzer_tour(adj_list, v)
            print("hierholzer: additional tour = ", "".join(v_tour))
            # We reverse v_tour in order to add it to the tour in the correct order
            for (u_index, u) in enumerate(reversed(v_tour)):
                # The first vertex of v_tour (since we reversed, the last index now) 
                # is already in the original tour (as it is the starting point of v_tour).
                # Thus, we don't insert it into the original tour.
                if u_index == len(v_tour) - 1:
                    continue
                tour.insert(v_index + 1, u)

    return tour

def main():
    # Test graph 1
    gstr = "a:b,c,d,i; b:a,c,d,g; c:a,b,d,f; d:a,b,c,e,f,i; e:d,f; f:c,d,e,g; g:b,f,h,i; h:g,i; i:a,d,g,h;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    tour = hierholzer(graph)
    print("".join(tour))

    # Test graph 2
    gstr = "a:b,f; b:a,c,d,e; c:b,d; d:b,c,e,f; e:b,d; f:a,d;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    tour = hierholzer(graph)
    print("".join(tour))

    # Test graph 3
    gstr = "a:b,d; b:a,c; c:b,d; d:a,c;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    tour = hierholzer(graph)
    print("".join(tour))
    
    # Test graph 4
    gstr = "a:b,d,e,f; b:a,c,d,e; c:b,d; d:a,b,c,e; e:a,b,d,f; f:a,e;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    tour = hierholzer(graph)
    print("".join(tour))

    # Test graph 5 (more complicated graph that has 2 subtours
    # which are inserted during the algorithm)
    gstr = "a:b,c,e,f,g,h; b:a,c,g,h; c:a,b,d,e,h,i; d:c,e,f,i; e:a,c,d,f; f:a,d,e,g; g:a,b,f,h; h:a,b,c,g; i:c,d;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    tour = hierholzer(graph)
    print("".join(tour))
    
if __name__ == "__main__":
    main()
