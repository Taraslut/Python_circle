import sys

x = {}
args = sys.argv

print(args, len (args))
try:
    print("I'm here!!")
    print(args[1])
    print(x['z'])
    x = 1 / 0
except Exception:
    print("Something wrong")
    exit(3)

except ZeroDivisionError as e:
    print("Error with message:", e)
    exit(2)
except IndexError:
    print("You have no 2 arguments")
    exit(1)

