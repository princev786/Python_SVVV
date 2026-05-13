#1.Positional Arguments
# def profile(name,age):
#     print("name ;",name)
#     print("age ;",age)
#     print(name,age)

# profile(24,"Aditya")

#2.default Arguments
# def profile(name,age,alive="yes"):
#     print("name ;",name)
#     print("age ;",age)
#     print("alive ;",alive)
#     print(name,age,alive)
    
# profile("Aditya",110,"no")

#3.Keyword Arguments
# def profile(name,age):
#     print("name ;",name)
#     print("age ;",age)
#     print(name,age)

# profile(age=24,name="Aditya")

#4.Multiple Arguments(*args)
# def add(*num):
#     sum=0
#     for i in num:
#         sum+=i
#     print(sum)

# add(5,10,15)

#Multiple Keyword Arguments(** kwargs)
def profile(**data):
    for i in data:
        print(data[i])


profile(name="Prince",age=24,phone="9984908383")
