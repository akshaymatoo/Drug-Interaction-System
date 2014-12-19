__author__ = 'srv'

from db.db import DbConnection

class Therepy(object):

# Function to parse the txt file
     def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.therepy_sources

        with open(file_name, "rt") as f:
            next(f)
            for line in f:

                #Create a dictionary
                therepy_hash={}
                #splits the data according to the specific delimiter.
                data = line.split('$')

                if len(data[0]) != 0:
                    therepy_hash["primaryid"] = data[0]
                if len(data[1]) != 0:
                    therepy_hash["caseid"] = data[1]
                if len(data[2]) != 0:
                    therepy_hash["dsg_drug_seq"] = data[2]
                if len(data[3]) != 0:
                    therepy_hash["start_dt"] = data[3]
                if len(data[4]) != 0:
                    therepy_hash["end_dt"] = data[4]
                if len(data[5]) != 0:
                    therepy_hash["dur"] = data[5]
                if len(data[6]) != 0 and data[6] != '\n':
                    therepy_hash["dur_cod"] = data[6]

                collection.insert(therepy_hash)


#call Parse_file function.
file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\THER13Q4.txt"
therepy_parser_obj = Therepy()
therepy_parser_obj.parse_file(file_name)

