# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text) :
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
             opening_brackets_stack.append(Bracket(next,i+1))

        if next in ")]}":
            if not are_matching(opening_brackets_stack [-1]. char , next):
                return  i + 1
            if not opening_brackets_stack :
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack :
        return opening_brackets_stack [-1].position
    else : 
        return "Success"


def main() :
    do= input("I" or "F")
    if "I"  in do :
        text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success" :
        print ("Success")
    elif "F" in do :
        name = input("Enter name :")
    with open(name, "r", encoding = "latin1") as file :
            text = file.read()
            mismatch = find_mismatch(text)
            if mismatch == "Success" :
                print ("Success")
            else : print(mismatch)

if __name__ == "__main__":
    main()
