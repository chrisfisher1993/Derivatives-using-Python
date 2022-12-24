"""We the undersigned promise that we have in good faith attempted to follow the
principles of pair programming. Although we were free to discuss ideas with others, the implementation is our own. We
have shared a common workspace (possibly virtually) and taken turns at the keyboard for the majority of the work that we
are submitting. Furthermore, any non programming portions of the assignment were
done independently. We recognize that should this not be the case, we will be subject to penalties as outlined in the
course syllabus. [Christopher Fisher & Jesus Chavez]"""

def derivative(fpoly):
    """derivative(fpoly)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the derivative polynomial. We assume zero coefficients
    are present in the coefficient list/tuple.

    Returns polynomial coefficients for the derivative polynomial.
    Example: derivative((3,4,5))  # 3 * x**2 + 4 * x**1 + 5 * x**0
    returns:  [6, 4]     # 6 * x**1 + 4 * x**0
    """
    # fpoly is type integer
    result = []
    # keep a count of the length of fpoly
    count = len(fpoly)
    # each element i in range index 0 to length of fpoly
    for i in range(len(fpoly)):
        # decrement the count so that we start with the highest exponent
        count = count - 1
        # each element i gets multiplied by count
        result.append(fpoly[i] * count)
    # return derived coefficients
    return result[:-1]


def polyval(fpoly, x):
    """polyval(fpoly, x)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the value of the polynomial at x.  We assume zero coefficients
    are present in the coefficient list/tuple.

    Example:  f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at 5
    polyval([4, 0, 9, 3], 5))
    returns 548
    """
    n = len(fpoly)
    # Declaring the result
    result = 0
    # for each i [element] in length of fpoly
    for i in range(n):
        # sum = element in fpoly
        Sum = fpoly[i]
        # Running a for loop to multiply x (n-i-1)
        # times to the current coefficient
        for j in range(n - i - 1):
            # sum * value x
            Sum = Sum * x
        # Add the sum to the result
        result = result + Sum
    return result
