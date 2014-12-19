__author__ = 'srv'
__author__ = 'srv'

from db.db import DbConnection

class Reaction(object):

    def __init__(self):
        self.reaction_hash={}

    # Function to parse the txt file
    def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.reaction
        pt_list=[]
        current=''
        previous=''
        with open(file_name, "rt") as f:
            next(f)
            for line in f:

                #Create a dictionary
                #splits the data according to the specific delimiter.
                data = line.split('$')
                primary_id =data[0]
                current = primary_id
                case_id =data[1]
                pt =data[2]

                if current not in previous and previous !='':
                    #print(self.reaction_hash)
                    #collection.insert(self.reaction_hash)
                    self.reaction_hash={}
                    pt_list=[]

                if primary_id not in self.reaction_hash and case_id not in self.reaction_hash:
                    self.reaction_hash['primaryid']=primary_id
                    self.reaction_hash['caseid']=case_id
                    pt_list.append(pt)
                    self.reaction_hash['pt'] = pt_list
                elif primary_id in self.reaction_hash and case_id in self.reaction_hash:
                    self.reaction_hash['pt'].append(pt)

                '''
                if current not in previous:
                    #print(self.reaction_hash)
                    collection.insert(self.reaction_hash)

                if primary_id not in self.reaction_hash:
                    self.reaction_hash.clear()
                    self.reaction_hash[primary_id] = [pt]
                elif primary_id in self.reaction_hash:
                    self.reaction_hash[primary_id].append(pt)
                '''
                previous = primary_id


#call Parse_file function.
#file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\REAC13Q4.txt"
file_name ="reaction.txt"
reaction_parser_obj = Reaction()
reaction_parser_obj.parse_file(file_name)

