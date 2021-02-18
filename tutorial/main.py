''''
    For the purposes of this project, we'll treat all the words in Frankenstein as case-insensitive.
    A method is a function that is attached to an object. In this case, the object is the string.


    Outline
            This program can be divided into two phases:

            Gather input (read file and build dictionary)
            Process user input (report results)

'''
from pip._vendor.distlib.compat import raw_input


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


'''
    Gather input
    Using the open file, read all the lines at once using .readlines(). 
    Having done so, use a for loop to enumerate the words building the dictionary as you go. 
    In this case, the dictionary will map keys (words) to integers (the count of each word).
    
    Remember to strip new lines and to smash all words to lower case.
'''
def readfile():
    myfile = open('words.txt', 'r')
    line = myfile.readline()
    line = line.lower()
    words = []
    words.append(line)
    count =0
    while line:
        count += 1
        #print("Line{}: {}".format(count, line.strip()))
        line = myfile.readline()
        line = line.lower()
        words.append(line)

    myfile.close()

    #read how many times a word is been counted in a file
    total = 0
    test = True

    while True:
        which_word = raw_input('Which word you want to count(QUIT exits) : ')
        which_word.lower()
        if which_word.strip() == 'quit':
            break
        else:
            with open('words.txt') as f:
                    for line in f:
                        line = line.lower()
                        found = line.find(which_word)
                        if found != -1 and found != 0:
                            total += 1 #1+1
            print('The word', which_word, 'is found', total, 'times')
            #which_word = input('Which word you want to count(QUIT exits) : ')
            total =0



    #print('The word', which_word, 'is found', total, 'times')


'''
    Process user input
    In this phase, your program must loop over and over until the user enters "QUIT".  The looping construct to use is the while loop. 
'''

def readuser():
    how_many = int(input('How many words you want to insert?'))
    words = []
    #word=['sun', 'flower', 'sun', 'the', 'tmp' ]
    # 0, 1, 2, 3,4
    for i in range(how_many):
         word = input('Word: ')
         word = word.lower()
         if word == 'QUIT':
             break
         else:
            words.append(word)

    # count how many words
    while True:
        which_word = raw_input('Which word you want to count(QUIT exits) : ')
        which_word.lower()
        if which_word.strip() == 'quit':
            break
        else:
            total = words.count(which_word)
            print('The word',which_word, 'is found' ,total, 'times')


'''
    Output:
        Ask user which word you want to count
        Count the specific word and print how many times it was found in the input user/file.
        QUIT to terminate the program

def output(words):
    which_word = input('Which word you want to count: ')

    # count how many words
    which = words.count(which_word)

    print(which)
'''

#main method
if __name__ == '__main__':
    print_hi('PyCharm')
    readfile()

    #start = int(input('Which method you want to call, readfile[1], readuser[2]'))

    #if start == 1:
    #    readfile()
    #elif start ==2:
    #    readuser()
    #else:
    #    print('Wrong number, Try again')


