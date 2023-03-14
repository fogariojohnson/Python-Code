BOOK_FILE_NAME = """
Drxweiwakitw;

ur, kfi Vucirw Qruvikfioa

bj Vxrj Munnakuwihrxdk (Zucmtw) Afinnij


 HUWKIWKA

 Nikkir 1
 Nikkir 2
 Nikkir 3
 Nikkir 4
 Hfxqkir 1
 Hfxqkir 2
 Hfxqkir 3
 Hfxqkir 4
 Hfxqkir 5
 Hfxqkir 6
 Hfxqkir 7
 Hfxqkir 8
 Hfxqkir 9
 Hfxqkir 10
 Hfxqkir 11
 Hfxqkir 12
 Hfxqkir 13
 Hfxqkir 14
 Hfxqkir 15
 Hfxqkir 16
 Hfxqkir 17
 Hfxqkir 18
 Hfxqkir 19
 Hfxqkir 20
 Hfxqkir 21
 Hfxqkir 22
 Hfxqkir 23
 Hfxqkir 24




Nikkir 1

_Ku Vra. Axltnni, Iwznxwc._


Ak. Qikiraborzf, Cih. 11kf, 17—.
"""


def frequency(cipher_source):
    #To analyze the frequency of the letters
    letter_frequency = {}
    paragraph = cipher_source.lower()
    paragraph = ''.join(a for a in paragraph if a.isalpha())
    for letter in paragraph:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    sorted_letter_frequency = dict(sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True))
    frequency_table = {'a': 7.9, 'b': 1.4, 'c': 2.7, 'd': 4.1,'e': 12.2, 'f': 2.1, 'g': 1.9, 'h': 5.9, 'i': 6.8, 'j':.2,
                     'k': .8, 'l': 3.9, 'm': 2.3, 'n':6.5, 'o': 7.2, 'p': 1.8, 'q':.1, 'r': 5.8, 's': 6.1, 't': 8.8,
                     'u': 2.7, 'v': 1.0, 'w': 2.3, 'x': .2, 'y': 1.9, 'z': 1.0}
    sorted_frequency_table = dict(sorted(frequency_table.items(), key=lambda x: x[1], reverse=True))
  
    return sorted_letter_frequency


def decrypt(cipher_source):
    plain_text_alphabet = 'etrahcplnsomdiygfubwkz'
    cipher_text_alphabet = 'ikrxfhqnwauvctjzdobmel'

    cipher_to_plain = {}
    for letter in range(len(cipher_text_alphabet)):
        cipher_to_plain[cipher_text_alphabet[letter]] = plain_text_alphabet[letter]
 
    plain_text = ''
    for character in cipher_source:
        if character in cipher_to_plain:
            plain_text += cipher_to_plain[character]
        elif character.isupper():
            new_character = character.lower()
            plain_character = cipher_to_plain[new_character]
            plain_text += plain_character.upper()
        else:
            plain_text += character
    return plain_text


def main():
    cipher_source = BOOK_FILE_NAME
    print(decrypt(cipher_source))

if __name__ == "__main__":
    main()
