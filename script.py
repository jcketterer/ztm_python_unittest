def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        else: 
            return 'please enter a number'
    except ValueError as err:
        return err

print(do_stuff(-5))