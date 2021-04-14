import secrets

sign = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'

salt = secrets.token_hex(3) # create a salt function

print('salt: ', salt)


letter_index = dict(zip(sign, range(len(sign))))
index_letter = dict(zip(range(len(sign)), sign))

def encrypt(message, key):
    encrypted = ''

    splitMessageKey = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

    for every_split in splitMessageKey:
        i = 0
        for letter in every_split:
            number = (letter_index[letter] + letter_index[key[i]])
            encrypted += index_letter[number]
            i += 1

    return salt + encrypted

def decrypted(encM, key):
    decrypted = ''

    encM2 = encM[6:]

    splitEncM = [encM2[i:i + len(key)] for i in range(0, len(encM2), len(key))]

    for each_split in splitEncM:
        i = 0
        for letter in each_split:
            number = (letter_index[letter] - letter_index[key[i]])
            decrypted += index_letter[number]
            i += 1

    return decrypted


def main():
    mode = input('Hi, please choose you mode press (E)ncrypt or (D)ecrypt')

    if mode == 'e' or mode == 'E':
        print("Crypt mesasge: ")
        message = input('write your message: ')
        message = str(message)
        key = input('enter your secret key: ')
        key = str(key)
        print('origin message: ', message)
        encrypted_mess = encrypt(message, key)
        print ('encrypted message: ', encrypted_mess)

    elif mode == 'd' or mode == 'D':
        print ('Decrypt mode')
        encrypted_mess = input('wrtie your encrypted message: ')
        key = input('write your secret')
        print ('decrypted: ', decrypted(encrypted_mess, key))
    else:
        print('please chose mode')
main()



