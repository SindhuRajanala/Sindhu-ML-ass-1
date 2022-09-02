from turtle import clear


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("orginal list after sort"+str(ages))
mins = min(ages)
maxs = max(ages)
print("min ages is "+str(mins))
print("max ages is:"+str(maxs))
ages.append(mins)
ages.append(maxs)
ages.sort()
print("ages after adding"+str(ages))
mid = len(ages) // 2
res = (ages[mid] + ages[~mid]) / 2
print("The median of age:"+ str(res))
avg = sum(ages) / len(ages)
print("The average is:" + str(avg) )
ranges=maxs-mins
print("The Range is "+str(ranges))