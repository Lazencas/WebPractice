from unittest import result


print('hello world')
a=2
b=3
print(a+b)
a_list = ['사과','배','감']
print(a_list)
print(a_list[1])
a_list.append('수박맨')
print(a_list)
a_dict={'name':'bob', 'age':26}
print(a_dict['name'])

def sum(a,b):
    return a+b
result =sum(1,2)
print(result)

def is_adult(age):
    if age > 20:
        print('성인')
    else:
        print('청소년')
is_adult(10)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count =0
for aaa in fruits:
    if aaa == '사과':
        count+= 1
print(count)

people = [{'name': 'bob', 'age': 20}, 
{'name': 'carry', 'age': 38},
{'name': 'john', 'age': 7},
{'name': 'smith', 'age': 17},
{'name': 'ben', 'age': 27}]

for bravo in people:
    if bravo['age'] > 20:
        print(bravo['name'])