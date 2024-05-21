# Ex 1
#  Գրել հետևյալ ծրագիրը,
#    - բացել jupyter notebook-ը,
#    - գեներացնել list, որը կպարունակի 1-ից 1_000_000 միջակայքում գտնվող կենտ թվերը,
#    - պահել գեներացված list-ը համապատասխան ֆորմատով համակարգչի մեջ data անունով,
#    - բացել pycharm-ը,
#    - pycharm-ում կարդալ data ֆայլը,
#    - կարդացած list-ում կթողնի միայն 3-ի բաժանվող թվերը,
#    - կտպի ստացված list-ի արժեքների միջին թվաբանականը

# odd_numbers = [i for i in range(1, 1000001, 2)]

# with open("data.txt", "w") as f:
#     for i in odd_numbers:
#         f.write(str(i) + "\n")


# with open("data.txt", "r") as f:
#     data = f.readlines()
#     print(data)
#     data = [int(x.strip()) for x in data]
#     print(data)

# devide_to_three = [num for num in data if num % 3 == 0]

# if devide_to_three:
#     mean = sum(devide_to_three) / len(devide_to_three)
#     print(mean)





# Ex 2
# Գրել ծրագիր, որը․
#    - հետևյալ dict_1-ից կստանա նոր dict_2 այնպես, որ dict_2-ի key-երը լինեն dict_1-ի value-ները, 
#      իսկ value-ները՝ dict_1-ի value-ների երկարությունները

# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# dict_2 = {value: len(value) for value in dict_1.values()}
# print(dict_2)





# Ex 3
# Գրել ֆունկցիա, որը․
#    - կֆիլտրի տրված dictionary-ի value-ները, թողնելով միայն կենտ թվերը,
#    - կվերադարձնի ստացված dictionary-ն,

def filter_data(dictionary):
    filtered_dict = {}
    for key, value in dictionary.items():
        filtered_values = [num for num in value if num % 2 != 0]
        filtered_dict[key] = filtered_values
    return filtered_dict

data = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}

filtered_result = filter_data(data)
print(filtered_result)