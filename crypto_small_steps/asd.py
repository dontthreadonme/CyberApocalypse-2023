from decimal import Decimal, getcontext
e = 3
c = 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
n = 6293575298056902337592951921902985459999669338554636985271898764262424538059337910681221229085926587998597565905456957803548514189597672026251012894915403


c = Decimal(c)
e = Decimal(e)

getcontext().prec = 10000
root = pow(c, 1/e)
print(root)

m = hex(int(root))[2:-1]
m = ''.join(chr(int(m[i:i+2], 16))
            for i in range(0, len(m), 2))
print(m)
