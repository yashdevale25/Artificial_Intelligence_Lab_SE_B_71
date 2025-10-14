import math

# Define the alpha-beta pruning function
def alpha_beta(node, depth, alpha, beta, maximizingPlayer, values, tree):
    if depth == 0 or node not in tree:
        return values[node]

    if maximizingPlayer:
        value = -math.inf
        for child in tree[node]:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False, values, tree))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # β cut-off
        return value
    else:
        value = math.inf
        for child in tree[node]:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True, values, tree))
            beta = min(beta, value)
            if beta <= alpha:
                break  # α cut-off
        return value


tree = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': ['I', 'J'] ,
    'E':['K' ,'L'] ,
    'F':['M' ,'N'],
    'G':['O','P']
}

# Heuristic values of the leaf nodes
values = {
    'I': 3,
    'J': 5,
    'K': 6,
    'L': 9,
    'M': 1,
    'N': 2,
    'O': 0,
    'P' :-1 
}

# Run Alpha-Beta pruning
optimal_value = alpha_beta('A', 3, -math.inf, math.inf, True, values, tree)

print("Optimal value (with Alpha-Beta Pruning):", optimal_value)

