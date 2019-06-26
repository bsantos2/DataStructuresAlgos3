def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root

    """
    if number == 0:
        return 0
    else:
        guess = float(number) / 2
        num = float(number)
        x = 0
        y = 1
        while x != y:
            ans = 0.5 * (guess + num / guess)

            x = int(guess)
            y = int(ans)

            if x != y:
                guess = ans
    return x

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")