def gauss(M):
    for d in range(len(M)):
        for c in range(len(M[0]) - 1, -1, -1):
            M[d][c] = M[d][c] / M[d][d]
            
        for lin in range(d + 1, len(M)):
            for col in range(len(M[0]) - 1, -1, -1):
                M[lin][col] = M[lin][col] - M[d][col] * M[lin][d]
                
    return M            
            
def subst(M): # Resolves the now triangularized matrix in order to the variables
    results = []
    indexes = [len(M[0]) - 2] # 2
    counter = 0
    
    for lin in M[::-1]:       
        if results != []:
            for i in indexes[::-1][0:len(indexes) - 1]:
                lin[-1] -= lin[i] * results[counter]
                counter += 1
            
        results.insert(0, lin[-1])  
        indexes.insert(0, indexes[-1] - 1)
        counter = 0
        
    return results
  
matrix = [[9, 1, 5, 25], [1,4, 6, 16], [2, 9, 7, 29]]               
final_matrix = [[9, 1, 5, 25], [1,4, 6, 16], [2, 9, 7, 29]]           
      
gauss(final_matrix)
subst(final_matrix)