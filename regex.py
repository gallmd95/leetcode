import string

s = "aaaaaa"
p = "aa*"

letters = string.ascii_lowercase
    def regex(s,p):
        status = True
        if len(s) == 0:
            return False
        for i,each in enumerate(p):
            if each in letters:
                temp = s[0]
                s = s[1:]
                status = status and True if temp == each else False
            elif each == ".":
                temp = s[0]
                s = s[1:]
                status = status and True if temp in letters else False  
            elif each == "*":
                count = 0
                c = p[i-1]
                if c in letters:
                    while len(s) > 0 and  c == s[0]:
                        s = s[1:]
                if c == ".":
                    while len(s) > 0:
                        s = s[1:]
            else:
                status = False
        return status and True if len(s) == 0 else False
print regex