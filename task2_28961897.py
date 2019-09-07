
#--------------- ---BUILDING A CHILD LANGUAGE ANALYSER----------------------------------
"""
NAME               : SUYOGYA TANEJA
STUDENT ID         : 28961897
START DATE         : 30/09/2018
LAST MODIFIED DATE : 10/10/2018
TASK-2            :  BUILDING A CLASS FOR DATA ANALYSIS
BRIEF DESCRIPTION  :In this task the cleaned data of both the groups of children transcripts are analysed.
                    The class for  data analysis is named as STATISTICS.
"""



class Statistics:

    def __init__(self):

        #Empty dictionary to store the all the statistics
        self.the_dict=dict()

        #A empty list is used to store the value of LENGTH OF THE TRANSCRIPT in a dictionary
        # where key="LENGTH OF THE TRANSCRIPT" and value is an EMPTY LIST
        self.the_dict["LENGTH OF THE TRANSCRIPT :"] = []

        #A empty list is used to store the value of SIZE OF THE VOCABULARY  in a dictionary
        # where key="SIZE OF THE VOCABULARY " and value is an EMPTY LIST
        self.the_dict["SIZE OF THE VOCABULARY :"] = []

        # A empty list is used to store the value of REPITITION OF WORDS:  in a dictionary
        # where key="REPITITION OF WORDS: "  and value is an EMPTY LIST
        self.the_dict["REPITITION OF WORDS: "] = []

        # A empty list is used to store the value of NUMBER OF RETRACING OF CERTAIN WORDS :  in a dictionary
        # where key="NUMBER OF RETRACING OF CERTAIN WORDS : "  and value is an EMPTY LIST
        self.the_dict["NUMBER OF RETRACING OF CERTAIN WORDS :"] = []

        # A empty list is used to store the value of NUMBER OF GRAMMATICAL ERRORS DETECTED:   in a dictionary
        # where key="NUMBER OF GRAMMATICAL ERRORS DETECTED: "   and value is an EMPTY LIST
        self.the_dict["NUMBER OF GRAMMATICAL ERRORS DETECTED: "] = []

        # A empty list is used to store the value of "NUMBER OF PAUSES MADE: "  in a dictionary
        # where key="NUMBER OF PAUSES MADE: "   and value is an EMPTY LIST
        self.the_dict["NUMBER OF PAUSES MADE:"] = []

        # A empty list is used to store the value of "cleaned file"   in a dictionary
        # where key="cleaned file"    and value is an EMPTY LIST
        self.the_dict["cleaned file"] = []

    def __str__(self):
        string="\t \t CLEANED FILE \t LENGTH OF THE TRANSCRIPT \t SIZE OF THE VOCABULARY \t REPITITION OF WORDS \t NUMBER OF RETRACING OF CERTAIN WORDS \t NUMBER OF GRAMMATICAL ERRORS DETECTED\t NUMBER OF PAUSES MADE:\n"
        string+="%21s"% str(self.the_dict["cleaned file"][0])
        string+="%26s"% str(self.the_dict["LENGTH OF THE TRANSCRIPT :"][0])
        string+="%20s"% str(self.the_dict["SIZE OF THE VOCABULARY :"][0])
        string += "%21s" % str(self.the_dict["REPITITION OF WORDS: "][0])
        string += "%36s" % str(self.the_dict["NUMBER OF RETRACING OF CERTAIN WORDS :"][0])
        string += "%36s" % str(self.the_dict["NUMBER OF GRAMMATICAL ERRORS DETECTED: "][0])
        string += "%36s" % str(self.the_dict["NUMBER OF PAUSES MADE:"][0]) + "\n"


        string+="%21s"% str(self.the_dict["cleaned file"][1])
        string+="%26s"% str(self.the_dict["LENGTH OF THE TRANSCRIPT :"][1])
        string+="%20s"% str(self.the_dict["SIZE OF THE VOCABULARY :"][1])
        string += "%21s" % str(self.the_dict["REPITITION OF WORDS: "][1])
        string += "%36s" % str(self.the_dict["NUMBER OF RETRACING OF CERTAIN WORDS :"][1])
        string += "%36s" % str(self.the_dict["NUMBER OF GRAMMATICAL ERRORS DETECTED: "][1])
        string += "%36s" % str(self.the_dict["NUMBER OF PAUSES MADE:"][1])

        return str(string)


    #getter method to return the dictionary
    def get_dictionary(self):
        return self.the_dict

    #Method is used to calculate the number of statements
    def len_of_transcript(self, path ):

        # The file SLI_CLEANED.txt is opened in WRITE mode
        f1 = open(path, "r")
        length1 = f1.read()
        f1.close()
        count=0
        for each in length1:
            if each == "." or each == "!" or each == "?":
                count+=1
        return count



    # method is used calculate the size of the vocabulary i.e is indicated by number of unique words
    def size_of_vocabulary(self, path ):
        f1 = open(path, "r")
        vocab = f1.read()
        f1.close()

        size1= vocab.split(" ")
        #print(size1)
        unique=set()
        for word in size1:
            if not (word=="" or word=="\t" or word=="\n"):
                unique.add(word)
        #print(unique)

        final= len(unique)
        return final


    #This method is used to calculate the repetition of certain words or phrases indicated by chat symbol [/]
    def repitition(self, path ):
        f1 = open(path, "r")
        repeate = f1.read()
        f1.close()

        repeate1 = repeate.split(" ")
        #print(repeate1)
        count1=0
        for each in repeate1:
            if "[/]" in each:
                count1+=1
        return count1

    # This method is used to calculate the retracing of certain words or phrases indicated by chat symbol [//]
    def retracing(self,path):
        f1=open(path,"r")
        retrace= f1.read()
        f1.close()

        retrace1 = retrace.split(" ")
        #print(retrace1)
        count=0

        for each in retrace1:
            if "[//]" in each:
                count+=1
        return count
        #return length1

    # This method is used to detect grammatical errors indicated by chat symbol [* m:+ed]
    def grammar_error(self,path):
        f1=open(path,'r')
        grammar=f1.read()
        f1.close()


        return grammar.count("[* m:+ed]")

    # This method is used to calculate the number of pauses made indicated by chat symbol (.)
    def pauses(self,path):

        f1=open(path,'r')
        pause=f1.read()
        f1.close()

        pause1 = pause.split(" ")

        count = 0

        for each in pause1:
            if "(.)"  in each :
                count+=1
        return count


    #This is the method that performs the analysis on a given cleaned script i.e SLI_CLEANED.txt and TD_CLEANED.txt
    #It accepts the cleaned script as the argument, and  extracts the required
    #data for analysis — all the six statistics.
    def analyse_script(self, cleaned_file):


        number_of_statements = self.len_of_transcript(cleaned_file)

        #appending the length of the transcript to number of statements
        self.the_dict["LENGTH OF THE TRANSCRIPT :"].append(number_of_statements)

        #appending the "cleaned file" to an cleaned file
        self.the_dict["cleaned file"].append(cleaned_file)

        vocabulary_size = self.size_of_vocabulary(cleaned_file)

        #appending the vocaobulary size
        self.the_dict["SIZE OF THE VOCABULARY :"].append(vocabulary_size)

        size = self.repitition(cleaned_file)

        # appending the size of repetition of words
        self.the_dict["REPITITION OF WORDS: "].append(size)

        size1 = self.retracing(cleaned_file)

        # appending the size of the number of retracing words
        self.the_dict["NUMBER OF RETRACING OF CERTAIN WORDS :"].append(size1)

        size2 = self.grammar_error(cleaned_file)

        # appending the sizef of the grammatical errors detected
        self.the_dict["NUMBER OF GRAMMATICAL ERRORS DETECTED: "].append(size2)

        pause_count = self.pauses(cleaned_file)

        # appending the pauses count
        self.the_dict["NUMBER OF PAUSES MADE:"].append(pause_count)


if __name__ =="__main__":
    #statistics class is being called by creating an object called s1
    s1=Statistics()

    #analyse_script method is being called for SL1_CLEANED
    s1.analyse_script("SLI_CLEANED.txt")

    # analyse_script method is being called for TD_CLEANED
    s1.analyse_script("TD_CLEANED.txt")

    #s1.get_dictionary()
    #s1 obeject is printed to display all the calculates statistics of SLI AND TD
    print(s1)