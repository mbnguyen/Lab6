#
#  PythonOrC2a.py
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

    outputFileName = "hex_dump.txt"

    input = open(str(sys.argv[1]), "rb")
    output = open(outputFileName, "wb")
    outputContent = ""
    try:
        print("\n***********************************\n")
        print("I'm reading the file " + str(input.name) + " byte by byte, and convert them to HEX:")
        for line in input:
            for c in line:
                char = ""
                char += hex(c)
                char = char.split("0x")[1]
                if c == ord("\n") or c == ord("\r"):
                    char = "\n"
                print(char, end="")
                outputContent += char
        output.write(outputContent.encode('utf-8'))

    except IOError:
        print("Cannot open the file(s). Please try again.")
    finally:
        input.close()
        output.close()

    print("\n***********************************\n")
    print("The output file: " + outputFileName)

main()
