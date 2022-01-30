k = int(input())
m = int(input())
n = int(input())


def calc_mendel_first_low(dom, hetero, recess):
    """
    """
    #calculate the probability of recessive traits only
    population = dom + hetero + recess
    two_recess = (recess / population) * ((recess - 1) / (population - 1))
    two_hetero = (hetero / population) * ((hetero - 1) / (population - 1))
    hetero_recess = (recess / population) * (hetero / (population - 1)) + (hetero / population) * (recess / (population - 1))

    recess_prob = two_recess + two_hetero * 1/4 + hetero_recess * 1/2
    
    return 1- recess_prob


print(calc_mendel_first_low(k, m, n))