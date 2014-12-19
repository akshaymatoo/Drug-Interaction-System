__author__ = 'srv'

from db.db import DbConnection

class Demographic(object):

# Function to parse the txt file
     def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.demographic

        with open(file_name, "rt") as f:
            next(f)
            for line in f:

                #Create a dictionary
                demographic_hash={}
                #splits the data according to the specific delimiter.
                data = line.split('$')

                if len(data[0]) != 0:
                    demographic_hash["primaryid"] = data[0]
                if len(data[1]) != 0:
                    demographic_hash["caseid"] = data[1]
                if len(data[2]) != 0:
                    demographic_hash["caseversion"] = data[2]
                if len(data[3]) != 0:
                    demographic_hash["i_f_code"] = data[3]
                if len(data[4]) != 0:
                    demographic_hash["event_dt"] = data[4]
                if len(data[5]) != 0:
                    demographic_hash["mfr_dt"] = data[5]
                if len(data[6]) != 0:
                    demographic_hash["init_fda_dt"] = data[6]
                if len(data[7]) != 0:
                    demographic_hash["fda_dt"] = data[7]
                if len(data[8]) != 0:
                    demographic_hash["rept_cod"] = data[8]
                if len(data[9]) != 0:
                    demographic_hash["mfr_num"] = data[9]
                if len(data[10]) != 0:
                    demographic_hash["mfr_sndr"] = data[10]
                if len(data[11]) != 0:
                    demographic_hash["age"] = data[11]
                if len(data[12]) != 0:
                    demographic_hash["age_cod"] = data[12]
                if len(data[13]) != 0:
                    demographic_hash["gndr_cod"] = data[13]
                if len(data[14]) != 0:
                    demographic_hash["e_sub"] = data[14]
                if len(data[15]) != 0:
                    demographic_hash["wt"] = data[15]
                if len(data[16]) != 0:
                    demographic_hash["wt_cod"] = data[16]
                if len(data[17]) != 0:
                    demographic_hash["rept_dt"] = data[17]
                if len(data[18]) != 0:
                    demographic_hash["to_mfr"] = data[18]
                if len(data[19]) != 0:
                    demographic_hash["occp_cod"] = data[19]
                if len(data[20]) != 0:
                    demographic_hash["reporter_country"] = data[20]
                if len(data[21]) != 0 and data[21] != '\n':
                    demographic_hash["occr_country"] = data[21]

                #print(demographic_hash['occr_country'])
                collection.insert(demographic_hash)
                # and data[6] != '\n'

#call Parse_file function.
file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\DEMO13Q4.txt"
demo_parser_obj = Demographic()
demo_parser_obj.parse_file(file_name)
