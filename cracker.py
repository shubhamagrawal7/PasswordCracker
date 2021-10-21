import argparse
from itertools import product
import os

class Cracker:
    def __init__(self, args):
        self.min = args.min
        self.max = args.max
        self.chars = args.chars
        self.output = args.output

    def create_list(self):
        current_dir = os.getcwd()
        file_open = open(f"{current_dir}/{self.output}", "w")
        for length in range(self.min, self.max+1):
            for char in product(self.chars, repeat=length):
                word = ''.join(char)
                file_open.write(word + "\n")
        file_open.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Python Wordlist Generator and Cracker')
    parser.add_argument("-m", "--min", default=1, help="Enter min no of characters", type=int)
    parser.add_argument("-M", "--max", default=2, help="Enter max no of characters", type=int)
    parser.add_argument("-c", "--chars", default="abcdefghijklmnopqrstuvwxyz", help="Enter the characters to be used")
    parser.add_argument("-o", "--output", default="wordlist.txt")
    args = parser.parse_args()

    cracker = Cracker(args)
    cracker.create_list()