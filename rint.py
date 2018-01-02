def reverse( x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = int(str(x)[::-1])
            return x if x <= 2147483647 and x >= -2147483648 else 0
        else:
            x = int("-" + str(x)[1:][::-1])
            return x if x <= 2147483647 and x >= -2147483648 else 0
print reverse(-123128936)