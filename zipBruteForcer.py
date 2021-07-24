from zipfile import ZipFile
import argparse
import sys
from time import time

AUTHOR = "Bashar Oumari"
VERSION = "2.0"
art = print("""\
                         v
                   (__)v | v
                   /\/\\_|_/
                  _\__/  |
                 /  \/`\<`)
                 \ (  |\_/
                 /)))-(  |
                / /^ ^ \ |
               /  )^/\^( |
               )_//`__>> |
                 #   #`  |  """)
parser = argparse.ArgumentParser(description="\nUsage: python zipBruteForcer.py -z <zipfile.zip> -p <passwordfile.txt>"+
                                 "\n-V " + VERSION + " by " + AUTHOR )

parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="passwordFile")

parsed_args = parser.parse_args()


try:
    ziparchiver = ZipFile(parsed_args.ziparchive)
    passfile = parsed_args.passfile
    foundpass1 = ""


except:
    print(parser.description)
    exit(0)

try:
    NFound = sum(1 for line in open(passfile, 'r'))

except Exception:
    print("Error: wordlist not found!")
    sys.exit(1)
c_t = time()
i = 0
with open(passfile, "r") as f:
    passes = f.readlines()
    print("Testing every password in the list Please be patient...")
    for line in passes:
        password = line.strip("\n")
        password = password.encode("utf-8")

        try:
            foundpass1 = ziparchiver.extractall(pwd=password)
            tT = time() - c_t
            if foundpass1 is None:
                print("\n# Found password:", password.decode())
                print("\n# Took", round(tT, 2), "seconds to crack the password")
                print()
                quit()
        except Exception:
            pass

    if foundpass1 == "":
        print("\nPassword not found. Try a bigger password list.")
        quit()


