import os
import fitz

import pandas as pd
import matplotlib.pyplot as plt


class textprocessing(object):

    def __init__(self):
        
        #Config
        self.DIR_MINUTES = 'data/pdf'
        self.ls_dates_file = 'data/copom_dates.xlsx'
        self.text_data = 'data/raw_data.txt'
        self.pickle_minutes = 'data/minutes.pkl'

        # Plot display preference
        plt.rcParams["figure.figsize"] = (18,9)
        plt.style.use('fivethirtyeight')
    
    def convertpdf2text(self,
                        heading_ls):

        """
        Generates a pickle file where each row contains a minutes

        """
        
        ls_pdf = os.listdir(self.DIR_MINUTES) # Change path when doing the real script

        df = pd.read_excel(self.ls_dates_file)

        #Converting pdf to string
        col_minutes = []
        for minute in ls_pdf:
            minute_number = int(minute[:-4].split("Minutes ", 1)[1])
            path_minute = self.DIR_MINUTES +'/'+ minute
            doc = fitz.open(path_minute)
            text = ""
            for page in doc:
                text += page.get_text()

            try:
                if minute_number <= 44:
                    #Saving raw content into .txt
                    text_file = open(self.text_data, "w", encoding="utf-8")
                    n = text_file.write(text.split("Aggregate supply and demand", 1)[1])
                    text_file.close()

                elif 45 <= minute_number <= 58:
                    #Saving raw content into .txt
                    text_file = open(self.text_data, "w", encoding="utf-8")
                    n = text_file.write(text.split("Aggregate demand and supply", 1)[1])
                    text_file.close()
                
                elif 59 <= minute_number < 83:
                    #Saving raw content into .txt
                    text_file = open(self.text_data, "w", encoding="utf-8")
                    n = text_file.write(text.split("government", 1)[1])
                    text_file.close()

                else:
                    #Saving raw content into .txt
                    text_file = open(self.text_data, "w", encoding="utf-8")
                    n = text_file.write(text.split("1. ",1)[1])
                    text_file.close()
            except:
                print(f'Something went wrong with minute {minute_number}, saving NaN instead')
                text_file = open(self.text_data, "w", encoding="utf-8")
                n = text_file.write("NaN")
                text_file.close()

            #Deleting subheadings
            with open(self.text_data, "r", encoding="utf-8") as file:
                mystring = file.readlines()
                for i, line in enumerate(mystring):
                    for pattern in heading_ls:
                        if pattern in line:
                            mystring[i] = line.replace(pattern,"")
                text_2 = "".join(mystring)

                #Save each minute as a row in a dataframe (copom dates)
                col_minutes.append(text_2)

        # Save df as a pickle
        df['minutes'] = pd.DataFrame(col_minutes).fillna(value = 0)
        df.to_pickle(self.pickle_minutes)

DEBUG = True

if __name__ == "__main__":

    if DEBUG:

        myclass = textprocessing()
        myclass.convertpdf2text(heading_ls=['A) Update of economic outlook and Copom’s scenario',
                            'B) Scenarios and risk analysis ',
                            'C) Discussion about the conduct of monetary policy ', 
                            'D) Monetary policy decision ', 'bcb.gov.br'])