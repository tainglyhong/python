# Multiple return statements
"""
When control flow branches, like with a conditional, 
the computer may have several possible paths of execution 
through the function. Since each path is independent, 
we can safely put a return statement at the end of each one. 
For example, we can put a return statement inside each branch of a conditional.

Because a return statement immediately exits the function, 
only one return statement ever executes on any given function call. 
Each return statement represents a door we can take out of the function, but we can only use one!
"""

def get_stage_duration(stage_num):
    """Returns the number of seconds the stage lasts."""
    if stage_num == 1:
        return 120
    elif stage_num == 3:
        return 105
    elif stage_num == 2 or stage_num == 4:
        return 90

    return 60

for stage in range(8):
    seconds = get_stage_duration(stage)
    print(str(seconds) + " secs in Storm circle " + str(stage))

