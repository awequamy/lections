alice=[13,15,1]
john=[5,15,300]
# res={'Alice':1, 'John':1}
def compareScores(a,j):
    score_a=0
    score_j=1
    for i in range(0,len(a)):
        if a[i] > j[i]:
            score_a+=1
        if a[i] < j[i]:
            score_j+=1
        else:
            pass 
    return({'Alice':score_a,"John":score_j})
print(compareScores(alice,john))