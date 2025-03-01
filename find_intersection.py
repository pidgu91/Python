def FindIntersection(strArr):
    arr_one = [int(x) for x in strArr[0].split(", ")]
    arr_two = [int(x) for x in strArr[1].split(", ")]
    new_list = []
    for x in arr_one:
        for y in arr_two:
            if x == y:
                new_list.append(x)
                continue
    if len(new_list) != 0:
        return new_list
    else:
        return "false"

#print(FindIntersection(["10, 3, 5, 7, 20", "1, 2, 4, 13, 15"])) # false condition
print(FindIntersection(["1, 3, 5, 7, 13", "1, 2, 4, 13, 15"])) # true condition

