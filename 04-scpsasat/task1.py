from sympy import symbols, Matrix

lam, mu, ro = symbols('λ μ ρ')

A = Matrix.zeros(9, 9)

for i in range(3):
    A[i, i + 3] = -1 / ro
A[3, 0] = -(lam + 2 * mu)
for j in range(4, 6):
    A[j, j - 3] = -mu
A[6, 0] = -lam
A[8, 0] = - lam

print("Matrix:")
print("[" + ",\n ".join([str(list(row)) for row in A.tolist()]) + "]")
print("==============")
eigenvals = A.eigenvals()
for i, (eigval, multiplicity) in enumerate(eigenvals.items()):
    print(f"λ{i+1}: {eigval}")
