#!/usr/bin/env python3
import os
import colorama
import leakz

try:
    input = raw_input
except NameError:
    pass

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def back():
    print()
    back = input('\033[92mDo you want to contunue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        menu()
    elif back[0].upper() == 'N':
        print('\033[93m[+] Remember to checkout: https://GitHackTools.blogspot.com')
        exit(0)
    else:
        print('\033[92m?')
        exit(0)

def banner():
    print("""\033[93m ___       _______   ________  ___  __    _______   ________  ________      
|\  \     |\  ___ \ |\   __  \|\  \|\  \ |\  ___ \ |\   ___ \|\_____  \     
\ \  \    \ \   __/|\ \  \|\  \ \  \/  /|\ \   __/|\ \  \_|\ \|____|\  \    
 \ \  \    \ \  \_|/_\ \   __  \ \   ___  \ \  \_|/_\ \  \ \\ \    \ \__\   
  \ \  \____\ \  \_|\ \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \_\\ \    \|__|   
   \ \_______\ \_______\ \__\ \__\ \__\\ \__\ \_______\ \_______\       ___ 
    \|_______|\|_______|\|__|\|__|\|__| \|__|\|_______|\|_______|      |\__\\
                                                                        \|__| 2.0
     A Checking tool for Hash codes, Passwords and Emails leaked
     """)

def menu():
    try:
        print("""\033[96mWhat do you want to check?
    1. Password Hashes      4. Update Leaked?
    2. Hash Leaked          5. About Author
    3, Email Leaked         6, Exit (or just need Crtl+C)
    """)

        choice = input('Enter your choice (1-6): ')
        if choice == '1':
            password = input('\nEnter or paste a password you want to check: ')
            hashs = leakz.hashes_from_password(password)
            print("""\n\033[93mIT LEAKED!!! The Hash codes of the Password is:
[-] MD5: """ + hashs['md5'] + """
[-] SHA1: """ + hashs['sha1'] + """
[-] SHA224: """ + hashs['sha224'] + """
[-] SHA256: """ + hashs['sha256'] + """
[-] SHA384: """ + hashs['sha384'] + """
[-] SHA512: """ + hashs['sha512'] + """""")
            back()

        elif choice == '2':
            hashcode = input('\nEnter or paste a hash code you want to check: ')
            passwd = leakz.password_from_hash(hashcode)
            print(
                '\n\033[93m[-] THAT HASH CODE HAS BEEN LEAKED! It means:',passwd)
            back()

        elif choice == '3':
            email = input('\nEnter or paste a email you want to check: ')
            info = leakz.leaked_mail(email)
            print("""\n\033[93m[-] THAT EMAIL HAS BEEN LEAKED!
    It was used for:""",info)
            back()

        elif choice == '4':
            os.system('sudo git pull -f')
            print('\n\033[93m[-] Leaked updated!')
            back()

        elif choice == '5':
            print("""\033[93mLeaked? 2.0 - A Checking tool for Hash codes and Passwords leaked

    AUTHOR: https://GitHackTools.blogspot.com
            https://twitter.com/SecureGF
            https://fb.com/githacktools
            https://plus.google.com/+TVT618""")
            back()

        elif choice == '6':
            print("\033[93m[+] Don't forget https://GitHackTools.blogspot.com")
            exit(0)

        else:
            print('?\n')
            menu()

    except KeyboardInterrupt:
        back()
    except leakz.exceptions.LeakzRequestException:
        print('\033[91m[!] Your Internet Offline!!!')
        exit(1)
    except leakz.exceptions.LeakzNotLeaked:
        print('\033[93m[+] Congratulations! It was not leaked!!!')
        print()
        menu()
    except leakz.exceptions.LeakzJSONDecodeException:
        print('\033[93m[+] Congratulations! It was not leaked!!!')
        print()
        menu()
    except AttributeError:
        print('\033[93m[+] Congratulations! It was not leaked!!!')
        print()
        menu()

if __name__ == "__main__":
    colorama.init()
    clear()
    banner()
    menu()
