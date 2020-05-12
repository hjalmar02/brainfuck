import sys

def evaluate(script):

    script.rstrip()
    script = [char for char in script]

    # Memory array
    array = [0]

    # Pointer index
    pointer = 0

    # Script index
    i = 0

    # List of loop indexes, allows nested loops
    loops = []

    input_str = input('IN: ')
    if input_str != '':
        inputs = [int(n) for n in input_str.split(',')]

    while i < len(script):
        
        if script[i] == '[':
        
            loops.append(i + 1)

        elif script[i] == ']':

            if array[pointer] != 0:
                i = loops[-1] - 1
            else:
                loops.pop()

        elif script[i] == '>':
            pointer += 1
            if pointer == len(array):
                array.append(0)

        elif script[i] == '<':
            if pointer > 0:
                pointer -= 1

        elif script[i] == '+':
            array[pointer] += 1
        
        elif script[i] == '-':
            if array[pointer] > 0:
                array[pointer] -= 1

        elif script[i] == '.':
            print(chr(array[pointer]), end='')

        elif script[i] == ',':
            
            array[pointer] = inputs.pop(0)
        
        i += 1
    

if __name__ == '__main__':

    args = sys.argv[1:]
    
    if len(args) > 0:

        if len(args) == 1:
            with open(args[0], 'r') as file:
                script = file.read()
            evaluate(script)

        if args[0] == 'eval':
            with open(args[1], 'r') as file:
                script = file.read()
            evaluate(script)
    
    else:
        while True:
            user_input = input('\n>>> ')
            if user_input.lower() == 'exit':
                sys.exit()
            else:
                evaluate(user_input)