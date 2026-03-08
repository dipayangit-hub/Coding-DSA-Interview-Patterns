def weighted_median(values, weights):
    pairs = sorted(zip(values, weights))
    total_weight = sum(weights)
    cumulative = 0

    for value, weight in pairs:
        cumulative += weight
        if cumulative >= total_weight / 2:
            return value


def optimal_control_center(x, y, premium):
    X = weighted_median(x, premium)
    Y = weighted_median(y, premium)

    total_cost = sum(
        w * (abs(X - xi) + abs(Y - yi))
        for xi, yi, w in zip(x, y, premium)
    )

    return (X, Y), total_cost


# Example
x = [1, 3, 2, 4]
y = [1, 2, 3, 4]
premium = [1, 3, 2, 4]

location, cost = optimal_control_center(x, y, premium)
print("Optimal location:", location)
print("Total cost:", cost)
