__author__ = 'srv'

from db.db import DbConnection

class Drug(object):

# Function to parse the txt file
     def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.drug

        with open(file_name, "rt") as f:
            next(f)
            for line in f:

                #Create a dictionary
                drug_hash={}
                #splits the data according to the specific delimiter.
                data = line.split('$')

                if len(data[0]) != 0:
                    drug_hash["primaryid"] = data[0]
                if len(data[1]) != 0:
                    drug_hash["caseid"] = data[1]
                if len(data[2]) != 0:
                    drug_hash["drug_seq"] = data[2]
                if len(data[3]) != 0:
                    drug_hash["role_cod"] = data[3]
                if len(data[4]) != 0:
                    drug_hash["drugname"] = data[4]
                if len(data[5]) != 0:
                    drug_hash["val_vbm"] = data[5]
                if len(data[6]) != 0:
                    drug_hash["route"] = data[6]
                if len(data[7]) != 0:
                    drug_hash["dose_vbm"] = data[7]
                if len(data[8]) != 0:
                    drug_hash["cum_dose_chr"] = data[8]
                if len(data[9]) != 0:
                    drug_hash["cum_dose_unit"] = data[9]
                if len(data[10]) != 0:
                    drug_hash["dechal"] = data[10]
                if len(data[11]) != 0:
                    drug_hash["rechal"] = data[11]
                if len(data[12]) != 0:
                    drug_hash["lot_num"] = data[12]
                if len(data[13]) != 0:
                    drug_hash["exp_dt"] = data[13]
                if len(data[14]) != 0:
                    drug_hash["nda_num"] = data[14]
                if len(data[15]) != 0:
                    drug_hash["dose_amt"] = data[15]
                if len(data[16]) != 0:
                    drug_hash["dose_unit"] = data[16]
                if len(data[17]) != 0:
                    drug_hash["dose_form"] = data[17]
                if len(data[18]) != 0 and data[18]!='\n':
                    drug_hash["dose_freq"] = data[18]

                #print(drug_hash['dose_freq'])
                collection.insert(drug_hash)
                # and data[6] != '\n'

#call Parse_file function.
#file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\DRUG13Q4.txt"
file_name ="DRUG\\xag.txt"
drug_parser_obj = Drug()
drug_parser_obj.parse_file(file_name)


#call Parse_file function.

