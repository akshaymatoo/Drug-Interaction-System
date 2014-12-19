__author__ = 'Akshay'

from db import DbConnection

class Pymg(object):

    def getData(self, name):
        term_search = name.upper()
        print ("Term Search", term_search)
        term_search_lower = term_search.lower()
        term_search_title = term_search_lower.title()
        final_dict = {}
        connection = DbConnection().get_connection()

        rxtermsCollection = connection.rxterms
        cursor_rxterms = rxtermsCollection.find({},{'_id':0})
        rxterms_list = []
        for item in cursor_rxterms:
            if term_search in item['display_name'] or term_search_title in item['display_name'] or term_search_lower.title() in item['sxdg_name'] or term_search_lower.title() in item['full_name']:
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

        primaryid_list = list(set(primaryid_list))
        caseid_list = list(set(caseid_list))


        demo_list=[]
        demo_collection = connection.demographic
        cursor_demo = demo_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0})
        for demo in cursor_demo:
            demo_list.append(demo)

        final_dict['demographic']=demo_list

        indi_list = []
        indication_collection = connection.indication
        cursor_indi = indication_collection.find({'primaryid':{'$in':primaryid_list},'caseid':{'$in':caseid_list}},{'_id':0,'primaryid':0,'caseid':0})
        for indication in cursor_indi:
            indi_list.append(indication)

        unique = []
        for item in indi_list:
            if item not in unique:
                unique.append(item)
        final_dict['indication']=unique

        outcome_list = []
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
        cursor_concept_def = concept_def_collection.find({},{'_id':0})
        concept_def_list = []
        for item in cursor_concept_def:
            if term_search in item['name'] or term_search_lower.title() in item['name']:
                concept_def_list.append(item)

        final_dict['concept_definition'] = concept_def_list
        return final_dict

if __name__ == "__name__":
    rest_api = Pymg()
    tasks = rest_api.getData()
    print tasks
