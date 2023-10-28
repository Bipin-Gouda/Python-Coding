
'''flexiple = "join are freelance community"

print(flexiple.upper())                  # FUNCTIONS
print(flexiple.lower())
print(flexiple.title())
print(flexiple)'''
x='Hello'
print(x.split())

def convertString(str):
    # Write your code here
    lst=str.split()
    s=""
    lst1=[]
    print(lst)
    for i in lst:
        lst2=[*i]
        lst2[0]=lst2[0].upper()
        lst2=s.join(lst2)
        print(lst2)
        lst1.append(lst2)
    print((" ").join(lst1))

print(convertString('d bAhGiRTWAb vbgGMnCNKY BVmGVbweFo JrOQXyIQuK RqLzyaMaN'))
'''
d MAhGiRTWAb VbgGMnCNKY BVmGVbweFo JrOQXyIQuK RqLzyaMaN
w AQUpxPqvvV JGOZZLZHdu TwmgWKgkmw jMmdDJuTfP qqXGSWrRf
W NYtZfRlNbx jkMYnpHHLo YDhykZudsA CgaVHHoTvp SgcEepwoz
J eZOlxYMuEf wgNwDueRPb IIJKOqCMEb vkCkwCKKWQ rsWeqbbWu
Q XdyjpPbRBF uXrXJNbVaX MrRkYhmZeG PDlQMBFNUg UpFmOQBPM
B oyvfItmwsS FJwQzKTGaq pUFUIVLMmZ PAZkFHDtGV mlFIDGUZn
U pCrwYBrJnD kdFjnktRfZ orMTBRAwQp SHRjFPLybA DlDivtUqk
'''