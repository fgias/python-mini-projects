my_dict = {"A": "one", "B": 2, "C":"two"}

copy_of_dict = my_dict.copy()

print(copy_of_dict)

copy_of_dict['A'] = 1 # update

copy_of_dict.update({"C":3}) # another way to update

print(copy_of_dict)