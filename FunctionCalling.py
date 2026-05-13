#call by value(Immutable)
# def update(v):
#     v="hii"
#     print(v)

# v="hello"
# update(v)
# print(v)

#call by reference(Mutable)
def update(lst):
    lst[0]=21

lst = [10,20,30,40,50]
update(lst)
print(lst)