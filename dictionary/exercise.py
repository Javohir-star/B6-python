# fruits = ['banana', 'apple', 'orange', 'strawberry']
#
# d = {len(i): i for i in fruits}
# print(d)

d= {
    "Eshmat": {
        "math": 50,
        "science": 50
    },
    "Gulchapchap": {
        "math": 60,
        "science": 60
    }
}

for key, value in d.items():
    sum = 0
    for _, val in value.items():
        sum += val
    print(key, sum/len(value))