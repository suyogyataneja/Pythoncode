"""----------------------------ASSIGNMENT-2--------------------------------------------------------"""
"""-----------------------------BUILDING A CHILD LANGUAGE ANALYSER---------------------"""
"""
NAME               : SUYOGYA TANEJA
STUDENT ID         : 28961897
START DATE         : 30/09/2018
LAST MODIFIED DATE : 10/10/2018
TASK-1             :  HANDLING WITH FILE CONTENTS AND PRE-PROCESSING
BRIF DESCRIPTION   :In this task the the data sets of SLI and TD are refined.The output of the cleaned 
                    dataset is stored in the following two files:
                        1.	SLI_CLEANED.txt
                        2.	TD_CLEANED.txt

"""

#glob module finds all the pathnames matching a specified pattern
import glob

#ALL THE DATASET IS IN THE FOLDER NAMED SLI_DATASET
code_path = glob.glob("SLI_DATASET/*.txt")
#print(code_path)

#The file SLI_CLEANED.txt is opened in WRITE mode
f1 = open("SLI_CLEANED.txt", "w")

#for loop iterates through the all the txt files in SLI_DATASET
for each in code_path:

    # each .txt file is opened in READ mode from the SLI_DATASET
    with open(each,"r") as f:

        #new_list is an empty list to append the values from the DATASET
        #new_list = []
        #readlines() reads the entire content of a file and return it as a list
        lines = f.readlines()

        # for loop is used to iterate the whole list named "lines"
        for line in lines:

            #STARTSWITH STRING METHOD check whether string starts with "*CHI:" to refine the data from every .txt file
            if line.startswith("*CHI:"):


                #strip method strip() returns a copy of the string in which all chars have
                #been stripped from the beginning and the end of the string (default whitespace characters)
                #HERE, STRIP method strips "*CHI" from the whole string after refining the data with *CHI: only
                line = line.strip("*CHI: ")

                #here, STRIP method strips \n from the entire string
                line = line.strip("\n")

                #Here,REPLACE method replaces [* m:+ed]  with [*m:+ed]
                line=line.replace("[* m:+ed]" ,"[*m:+ed]")

                # split() method splits a string into a list using
                words_list = line.split(" ")
                # print(words_list)

                #List_sli list is used to append the filtered elements
                list_sli = []

                # this loop iterates whole words_list
                for i in words_list:

                    #strip method strips the empty space
                    i = i.strip()

                    #startswith and endswith is used for filtering the string
                    if i.startswith("[") or i.endswith("]"):

                        #condition is being checked
                        if i == "[//]" or i == "[/]" or i == "[*]" or i == "[*m:+ed]":

                            #here i  is appended  appended to list_sli
                            list_sli.append(i)

                    #here,condition is being checked
                    #startswith and endswith is used for filtering the string
                    elif i.startswith("<") or i.endswith(">"):

                        #">" and "<" is removed from the string
                        i = i.strip("<")
                        i = i.strip(">")
                        # print(i)

                        # here i  is appended  appended to list_sli
                        list_sli.append(i)

                    #here, condition is being checked

                    elif i == "(.)":
                        list_sli.append(i)
                    else:

                        # startswith and endswith is used for filtering the string
                        if not i.startswith("&") and not i.startswith("+"):
                            i = i.replace("(", "")
                            i = i.replace(")", "")
                            # print(i)
                            list_sli.append(i)


                #The join() method is a string method and returns a
                # string in which the elements of sequence have been joined by str separator.
                str2 = ' '.join(list_sli)

                str2 = str2.replace("[*m:+ed]", "[* m:+ed]")

                print(str2)

                #str2 output is wrritten to the file  one line at a time.
                f1.write(str2 + "\n")

##################################################################
#################-----------TD FILE-------############################


#ALL THE DATASET IS IN THE FOLDER NAMED TD_DATASET
code_path_TD = glob.glob("TD_DATASET/*.txt")
print(code_path_TD)

#The file TD_CLEANED.txt is opened in WRITE mode
f2 = open("TD_CLEANED.txt", "w")


#for loop iterates through the all the txt files in TD_DATASET
for each1 in code_path_TD:

    # each .txt file is opened in READ mode from the TD_DATASET
    with open(each1,"r") as f3:
        # new_list_td is an empty list to append the values from the DATASET
        #new_list_TD = []
        lines_TD = f3.readlines()

        # for loop is used to iterate the whole list named "lines"
        for line1 in lines_TD:

            # STARTSWITH STRING METHOD check whether string starts with "*CHI:" to refine
            #  the data from every .txt file
            if line1.startswith("*CHI:"):

                #strip method strip() returns a copy of the string in which all chars have
                #been stripped from the beginning and the end of the string (default whitespace characters)
                #HERE, STRIP method strips "*CHI" from the whole string after refining the data with *CHI: only

                line1 = line1.strip("*CHI: ")
                line1 = line1.strip("\n")

                line1=line1.replace("[* m:+ed]" , "[*m:+ed]")

                words_list_sl = line1.split(" ")
                # print(words_list)
                list_TD = []
                for k in words_list_sl:
                    k = k.strip()
                    if k.startswith("[") or k.endswith("]"):
                        if k == "[//]" or k == "[/]" or k == "[*]" or k == "[*m:+ed]":
                            list_TD.append(k)

                    elif k.startswith("<") or k.endswith(">"):
                        k = k.strip("<")
                        k = k.strip(">")
                        # print(i)
                        list_TD.append(k)

                    elif k == "(.)":
                        list_TD.append(k)
                    else:
                        if not k.startswith("&") and not k.startswith("+"):
                            k = k.replace("(", "")
                            k = k.replace(")", "")
                            # print(i)
                            list_TD.append(k)

                # The join() method is a string method and returns a
                # string in which the elements of sequence have been joined by str separator.
                str_TD = ' '.join(list_TD)
                str_TD = str_TD.replace("[*m:+ed]", "[* m:+ed]")
                print(str_TD)

                # str_TS output is wrritten to the file  one line at a time.
                f2.write(str_TD + "\n")