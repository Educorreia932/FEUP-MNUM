def gauss(M):
    for d in range(len(M)):
        for c in range(len(M[0]) - 1, -1, -1):
            M[d][c] = M[d][c] / M[d][d]
            
        for lin in range(d + 1, len(M)):
            for col in range(len(M[0]) - 1, -1, -1):
                M[lin][col] = M[lin][col] - M[d][col] * M[lin][d]
                
    return M            
            
def subst(M): # Resolves the now triangularized matrix in order to the variables
    first = True
    counter = 0 # For each variable x, y, z...
    
    for lin in M[::-1]:       
        if first:
            results = [M[-1][-1]]
            indexes = [len(M[0]) - 2] # 2
            first = False
            
        else:
            for i in indexes:
                lin[-1] -= lin[i] * results[counter]
                counter += 1
                
            results.insert(0, lin[-1])  
            indexes.insert(0, indexes[-1] - 1)
            counter = 0
        
    return results
  
def calculate_residue(M, M1):
    for element, element1 in zip(M, M1):
        print(element1 - element)

def extern(M):
    for element in M:
        element[-1] * 1.1

matrix = [[9, 1, 5, 25], [1,4, 6, 16], [2, 9, 7, 29]]               
final_matrix = [[9, 1, 5, 25], [1,4, 6, 16], [2, 9, 7, 29]]           
      
gauss(final_matrix)

calculate_residue(subst(final_matrix), [2, 2, 1])

