# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

#two condition criteria
#1. when we have read n number of char or 2. no char left for reading
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while n > 0:
            buf4 = [""]*4
            l = read4(buf4)
            if not l: return i #1. No char left for reading
            for j in range(min(n,l)):
                buf[i] = buf4[j]
                n -= 1
                i +=1
        return i #2. when we have read n number of char