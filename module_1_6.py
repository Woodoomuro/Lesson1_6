from multiprocessing.connection import reduce_pipe_connection

my_dict={'Dima':2000,'Jeny':2001,'Oleg':1999}
print(my_dict['Dima'])
my_dict['Anton']=1998
print(my_dict)
my_dict['Vasya']=1997
my_dict['Volodya']=1996
del my_dict ['Anton']
print(my_dict)
a=my_dict.pop('Dima')
print(my_dict)
print(a)

my_set={1,2,3,4,5,6,2,4,8,9}
print(type(my_set))
print(my_set)
print(my_set.add(10))
print(my_set.add('12'))
print(my_set)