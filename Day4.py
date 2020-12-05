def check_cred(input):
    try:
    #birth year
        byr = int(input['byr'])
        if byr<1920 or byr>2002:
            return 0
    #issue year
        iyr = int(input['iyr'])
        if iyr < 2010 or iyr > 2020:
            return 0
    #expiration year
        eyr = int(input['eyr'])
        if eyr < 2020 or eyr > 2030:
            return 0
    #height
        unit = "" + input['hgt'][-2] + input['hgt'][-1]
        height = int(input['hgt'][:-2])
        if unit == 'cm':
            if height < 150 or height > 193:
                return 0
        elif unit == 'in':
            if height < 59 or height > 76:
                return 0
        else:
            return 0
    #hair color
        if len(input['hcl']) != 7 or input['hcl'][0] != '#':
            return 0
        int(input['hcl'][1:],16)
    #eye color
        colors = ['amb','blu','brn','gry','grn','hzl','oth']
        if input['ecl'] not in colors:
            return 0
    #pid
        if len(input['pid']) != 9:
            return 0
        int(input['pid'])
        return 1
    except:
        return 0

def handle(x):
    creds = {}
    for i in x:
        cred = i.split(":")
        creds.update({cred[0]:cred[1]})

    if 'byr' not in creds:
        return 0
    if 'iyr' not in creds:
        return 0
    if 'eyr' not in creds:
        return 0
    if 'hgt' not in creds:
        return 0
    if 'hcl' not in creds:
        return 0
    if 'ecl' not in creds:
        return 0
    if 'pid' not in creds:
        return 0
    return check_cred(creds)



file = open("C:\\Users\\mihai\\PycharmProjects\\AocDay4.2\\input.txt")

input = file.readlines()
file.close()
credentials = []
result = 0
for i in input:
    if i!='\n':
        credentials.extend(i.split())
    else:
        if handle(credentials) == 1:
            result += 1
        credentials=[]

print(result)

