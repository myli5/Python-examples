"""
Q15. Valid ip - Write a function that validates IP addresses. 
If the IP address is valid: 
a) if it is in IPv4 format then it should return "IPv4" 
b) if it is in IPv6 format it should return "IPv6", 
Else it should return "Neither"
Time complexity: O(4 or 7) ~ O(1)
Space complexity: O(1)
"""
def validip(IP):  
    def isIPv4(s):
        try: return str(int(s)) == s and 0 <= int(s) <= 255
        except: return False
            
    def isIPv6(s):
        if len(s) > 4:return False
        try : return int(s, 16) >= 0 and s[0] != '-'
        except:return False
            
    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):return "IPv6"
    return "Neither"

assert validip("0.0.0.0") == "IPv4"
assert validip("100.2.300.3") == "Neither"
assert validip("2003:dead:bef:4dad:ab33:46:abab:62") == "IPv6"