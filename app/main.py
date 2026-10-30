import sys


def main():
    built_in = ['echo', 'exit', 'type']
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        
        command = input()
        if command == 'exit':
            break
        elif command.startswith('echo '):
            print(command[5:])
        elif command.startswith('type '):
            if command[5:].strip() in built_in:
                print(f'{command[5:]} is a shell builtin')
            else: 
                print(f'{command[5:]}: not found')
        else:
            print(f'{command}: command not found')


if __name__ == "__main__":
    main()
