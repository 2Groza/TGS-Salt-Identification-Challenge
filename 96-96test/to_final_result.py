def to_final_result(line):
    i = 1
    starts = []
    lenths = []
    while i<=len(line):
        j = 0
        if line[i-1] == 1:
            starts.append(i)
            j = 1
            if i<len(line):
                while line[i-1+j]==1:
                    j+=1
                    if i-1+j>= len(line):
                        break
            lenths.append(j)
        i += j+1
    comma_split = []
    for i in range(len(starts)):
        comma_split.append(starts.pop(0))
        comma_split.append(lenths.pop(0))
    return comma_split
