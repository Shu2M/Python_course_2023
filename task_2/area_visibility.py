vid_1 = 12


def global_func():
    print('')


print(vid_1)


def func_two():
    vid_1 = 'local value'
    print(vid_1)


def global_three():
    global vid_1
    vid_1 = 'local to global'


func_two()
print(vid_1)
global_three()
print(vid_1)
