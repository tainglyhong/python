"""
if True:            (execute)
    do something    (print)
else:
    do something
do something        (jump to here)

if false:
    do something
else:               (execute)
    do something    (print)
do something        (jump to here)
"""

screen_width = 1080

if screen_width < 320:
    print("Mobile layout")
elif screen_width < 760:
    print("Tablet layout")
elif screen_width < 960:
    print("Desktop layout")
else:
    print("Unknow layout")