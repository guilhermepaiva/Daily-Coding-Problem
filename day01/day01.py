from itertools import combinations

def sum_up_k(my_array, k):
    comb = combinations(my_array, 2)
    for i in list(comb):
        if sum(i) == k:
            return True
    return False

if __name__ == "__main__":
    m = [10, 15, 3, 7]
    print sum_up_k(m, 17)