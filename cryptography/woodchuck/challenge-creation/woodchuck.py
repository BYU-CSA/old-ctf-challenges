import sys

def flagify(message):
    return '\n'.join('How much wood would a ' + bin(ord(c))[2:].zfill(8)[1:].replace('0', 'woodchuck could chuck ').replace('1', 'woodchuck chuck if a ') + 'wood?' for c in message)

if __name__ == "__main__":
    print(flagify(' '.join(sys.argv[1:])))