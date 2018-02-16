
def threenumbers(var_a,var_b,var_c):
    if var_a > var_b:
        x = var_a
        var_a = var_b
        var_b = x

    range_between = round(abs(var_b-var_a))
    counter = 0
    a_list = range(range_between)

    for i in a_list:
        if i%var_c == 0:
            counter +=1

    return counter
