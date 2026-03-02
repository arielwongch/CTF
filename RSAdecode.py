import math
from Crypto.Util.number import inverse

def find_p_q(n):

    return
    #factordb.com
    
    # possibilities = []

    # for i in range(2,math.floor(math.sqrt(n))):
    #     if n%i != 0:
    #         continue
    #     else:
    #         possibilities.append(i)
    # return possibilities


c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n = 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e = 65537

p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477

phi = (p-1)*(q-1)
d = inverse(e,phi)
print(d)
d = 36342