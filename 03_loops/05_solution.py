# str = "TEETEER"




# for char in str:
#     if str.count(char) == 1:
#         print(char)
#         break # count is use to check hoow many times something is repeated 




str = "teeteerabcdabcd"

str_dictsnoray ={}


for char in str:
    if char in str_dictsnoray:
        str_dictsnoray[char]+=1
    else:
        str_dictsnoray[char]=1

for char in str:
    if str_dictsnoray[char]== 1:
        print(str_dictsnoray)
        print(char)
        break