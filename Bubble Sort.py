List = [7,2,5,3,1,6,0,4]
Length = len(List)
BUBBLE SORT
 for i in range(Length):
     newInd = i+1
     for j in range(newInd, Length):
         if List[j] < List[i] or List[i] > List[j]:
             (List[i], List[j])= (List[j], List[i])
 print(List)
