def secretnum(x):
    seq = [((x // i) + i) for i in range(1, 6)] 
    custom_sum = sum(seq)  
    nonlinear = lambda y: (y * 3) - (y // 2)
    nonlinear_result = nonlinear(x)  
    result = custom_sum + nonlinear_result - (x // 6)
    if x % 7 == 0:
        result += 1 
    result -= 4
    return result

# Test
print(secretnum(42)) 