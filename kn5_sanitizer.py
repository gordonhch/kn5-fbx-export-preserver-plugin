#rem ghetto function here

def del_name_dot_index(obj_name):
    # print ('--------newloop')
    for x in range(1, 99):
        num = "." + str(str(x).zfill(3))
        bname = obj_name[-4:]
        if (num == bname):
            # print ('obj_name[:-4] is ' + obj_name[:-4])
            return obj_name[:-4]
    # print ('obj_name is ' + obj_name)
    return obj_name