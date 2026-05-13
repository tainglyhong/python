"""
if false:
    do something
else:
    do something
    do something
do something

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
