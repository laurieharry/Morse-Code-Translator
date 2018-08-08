# Morse-Code-Translator
# Turns text to morse code. Potentially does the reverse in future!


def morse(a):
    return{
        'a': 'o-',
        'b': '-ooo',
        'c': '-o-o',
        'd': '-oo',
        'e': 'o',
        'f': 'oo-o',
        'g': '--o',
        'h': 'oooo',
        'i': 'oo',
        'j': 'o---',
        'k': '-o-',
        'l': 'o-oo',
        'm': '--',
        'n': '-o',
        'o': '---',
        'p': 'o--o',
        'q': '--o-',
        'r': 'o-o',
        's': 'ooo',
        't': '-',
        'u': 'oo-',
        'v': 'ooo-',
        'w': 'o--',
        'x': '-oo-',
        'y': '-o--',
        'z': '--oo',
        ' ': '       ',#space between words is 7 units
        }[a]



def pr_morse(x): 
   for a in x:
    print(morse(a), end='   ')#space between letters is 3 units

i = input("Enter a word: ")
pr_morse(i)

