__author__ = 'srv'

#in this file rxhash has the value and ingredient hash has the rxcui and other map
class RxTermParserIngredients(object):

    def __init__(self):
        self.ingredient_hash={}
        self.ingredient_list=[]
        self.ingredient_rxu_hash = {}
        self.parse_file(file_name)


    def getIngHash(self):
        return self.ingredient_hash

    def getIngLst(self):
        return self.ingredient_list

    def getIngRxuHash(self):
        return self.ingredient_rxu_hash

    def parse_file(self,file_name):
        dic_list=[]
        with open(file_name, "rt") as f:
            next(f)
            for line in f:
                #Create a dictionary
                data = line.split('|')
                rxcui = data[0]
                ingredient = data[1]
                ing_rxcui = data[2]

                self.ingredient_rxu_hash[ing_rxcui] = ingredient

                if rxcui not in self.ingredient_hash:
                    self.ingredient_hash[rxcui] = [ing_rxcui]
                elif rxcui in self.ingredient_hash:
                    self.ingredient_hash[rxcui].append(ing_rxcui)
        #print(self.ingredient_hash)


#call Parse_file function.
file_name = 'E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\RxTerms\\RxTermsIngredients201408.txt'

ParserClass = RxTermParserIngredients()
ParserClass.parse_file(file_name)
#print (ParserClass.getIngRxuHash())
print (ParserClass.getIngHash())