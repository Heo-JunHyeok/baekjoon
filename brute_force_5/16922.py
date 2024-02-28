import itertools

Rome = {"I": 1, "V": 5, "X": 10, "L": 50}


def diff_num(num):
    result = []
    
    for combination in itertools.combinations_with_replacement(list(Rome.keys()), num):
        sum_num=0
        for i in combination:
            sum_num+=Rome[i]
        
        if sum_num not in result:
            result.append(sum_num)
    
    return len(result)


print(diff_num(int(input())))
