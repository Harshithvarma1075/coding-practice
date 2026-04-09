'''
# convert the 12clock into 24 clock:
time_aday = input("Enter the 24 hours time: ")
parts_ = time_aday.split(":")
print(parts_)
hours_ = int(parts_[0])
min_ = int(parts_[1])
print(hours_)
print(min_)
if hours_ >= 13 and min_ < 60:
    print(f"{time_aday} converted into {hours_ - 12} : {min_} pm")
else:
    print(f"you have entered normal time or minutes are incorrect")
<------------------------------------------------------------------------------------------------------------->
List-----> collection of different data types or items inside the [] which are seperated by (,) is called list.
eg:- [1,"name",[1,2,"kartheek"],"apple"]
<------------------------------------------------------------------------------------------------------------->
list_1= [1,2,3,"Pyhton",[1,2,["Pyhton","Java"],"language"]]
print(list_1[4])
print(list_1[4][2])
print(list_1[4][2][0])
print(list_1[4][2][0][2])
<------------------------------------------------------------------------------------------------------------->

'''
'''
data_structure = [101, 202, 303, "Database", [500, 600, ["SQL", "NoSQL"], "Storage"]]
print(data_structure[4][3][1])
'''
'''
Methods of List
---------------------
Append()-----> This method used to add new items into list. it will only add the in the last position of the index
Synatx ----> variable_name.append(item)
List_2 = [1,2,3,4,5]
print(List_2)
List_2.append (67)
print(List_2)
List_2.append (679)
print(List_2)
List_2.append([1,2])
print(List_2)
---------------------
Extend()--------> This method is used to add items to list in the last index where each item or substring is the each index in the list.
Synatx ---------> variable_name.extend(item)

List_3 = [89,95,90,35]
List_3.extend("Kartheek")
print(List_3)
List_3.append(125)
List_3.extend([12,35,67,8])
print(List_3)
List_3.extend([3])
print(List_3)
---------------------
Remove()--------> This method will or will delete delete the item or a value directly
Syntax --------> variable_name.remove(item)

list_4 = [23,46,78,98,6,"Kartheek","kumar","sai"]
list_4.remove("Kartheek")
list_4.remove("kumar")
list_4.remove(46)
print(list_4)
---------------------
Pop()--------> This method will delete the item or value based on index position.
Syntax--------> Variable.pop(index value)

list_5 = [23,46,78,98,6,"Kartheek","kumar","sai"]
list_5.pop(2)
list_5.pop(6)
print(list_5)
---------------------
Mutable -----> I can directly modify on that particular variable.
Immutable -------> i cannot directly modify on that particular variable.
'''



































