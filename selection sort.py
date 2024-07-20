
List = [7,2,5,3,1,6,0,4]
Length = len(List)

#SELECTION SORT
 for i in range(Length):
     minInd = i
     for j in range(i+1, Length):
         if List[j] < List[minInd]:
             minInd = j
     (List[i], List[minInd])= (List[minInd], List[i])



