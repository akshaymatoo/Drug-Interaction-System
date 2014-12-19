from xml.dom import minidom
import time
from db.db import DbConnection


class NdfrtParser(object):
    def __init__(self):
        self.doc = minidom.parse("XMLCut\\xak.xml")
        self.connection = DbConnection().getConnection()


    def parseKindDef(self):
        kindDef = self.doc.getElementsByTagName("kindDef")
        # get the rxterms collection
        collection = self.connection.kind_definition

        for kindDef in kindDef:
            kind_hash = {}
            kind_hash['name'] = kindDef.getElementsByTagName("name")[0].firstChild.data
            kind_hash['code'] = kindDef.getElementsByTagName("code")[0].firstChild.data
            kind_hash['id'] = kindDef.getElementsByTagName("id")[0].firstChild.data
            kind_hash['namespace'] = kindDef.getElementsByTagName("namespace")[0].firstChild.data
            collection.insert(kind_hash)
            #print(kind_hash)

    def parseRoleDef(self):
        roleDef = self.doc.getElementsByTagName("roleDef")
        collection = self.connection.role_definition
        for roleDef in roleDef:
            role_hash = {}
            role_hash['name'] = roleDef.getElementsByTagName("name")[0].firstChild.data
            role_hash['code'] = roleDef.getElementsByTagName("code")[0].firstChild.data
            role_hash['id'] = roleDef.getElementsByTagName("id")[0].firstChild.data
            role_hash['namespace'] = roleDef.getElementsByTagName("namespace")[0].firstChild.data
            role_hash['domain'] = roleDef.getElementsByTagName("domain")[0].firstChild.data
            role_hash['range'] = roleDef.getElementsByTagName("range")[0].firstChild.data
            collection.insert(role_hash)
            #print(role_hash)


    def parsePropertyDef(self):
        propertyDef = self.doc.getElementsByTagName("propertyDef")
        collection = self.connection.property_definition
        for propertyDef in propertyDef:
            property_hash = {}
            pickList = []
            property_hash['name'] = propertyDef.getElementsByTagName("name")[0].firstChild.data
            property_hash['code'] = propertyDef.getElementsByTagName("code")[0].firstChild.data
            property_hash['id'] = propertyDef.getElementsByTagName("id")[0].firstChild.data
            property_hash['namespace'] = propertyDef.getElementsByTagName("namespace")[0].firstChild.data
            property_hash['range'] = propertyDef.getElementsByTagName("range")[0].firstChild.data
            pickListItem = propertyDef.getElementsByTagName("pickListItem")
            # print(len(pickListItem))
            for pickListItem in pickListItem:
                pickList.append(pickListItem.firstChild.nodeValue)

            if len(pickList) > 0:
                property_hash['pickList'] = pickList
            collection.insert(property_hash)


    def parseAssociationDef(self):

        associationDef = self.doc.getElementsByTagName("associationDef")
        collection = self.connection.association_definition
        for associationDef in associationDef:
            association_hash = {}
            association_hash['name'] = associationDef.getElementsByTagName("name")[0].firstChild.data
            association_hash['code'] = associationDef.getElementsByTagName("code")[0].firstChild.data
            association_hash['id'] = associationDef.getElementsByTagName("id")[0].firstChild.data
            association_hash['namespace'] = associationDef.getElementsByTagName("namespace")[0].firstChild.data

            collection.insert(association_hash)


    def parseQualifierDef(self):

        qualifierDef = self.doc.getElementsByTagName("qualifierDef")
        collection = self.connection.qualifier_definition
        for qualifierDef in qualifierDef:
            qualifier_hash = {}
            pickList = []
            qualifier_hash['name'] = qualifierDef.getElementsByTagName("name")[0].firstChild.data
            qualifier_hash['code'] = qualifierDef.getElementsByTagName("code")[0].firstChild.data
            qualifier_hash['id'] = qualifierDef.getElementsByTagName("id")[0].firstChild.data
            qualifier_hash['namespace'] = qualifierDef.getElementsByTagName("namespace")[0].firstChild.data
            pickListItem = qualifierDef.getElementsByTagName("pickListItem")
            # print(len(pickListItem))

            for pickListItem in pickListItem:
                pickList.append(pickListItem.firstChild.nodeValue)

            if len(pickList) > 0:
                qualifier_hash['pickList'] = pickList

            collection.insert(qualifier_hash)


    def parseConceptDef(self):

        conceptDef = self.doc.getElementsByTagName("conceptDef")
        collection = self.connection.concept_definition
        for conceptDef in conceptDef:
            concept_hash = {}
            #pickList = []
            try:

                name =conceptDef.getElementsByTagName("name")[0].firstChild.data
                if name is not None and name != "":
                    concept_hash['name'] = name

                code = conceptDef.getElementsByTagName("code")[0].firstChild.data
                if code is not None and code !="":
                    concept_hash['code'] = code

                id =  conceptDef.getElementsByTagName("id")[0].firstChild.data
                if id is not None and id !="":
                    concept_hash['id'] = id
                namespace = conceptDef.getElementsByTagName("namespace")[0].firstChild.data
                if namespace is not None and namespace !="":
                    concept_hash['namespace'] = namespace

                try:
                    primitive = conceptDef.getElementsByTagName("primitive")[0].firstChild.data
                    if primitive is not None and primitive !="":
                        concept_hash['primitive']=primitive
                except:
                    pass

                kind = conceptDef.getElementsByTagName("kind")[0].firstChild.data
                if kind is not None and kind !="":
                    concept_hash['kind'] = kind
                try:
                    definingConcepts = conceptDef.getElementsByTagName("definingConcepts")[0].firstChild.data
                    if definingConcepts is not None and definingConcepts !="":
                        concept_hash['definingConcepts']=definingConcepts
                except:
                    pass
                try:

                    definingRoles = conceptDef.getElementsByTagName("definingRoles")[0].firstChild.data
                    if definingRoles is not None and definingRoles !="":
                        concept_hash['definingRoles']=definingRoles
                except:
                    pass

                property = conceptDef.getElementsByTagName("property")
                #print(len(property))
                p_list = []

                for property in property:
                    p_hash = {}
                    name = property.getElementsByTagName('name')
                    value = property.getElementsByTagName('value')
                    p_hash['name'] = name[0].firstChild.nodeValue
                    p_hash['value'] = value[0].firstChild.nodeValue
                    p_list.append(p_hash)
                concept_hash['propertyList'] = p_list

                collection.insert(concept_hash)
            except:
                pass


ndfrt_obj = NdfrtParser()
ndfrt_obj.parseKindDef()

ndfrt_obj.parseRoleDef()

ndfrt_obj.parsePropertyDef()

ndfrt_obj.parseAssociationDef()

ndfrt_obj.parseQualifierDef()

ndfrt_obj.parseConceptDef()

print(time.strftime("%H:%M:%S"))