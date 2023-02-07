#HEADER
    #Bui Thanh Huy
    #s3740934
#Library
import string

#Function
count_words = {}    #Dictionary used to plug in words appears and amount of time it appears
def file_words(count_words):
    count = 0
    file = open("kieu.txt", "r")    # File is open
    lines = file.readlines()    # Read mutiple lines
    #print(lines)
    for data in lines:
        items = data.split()    # Split data into list
        #print(items)
        for char in items:
            #if char.isprintable() and char != ' ':
                #char.
            if char.lower() not in count_words: # If the words is not in the dictionary
                count_words[char.lower()] = 1
            elif char.lower() in count_words:   #If the words is already in the dictionary
                count_words[char.lower()] += 1
    #print(char.lower(), count_words[char.lower()])
    file.close() # File is closed

    return count_words
def in_dictionary(count_words):
    outfile = open("poem_stats.txt","w")    # Open the poem_stats.txt to write
    print("Different words are used in the poem:", len(count_words))    # Amount of words are used in the poem
    data3 = "Different words are used in the poem" + str(len(count_words)) + '\n'
    outfile.write(data3)
    count_char = {} #Dictionary used to count amount of characters of words appear in the file
    count_letter = {}    #Dictionary used to count amount of character of words appear exactly 9 times
    count_13letter = {}  # Dictionary to put in words that has length 13 and amount of times it appears.
    list_values = list(count_words.values())    # Turn the values in the count_words dictionary into a list

    for (k,v) in count_words.items():
        if v == max(list_values):   # The largest times the words in the list is the maximum of the value in the values list
            print("words appears most frequently: '",k ,"' with amount: ", max(list_values))
            data_line = "words appears most frequently: " + k + '\n'
            outfile.write(data_line)
        elif v == 9:    # If the words appear exactly 9 times
            count_letter[k] = len(k)    # INPUT the words and its length
            #print("Longest word that appears exactly 9 times: ", k)
    #print(count_letter)
    list_letter = list(count_letter)
    #print(list_letter)
    print("This is the longest word that appears exactly 9 times:", max(list_letter))
    data2 = "This is the longest word that appears exactly 9 times: " + max(list_letter) + '\n'
    outfile.write(data2)
    # Part to count longest words in the poem
    list_keys = list(count_words.keys())

    for item in list_keys:
        count_char[item] = len(item)    #Input the item and its length of characters in the word.
    list_countchar = list(count_char.values())  # Taking dictionary that count amount of words appear in the file into list of values
    list_countkeys = list(count_char.keys())    # Taking dictionary that count amount of words appear in the file into list of keys
    #print(list_countkeys)
    for item in list_countkeys:
        if len(item) == 13: # If len of the words is 13
            count_13letter[item] = count_words[item]    #Input the words that has 13 length and amount of times it appears
    #print("DICTIONARY:",count_13letter)
    max_list13 = list(count_13letter.values())

    for (k,v) in count_13letter.items():    # See in the count_13letter dictionary
        if v == max(max_list13):
            print("The 13-letter word appears most frequently is :", k)
            data_sth = "The 13-letter word appears mosth frequently is: " + k + '\n'
            outfile.write(data_sth)
    for (k,v) in count_char.items():
        if v == max(list_countchar):
            print("The longest words in the poem:",k, "with amount of characters : ", max(list_countchar))
            data1 = "The longest words in the poem" + k + '\n'
            outfile.write(data1)    # Writing into the file
    #print(count_char)

#MAIN PROGRAM
print(file_words(count_words))
in_dictionary(count_words)