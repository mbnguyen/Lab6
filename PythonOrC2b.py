#
#  PythonOrC2b.py
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

    outputFileName = "de_hex.txt"

    input = open(str(sys.argv[1]), "rb")
    output = open(outputFileName, "wb")
    outputContent = ""
    try:
        print("\n***********************************\n")
        print("I'm reading the file " + str(input.name) + " byte by byte, and convert them from HEX to ASCII:\n")
        byte = input.read(1)
        while byte:
            if byte == b"\n" or byte == b"\r":
                print()
                outputContent += "\n"
            else:
                num = byte
                byte = input.read(1)
                if byte:
                    num += byte
                char = str(chr(int(num, 16)))
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
