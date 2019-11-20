# Propriedade Intelectual do Iargo, plz no steal :(

import copy

# Doesn't alter anything
def gauss_seidel(mat_reference, guesses):
  sol = guesses.copy()
  n = len(mat_reference)
  # while (True):  # FAZER CONDIÇÃO DE PARAGEM
  for _ in range(400):
    for i in range(n): # Linhas
      sol[i] = mat_reference[i][-1]
      for j in range(n): # Colunas
        if (i == j):
          continue
        sol[i] -= mat_reference[i][j] * sol[j]
      sol[i] /= mat_reference[i][i]
  
  return sol


def gauss_elimination(mat_reference):

  mat = copy.deepcopy(mat_reference)

  for d in range(len(mat)): # d = diagonal
    for c in range(len(mat[0]) - 1, -1, -1): # Pôr a "diagonal" desta linha a 1
      mat[d][c] = mat[d][c] / mat[d][d]
    for lin in range(d + 1, len(mat)):
      for col in range(len(mat[0]) - 1, d-1, -1):
        mat[lin][col] = mat[lin][col] - (mat[d][col] * mat[lin][d])
  
  sol = [mat[i][-1] for i in range(len(mat))]
  for d in range(len(sol)-1, -1, -1):
    for c in range(d+1, len(mat[0])-1):
      sol[d] -= sol[c]*mat[d][c]

  return sol

# Doesn't alter either sol or mat
def matrix_residue(mat, sol):
  residue = [mat[i][-1] for i in range(len(mat))]
  
  for i in range(len(mat)):
    for j in range(len(mat[0]) - 1):
      residue[i] -= mat[i][j] * sol[j]
  return residue

# Alters mat
def matrix_internal_stability(mat_reference, residue):

  mat = copy.deepcopy(mat_reference)
  for i in range(len(mat)):
    mat[i][-1] = residue[i]
  
  return gauss_elimination(mat)

# deltas: [dA, dB, dC, db]
def matrix_external_stability(mat_reference, sol, deltas):
  # A*dx + B*dy + C*dz = db - dA*x0 - dB*y0 - dC*z0
  mat = copy.deepcopy(mat_reference)

  for i in range(len(mat)):
    mat[i][-1] = deltas[-1]
    for j in range(len(sol)):
      mat[i][-1] -= deltas[j] * sol[j]

  return gauss_elimination(mat)

def gauss_elimination_cycle(mat_reference):
  solution = gauss_elimination(mat_reference)
  res = matrix_residue(mat_reference, solution)
  int_stab = matrix_internal_stability(mat_reference, res)
  return (solution, res, int_stab)

def main():
  matrix = [[9.0, 1.0, 5.0, 25.0], [1.0, 4.0, 6.0, 16.0], [2.0, 9.0, 7.0, 29.0]]
  # matrix = [[9.0, 1.0, 5.0, 25.0], [2.0, 9.0, 7.0, 29.0], [1.0, 4.0, 6.0, 16.0]] # Reordenado para Sidel
  # solution = [2, 2, 1]

  # print(gauss_seidel(copy.deepcopy(matrix), [1, 1, 1]))

  print("-----------------------")
  print("| Gauss Eliminination |")
  print("-----------------------")
  (sol, res, internal_stability) = gauss_elimination_cycle(matrix)
  print("Solution:  ", sol)
  print("Residue:   ", res)
  print("Int. Stab: ", internal_stability)

  # Para uma perturbação de |deltas|, a ext. stab é:
  deltas = [10, 10, 10, 10]
  external_stability = matrix_external_stability(matrix, sol, deltas)
  print("Ext. Stab: ", external_stability)

main()
