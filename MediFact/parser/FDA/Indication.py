__author__ = 'srv'

from db.db import DbConnection

class Indication(object):

# Function to parse the txt file
     def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.indication

        with open(file_name, "rt") as f:
            #next(f)
            for line in f:

                #Create a dictionary
                indication_hash={}
                #splits the data according to the specific delimiter.
                data = line.split('$')

                if len(data[0]) != 0:
                    indication_hash["primaryid"] = data[0]
                if len(data[1]) != 0:
                    indication_hash["caseid"] = data[1]
                if len(data[2]) != 0:
                    indication_hash["indi_drug_seq"] = data[2]
                if len(data[3]) != 0:
                    indication_hash["indi_pt"] = data[3]

                #print(indication)
                collection.insert(indication_hash)


#call Parse_file function.
file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\INDI13Q4.txt"
#file_name="ind.txt"
indi_parser_obj = Indication()
indi_parser_obj.parse_file(file_name)



