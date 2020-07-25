#
#  PythonOrC1.py
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

    outputFileName = "output.txt"
    stringToWrite = "Hello.\n" \
                    "This content will be written in a binary file.\n"

    input = open(str(sys.argv[1]), "rb")
    try:
        print("\n***********************************\n")
        print("I'm reading the file " + str(input.name) + " line by line:")
        for line in input:
            print(line)
        input.seek(0)
        print("\n***********************************\n")
        print("I'm reading the file " + str(input.name) + " using read():")
        print(input.read())
    except IOError:
        print(str(sys.argv[1]) + " doesn't exist. Please try again.")
    finally:
        input.close()

    output = open(outputFileName, "wb")
    try:
        print("\n***********************************\n")
        print("I'm writing to the file " + str(output.name) + ":")
        print(stringToWrite)
        output.write(stringToWrite.encode("ascii"))
    except IOError:
        print(outputFileName + " doesn't exist. Please try again.")
    finally:
        output.close()

    print("\n***********************************\n")
    print("The output file: " + outputFileName)
main()
