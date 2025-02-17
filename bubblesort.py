myarr= [94,5,34,66,232,6564,32323,46,3]
arraylen = len(myarr)
print(arraylen)
for i in range(arraylen-1):
    for j in range(arraylen-i-1):
        if(myarr[j]>myarr[j+1]):
            myarr[j],myarr[j+1] = myarr[j+1],myarr[j]
print('sorted array:',myarr)