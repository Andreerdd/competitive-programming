def sum(idx, F):
    running_sum = 0
    while idx > 0:
        running_sum += F[idx]
        right_most_set_bit = (idx & -idx)
        idx -= right_most_set_bit
    return running_sum

def add(idx, X, F):
    while idx < len(F):
        F[idx] += X
        right_most_set_bit = (idx & -idx)
        idx += right_most_set_bit

def range_query(l, r, F):
    return sum(r, F) - sum(l - 1, F)

def main():
    n = 5

    # 1-based indexing
    arr = [-1e9, 1, 2, 3, 4, 5]
    # Initially, all the values of Fenwick tree are 0
    F = [0] * (n + 1)

    # Build the Fenwick tree
    for i in range(1, n + 1):
        add(i, arr[i], F)

    # Query the sum from index 1 to 3
    print(range_query(1, 3, F))
    # Query the sum from index 2 to 5
    print(range_query(2, 5, F))

    # Update element at index i to X
    i = 3
    X = 7
    # We have passed X - arr[i] to the add method because
    # the add method simply adds a number at a particular index.
    # If we need to update the element, we need to pass
    # the difference between the ith element and X to the add
    # method.
    add(i, X - arr[i], F)

    # Query the sum from index 1 to 3
    print(range_query(1, 3, F))
    # Query the sum from 2 to 5
    print(range_query(2, 5, F))

if __name__ == "__main__":
    main()