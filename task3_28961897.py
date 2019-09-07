#--------------- ---BUILDING A CHILD LANGUAGE ANALYSER----------------------------------
"""
NAME               : SUYOGYA TANEJA
STUDENT ID         : 28961897
START DATE         : 30/09/2018
LAST MODIFIED DATE : 10/10/2018
TASK-3            :  BUILDING A CLASS FOR DATA VISUALISATION
BRIEF DESCRIPTION :In this task a class named Visualise has been implementated.
                    The data set of both the groups has been used to create suitable graphs using matplotlib.
"""


#Statistics class has been imported from task2_289618967 as it is required in this task to visualise the date
from  task2_28961897 import Statistics

#Pandas library has been imported to store the DataSet that is to required to plot the graph
import pandas as pd

#matplotlib library has been imported to PLOT THE GRAPH of the statistics calculated in task2
import matplotlib.pyplot as plt

#This class is used to visualise the statistics that has been calculated
class Visualise:

    def __init__(self):

        #Statistics class is being called as the data from statistics class is to be visualised
        s2=Statistics()

        #analyse_script method from Statistics class is being called visualise the data from SL1_CLEANED
        s2.analyse_script("SLI_CLEANED.txt")

        # analyse_script method from Statistics class is being called visualise the data from TD_CLEANED
        s2.analyse_script("TD_CLEANED.txt")

        #A PANDAS DATAFRAME IS CREATED TO STORE the analaysed data so that it can be plotted
        self.the_dict=pd.DataFrame(s2.get_dictionary())


     #This method presents the output in readable format and returns a formatted string
    def __str__(self):

        # string variable is used to store the formatted
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


    #This method returns the average or mean of the six statistics for each child group (i.e.
    #both the SLI and TD groups).
    def compute_averages(self):

        #statistics class is called from task2
        s2=Statistics()
        s2.analyse_script("SLI_CLEANED.txt")
        s2.analyse_script("TD_CLEANED.txt")

        #   SLI STATISTICS
        #value of length of transcript is being retrieved to calculate the average
        number_of_statements = self.the_dict["LENGTH OF THE TRANSCRIPT :"][0]

        #size of the vocabulary is being retrieved to calculate the average
        vocabulary_size = self.the_dict["SIZE OF THE VOCABULARY :"][0]

        #Repetition of words is being retrieved to calculate the average
        size = self.the_dict["REPITITION OF WORDS: "][0]

        #Number of retracing words is being retrieved to calculate the average
        size1 = self.the_dict["NUMBER OF RETRACING OF CERTAIN WORDS :"][0]

        #Number of grammatical errors  is being retrieved to calculate the average
        size2 = self.the_dict["NUMBER OF GRAMMATICAL ERRORS DETECTED: "][0]

        #Number of pauses is being retrieved to calculate the average
        pause_count = self.the_dict["NUMBER OF PAUSES MADE:"][0]

        #AVERAGE OF STATISTICS OF SLI_CLEANED DATASET IS BEING CALCULATED
        average = (number_of_statements + vocabulary_size + size + size1 + size2 + pause_count) / 6


        #-----------TD STATISTICS--------------------------------------------
        #length of transcript is being retrieved to calculate the average
        number_of_statements_TD = self.the_dict["LENGTH OF THE TRANSCRIPT :"][1]

        #SIZE OF VOCABULARY is being retrieved to calculate the average
        vocabulary_size_TD = self.the_dict["SIZE OF THE VOCABULARY :"][1]

        #REPETITION OF WORDS is being retrieved to calculate the average
        size_TD = self.the_dict["REPITITION OF WORDS: "][1]

        #NUMBER OF RETRACING OF CERTAIN WORDS is being retrieved to calculate the average
        size1_TD = self.the_dict["NUMBER OF RETRACING OF CERTAIN WORDS :"][1]

        #NUMBER OF GRAMMATICAL ERRORS DETECTED: is being retrieved to calculate the average
        size2_TD = self.the_dict["NUMBER OF GRAMMATICAL ERRORS DETECTED: "][1]

        # NUMBER OF PAUSES MADE:is being retrieve to calculate the average
        pause_count_TD = self.the_dict["NUMBER OF PAUSES MADE:"][1]

        #AVERAGE OF STATISTICS OF TD_CLEANED DATASET IS BEING CALCULATED
        average_TD = (number_of_statements_TD + vocabulary_size_TD + size_TD + size1_TD + size2_TD + pause_count_TD) / 6

        return "Average of STATISTICS OF SLI_CLEANED.txt: " + str(average)  +"\n" +"Average of STATISTICS TD_CLEANED.txt: " +str(average_TD)


    #This method constructs the BAR graph to demonstrate the mean difference between the two groups
    # i.e SLI and TD for each of the six statistic for comparison purpose.
    def visualise_statistics(self):

        self.the_dict.plot(kind='bar',figsize=(10,4))

        plt.legend(loc="best", prop={'size': 6})

        plt.xlabel('SLI STATISTICS                  Statistics                    TD STATISTICS ' )
        plt.ylabel('Frequency')
        plt.title('SLI VS TD STATISTICS')
        plt.show()

if __name__ =="__main__":
    # VISUALISE CLASS is being called and an object v1 is created
    v1=Visualise()

    # average of statistics is  PRINTED
    print(v1.compute_averages())

    #visualise method is CALLLED to DISPLAY the graphs
    print(v1.visualise_statistics())

    #print(v1)