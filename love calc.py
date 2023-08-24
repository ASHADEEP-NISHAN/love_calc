print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()
name1_split = [j for j in name1]
name2_split = [i for i in name2]
combine_name = name1_split + name2_split
list1 = ['t', 'r', 'u', 'e']
list2 = ['l', 'o', 'v', 'e']
# z=set(combine_name).intersection(set(list))
# print(name1_split)
# print()
# print(combine_name)
z = 0
for i in list1:

    while i in combine_name:
        z = z + 1
        combine_name.remove(i)
#     print(z)
# print("\n")
m = 0
for i in list2:

    while i in combine_name:
        m = m + 1
        combine_name.remove(i)
    # print(m)
percentage = str(z) + str(m)
if int(percentage) < 10 or int(percentage) > 90:
    print(f"Your score is **{percentage}**, you go together like coke and mentos.")
elif int(percentage) > 40 and int(percentage) < 50:
    print(f"Your score is **{percentage}**, you are alright together.")
else:
    print(f"Your score is **{percentage}**")