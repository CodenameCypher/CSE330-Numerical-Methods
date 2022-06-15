import math

string = '11110000'

sign = string[0]
exp = string[1:5]
mentissa = string[4:]

print(sign, exp, mentissa)

if exp == '1111':
    if mentissa == '00000000000':
        val = math.pow(-1, int(sign))*math.inf
    else:
        val = str(math.nan)
elif exp == '0000':
    # subnormal
    val = 0.0
    for i in range(len(mentissa)):
        e = (-1)*(i+1)
        val += int(mentissa[i])*math.pow(2, e)
    val *= math.pow((-1), int(sign)) * math.pow(2, -6)

else:
    val = 1.0
    for i in range(len(mentissa)):
        e = (-1)*(i+1)
        val += int(mentissa[i])*math.pow(2, e)

    e = int(exp, 2)

    val *= math.pow((-1), int(sign)) * math.pow(2, e-7)

print(val)
