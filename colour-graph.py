import pprint

def tiebreaker(vertices, mrv_list):
    if len(mrv_list) == 1:
        return mrv_list[0]
    else:
        unassigned_var_total = []
        
        for vertex in vertices:
            unassigned_var_total.append(len(vertex[1]))

        max_constraints = max(unassigned_var_total)
        for i in range(len(unassigned_var_total)):
            if unassigned_var_total[i] == max_constraints:
                return i


def mrv(vertices): #return variable with least amount of colour options
    free_colours_total = []
    for vertex in vertices:
        free_colours_total.append(len(vertex[2]))
    print(free_colours_total)
    mrv = min(x for x in free_colours_total if x is not None)
    print("mrv is: " + str(mrv))
    mrv_list = []
    for i in range(len(free_colours_total)):
        if free_colours_total[i] == mrv:
            mrv_list.append(i)
    print("Vertices with MRV:")
    print(mrv_list)

    chosen_vertex = tiebreaker(vertices, mrv_list)
    print("Chosen vertex: " + str(chosen_vertex))
    return chosen_vertex

def isConsistent(G, next_vertex, vertices, colour):
    neighbouring_vertices = G[next_vertex][1:]
    for neighbour in neighbouring_vertices:
        if vertices[neighbour][0] == colour:
            return False
    return True

def update_vertices(next_vertex, colour, vertices):
    updated_vertex = vertices[next_vertex]
    updated_vertex[0] = colour
    updated_vertex[2] = None
    print("next_vertex: " + str(next_vertex+1))
    for vertex in vertices:
        if next_vertex+1 in vertex[1]:
            vertex[1].remove(next_vertex+1)
    return vertices


def backtrack(G, vertices):
    solution = []
    solution_exists = True
    for vertex in vertices:
        if vertex[0] is None:
            solution_exists = False


    if solution_exists == True:
        for v in range(len(vertices)):
            solution.append((v+1, vertices[v][0]))
        return solution
    else:
        next_vertex = mrv(vertices)
        for colour in vertices[next_vertex][2]:
            if isConsistent(G, next_vertex, vertices, colour):
                update_vertices(next_vertex, colour, vertices)

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
    solution = update_vertices(1, 1, vertices)
    print(solution)
    return solution

n = 3
k = 3
G = [[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]]
solution = solve(n, k, G)
# for i in solution:
#     print(i)


def selectvertex():
    return None

