##Python divides the operators in the following groups:

##Arithmetic operators

##  +	Addition	x + y	
##  -	Subtraction	x - y	
##  *	Multiplication	x * y	
##  /	Division	x / y	
##  %	Modulus	        x % y	
##  **	Exponentiation	x ** y	
##  //	Floor division	x // y


##Assignment operators

##  =	    x = 5	    x = 5	
##  +=	    x += 3	    x = x + 3	
##  -=	    x -= 3	    x = x - 3	
##  *=	    x *= 3	    x = x * 3	
##  /=	    x /= 3	    x = x / 3	
##  %=	    x %= 3	    x = x % 3	
##  //=	    x //= 3	    x = x // 3	
##  **=	    x **= 3	    x = x ** 3	
##  &=	    x &= 3	    x = x & 3	
##  |=	    x |= 3	    x = x | 3	
##  ^=	    x ^= 3	    x = x ^ 3	
##  >>=	    x >>= 3	    x = x >> 3	
##  <<=	    x <<= 3	    x = x << 3

##x = 2

####x = x + 5

##x += 5

##print(x)


##Comparison operators
##returns boolean value

##==	Equal	                    x == y	
##!=	Not equal	            x != y	
##>	Greater than	            x > y	
##<	Less than	            x < y	
##>=	Greater than or equal to    x >= y	
##<=	Less than or equal to	    x <= y


##print(2 > 4)
##print(2 < 4)
##print(2 >= 2)
##print(2 <= 2)
##print(-2 <= -999999)
##print(-2 != -999999)
##print(999 == -999)


##Logical operators
##and or not

##print(2 > -4 and -9 < 0)
##print(2 > -4 and 9 < 0)

##print(2 > -4 or -9 < 0)
##print(2 > -4 or 9 < 0)

##print(not(not 2 > -4 or not -9 < 0))
##print(2 > -4 and not(9 < 0))


##Identity operators
##is is not

##a = 1
##b = a
##c = b
##d = [1,2]
##e = [1,2]

##print(a, id(a))
##print(b, id(b))
##print(c, id(c))

##print("a == b", a == b)
##print("a is b", a is b)
##print("a is not b", a is not b)

##print(d, id(d))
##print(e, id(e))

##print("d == e", d == e)
##print("d is e", d is e)
##print("d is not e", d is not e)


##Membership operators
##in not in

##name = "ocean"

##print("oc" in name)
##print("oc" not in name)


##Bitwise operators
