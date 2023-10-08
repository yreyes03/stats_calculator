### Module with Functions ###

import math as m

### Mean function ###

def mn(ls):
    mn_num = sum(ls)/ len(ls)
    
    return mn_num

### Standard deviation function ###

def sd(ls):
    s = sum(ls)

    sqr_ls = []
    for i in ls:
        d = (i - s)**2
        sqr_ls.append(d)

    s2 = sum(sqr_ls)

    sd_num = (s2/len(ls))**1/2

    return sd_num

### Variance function ###

def var(ls):
    s = sum(ls)

    s = sum(ls)

    sqr_ls = []
    for i in ls:
        d = (i - s)**2
        sqr_ls.append(d)

    s2 = sum(sqr_ls)

    var_num = (s2/len(ls))

    return var_num


### Standard error function ###

def se(ls):

    sd_num = sd(ls)

    se_num = sd_num/((len(ls))**(1/2))

    return se_num

### Z score function ###

def zs(ls):
    n = float(input('Please enter a new observation: '))
    m = mn(ls)
    s = sd(ls)
    
    zs_num = (n - m)/ s

    return zs_num
    












