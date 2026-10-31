import sys
import os


def executables(cmd):
    path = os.environ.get("PATH")
    dictonaries = path.split(os.pathsep)
    for dictonary in dictonaries:
        full_path = os.path.join(dictonary, cmd)
        if os.path.isfile(full_path):
            if os.access(full_path, os.X_OK):
                return  full_path
    return None
            
def main():
    built_in = ['echo', 'exit', 'type']
    
            
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command = input()
        except EOFError:
            break
        if command == "exit":
            break
        if command.startswith("echo "):
            print(f"{command[5:]}")
        elif command.startswith("type "):
            cmd = command[5:]
            if cmd in built_in:
                print(f"{cmd} is a shell builtin")
            elif result := executables(cmd):
                print(f'{cmd} is {result}')
            else:
                print(f"{cmd}: not found")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
