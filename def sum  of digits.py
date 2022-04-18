def sumofdigits(number):
    modulus = 0
    sum = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number//=10
    return sum
a=sumofdigits(123)
print(a)