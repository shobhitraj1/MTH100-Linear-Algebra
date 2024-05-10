f=open("matrixinput.txt")
r=f.readline()
for char in r:
    if char.isdigit():
        rows=int(char)
c=f.readline()
for char in c:
    if char.isdigit():
        columns=int(char)
f.readline()
matrix=[]
for line in f:
    l=line.split()
    l=[int(i) for i in l]
    matrix.append(l)
print("Matrix A:")
for item in matrix:
    print(item)
"""
ELEMENTARY ROW OPERATIONS to row reduce the matrix (From David C. Lay Textbook) -
1. (Interchange) Interchange two rows.
2. (Scaling) Multiply all entries in a row by a nonzero constant.
3. (Replacement) Replace one row by the sum of itself and a multiple of another row.
"""
def RREF(M):
    m = len(M)
    n = len(M[0])
    row = 0
    for col in range(n):
        pivot = row
        for r in range(row + 1, m):
            if row == m:
                break
            if abs(M[r][col]) > abs(M[pivot][col]):
                pivot = r
        if row == m:
            break
        if M[pivot][col] == 0:
            continue
        if pivot != row:
            M[pivot], M[row] = M[row], M[pivot]
        M=[[round(i,5) for i in elmt] for elmt in M]
        div = M[row][col]
        if div == 0:
            continue
        for c in range(n):
            M[row][c] /= div
        for r in range(m):
            if r == row:
                continue
            
            mult = M[r][col]
            for c in range(n):
                M[r][c] -= mult * M[row][c]    
        row += 1
    return M

rref_matrix = RREF(matrix)
rref_matrix=[[round(i,3) for i in item] for item in rref_matrix]
print("RREF of Matrix A:")
for item in rref_matrix:
    print(item)
def find_pivots(M):
    m = len(M)
    n = len(M[0])
    pivots = []
    pivot_rows = []
    pivot_columns = []
    for i in range(m):
        for j in range(n):
            if M[i][j] != 0:
                pivots.append((i+1, j+1))
                pivot_rows.append(i+1)
                pivot_columns.append(j+1)
                break
    return pivots, pivot_rows, pivot_columns
pivots, pivot_rows, pivot_columns=find_pivots(rref_matrix)
print("The pivot positions are:")
print(pivots)
var=[i for i in range(1,columns+1)]
free_vars=[i for i in var if i not in pivot_columns]
s=f"{[0 for i in range(columns)]}"
for item in free_vars:
    l=[0 for i in range(columns)]
    for i in range(len(pivot_columns)):
        l[i]=-(rref_matrix[i][item-1])
    l[item-1]=1
    old_value=-0.0
    new_value=0.0
    if old_value in l:
        for i in range(len(l)):
            if l[i]==old_value:
                l[i]=new_value
    s=s+f"+x_{item}*{l}"
print("The general solution in parametric vector form=")
print(s)


