#
#  PythonOrC2c.py
#  System Level Assignments
#
#  Created by Minh Nguyen on 7/22/20.
#  Copyright © 2020 Minh Nguyen. All rights reserved.
#
import sys

def main():
    if len(sys.argv) != 2:
        print("Please provide 1 input for this program:")
        print("   1. A name of input file.")
        print("Please run the program again.")
        return

    outputFileName = "string.txt"

    input = open(str(sys.argv[1]), "rb")
    output = open(outputFileName, "wb")
    outputContent = ""
    try:
        print("\n***********************************\n")
        print("I'm reading the file " + str(input.name) + " byte by byte, and display printable characters:\n")
        byte = input.read(1)
        while byte:
            if byte == b"\n" or byte == b"\r":
                print()
                outputContent += "\n"
            elif (ord(byte) >= 32 and ord(byte) <= 127):
                char = str(chr(ord(byte)))
                print(char, end="")
                outputContent += char
            byte = input.read(1)
        output.write(outputContent.encode('utf-8'))
    except IOError:
        print("Cannot open the file(s). Please try again.")
    finally:
        input.close()
        output.close()

    print("\n***********************************\n")
    print("The output file: " + outputFileName)

main()
