import time

def leastconstraining_colour(G, next_vertex, vertices, colours_available):
    neighbouring_vertices = G[next_vertex][1:]
    lowest_changes = None

    for colour in colours_available:
        colour_count = 0
        for neighbour in neighbouring_vertices:
            if vertices[neighbour-1][2] is not None:
                if colour in vertices[neighbour-1][2]:
                    colour_count += 1
        if lowest_changes is None:
            lowest_changes = colour_count
            optimal_colour = colour
        elif colour_count < lowest_changes:
            lowest_changes = colour_count   
            optimal_colour = colour

    return optimal_colour

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

    mrv = min(free_colours_total)
    
    mrv_list = []
    for vertex in vertex_mrv_list:
        if vertex[1] == mrv: 
            mrv_list.append(vertex[0])

    chosen_vertex = tiebreaker(vertices, mrv_list)

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
        neighbour_index = neighbour-1 # Needs to match vertex to its index
        if vertices[neighbour_index][2] is not None:
            if colour in vertices[neighbour_index][2]:
                vertices[neighbour_index][2].remove(colour)
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
        colours_available = []
        for colour in vertices[next_vertex][2]:
            if isConsistent(G, next_vertex, vertices, colour):
                colours_available.append(colour)

        present_vertices = vertices[:]
        for colour in present_vertices[next_vertex][2]:
            leastconstrainingcolour = leastconstraining_colour(G, next_vertex, vertices, colours_available)
            if isConsistent(G, next_vertex, vertices, leastconstrainingcolour):
                current_vertices = vertices[:]
                vertices = update_vertices(G, next_vertex, leastconstrainingcolour, vertices)
                solution = backtrack(G, vertices)
                if solution:
                    return solution
                vertices = current_vertices
            if leastconstraining_colour in colours_available:
                colours_available.remove(leastconstraining_colour)
    return solution

def solve(n, k, G):
    free_colours = range(0, k)
    vertices = []
    for i in range(len(G)):
        unassigned_var = G[i][1:]
        vertices.append([None, unassigned_var, free_colours[:]])
    solution = backtrack(G, vertices)
    # Increment colours by 1 to conform to output standard
    proper_solution = []
    if solution:
        for s in solution:
            proper_solution.append((s[0],s[1]+1))
    return proper_solution

# SUCCESS
n = 5
k = 3
G = [[1,2,3], [2,1,3], [3,1,2], [4,5], [5,4]]

# SUCCESS
# n = 4
# k = 2
# G = [[1,2,3],[2,1,4],[3,1,4],[4,2,3]]

# FAILS
# n = 4
# k = 2
# G = [[1,2,3],[2,1,3,4],[3,1,2,4],[4,2,3]]

# SUCCESS
# n = 10 
# k = 4
# G = [[1, 2, 3, 4, 6, 7, 10],[2, 1, 3, 4, 5, 6],[3, 1, 2],[4, 1, 2],[5, 2, 6],[6, 1, 2, 5, 7, 8],[7, 1, 6, 8, 9, 10],[8, 6, 7, 9],[9, 7, 8, 10],[10, 1, 7, 9]]

# solution = solve(n, k, G)
# print(solution)

# To test out the average time to calculate
time_elapsed = 0
t = 5
for i in range(t):
    start = time.clock()
    solution = solve(n, k ,G)
    end = time.clock()
    time_elapsed += end - start
print("Solution: ", solution)
print("Average time: ", time_elapsed/t)
