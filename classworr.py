name_list = ['Baraka Bala', 'Muhseen Muhammad', 'Aisha Abubakar']
number_of_names = len(name_list)
print('The number of people in this list are', number_of_names)
fname = []
lname = []

def new_list(fnames):
    for i in fnames:
        fname.append(i.split(' ')[0])
        lname.append(i.split(' ')[1])
        

new_list(name_list)
print('FIRST NAMES: ')
print(fname)
print('LAST NAMES: ')
print(lname)
        