__author__ = 'Akshay'

from db.db import DbConnection
import json
from bson import json_util
import re
import datetime
#import parser.RxTerms

class GetDataDrug(object):

    def getData(self):

        term_search="XEOMIN"

        term_search_lower = term_search.lower()

        print(datetime.datetime.now())
        #ing_rxterms_hash = RxTerms.RxTermsIngredients.RxTermParserIngredients().getIngHash()
        #print(ing_rxterms_hash)
        final_dict={}
        connection = DbConnection().getConnection()
        #get the rxterms collection


        rxtermsCollection = connection.rxterms
        #rxtermsCollection.find({$or:[{"display_name":'/.*IBUPROFEN.*/'},{ "sxdg_name":'/.*Ibuprofen.*/'}]})
        cursor_rxterms = rxtermsCollection.find({},{'_id':0})
        rxterms_list=[]
        for item in cursor_rxterms:
            if term_search in item['display_name'] or term_search_lower.title() in item['sxdg_name'] or term_search_lower.title() in item['full_name'] :
                #print(item['rxcui'] + item['sxdg_name']  + item['route'] + item['full_name'])
                ingredient_list=[]
                rxterms_list.append(item)

        final_dict['rxterms'] = rxterms_list

        drugCollection = connection.drug
        cursor_drug = drugCollection.find({'drugname':term_search},{'_id':0})
        drug_list=[]
        primaryid_list=[]
        caseid_list=[]
        for drug in cursor_drug:
            drug_list.append(drug)
            primaryid_list.append(drug['primaryid'])
            caseid_list.append(drug['caseid'])
        final_dict['drug']=drug_list

        #json_p1 = json.dumps(final_dict,default=json_util.default,indent=4, ensure_ascii=False)
        #print(json_p1)
        print("-----------------------------------------------------------")
        #print(len(primaryid_list))
        #print(len(caseid_list))
        primaryid_list = list(set(primaryid_list))
        caseid_list = list(set(caseid_list))


        demo_list=[]
        demo_collection = connection.demographic
        cursor_demo = demo_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0})
        #print(cursor_demo)
        for demo in cursor_demo:
            demo_list.append(demo)

        final_dict['demographic']=demo_list

        indi_list=[]
        indication_collection = connection.indication
        cursor_indi = indication_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0,'primaryid':0,'caseid':0})
        for indication in cursor_indi:
            indi_list.append(indication)

        unique = []
        for item in indi_list:
            if item not in unique:
                unique.append(item)
        final_dict['indication']=unique

        outcome_list=[]
        outcome_collection = connection.outcome
        cursor_outcome = outcome_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0})
        for outcome in cursor_outcome:
            outcome_list.append(outcome)

        final_dict['outcome']=outcome_list


        report_sources_list=[]
        report_sources_collection = connection.report_sources
        cursor_report_sources = report_sources_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0})
        for report_sources in cursor_report_sources:
            report_sources_list.append(report_sources)

        final_dict['report_sources']=report_sources_list


        therepy_list=[]
        therepy_collection = connection.therepy_sources
        cursor_therepy = therepy_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0})
        for therepy in cursor_therepy:
            therepy_list.append(therepy)

        final_dict['therepy']=therepy_list

        reaction_list=[]
        reaction_collection = connection.reaction
        cursor_reaction = reaction_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0})
        for reaction in cursor_reaction:
            reaction_list.append(reaction)

        final_dict['reaction']=reaction_list

        concept_def_collection = connection.concept_definition
        #rxtermsCollection.find({$or:[{"display_name":'/.*IBUPROFEN.*/'},{ "sxdg_name":'/.*Ibuprofen.*/'}]})
        cursor_concept_def = concept_def_collection.find({},{'_id':0})
        concept_def_list=[]
        for item in cursor_concept_def:
            if term_search in item['name'] or term_search_lower.title() in item['name'] :
                #print(item['rxcui'] + item['sxdg_name']  + item['route'] + item['full_name'])
                ingredient_list=[]

                concept_def_list.append(item)

        final_dict['concept_definition'] = concept_def_list

        #print(final_dict)

        json_p = json.dumps(final_dict,default=json_util.default,indent=4, ensure_ascii=True)
        f = open('final.json','w')
        f.write(json_p) # python will convert \n to os.linesep
        f.close()

        #print(json_p)

        print(datetime.datetime.now())
        #print(final_dict.keys())



    def gDta(self):
        connection = DbConnection().getConnection()
        test_collection = connection.test
        rxtermsCollection = connection.rxterms

        regx = re.compile("/.*IBUPROFEN.*/", re.IGNORECASE)
        regx1 = re.compile("/.*Ibuprofen.*/", re.IGNORECASE)
        cursor_rxterms = rxtermsCollection.find({'$or':[{"display_name":regx},{ "sxdg_name":regx1}]},{"rxcui":1})
        #rxtermsCollection.find({},{'_id':0})


        rxterms_list=[]
        for item in cursor_rxterms:
            print(item)
            rxterms_list.append(item)
        print(len(rxterms_list))

pm = GetDataDrug()
print(pm.gDta())


