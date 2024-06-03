#Given 2 n-bit binary integers represented by arrays A and B, along with the length n, how can we efficiently compute the sum of these 2 binary integers and store the result in an array

def Add_binary_int(A, B, n):
    C = [0]* (n+1)
    carry = 0
    for i in range(n-1, -1, -1):
        total = A[i] + B[i] + carry
        C[i+1] =  total % 2
        carry = total// 2
    C[0] = carry
    return C
A = [1,0,1,1] #11
B = [1,1,0,1] #13
n = len(A)
res = Add_binary_int(A, B, n)
print(res)
