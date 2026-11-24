#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 23th NOV 2026
# This program uses nested loops to print out integers from
# 1000 to 2000,  outputting five integers per
# line with each separated by a space
def main():
    # set loop for numbers between 1000 and 2000
    for counter in range(1000, 2001):
        print(counter, end=" ")

        # set up the if statement for cursor
        if counter % 5 == 4:
            print("")


if __name__ == "__main__":
    main()
