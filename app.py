# weight converter exercise:
weight = input('Weight: ') #enter weight
option = input('(K)g or (L)bs: ') # indicate if its kg or lb
# convert the weight to the other option:
weight = float(weight)
if option.upper() == 'K':
    weightLB = weight / 0.45
    print('Weight in Lb:', weightLB)
elif option.upper() == 'L':
    weightKg = weight * 0.45
    print('Weight in Kg:', weightKg)
