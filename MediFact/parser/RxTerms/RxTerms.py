
__author__ = 'srv'

import pymongo

from db.db import DbConnection

class RxTermParser(object):

    def __init__(self):
        self.ingredient_hash={}
        self.ingredient_list=[]
        self.ingredient_rxu_hash = {}


    def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.rxterms
        self.parse_file_ing(file_name1)

        with open(file_name, "rt") as f:
            next(f)
            for line in f:
                #Create a dictionary
                RxTermDict={}
                #splits the data according to the specific delimiter.
                data = line.split('|')

                if data[0] != '':
                    RxTermDict["rxcui"] = data[0]
                    if data[0] in self.ingredient_hash:
                        RxTermDict["ingredients"] = self.ingredient_hash[data[0]]
                if data[1] != '':
                    RxTermDict["generic_rxcui"] = data[1]
                if data[2] != '':
                    RxTermDict["tty"] = data[2]
                if data[3] != '':
                    RxTermDict["full_name"] = data[3]
                if data[4] != '':
                    RxTermDict["rxn_dose_form"] = data[4]
                if data[5] != '':
                    RxTermDict["full_generic_name"] = data[5]
                if data[6] != '':
                    RxTermDict["brand_name"] = data[6]
                if data[7] != '':
                    RxTermDict["display_name"] = data[7]
                if data[8] != '':
                    RxTermDict["route"] = data[8]
                if data[9] != '':
                    RxTermDict["new_dose_form"] = data[9]
                if data[10] != '':
                    RxTermDict["strength"] = data[10]
                if data[11] != '':
                    RxTermDict["supress_for"] = data[11]
                if data[12] != '':
                    RxTermDict["display_name_synonym"] = data[12]
                if data[13] != '':
                    RxTermDict["is_retired"] = data[13]
                if data[14] != '':
                    RxTermDict["sxdg_rxcui"] = data[14]
                if data[15] != '':
                    RxTermDict["sxdg_tty"] = data[15]
                if data[16] != '':
                    RxTermDict["sxdg_name"] = data[16]
                #print(RxTermDict)
                collection.insert(RxTermDict)


    def parse_file_ing(self,file_name):
        dic_list=[]
        with open(file_name, "rt") as f:
            next(f)
            for line in f:
                #Create a dictionary
                data = line.split('|')
                rxcui = data[0]
                ingrediant = data[1]
                ing_rxcui = data[2]

                self.ingredient_rxu_hash[ing_rxcui] = ingrediant

                if rxcui not in self.ingredient_hash:
                    self.ingredient_hash[rxcui] = [ing_rxcui]
                elif rxcui in self.ingredient_hash:
                    self.ingredient_hash[rxcui].append(ing_rxcui)




#call Parse_file function.
file_name = "E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\RxTerms\\RxTermsArchive201408.txt"
file_name1 = 'E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\RxTerms\\RxTermsIngredients201408.txt'
ParserClass = RxTermParser()
ParserClass.parse_file(file_name)




