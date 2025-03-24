import math
def calc_area(r):
    return math.pi*(r)**2
radius_list=[1,2,3,4,5]
area_list=[calc_area(radius_list[x]) for x in range(len(radius_list))]
print(area_list)
