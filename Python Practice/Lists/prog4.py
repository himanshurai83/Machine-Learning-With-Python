# Merge two lists and remove common elements.
lst_1 = [10, 20, 30, 40, 50, 60, 70]
lst_2 = [10, 23, 45, 70, 50]
lst_3 = lst_1+lst_2
s1 = set(lst_1)
s2 = set(lst_2)
common = s1.intersection(s2)
common_item = list(common)
print(lst_3)
for i in common_item:
    lst_3.remove(i)
print(lst_3)
