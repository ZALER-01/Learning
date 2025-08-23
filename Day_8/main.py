alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encryt ot 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = input("type to shift number:\n")

def encrypt(original_text , shift_text):

    chipher_text = ""
    for letters in original_text:
       shifted_position = alphabet.index(letters) + shift_text #7-> 9
       shifted_position %= len
       chipher_text += alphabet[shifted_position]

    print(f'Here is the encoded result:{chipher_text}')

    def decrypt(original_text , shift_text):
        cipher_text = "-"
        for letters in original_text-text:
            shifted_postion = alphabet.index(letters) -shift_text
            shifted_postion %= len(alphabet)
            cipher_text += alphabet[shifted_postion]
            print(f'Here is the decoded result:{cipher_text}')