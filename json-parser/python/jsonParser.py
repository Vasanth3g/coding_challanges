import sys
import os
import catchsignal as cs

present_dir = os.getcwd()

def validatebraces():
    count = 0
    with open(present_dir + '/json-parser/test.json', 'r') as f:
        data=f.read()
        for brace in list(data):
            if brace == "{":
                count += 1
            elif brace == "}":
                count += 1
        
        if (count % 2) == 0:
            print("Valid JSON")
        else:
            print("Invalid JSON")
            

def main():
    #In this step your goal is to parse a valid simple JSON object, specifically: ‘{}’ and an invalid JSON file 
    # and correctly report which is which. So you should build a very simple lexer and parser for this step.
    validatebraces()
    if cs.GracefulDeath().receivedSignal:
        print("Graceful Shutdown")
        sys.exit(143)
            
        
if __name__ == '__main__':
    main()