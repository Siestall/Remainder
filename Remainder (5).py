try:
    len_list = int(input('Enter the length of the list: '))
    if len_list >= 0:
        res = [5*k+3 for k in range(len_list)]
        print(f'{res}\n{res[::-1]}')
    else:
        print('len_list >= 0')
except:
    print('Enter integers')
