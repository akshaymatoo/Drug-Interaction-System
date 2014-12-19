__author__ = 'srv'

from db.db import DbConnection

class Outcome(object):

# Function to parse the txt file
     def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.outcome

        with open(file_name, "rt") as f:
            next(f)
            for line in f:

                #Create a dictionary
                outcome_hash={}
                #splits the data according to the specific delimiter.
                data = line.split('$')

                if len(data[0]) != 0:
                    outcome_hash["primaryid"] = data[0]
                if len(data[1]) != 0:
                    outcome_hash["caseid"] = data[1]
                if len(data[2]) != 0 and data[2] != '\n':
                    outcome_hash["outc_cod"] = data[2]

                collection.insert(outcome_hash)


#call Parse_file function.
file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\OUTC13Q4.txt"
outcome_parser_obj = Outcome()
outcome_parser_obj.parse_file(file_name)
