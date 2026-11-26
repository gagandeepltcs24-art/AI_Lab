
def alpha_beta(node, depth, alpha, beta, maximizing):

    if depth == 3:
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(
                value,
                alpha_beta(child, depth + 1, alpha, beta, False)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruned:", child)
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(
                value,
                alpha_beta(child, depth + 1, alpha, beta, True)
            )

            beta = min(beta, value)

            if beta <= alpha:
                print("Pruned:", child)
                break

        return value


tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

result = alpha_beta(
    tree,
    0,
    float('-inf'),
    float('inf'),
    True
)



print("Optimal value:", result)



output:
Pruned: 6
Pruned: [1, 2]
Optimal value: 5
