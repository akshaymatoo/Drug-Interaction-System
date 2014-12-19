__author__ = 'srv'

import pymongo
from db.db import DbConnection

class  Ndrft(object):


    def parse_file(self,file_name):
        #getting the database object
        connection = DbConnection().getConnection()
        #get the rxterms collection
        collection = connection.ndrft_nui

        dic_list=[]
        with open(file_name, "rt") as f:
            for line in f:
                #Create a dictionary
                data = line.split('\t')
                disease_finding = data[0].strip()
                code = data[1].strip()
                ndrft_hash={}

                ndrft_hash[code] = disease_finding
                #print(ndrft_hash)
                collection.insert(ndrft_hash)

file_name="E:\\UTA_SEMESTER_FOLDER\\fall2014\\CSE5320 Eknauth\\CS5320_Raw_Data\\CS5320_Raw_Data\\National Drug File - Reference Terminology(NDF-RT)\\NDFRT_Public_2014.07.07_NUI.txt"
ndfrt_obj = Ndrft()
ndfrt_obj.parse_file(file_name)

