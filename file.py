filename = str(input('Enter the file name: '))
try:
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(line)


except FileNotFoundError:
    print('The file does not exist')
except PermissionError:
    print("You don't have the permission to open the file")
except (IOError, OSError):
    print("You have encountered a system error")
except Exception:
    print("Unexpected error occured")