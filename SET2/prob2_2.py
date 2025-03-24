elements=['sodium','potassium','calcium','rubidium','livermorium']
longest=elements[0]
for x in range(len(elements)):
    if len(elements[x])>len(longest):
        longest=elements[x]
print(longest)
