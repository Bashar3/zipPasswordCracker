from zipfile import ZipFile
import argparse
import sys
from time import time

AUTHOR = "Bashar Oumari"
VERSION = "1.0"

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

with open(passfile, "r") as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode("utf-8")

        try:
            foundpass1 = ziparchiver.extractall(pwd=password)
            tT = time() - c_t
            if foundpass1 is None:
                print("\n# Found password:", password.decode())
                print("\n# Took", tT, "seconds to crack the password")
                print()
        except RuntimeError:
            pass

    if foundpass1 == "":
        print("\nPassword not found. Try a bigger password list.")
