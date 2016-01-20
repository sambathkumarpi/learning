nt(raw_input())
student = {}
for i in range(n):
    ind = {}
    name, mark1, mark2, mark3 = raw_input().split()
    name, mark1, mark2, mark3 = [name, float(mark1),float(mark2),float(mark3)]
    ind["m1"] = mark1
    ind["m2"] = mark2
    ind["m3"] = mark3
    student[name] = ind
a = (raw_input())
z = (student[a]["m1"] + student[a]["m2"] + student[a]["m3"])/3.0
print("{0:.2f}".format(z))
