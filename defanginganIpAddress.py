# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

address = "255.100.50.0"
dot = '.'
if dot in address:
    address= address.replace('.','[.]')
print(address)





#leetcode link https://leetcode.com/problems/defanging-an-ip-address/