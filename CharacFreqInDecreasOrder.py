import operator


def char_frequency(str1):
    global sorted_d
    d = {}
    for n in str1.lower():
        keys = d.keys()
        if n in keys:
            d[n] += 1
            sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
        else:
            d[n] = 1
            sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_d


string = input("Input string : ")
char_frequency(string)
print("Output :")

for i in sorted_d:
    print(i, "=", sorted_d[i])
