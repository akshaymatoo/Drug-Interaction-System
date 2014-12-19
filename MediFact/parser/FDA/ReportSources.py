__author__ = 'srv'

__author__ = 'srv'

from db.db import DbConnection

class ReportSource(object):

    def __init__(self):
        self.report_source_hash={}


    # Function to parse the txt file
    def parse_file(self, file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.report_sources
        previous=''
        current=''
        rpsr_cod_list=[]
        with open(file_name, "rt") as f:
            next(f)
            for line in f:

                #Create a dictionary
                #splits the data according to the specific delimiter.
                data = line.split('$')
                primary_id =data[0]
                current = primary_id
                case_id =data[1]
                rpsr_cod =data[2]


                if current not in previous and previous !='':
                    print(self.report_source_hash)
                    #collection.insert(self.report_source_hash)
                    self.report_source_hash={}
                    rpsr_cod_list=[]

                if primary_id not in self.report_source_hash and case_id not in self.report_source_hash:
                    self.report_source_hash['primaryid']=primary_id
                    self.report_source_hash['caseid']=case_id
                    rpsr_cod_list.append(rpsr_cod)
                    self.report_source_hash['rpsr_cod'] = rpsr_cod_list
                elif primary_id in self.report_source_hash and case_id in self.report_source_hash:
                    self.report_source_hash['rpsr_cod'].append(rpsr_cod)

                '''
                if current not in previous:
                    #print(self.report_source_hash)
                    collection.insert(self.report_source_hash)

                if primary_id not in self.report_source_hash:
                    self.report_source_hash.clear()
                    self.report_source_hash[primary_id] = [rpsr_cod]
                elif primary_id in self.report_source_hash:
                    self.report_source_hash[primary_id].append(rpsr_cod)
                '''
                previous = primary_id
                #print()



#call Parse_file function.
file_name ="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\FDA Adverse Event Reporting\\ascii\\RPSR13Q4.txt"
#file_name ="rp.txt"
report_parser_obj = ReportSource()
report_parser_obj.parse_file(file_name)