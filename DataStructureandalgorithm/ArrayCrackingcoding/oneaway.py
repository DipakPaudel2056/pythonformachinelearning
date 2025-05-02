# this is the classical problem from cracking coding interview where we are given 2 strings
# and our job is to find if the string is one edit away i.e. one insert, one delete, one replace away

# lets create a function
def oneAway(str1,str2):
    if(len(str1) == len(str2)):
        return oneEditReplace(str1,str2)
    elif (len(str1) + 1 == len(str2)):
        return oneEditInsert(str1,str2)
    elif (len(str1) - 1 == len(str2)):
        return oneEditInsert(str2,str1)
    return False

def oneEditReplace(str1,str2):
    foundDiff = False
    for x in range(len(str1)):
        if (str1[x] != str2[x]):
            if foundDiff:
                return False
            foundDiff = True
    return True

def oneEditInsert(str1,str2):
    # check if we can insert char in str1 to make str2
    index1 = 0
    index2 = 0
    while(index1 < len(str1) and index2 < len(str2)):
        if(str1[index1] != str1[index2]):
            if(index1 != index2):
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True
            
print(oneAway("pale","bale"))
print(oneAway("ski","ki"))