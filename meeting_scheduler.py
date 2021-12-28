def diff_min(t1,t2):
    h1,m1 = [int(x) for x in t1.split(':')]
    h2,m2 = [int(x) for x in t2.split(':')]

    diff = 0

    if(h1>h2):
        return 0

    if(h2>h1):
        diff = 60*(h2-h1)

    diff = diff + (m2 - m1)

    return diff

def free_slots(cal,cal_active,meet_limit):
    cal_outp = []

    if diff_min(cal_active[0],cal[0][0]) >= meet_limit:
        cal1_outp.append([cal_active[0],cal[0][0]])

    for i in range(len(cal)-1):
        if diff_min(cal[i][1],cal[i+1][0]) >= meet_limit:
            cal_outp.append([cal[i][1],cal[i+1][0]])

    if diff_min(cal[len(cal)-1][1],cal_active[1])>= meet_limit:
        cal_outp.append([cal[len(cal)-1][1],cal_active[1]])

    return cal_outp

def common_slots(l1,l2,meet_limit):
    slots = []

    for i in range(len(l1)):
        for j in range(len(l2)):
            if diff_min(l1[i][1],l2[j][0]) == 0:
                if diff_min(l1[i][0],l2[j][0]) > 0:
                    a = l2[j][0]
                else:
                    a = l1[i][0]

                if diff_min(l1[i][1],l2[j][1]) == 0:
                    b = l2[j][1]
                else:
                    b = l1[i][1]

                if diff_min(a,b) >= meet_limit:
                    slots.append([a,b])

    return slots

if __name__ == "__main__":
    cal1 = [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
    cal1_active = ['9:00','20:00']
    cal2 = [['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
    cal2_active = ['10:00','18:30']

    meet_limit = 30
    cal1_outp = []
    cal2_outp = []
    final_outp = []

    cal1_outp = free_slots(cal1,cal1_active,meet_limit)
    cal2_outp = free_slots(cal2,cal2_active,meet_limit)

    final_outp = common_slots(cal1_outp,cal2_outp,meet_limit)

    print(final_outp)
