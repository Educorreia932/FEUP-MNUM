def gauss_seidel(matrix, guesses):
    result = guesses.copy()
    n = len(matrix)

    for _ in range(400):
        for i in range(n): # Linhas
            result[i] = matrix[i][-1]
            
            for j in range(n): # Colunas
                if (i == j):
                    continue
            
                result[i] -= matrix[i][j] * result[j]
            
            result[i] /= matrix[i][i] 
    
    return result

def gauss_elimination(matrix):  
    for d in range(len(matrix)): # d = diagonal
        for c in range(len(matrix[0]) - 1, -1, -1): # Pôr a "diagonal" desta linha a 1
            matrix[d][c] = matrix[d][c] / matrix[d][d]
            
        for lin in range(d + 1, len(matrix)):
            for col in range(len(matrix[0]) - 1, d -1, -1):
                matrix[lin][col] = matrix[lin][col] - (matrix[d][col] * matrix[lin][d])
    
    solution = [matrix[i][-1] for i in range(len(matrix))]
    
    for d in range(len(solution) - 1, -1, -1):
        for c in range(d + 1, len(matrix[0])-1):
            solution[d] -= solution[c] * matrix[d][c]
    
    return solution

def matrix_residue(matrix, solution):
  residue = [matrix[i][-1] for i in range(len(matrix))]
  
  for i in range(len(matrix)):
      for j in range(len(matrix[0]) - 1):
          residue[i] -= matrix[i][j] * solution[j]
      
  return residue

def matrix_internal_stability(matrix, residue):
    for i in range(len(matrix)):
        matrix[i][-1] = residue[i]
    
    return gauss_elimination(matrix)

# deltas: [dA, dB, dC, db]
def matrix_external_stability(matrix, solution, deltas):
    # A*dx + B*dy + C*dz = db - dA*x0 - dB*y0 - dC*z0
    
    for i in range(len(matrix)):
        matrix[i][-1] = deltas[-1] # B = delta
        
        for j in range(len(solution)):
            matrix[i][-1] -= deltas[j] * solution[j]

    return gauss_elimination(matrix)

def gauss_elimination_cycle(matrix):
    solution = gauss_elimination(matrix)
    result = matrix_residue(matrix, solution)
    int_stab = matrix_internal_stability(matrix, result)
    
    return (solution, result, int_stab)

def main():
  matrix = [[9, 1, 5, 25], [1, 4, 6, 16], [2, 9, 7, 29]]
  # solution = [2, 2, 1]

  (sol, res, internal_stability) = gauss_elimination_cycle(matrix)
  print("Solution:  ", sol)
  print("Residue:   ", res)
  print("Int. Stab: ", internal_stability)

  # Para uma perturbação de |deltas|, a ext. stab é:
  deltas = [10, 10, 10, 10]
  external_stability = matrix_external_stability(matrix, sol, deltas)
  print("Ext. Stab: ", external_stability)

main()
