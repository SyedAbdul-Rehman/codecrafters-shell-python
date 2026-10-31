import sys
import os
import subprocess

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
            parts = command.strip().split()
        except EOFError:
            break
        if not parts:
            continue
        cmd = parts[0]
        args = parts[1:]
        if cmd == "exit":
            break
        if cmd == "echo":
            print(f"{command[5:]}")
        elif cmd == "type" and args:
            if args[0] in built_in:
                print(f"{args[0]} is a shell builtin")
            elif result := executables(args[0]):
                print(f'{args[0]} is {result}')
            else:
                print(f"{args[0]}: not found")
        else:
            if result := executables(cmd):
                subprocess.run(parts, executable=result)
            else:
                print(f'{cmd}: not found')


if __name__ == "__main__":
    main()
