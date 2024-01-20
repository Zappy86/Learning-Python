#In python you raise exceptions, in java you throw errors

class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("Not cool man!")
    # if type(x) is not str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError, means something is probably undefined.")
except ZeroDivisionError:
    print("Please don't divide by zero, the earth goes up in flames and crashes into the sun, lots of explosions, bad times.")
except Exception as error:
    print(error)
#the else happens when there aren't any errors, as an alternative to the excepts
else:
    print("No errors!")
finally:
    print("This'll print whether or not there's an error.")