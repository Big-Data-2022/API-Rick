#def test(name,*a):
#    return f'hello {name} animals'
#print(test(name='darhan'))
#def kwargs(**kwargs):
#    return kwargs.keys()
#print(kwargs(name='dar',age=16,animals=[1,2,3,4]))

#def test(a):
#    a+=1
#    print(a)
#    return test1(a)

#def test1(a):
#    a+=1
#    print(a)
#    return test(a)
#print(test(1))

#def test2():
#    return test2()
#test2()


#def define_factorial(num):
#    if num==1:
#        return num
#    else:
#        return num * define_factorial(num - 1)

#print(define_factorial(6))   #определение факториола


#def object_function(username):
#    return f'Привет {username}'

#ello_name=object_function(username=('hello_name'))
#print(hello_name('dar'))

#def hello_name(name):
#        return name

#def main_decorator(func):
#    def decore1():
#        print('Hello user')
#        func()
#        print(5*5)
#    return decore1

#def hello_name():
#    print('dar')

#get_main=main_decorator(hello_name)
#get_main()
#@main_decorator
#def hello_name2():
#    print('12345678')
#hello_name2




#ДЕКОРАТОР
#def get_main(food):
#    def get_decorator():
#        food()
#        print('onion,carrot,meat,salt')
##        print('<\_____/>')
#    return get_decorator

#@get_main
#def main():
#    print('tasty soup:)')

#main()



#def get_main(food):
#    def get_decorator(last_name,first_name):
#        print(f'Hello{last_name}{first_name}')
#        name_people(last_name,first_name)
#
#    return get_decorator

#@get_main
#def name_people(last_name,first_name):
#    print(f'my name is{last_name}{first_name}')


#name_people('dar','han')

#app=lambda x,y,z:x*y*z
#print(app(5,4,1))
#def new_year(d,m,y):
#    import datetime
#    day=31
#    mouth=12
#3    year=2022
#    d1=datetime.datetime.now().strftime('%d')
#    m1=datetime.datetime.now().strftime('%m')
#    y1=datetime.datetime.now().strftime('%Y')
#    return f'до нового года осталось {d-int(d1)}d {m-int(m1)}m {y-int(y1)}'


#print(new_year(31,1,2023))


#def main(a,n=1):
#    if n>a:
#        return
#    else:
#        print(n,end='  ')
#        main(a,n+2)
#main(20)