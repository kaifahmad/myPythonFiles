# 2D list
number_grid=[[1,2,3],[1,3,6],[2,4,8]]
# accessing 2d list
# Its basically a MAtrix
print(number_grid[0][2])

# lets make a nested loop using for
for i in number_grid :
    for j in i :
        print(j)

# Small project to build a Translator
# Replaces AUEIO WITH G
def translate (phrase) :
    result=""
    for c in phrase :
        if c in "AEIOUaeiou" :
            result=result+"g"
        else :
            result=result+c
    return result

print(translate("Kaif"))

