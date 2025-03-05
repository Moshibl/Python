str1="hello"
print(str1[::-1])
#################################
print(str1==str1[::-1])
#################################
print("".join(set(str1)))
#################################
text = "Python is a great programming language"
print(max(text.split(" ")))
#################################
tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)
print(tuple(set(tuple1).intersection(set(tuple2))))
#################################
my_dict = {"a": 10, "b": 20, "c": 5} 
print(f"Max={max(my_dict.values())} Min={min(my_dict.values())}")
#################################
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2.items())
print(dict1)
#################################
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}
print(set(dict1.keys()).intersection(set(dict2.keys())))
#################################
s= "abdulrahman"
longest = current = s[0]
for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        current += s[i]
    else:
        if len(current) > len(longest):
            longest = current
        current = s[i]

if len(current) > len(longest):
    longest = current
print(longest)