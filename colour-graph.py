import pprint

def tiebreaker(vertices, mrv_list):
    if len(mrv_list) == 1:
        return mrv_list[0]
    else:
        unassigned_var_total = []
        vertex_var_list = []
        
        for v in mrv_list:
            unassigned_var_total.append(len(vertices[v][1]))
            vertex_var_list.append([v, len(vertices[v][1])])

        max_constraints = max(unassigned_var_total)
        for vertex in vertex_var_list:
            if vertex[1] == max_constraints:
                return vertex[0]


def mrv(vertices): #return variable with least amount of colour options
    free_colours_total = []
    vertex_mrv_list = []
    for v in range(len(vertices)):
        # print("vertex[2]: ")
        # print(vertex[2])
        if vertices[v][2] is not None:
            free_colours_total.append(len(vertices[v][2])) #Gets number of colours available for each unassigned vertex
            vertex_mrv_list.append([v, len(vertices[v][2])]) #Make a list that maps the vertex and the number of colours

    # print(free_colours_total)
    # mrv = min(x for x in free_colours_total if x is not None)
    mrv = min(free_colours_total)
    
    # print("mrv is: " + str(mrv))
    mrv_list = []
    print("free_colours_total")
    print(free_colours_total)
    for vertex in vertex_mrv_list:
        if vertex[1] == mrv: 
            mrv_list.append(vertex[0])
    print("Vertices with MRV:")
    print(mrv_list)

    chosen_vertex = tiebreaker(vertices, mrv_list)
    print("Chosen vertex: " + str(chosen_vertex))
    return chosen_vertex

def isConsistent(G, next_vertex, vertices, colour):
    neighbouring_vertices = G[next_vertex][1:]
    for neighbour in neighbouring_vertices:
        if vertices[neighbour-1][0] == colour:
            return False
    return True

def update_vertices(G, next_vertex, colour, vertices):
    #update possible colouring from neighbours
    updated_vertex = vertices[next_vertex]
    updated_vertex[0] = colour
    updated_vertex[2] = None
    for vertex in vertices:
        if next_vertex+1 in vertex[1]: #Have to remove vertex+1 because values stored are +1 of the index
            vertex[1].remove(next_vertex+1)

    neighbouring_vertices = G[next_vertex][1:]
    for neighbour in neighbouring_vertices:
        print("NEIGHBOURING COLOURS")
        print(vertices[neighbour-1][2])
        print("\n")
        if vertices[neighbour-1][2] is not None:
            if colour in vertices[neighbour-1][2]:
                vertices[neighbour-1][2].remove(colour)
    return vertices


def backtrack(G, vertices):
    solution = []
    solution_exists = True
    for vertex in vertices:
        if vertex[0] is None:
            solution_exists = False
   
    print("NEW SET OF VERTICES")
    print(vertices)
    print("\n")

    if solution_exists == True:
        for v in range(len(vertices)):
            solution.append((v+1, vertices[v][0]))
        return solution
    else:
        next_vertex = mrv(vertices)
        
        print("next_vertex " + str(next_vertex))
        for colour in vertices[next_vertex][2]:
            if isConsistent(G, next_vertex, vertices, colour):
                current_vertices = vertices[:]
                vertices = update_vertices(G, next_vertex, colour, vertices)
                solution = backtrack(G, vertices)
                if solution:
                    return solution
                vertices = current_vertices
                



    return solution

def solve(n, k, G):
    free_colours = range(0, k)
    # vertices = {}
    vertices = []
    for i in range(len(G)):
        unassigned_var = G[i][1:]
        # vertices[G[i][0]]=[None, unassigned_var, free_colours]
        vertices.append([None, unassigned_var, free_colours])
    # unsolveable =empty list
	# return solution # solution is a list of pairs (each vertex and a colour) 
    # solution = backtrack(G, vertices)
    solution = backtrack(G, vertices)
    return solution

# FAILS
# n = 3
# k = 2
# G = [[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]]

# SUCCESS
# n = 3
# k = 3
# G = [[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]]

n = 3
k = 2
G = [[1,2,3],[2,1,4],[3,1,4],[4,2,3]]
solution = solve(n, k, G)
print("THE FUCKING SOLUTION")
print(solution)
# for i in solution:
#     print(i)


def selectvertex():
    return None

