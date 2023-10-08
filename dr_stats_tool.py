### Statistics Calculator ###

import dr_stats_module as dr

print('You are now using a statistics calculator.')
print('Please enter numbers one by one. Type done when finished.')

ls = []
a = input()
a = a.strip()
st = ''

while a != 'done':
    ls.append(a)
    st = st + a
    a = input()
    a = a.strip()

#print(ls)
#print(st)

####################################################
### Checking for valid input ###

### Making sure there are no blank 'numbers' ###
while '' in ls:
    print('Your input is invalid. Try again.')

    print('\nPlease enter numbers one by one. Type done when finished.')
    a = input()
    a = a.strip()
    ls = []
    st = ''
    while a != 'done':
        ls.append(a)
        st = st + a
        a = input()
        
### Making sure all are numbers ###       
while st.isnumeric() != True:
    print('Your input is invalid. Try again.')

    print('\nPlease enter numbers one by one. Type done when finished.')
    a = input()
    a = a.strip()
    ls = []
    st = ''
    while a != 'done':
        ls.append(a)
        st = st + a
        a = input()
        
#####################################################
### Making list to store input numbers as floats ###
        
num_ls = []  
for num in ls:
    num_ls.append(float(num))
#print(num_ls)

#####################################################

### Intro ###    
print('\nPlease select the operation you wish to perform.')
print('(a): Calculate the mean.')
print('(b): Calculate the variance.')
print('(c): Calculate the standard deviation.')
print('(d): Calculate the standard error.')
print('(e): Calculate a Z-score.')
print('(f): Print a summary of the statistics.')
print('(g): Enter new set of numbers.')
print('(h): Exit calculator.')

op = input()

op = op.strip()
op = op.lower()

### Loop that allows user to keep using calculator ###
while op != 'h':
    if op == 'a':
        print(format(dr.mn(num_ls), '.5f'))
    elif op == 'b':
        print(format(dr.var(num_ls), '.5f'))
    elif op == 'c':
        print(format(dr.sd(num_ls), '.5f'))
    elif op == 'd':
        print(format(dr.se(num_ls), '.5f'))
    elif op == 'e':
        print(format(dr.zs(num_ls), '.5f'))
    elif op == 'f':
        print('Here is a summary of all available statistics:')
        print('Mean:', format(dr.mn(num_ls), '.5f'))
        print('Variance:', format(dr.var(num_ls), '.5f'))
        print('Standard Deviation:', format(dr.sd(num_ls), '.5f'))
        print('Standard Error:', format(dr.se(num_ls), '.5f'))
    elif op == 'g':
        print('Please enter numbers one by one. Type done when finished.')

        ls = []
        a = input()
        a = a.strip()
        st = ''

        while a != 'done':
            ls.append(a)
            st = st + a
            a = input()
            
        num_ls = []  
        for num in ls:
            num_ls.append(float(num))
        
        
    else:
        print('That is not valid input. Please try again.')

    print('\nPlease select the operation you wish to perform.')
    print('(a): Calculate the mean.')
    print('(b): Calculate the variance.')
    print('(c): Calculate the standard deviation.')
    print('(d): Calculate the standard error.')
    print('(e): Calculate a Z-score.')
    print('(f): Print a summary of the statistics.')
    print('(g): Enter new set of numbers.')
    print('(h): Exit calculator.')
    
    op = input()
    op = op.strip()
    op = op.lower()
        
print('You have now exited the statistics calculator. Have a nice day!')       






