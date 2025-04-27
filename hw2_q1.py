MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }



def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt",
    morse_dictionary = MORSE_CODE
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    dictionary : dict
        Ditionary contaning Morse codes for every English letter
    """
    import os 
    script_path = os.path.abspath(__file__) # full path to this script
    script_dir = os.path.dirname(script_path)
    input_file = os.path.join(script_dir, input_file)
    output_file = os.path.join(script_dir, output_file) 
    # build a translation map
    morse_map = {char: code for char, code in morse_dictionary.items()} # map morse code for every letter
    morse_map[' '] = '\n' # map new line to every space
    trans_table = str.maketrans(morse_map)

    # read input file
    with open(input_file, 'r', encoding='utf-8') as fin:
        text = fin.read()
    
    text = text.replace('\n', ' ').replace('\t', ' ')  # turn all tabs and newline into single space
    text = text.upper()  # make all letters uppercase so keys match

    morse_text = text.translate(trans_table) # translate string

    morse_text = morse_text.rstrip() # strip end spaces/newlines

    # write output
    with open(output_file, 'w', encoding='utf-8') as fout:
        fout.write(morse_text)


if __name__ == "__main__":
    english_to_morse()
