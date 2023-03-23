# phase 1: h all except x h last
# barrier all
# cx every 2k with last
# barrier all
# h all except last
# barrier all
# measure

comm = """
cx q[0],q[176];
cx q[2],q[176];
cx q[3],q[176];
cx q[4],q[176];
cx q[5],q[176];
cx q[6],q[176];
cx q[8],q[176];
cx q[9],q[176];
cx q[12],q[176];
cx q[13],q[176];
cx q[20],q[176];
cx q[21],q[176];
cx q[22],q[176];
cx q[28],q[176];
cx q[29],q[176];
cx q[35],q[176];
cx q[37],q[176];
cx q[38],q[176];
cx q[40],q[176];
cx q[41],q[176];
cx q[42],q[176];
cx q[43],q[176];
cx q[44],q[176];
cx q[46],q[176];
cx q[49],q[176];
cx q[50],q[176];
cx q[53],q[176];
cx q[54],q[176];
cx q[60],q[176];
cx q[61],q[176];
cx q[64],q[176];
cx q[65],q[176];
cx q[66],q[176];
cx q[67],q[176];
cx q[68],q[176];
cx q[70],q[176];
cx q[72],q[176];
cx q[73],q[176];
cx q[76],q[176];
cx q[77],q[176];
cx q[80],q[176];
cx q[81],q[176];
cx q[84],q[176];
cx q[85],q[176];
cx q[86],q[176];
cx q[92],q[176];
cx q[93],q[176];
cx q[94],q[176];
cx q[96],q[176];
cx q[98],q[176];
cx q[99],q[176];
cx q[101],q[176];
cx q[102],q[176];
cx q[104],q[176];
cx q[108],q[176];
cx q[109],q[176];
cx q[114],q[176];
cx q[115],q[176];
cx q[117],q[176];
cx q[118],q[176];
cx q[120],q[176];
cx q[121],q[176];
cx q[122],q[176];
cx q[125],q[176];
cx q[126],q[176];
cx q[128],q[176];
cx q[129],q[176];
cx q[130],q[176];
cx q[131],q[176];
cx q[132],q[176];
cx q[134],q[176];
cx q[136],q[176];
cx q[141],q[176];
cx q[142],q[176];
cx q[144],q[176];
cx q[145],q[176];
cx q[147],q[176];
cx q[148],q[176];
cx q[149],q[176];
cx q[150],q[176];
cx q[153],q[176];
cx q[158],q[176];
cx q[162],q[176];
cx q[164],q[176];
cx q[166],q[176];
cx q[171],q[176];
cx q[174],q[176];
"""

nums = []
for l in comm.strip().split("\n"):
    nums.append(int(l.split("[")[1].split("]")[0]))

ans = ""
for i in range(176):
    if i in nums:
        ans += "1"
    else:
        ans += "0"

print(ans[::-1])
