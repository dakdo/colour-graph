import pprint

def solve(n, k, G):
    free_colours = range(0, k)
    vertices = {}
    for i in range(len(G)):
        unassigned_var = G[i][1:]
        vertices[G[i][0]]=[None, unassigned_var, free_colours]
    # unsolveable =empty list
	# return solution # solution is a list of pairs (each vertex and a colour) 
    return vertices

n = 3
k = 3
G = [[1,2,3],[2,1,3],[3,1,2]]
solution = solve(n, k, G)
print(solution)

def backtrack():
    return None

def constraint(vertices):
    return None

def selectvertex():
    return None

def mrv(vertices): #return variable with least amount of colour options
    


