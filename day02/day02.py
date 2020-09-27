def multiply_list(ar):
    result = 1
    for i in range(len(ar)):
        result *= ar[i]
    return result

def product_except_i(ar):
    my_result = []
    for i in range(len(ar)):
        array_except_i = ar[:i] + ar[i+1:]
        my_result.append(multiply_list(array_except_i))
    return my_result


if __name__ == "__main__":
    array_test = [3, 2, 1]
    result = product_except_i(array_test)
    print result