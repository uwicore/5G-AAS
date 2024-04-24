#Here we import needed libraries

import datetime
from pathlib import Path  # Used for easier handling of auxiliary file's local path

import pyecma376_2  # The base library for Open Packaging Specifications. We will use the OPCCoreProperties class.
from aas import model
from aas.adapter import aasx
import aas
from aas.model import Submodel, SubmodelElement, SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered, Property, Identifier,Operation, SubmodelElementCollection, MultiLanguageProperty, Asset, AssetAdministrationShell, AASReference, Asset, Identifier, LangStringSet, Namespace, AdministrativeInformation, Security, Submodel, ConceptDictionary, View, AbstractObjectProvider  # Importa las clases necesarias
import pprint
import copy         #To copy nested structures
import math
from AASsubmodels import *       #Here we have the created structure for the AAS

#Object Store and File store must be created to correctly read the AASX file

new_object_store: model.DictObjectStore[model.Identifiable] = model.DictObjectStore()
new_file_store = aasx.DictSupplementaryFileContainer()

#Here we read the AASX in which we have 2 5G UE AAS and the 5G Network AAS

with aasx.AASXReader("5G_Network_AAS.aasx") as reader:
    # Read all contained AAS objects and all referenced auxiliary files
    # In contrast to the AASX Package Explorer, we are not limited to a single XML part in the package, but instead we
    # will read the contents of all included JSON and XML parts into the ObjectStore
    reader.read_into(object_store=new_object_store,
                     file_store=new_file_store)

    # We can also read the meta data
    new_meta_data = reader.get_core_properties()


#Configuration of IRIs
#Here we have to configurate our IRIs based on our AASX file
nameplate_IRI= "https://example.com/ids/sm/9403_2190_2042_0302"
identification_IRI= "https://example.com/ids/sm/0413_2190_2042_7899"
documentation_IRI= "https://example.com/ids/sm/6543_6140_9032_5727"
service_IRI= "https://example.com/ids/sm/2523_2190_2042_9199"
technicalData_IRI= "https://example.com/ids/sm/4110_6122_3042_6134"
npn5GNWIdentity="https://example.com/ids/sm/6324_6140_9032_3623"
assetServiceRegistry="https://example.com/ids/sm/2254_6150_9032_5216"
tsnCapabilities="https://example.com/ids/sm/9200_7150_9032_5023"
network5GDataSheet="https://example.com/ids/sm/6042_5122_3042_7804"
virtualsNetwork="https://example.com/ids/sm/8131_6122_3042_7812"
connectivity="https://example.com/ids/sm/5280_1152_3042_0914"
qosPerformance="https://example.com/ids/sm/5312_6191_0132_6842"
dataAnalytics="https://example.com/ids/sm/7465_1152_3042_5525"
location_IRI= "https://example.com/ids/sm/4202_7182_2042_8979"



#First we read the assets    
for obj in new_object_store:
    if isinstance(obj, Asset):    
        if obj.id_short=="NETWORK_5G":
            network5G=Network5G(obj.kind, obj.identification, obj.id_short, obj.category, obj.description)

#Now the submodels
for obj in new_object_store:
    if isinstance(obj, Submodel):
        if(obj.identification.id==nameplate_IRI):  #Nameplate Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="ManufacturerName": manufacturerName=elemento_contenido
                if elemento_contenido.id_short=="ManufacturerTypName": manufacturerTypName=elemento_contenido
                if isinstance(elemento_contenido, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for elemento_ref in elemento_contenido.value:  
                        if elemento_ref.id_short=="CountryCode": countryCode=elemento_ref
                        if elemento_ref.id_short=="Street": street=elemento_ref
                        if elemento_ref.id_short=="PostalCode": postalCode=elemento_ref
                        if elemento_ref.id_short=="City": city=elemento_ref
                        if elemento_ref.id_short=="StateCounty": 
                            stateCounty=elemento_ref
                            physical_address=PhysicalAddress(countryCode,street, postalCode, city, stateCounty, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                            
                if elemento_contenido.id_short=="TypClass": typClass=elemento_contenido
                if elemento_contenido.id_short=="SerialNo": serialNo=elemento_contenido
                if elemento_contenido.id_short=="ChargeId": chargeId=elemento_contenido
                if elemento_contenido.id_short=="CountryOfOrigin": countryOfOrigin=elemento_contenido
                if elemento_contenido.id_short=="YearOfConstruction": yearOfConstruction=elemento_contenido
            nameplate=Nameplate(manufacturerName,manufacturerTypName,physical_address,typClass,serialNo,chargeId,countryOfOrigin,yearOfConstruction, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)       
        elif(obj.identification.id==identification_IRI):  #Identification Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="ManufacturerName": manufacturerName=elemento_contenido
                if elemento_contenido.id_short=="ManufacturerId01": manufacturerId01=elemento_contenido
                if elemento_contenido.id_short=="ManufacturerIdProvider": manufacturerIdProvider=elemento_contenido
                if elemento_contenido.id_short=="ManufacturerTypId": manufacturerTypId=elemento_contenido
                if elemento_contenido.id_short=="ManufacturerTypName": manufacturerTypName=elemento_contenido
                if elemento_contenido.id_short=="ManufacturerTypDescription": manufacturerTypDescription=elemento_contenido
                if elemento_contenido.id_short=="SupplierName": supplierName=elemento_contenido
                if elemento_contenido.id_short=="SupplierId": supplierId=elemento_contenido
                if elemento_contenido.id_short=="SupplierIdProvider": supplierIdProvider=elemento_contenido
                if elemento_contenido.id_short=="SupplierTypId": supplierTypId=elemento_contenido
                if elemento_contenido.id_short=="SupplierTypName": supplierTypName=elemento_contenido
                if elemento_contenido.id_short=="SupplierTypDescription": supplierTypDescription=elemento_contenido
                if elemento_contenido.id_short=="TypClass": typClass=elemento_contenido
                if elemento_contenido.id_short=="ClassificationSystem": classificationSystem=elemento_contenido
                if elemento_contenido.id_short=="SecondaryKeyTyp": secondaryKeyTyp=elemento_contenido
                if elemento_contenido.id_short=="AssetId": assetId=elemento_contenido
                if elemento_contenido.id_short=="InstanceId": instanceId=elemento_contenido
                if elemento_contenido.id_short=="ChargeId": assetId=elemento_contenido
                if elemento_contenido.id_short=="SecondaryKeyInstance": secondaryKeyInstance=elemento_contenido
                if elemento_contenido.id_short=="ManufacturingDate": manufacturingDate=elemento_contenido
                if elemento_contenido.id_short=="DeviceRevision": deviceRevision=elemento_contenido
                if elemento_contenido.id_short=="SoftwareRevision": softwareRevision=elemento_contenido
                if elemento_contenido.id_short=="HardwareRevision": hardwareRevision=elemento_contenido
                if isinstance(elemento_contenido, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for elemento_ref in elemento_contenido.value:   
                        if elemento_ref.id_short=="Name": name=elemento_ref
                        if elemento_ref.id_short=="Role": role=elemento_ref
                        if isinstance(elemento_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)): 
                            for elemento_ref_2 in elemento_ref.value:
                                if elemento_ref_2.id_short=="CountryCode": countryCode=elemento_ref_2
                                if elemento_ref_2.id_short=="Street": street=elemento_ref_2
                                if elemento_ref_2.id_short=="PostalCode": postalCode=elemento_ref_2
                                if elemento_ref_2.id_short=="City": city=elemento_ref_2
                                if elemento_ref_2.id_short=="StateCounty": 
                                    stateCounty=elemento_ref_2
                                    physical_address=PhysicalAddress(countryCode,street, postalCode, city, stateCounty, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                        elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)

                        if elemento_ref.id_short=="Email": email=elemento_ref
                        if elemento_ref.id_short=="URL": url=elemento_ref
                        if elemento_ref.id_short=="Phone": phone=elemento_ref
                        if elemento_ref.id_short=="Fax":
                            fax=elemento_ref
                            contact_info=ContactInfo(name,role,physical_address,email,url,phone,fax, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="URL": url=elemento_contenido
            identification=Identification(manufacturerName,manufacturerId01,manufacturerIdProvider,manufacturerTypId,manufacturerTypName,manufacturerTypDescription,supplierName,supplierId,supplierIdProvider,supplierTypId,supplierTypName,supplierTypDescription,typClass,
                                        classificationSystem, secondaryKeyTyp,assetId,instanceId,chargeId,secondaryKeyInstance,manufacturingDate,deviceRevision,softwareRevision,hardwareRevision,contact_info,url,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.identification.id==documentation_IRI):  #Documentation Network
            documentation= Documentation(obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind) 
        elif(obj.identification.id==service_IRI):  #Service Network
            for elemento_contenido in obj:
                if isinstance(elemento_contenido,(SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="NameOfSupplier": nameOfSupplier=elemento_ref
                        if elemento_ref.id_short=="ContactInfo_Role": contactInfo_role=elemento_ref
                        if isinstance(elemento_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)): 
                            for elemento_ref_2 in elemento_ref.value:
                                if elemento_ref_2.id_short=="CountryCode": countryCode=elemento_ref_2
                                if elemento_ref_2.id_short=="Street": street=elemento_ref_2
                                if elemento_ref_2.id_short=="Zip": postalCode=elemento_ref_2
                                if elemento_ref_2.id_short=="CityTown": city=elemento_ref_2
                                if elemento_ref_2.id_short=="StateCounty": 
                                    stateCounty=elemento_ref_2
                                    physical_address=PhysicalAddress(countryCode,street, postalCode, city, stateCounty, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                        elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                        if elemento_ref.id_short=="Email": email=elemento_ref
                        if elemento_ref.id_short=="URL": url=elemento_ref
                        if elemento_ref.id_short=="PhoneNumber": phone=elemento_ref
                        if elemento_ref.id_short=="Fax":
                            fax=elemento_ref
                            contact_info=ContactInfo(nameOfSupplier,contactInfo_role,physical_address,email,url,phone,fax, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            
            service=Service(contact_info, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.identification.id==location_IRI):  #Location Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="ListOfConnectedUes": 
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="ConnectedUE01": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="XPosition":xPosition=elemento_ref2
                                if elemento_ref2.id_short=="YPosition":yPosition=elemento_ref2
                                if elemento_ref2.id_short=="ZPosition":zPosition=elemento_ref2 
                                if elemento_ref2.id_short=="Speed":speed=elemento_ref2
                                if elemento_ref2.id_short=="Aceleration":aceleration=elemento_ref2
                                if elemento_ref2.id_short=="LCSQosClass": lcsQosClass=elemento_ref2
                                if elemento_ref2.id_short=="Accuracy": accuracy=elemento_ref2
                                if elemento_ref2.id_short=="ResponseTime": responseTime=elemento_ref2
                            connectedUE1=ConnectedUe(xPosition, yPosition, zPosition, speed, aceleration, lcsQosClass,accuracy, responseTime,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            listOfConnectedUes=ListOfConnectedUes(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                            listOfConnectedUes.add_ue(connectedUE1)
                        if elemento_ref.id_short=="ConnectedUE02": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="XPosition":xPosition=elemento_ref2
                                if elemento_ref2.id_short=="YPosition":yPosition=elemento_ref2
                                if elemento_ref2.id_short=="ZPosition":zPosition=elemento_ref2 
                                if elemento_ref2.id_short=="Speed":speed=elemento_ref2
                                if elemento_ref2.id_short=="Aceleration":aceleration=elemento_ref2
                                if elemento_ref2.id_short=="LCSQosClass": lcsQosClass=elemento_ref2
                                if elemento_ref2.id_short=="Accuracy": accuracy=elemento_ref2
                                if elemento_ref2.id_short=="ResponseTime": responseTime=elemento_ref2
                            connectedUE2=ConnectedUe(xPosition, yPosition, zPosition, speed, aceleration, lcsQosClass,accuracy, responseTime, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                    elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            listOfConnectedUes.add_ue(connectedUE2)
                if elemento_contenido.id_short=="SubscriptionRequestFunction":subscriptionRequestFunction=elemento_contenido

                
                if elemento_contenido.id_short=="ListOfSubscriptions":
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="ListOfEvents":
                            for elemento_ref2 in elemento_ref:  
                                if elemento_ref2.id_short=="Event1":
                                        event1=elemento_ref2
                                        listOfEvents= ListOfNetworkLocationEvents(elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description,
                                                                                                    elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                        listOfEvents.add_event(event1)
                        if elemento_ref.id_short=="Subscription1":
                            subscription1=elemento_ref
                            listOfSubscriptions= ListOfNetworkLocationSubscriptions(listOfEvents,elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description,
                                                                                        elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                            listOfSubscriptions.add_subscription(subscription1)

            networkLocation=Location(listOfConnectedUes,subscriptionRequestFunction,listOfSubscriptions,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)       
        elif(obj.identification.id==npn5GNWIdentity):  #NPN5GNWIdentity Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="PLMNID": plmnid=elemento_contenido
                if elemento_contenido.id_short=="NPNID": npnid=elemento_contenido
            npn5GNWIdentity=NPN5GNWIdentity(plmnid, npnid,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.identification.id==assetServiceRegistry):  #AssetServiceRegistry Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="AssetService": assetService=elemento_contenido
                if elemento_contenido.id_short=="IntegratorCompany": integratorCompany=elemento_contenido
                if elemento_contenido.id_short=="PlanningReferences": planningReferences=elemento_contenido
                if elemento_contenido.id_short=="SLA": sla=elemento_contenido
                if elemento_contenido.id_short=="CoverageMap": coverageMap=elemento_contenido
            assetServiceRegistry=AssetServiceRegistry(assetService, integratorCompany, planningReferences, sla, coverageMap, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.identification.id==technicalData_IRI):  #TechnicalData Network
            for elemento_contenido in obj:
                if isinstance(elemento_contenido, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for elemento_ref in elemento_contenido.value:  
                        if elemento_ref.id_short=="ManufacturerName": manufacturerName=elemento_ref
                        if elemento_ref.id_short=="ManufacturerProductDesignation": manufacturerProductDesignation=elemento_ref
                        if elemento_ref.id_short=="ManufacturerPartNumber": manufacturerPartNumber=elemento_ref
                        if elemento_ref.id_short=="ManufacturerOrderCode": 
                            manufacturerOrderCode=elemento_ref
                            general_info=GeneralInformation(manufacturerName,manufacturerProductDesignation,manufacturerPartNumber, manufacturerOrderCode, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                        if elemento_ref.id_short=="TextStatement01": textStatement=elemento_ref
                        if elemento_ref.id_short=="ValidDate": 
                            
                            validDate=elemento_ref
                            further_info=FurtherInformation(textStatement,validDate,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                        if isinstance(elemento_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                            for elemento_ref_2 in elemento_ref.value:   
                                if elemento_ref_2.id_short=="ProductClassificationSystem": productClassificationSystem=elemento_ref_2
                                if elemento_ref_2.id_short=="ClassificationSystemVersion": classificationSystemVersion=elemento_ref_2
                                if elemento_ref_2.id_short=="ProductClassId": 
                                    productClassId=elemento_ref_2
                                    prod_class_system=ProductClassificationItem(productClassificationSystem,classificationSystem,productClassId, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                        elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)

                                    technicalProperties=TechnicalProperties(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            technicalDataNetwork=TechnicalData(general_info,prod_class_system,technicalProperties,further_info,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)   
        elif(obj.identification.id==tsnCapabilities):  #TSNCapabilities Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="Bridge5GS": 
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="Parameters5GS": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="BridgeID":bridgeID=elemento_ref2
                                if elemento_ref2.id_short=="ListOfPorts":listOfPorts=elemento_ref2
                                if elemento_ref2.id_short=="System5GBridgeDelay":system5GBridgeDelay=elemento_ref2
                                if elemento_ref2.id_short=="StreamFilters":streamFilters=elemento_ref2 
                                if elemento_ref2.id_short=="UeDsTtResidenceTime":ueDsTtResidenceTime=elemento_ref2
                                if elemento_ref2.id_short=="PropagationDelayPerPort":propagationDelayPerPort=elemento_ref2 
                                if elemento_ref2.id_short=="TimeSynchronizationStatus":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="SynchronizationState":synchronizationState=elemento_ref3
                                        if elemento_ref3.id_short=="ClockAccuracy":clockAccuracy=elemento_ref3
                                        if elemento_ref3.id_short=="FrequencyStability":
                                            frequencyStability=elemento_ref3
                                            timeSynchronizationStatus= TimeSynchronizationStatus(synchronizationState, clockAccuracy, frequencyStability, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description,
                                                                                        elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                            parameters5GS=Parameters5GS(bridgeID, listOfPorts, system5GBridgeDelay, streamFilters, ueDsTtResidenceTime, propagationDelayPerPort, timeSynchronizationStatus, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)

                        if elemento_ref.id_short=="TsnFlowList": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="TsnFlowN":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="DestinationIP":destinationIP=elemento_ref3
                                        if elemento_ref3.id_short=="DestinationMacAddress":destinationMacAddress=elemento_ref3
                                        if elemento_ref3.id_short=="StreamId":streamId=elemento_ref3
                                        if elemento_ref3.id_short=="QosProfileAssociated":qosProfileAssociated=elemento_ref3
                                        if elemento_ref3.id_short=="TsnTrafficClasses":tsnTrafficClasses=elemento_ref3
                                        if elemento_ref3.id_short=="TsnTrafficPriority":tsnTrafficPriority=elemento_ref3
                                        if elemento_ref3.id_short=="VLANID":vlanID=elemento_ref3
                                        if elemento_ref3.id_short=="VLANPriority":vlanPriority=elemento_ref3
                                        if elemento_ref3.id_short=="MaximumLatency":maximumLatency=elemento_ref3
                                        if elemento_ref3.id_short=="Reliability":reliability=elemento_ref3
                                        if elemento_ref3.id_short=="Port":port=elemento_ref3
                                        if elemento_ref3.id_short=="TSCAI":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="SurvivalTime":survivalTime=elemento_ref4
                                                if elemento_ref4.id_short=="PacketArrivalTime":packetArrivalTime=elemento_ref4
                                                if elemento_ref4.id_short=="Periodicity":
                                                    periodicity=elemento_ref4
                                                    tscai= TSCAI(survivalTime, packetArrivalTime, periodicity, elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    tsnFlow=TsnFlowN(destinationIP, destinationMacAddress, streamId, qosProfileAssociated, tsnTrafficClasses, tsnTrafficPriority, vlanID, vlanPriority, maximumLatency, reliability, port, tscai, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            tsnFlowList=TsnFlowList(elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)   
                            tsnFlowList.add_tsnFlow(tsnFlow)
                    bridge5GS=Bridge5GS(parameters5GS, tsnFlowList, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            tsnCapabilities=TSNCapabilities(bridge5GS,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.identification.id==network5GDataSheet):  #Network5GDataSheet Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="ReleaseCompatibility3GPP": releaseCompatibility3GPP=elemento_contenido
                if elemento_contenido.id_short=="NetworkProtocols": networkProtocols=elemento_contenido
                if elemento_contenido.id_short=="CoverageRange": coverageRange=elemento_contenido
                if elemento_contenido.id_short=="SupportedSpectrum": supportedSpectrum=elemento_contenido
                if elemento_contenido.id_short=="SupportedTransmissionPower": supportedTransmissionPower=elemento_contenido
                if elemento_contenido.id_short=="TransmissionModeCharacteristics": 
                    for elemento_ref in elemento_contenido.value: 
                        if elemento_ref.id_short=="ModulationTypes": modulationTypes=elemento_ref
                        if elemento_ref.id_short=="MaximumBitRate": maximumBitRate=elemento_ref
                    transmissionModeCharacteristics=TransmissionModeCharacteristics(modulationTypes, maximumBitRate,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="NetworkTopology": 
                    for elemento_ref in elemento_contenido.value:
                        if elemento_ref.id_short=="ListOfRanNodes": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="RanNodeN":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Connections":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="UPFByInterfaceN3":upfByInterfaceN3=elemento_ref4
                                                if elemento_ref4.id_short=="AMFByInterfaceN2":amfByInterfaceN2=elemento_ref4
                                                if elemento_ref4.id_short=="UE": ue=elemento_ref4
                                            ranConnections=RANConnections(upfByInterfaceN3,amfByInterfaceN2, ue,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)

                                        if elemento_ref3.id_short=="gNBBasebandUnitResources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            gNBBasebandUnitResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                        if elemento_ref3.id_short=="gNBRemoteRadioUnitResources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            gNBRemoteRadioUnitResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)

                                        if elemento_ref3.id_short=="SupportedSpectrum":supportedSpectrum=elemento_ref3
                                        if elemento_ref3.id_short=="TransmissionPower":transmissionPower=elemento_ref3
                                        if elemento_ref3.id_short=="MaximumTransmissionBandwidth":maximumTransmissionBandwidth=elemento_ref3
                                        if elemento_ref3.id_short=="ReceiverSensitivity":receiverSensitivity=elemento_ref3
                                        if elemento_ref3.id_short=="TransceiverTiming":transceiverTiming=elemento_ref3
                                        if elemento_ref3.id_short=="NumAntennas":numAntennas=elemento_ref3
                                        if elemento_ref3.id_short=="NumLayers": numLayers=elemento_ref3
                                    ranNodeN=RanNodeN(description,ipAddress, ranConnections,gNBBasebandUnitResources,gNBRemoteRadioUnitResources,supportedSpectrum,transmissionPower, maximumTransmissionBandwidth, receiverSensitivity,transceiverTiming,numAntennas, numLayers,elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description,
                                                                                        elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                            listOfRanNodes=ListOfRanNodes(elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            listOfRanNodes.add_node(ranNodeN)
                        if elemento_ref.id_short=="ListOfCN": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="LMF":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="LMF_resources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            lmfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    lmf=CoreNetwork(ipAddress, description,lmfResources, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="NSSF":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="NSSF_resources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            nssfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    nssf=CoreNetwork(ipAddress, description,nssfResources, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="AF":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="AF_resources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            afResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    af=CoreNetwork(ipAddress, description,afResources, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="PCF":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="PCF_resources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            pcfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    pcf=CoreNetwork(ipAddress, description,pcfResources, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="SMF":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="SMF_resources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                            smfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    smf=CoreNetwork(ipAddress, description,smfResources, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="AMF":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="IpAddress":ipAddress=elemento_ref3
                                        if elemento_ref3.id_short=="Description":description=elemento_ref3
                                        if elemento_ref3.id_short=="AMF_resources":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="Position":position=elemento_ref4
                                                if elemento_ref4.id_short=="VirtualMachineID":virtualMachineID=elemento_ref4
                                                if elemento_ref4.id_short=="StorageMemory":storageMemory=elemento_ref4
                                                if elemento_ref4.id_short=="RamMemory":ramMemory=elemento_ref4
                                        amfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    amf=CoreNetwork(ipAddress, description,amfResources, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="UPFList":
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="UPFn":
                                            for elemento_ref4 in elemento_ref3:
                                                if elemento_ref4.id_short=="IpAddress":ipAddress=elemento_ref4
                                                if elemento_ref4.id_short=="Description":description=elemento_ref4
                                                if elemento_ref4.id_short=="UPF_resources":
                                                    for elemento_ref5 in elemento_ref4:
                                                        if elemento_ref5.id_short=="Position":position=elemento_ref5
                                                        if elemento_ref5.id_short=="VirtualMachineID":virtualMachineID=elemento_ref5
                                                        if elemento_ref5.id_short=="StorageMemory":storageMemory=elemento_ref5
                                                        if elemento_ref5.id_short=="RamMemory":ramMemory=elemento_ref5
                                                    upfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,elemento_ref4.id_short,elemento_ref4.value, elemento_ref4.category, elemento_ref4.description,
                                                                                                elemento_ref4.parent, elemento_ref4.semantic_id, elemento_ref4.qualifier, elemento_ref4.kind)
                                            upfN=CoreNetwork(ipAddress, description,upfResources, elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)
                                    listOfUPF=ListOfUPF(elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                    listOfUPF.add_upf(upfN)
                            listOfCN=ListOfCN(listOfUPF,af,pcf,smf,amf,nssf,lmf,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                        if elemento_ref.id_short=="InterfacesCapacityMbps": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="N1":n1=elemento_ref2
                                if elemento_ref2.id_short=="N2":n2=elemento_ref2
                                if elemento_ref2.id_short=="N3":n3=elemento_ref2
                                if elemento_ref2.id_short=="N4":n4=elemento_ref2 
                                if elemento_ref2.id_short=="N5":n5=elemento_ref2
                                if elemento_ref2.id_short=="N6":n6=elemento_ref2
                                if elemento_ref2.id_short=="Rx":rx=elemento_ref2
                                if elemento_ref2.id_short=="Naf":naf=elemento_ref2
                                if elemento_ref2.id_short=="Npcf":npcf=elemento_ref2
                                if elemento_ref2.id_short=="Nsmf":nsmf=elemento_ref2
                                if elemento_ref2.id_short=="Namf":namf=elemento_ref2 
                            interfacesCapacityMbps=InterfacesCapacityMbps(n1,n2,n3,n4,n5,n6,rx,naf,npcf,nsmf,namf,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                    networkTopology=NetworkTopology(listOfRanNodes,listOfCN,interfacesCapacityMbps,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)  
            network5GDataSheet=Network5GDataSheet(releaseCompatibility3GPP,networkProtocols, coverageRange, supportedSpectrum, supportedTransmissionPower,transmissionModeCharacteristics, networkTopology, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)                    
        elif(obj.identification.id==virtualsNetwork):  #VirtualsNetwork Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="ListOfVirtualLANs": 
                    for elemento_ref in elemento_contenido.value:
                        if elemento_ref.id_short=="VirtualLANN": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="VirtualLANId": virtualLANId=elemento_ref2
                                if elemento_ref2.id_short=="VLANPriority": vlanPriority=elemento_ref2
                                if elemento_ref2.id_short=="VLANTag":vlanTag=elemento_ref2
                                if elemento_ref2.id_short=="IpAddress":ipAddress=elemento_ref2
                                if elemento_ref2.id_short=="VirtualLANComputingCapability": 
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="VirtualMachineID":virtualMachineID=elemento_ref3
                                        if elemento_ref3.id_short=="StorageMemory":storageMemory=elemento_ref3
                                        if elemento_ref3.id_short=="RamMemory":ramMemory=elemento_ref3
                                    virtualLANComputingCapability=ComputingCapability(virtualMachineID, storageMemory, ramMemory, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                            virtualLAN=VirtualLANN(virtualLANId,vlanPriority,vlanTag,virtualLANComputingCapability,ipAddress, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                    virtualLANList=ListOfVirtualLANs(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    virtualLANList.add_virtualLAN(virtualLAN)
                if elemento_contenido.id_short=="ListOfNetworkSlices": 
                    for elemento_ref in elemento_contenido.value:
                        if elemento_ref.id_short=="NetworkSliceN": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="SNSSAI": 
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="SliceServiceType":sliceServiceType=elemento_ref3
                                        if elemento_ref3.id_short=="SliceDifferenciator": sliceDifferenciator=elemento_ref3
                                    snssai=SNSSAI(sliceServiceType, sliceDifferenciator, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="IpAddress":ipAddress=elemento_ref2
                                if elemento_ref2.id_short=="SliceComputingCapability": 
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="VirtualMachineID":virtualMachineID=elemento_ref3
                                        if elemento_ref3.id_short=="StorageMemory":storageMemory=elemento_ref3
                                        if elemento_ref3.id_short=="RamMemory":ramMemory=elemento_ref3
                                    sliceComputingCapability=ComputingCapability(virtualMachineID, storageMemory, ramMemory, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                if elemento_ref2.id_short=="SliceCommunicationAtributes": 
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="RadioSpectrum":radioSpectrum=elemento_ref3
                                        if elemento_ref3.id_short=="Availability":availability=elemento_ref3
                                        if elemento_ref3.id_short=="AreaOfService":areaOfService=elemento_ref3
                                        if elemento_ref3.id_short=="IsolationLevel":isolationLevel=elemento_ref3
                                        if elemento_ref3.id_short=="MaximumSupportedPacketSize":maximumSupportedPacketSize=elemento_ref3
                                        if elemento_ref3.id_short=="ServiceCategory":serviceCategory=elemento_ref3
                                        if elemento_ref3.id_short=="NetworkSliceEnergyEficiency":networkSliceEnergyEficiency=elemento_ref3
                                    sliceCommunicationAtributes=SliceCommunicationAtributes(radioSpectrum, availability, areaOfService, isolationLevel, maximumSupportedPacketSize, serviceCategory, networkSliceEnergyEficiency, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                            networkSliceN=NetworkSliceN(snssai,sliceComputingCapability,ipAddress,sliceCommunicationAtributes,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                    networkSliceList=ListOfNetworkSlices(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    networkSliceList.add_networkSlice(networkSliceN)
                if elemento_contenido.id_short=="NetworkSliceReconfigurationFunction": networkSliceReconfigurationFunction=elemento_contenido
            virtualsNetwork=VirtualsNetwork(virtualLANList,networkSliceList,networkSliceReconfigurationFunction, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)              
        elif(obj.identification.id==connectivity):  #Connectivity Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="UesAttachedList": 
                    for elemento_ref in elemento_contenido.value:
                        if elemento_ref.id_short=="UeAttachedN": 
                            for elemento_ref2 in elemento_ref:
                                if elemento_ref2.id_short=="UeDescription":ueDescription=elemento_ref2
                                if elemento_ref2.id_short=="UeID": 
                                    for elemento_ref3 in elemento_ref2:
                                        if elemento_ref3.id_short=="PEI":pei=elemento_ref3
                                        if elemento_ref3.id_short=="GPSI":gpsi=elemento_ref3
                                    ueID=UeID(pei, gpsi, elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                            ueAttachedN=UeAttachedN(ueID,ueDescription,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                    uesAttachedList=UEAttachedList(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    uesAttachedList.add_ue(ueAttachedN)
                    
                if elemento_contenido.id_short=="PDUSessionList": 
                    for elemento_ref in elemento_contenido.value:
                        if elemento_ref.id_short=="PDUSessionN":                                                                                
                            for elemento_ref2 in elemento_ref.value:
                                if elemento_ref2.id_short=="IPAddress": ip_address=elemento_ref2
                                if elemento_ref2.id_short=="UE": ue=elemento_ref2
                                if elemento_ref2.id_short=="DDNDestination": ddnDestination=elemento_ref2
                                if elemento_ref2.id_short=="LinkDirection": linkDirection=elemento_ref2 
                                if elemento_ref2.id_short=="QosFlowList":
                                    for elemento_ref3 in elemento_ref2.value: 
                                        if elemento_ref3.id_short=="QosFlowN":
                                            for elemento_ref4 in elemento_ref3.value: 
                                                if elemento_ref4.id_short=="QFI": qfi= elemento_ref4
                                                if elemento_ref4.id_short=="PDUSessionID": pduSessionID= elemento_ref4
                                                if elemento_ref4.id_short=="PDUSessionType": pduSessionType= elemento_ref4
                                                if elemento_ref4.id_short=="QosProfileRequested": 
                                                    for elemento_ref5 in elemento_ref4.value: 
                                                        if elemento_ref5.id_short=="QosParameters":
                                                            for elemento_ref6 in elemento_ref5.value: 
                                                                if elemento_ref6.id_short=="QosIdentifier": qosIdentifier=elemento_ref6
                                                                if elemento_ref6.id_short=="ARP": arp=elemento_ref6
                                                                if elemento_ref6.id_short=="RQA": rqa=elemento_ref6
                                                                if elemento_ref6.id_short=="NotificationControl": notificationControl=elemento_ref6
                                                                if elemento_ref6.id_short=="GFBRUL": gfbr_ul=elemento_ref6
                                                                if elemento_ref6.id_short=="GFBRDL": gfbr_dl=elemento_ref6
                                                                if elemento_ref6.id_short=="MFBRUL": mfbr_ul=elemento_ref6
                                                                if elemento_ref6.id_short=="MFBRDL": mfbr_dl=elemento_ref6
                                                                if elemento_ref6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref6
                                                                if elemento_ref6.id_short=="AggregateBitRates": 
                                                                    AggregateBitRates=elemento_ref6
                                                                    qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                elemento_ref5.id_short,elemento_ref5.value, elemento_ref5.category, elemento_ref5.description,
                                                                                                elemento_ref5.parent, elemento_ref5.semantic_id, elemento_ref5.qualifier, elemento_ref5.kind)
                                                                    
                                                        if elemento_ref5.id_short=="QosCharacteristics":
                                                            for elemento_ref6 in elemento_ref5.value: 
                                                                if elemento_ref6.id_short=="ResourceType": ResourceType=elemento_ref6
                                                                if elemento_ref6.id_short=="PriorityLevel": PriorityLevel=elemento_ref6
                                                                if elemento_ref6.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref6
                                                                if elemento_ref6.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref6
                                                                if elemento_ref6.id_short=="AveragingWindow": AveragingWindow=elemento_ref6
                                                                if elemento_ref6.id_short=="MaximumDataBurstVolume": 
                                                                    MaximumDataBurstVolume=elemento_ref6
                                                                    qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                elemento_ref5.id_short,elemento_ref5.value, elemento_ref5.category, elemento_ref5.description,
                                                                                                elemento_ref5.parent, elemento_ref5.semantic_id, elemento_ref5.qualifier, elemento_ref5.kind)
                                                                    
                                                        if elemento_ref5.id_short=="AlternativeQosProfiles":
                                                            for elemento_ref6 in elemento_ref5.value:
                                                                    if elemento_ref6.id_short=="AlternativeQosProfileN":
                                                                        for elemento_ref7 in elemento_ref6.value:
                                                                            if elemento_ref7.id_short=="QosParameters":
                                                                                for elemento_ref8 in elemento_ref7.value:
                                                                                    if elemento_ref8.id_short=="QosIdentifier": qosIdentifier=elemento_ref8
                                                                                    if elemento_ref8.id_short=="ARP": arp=elemento_ref8
                                                                                    if elemento_ref8.id_short=="RQA": rqa=elemento_ref8
                                                                                    if elemento_ref8.id_short=="NotificationControl": notificationControl=elemento_ref8
                                                                                    if elemento_ref8.id_short=="GFBRUL": gfbr_ul=elemento_ref8
                                                                                    if elemento_ref8.id_short=="GFBRDL": gfbr_dl=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MFBRUL": mfbr_ul=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MFBRDL": mfbr_dl=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref8
                                                                                    if elemento_ref8.id_short=="AggregateBitRates": 
                                                                                        AggregateBitRates=elemento_ref8
                                                                                        alternative_qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                                    elemento_ref7.id_short,elemento_ref7.value, elemento_ref7.category, elemento_ref7.description,
                                                                                                                    elemento_ref7.parent, elemento_ref7.semantic_id, elemento_ref7.qualifier, elemento_ref7.kind)
                                                                                          
                                                                            if elemento_ref7.id_short=="QosCharacteristics":
                                                                                for elemento_ref8 in elemento_ref7.value:
                                                                                    if elemento_ref8.id_short=="ResourceType": ResourceType=elemento_ref8
                                                                                    if elemento_ref8.id_short=="PriorityLevel": PriorityLevel=elemento_ref8
                                                                                    if elemento_ref8.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref8
                                                                                    if elemento_ref8.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref8
                                                                                    if elemento_ref8.id_short=="AveragingWindow": AveragingWindow=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MaximumDataBurstVolume": 
                                                                                        MaximumDataBurstVolume=elemento_ref8
                                                                                        alternative_qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                                    elemento_ref7.id_short,elemento_ref7.value, elemento_ref7.category, elemento_ref7.description,
                                                                                                                    elemento_ref7.parent, elemento_ref7.semantic_id, elemento_ref7.qualifier, elemento_ref7.kind)
                                                                        alternativeQosProfile=AlternativeQosProfile(alternative_qos_parameters,alternative_qos_characteristics,
                                                                                                elemento_ref6.id_short,elemento_ref6.value, elemento_ref6.category, elemento_ref6.description,
                                                                                                elemento_ref6.parent, elemento_ref6.semantic_id, elemento_ref6.qualifier, elemento_ref6.kind)
                                                            alternativeQosProfiles=AlternativeQosProfiles(elemento_ref5.id_short,elemento_ref5.value, elemento_ref5.category, elemento_ref5.description,
                                                                                                elemento_ref5.parent, elemento_ref5.semantic_id, elemento_ref5.qualifier, elemento_ref5.kind)
                                                            alternativeQosProfiles.add_alternative_qos_profile(alternativeQosProfile)
                                                    qosProfileRequested=QosProfileRequested(qos_parameters, qos_characteristics, alternativeQosProfiles, elemento_ref4.id_short,elemento_ref4.value, elemento_ref4.category, 
                                                                                        elemento_ref4.description, elemento_ref4.parent, elemento_ref4.semantic_id, elemento_ref4.qualifier, elemento_ref4.kind)                
                                                            
                                                                                    
                                                if elemento_ref4.id_short=="QosProfileGuaranteed":
                                                    for elemento_ref5 in elemento_ref4.value: 
                                                        if elemento_ref5.id_short=="QosParameters":
                                                            for elemento_ref6 in elemento_ref5.value: 
                                                                if elemento_ref6.id_short=="QosIdentifier": qosIdentifier=elemento_ref6
                                                                if elemento_ref6.id_short=="ARP": arp=elemento_ref6
                                                                if elemento_ref6.id_short=="RQA": rqa=elemento_ref6
                                                                if elemento_ref6.id_short=="NotificationControl": notificationControl=elemento_ref6
                                                                if elemento_ref6.id_short=="GFBRUL": gfbr_ul=elemento_ref6
                                                                if elemento_ref6.id_short=="GFBRDL": gfbr_dl=elemento_ref6
                                                                if elemento_ref6.id_short=="MFBRUL": mfbr_ul=elemento_ref6
                                                                if elemento_ref6.id_short=="MFBRDL": mfbr_dl=elemento_ref6
                                                                if elemento_ref6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref6
                                                                if elemento_ref6.id_short=="AggregateBitRates": 
                                                                    AggregateBitRates=elemento_ref6
                                                                    qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                elemento_ref5.id_short,elemento_ref5.value, elemento_ref5.category, elemento_ref5.description,
                                                                                                elemento_ref5.parent, elemento_ref5.semantic_id, elemento_ref5.qualifier, elemento_ref5.kind)
                                                                    
                                                        if elemento_ref5.id_short=="QosCharacteristics":
                                                            for elemento_ref6 in elemento_ref5.value: 
                                                                if elemento_ref6.id_short=="ResourceType": ResourceType=elemento_ref6
                                                                if elemento_ref6.id_short=="PriorityLevel": PriorityLevel=elemento_ref6
                                                                if elemento_ref6.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref6
                                                                if elemento_ref6.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref6
                                                                if elemento_ref6.id_short=="AveragingWindow": AveragingWindow=elemento_ref6
                                                                if elemento_ref6.id_short=="MaximumDataBurstVolume": 
                                                                    MaximumDataBurstVolume=elemento_ref6
                                                                    qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                elemento_ref5.id_short,elemento_ref5.value, elemento_ref5.category, elemento_ref5.description,
                                                                                                elemento_ref5.parent, elemento_ref5.semantic_id, elemento_ref5.qualifier, elemento_ref5.kind)
                                                                    
                                                        if elemento_ref5.id_short=="AlternativeQosProfiles":
                                                            for elemento_ref6 in elemento_ref5.value:
                                                                    if elemento_ref6.id_short=="AlternativeQosProfileN":
                                                                        for elemento_ref7 in elemento_ref6.value:
                                                                            if elemento_ref7.id_short=="QosParameters":
                                                                                for elemento_ref8 in elemento_ref7.value:
                                                                                    if elemento_ref8.id_short=="QosIdentifier": qosIdentifier=elemento_ref8
                                                                                    if elemento_ref8.id_short=="ARP": arp=elemento_ref8
                                                                                    if elemento_ref8.id_short=="RQA": rqa=elemento_ref8
                                                                                    if elemento_ref8.id_short=="NotificationControl": notificationControl=elemento_ref8
                                                                                    if elemento_ref8.id_short=="GFBRUL": gfbr_ul=elemento_ref8
                                                                                    if elemento_ref8.id_short=="GFBRDL": gfbr_dl=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MFBRUL": mfbr_ul=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MFBRDL": mfbr_dl=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref8
                                                                                    if elemento_ref8.id_short=="AggregateBitRates": 
                                                                                        AggregateBitRates=elemento_ref8
                                                                                        alternative_qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                                    elemento_ref7.id_short,elemento_ref7.value, elemento_ref7.category, elemento_ref7.description,
                                                                                                                    elemento_ref7.parent, elemento_ref7.semantic_id, elemento_ref7.qualifier, elemento_ref7.kind)
                                                                                          
                                                                            if elemento_ref7.id_short=="QosCharacteristics":
                                                                                for elemento_ref8 in elemento_ref7.value:
                                                                                    if elemento_ref8.id_short=="ResourceType": ResourceType=elemento_ref8
                                                                                    if elemento_ref8.id_short=="PriorityLevel": PriorityLevel=elemento_ref8
                                                                                    if elemento_ref8.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref8
                                                                                    if elemento_ref8.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref8
                                                                                    if elemento_ref8.id_short=="AveragingWindow": AveragingWindow=elemento_ref8
                                                                                    if elemento_ref8.id_short=="MaximumDataBurstVolume": 
                                                                                        MaximumDataBurstVolume=elemento_ref8
                                                                                        alternative_qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                                    elemento_ref7.id_short,elemento_ref7.value, elemento_ref7.category, elemento_ref7.description,
                                                                                                                    elemento_ref7.parent, elemento_ref7.semantic_id, elemento_ref7.qualifier, elemento_ref7.kind)
                                                                        alternativeQosProfile=AlternativeQosProfile(alternative_qos_parameters,alternative_qos_characteristics,
                                                                                                elemento_ref6.id_short,elemento_ref6.value, elemento_ref6.category, elemento_ref6.description,
                                                                                                elemento_ref6.parent, elemento_ref6.semantic_id, elemento_ref6.qualifier, elemento_ref6.kind)
                                                            alternativeQosProfiles=AlternativeQosProfiles(elemento_ref5.id_short,elemento_ref5.value, elemento_ref5.category, elemento_ref5.description,
                                                                                                elemento_ref5.parent, elemento_ref5.semantic_id, elemento_ref5.qualifier, elemento_ref5.kind)
                                                            alternativeQosProfiles.add_alternative_qos_profile(alternativeQosProfile)
                                                    qosProfileGuaranteed=QosProfileGuaranteed(qos_parameters, qos_characteristics, alternativeQosProfiles, elemento_ref4.id_short,elemento_ref4.value, elemento_ref4.category, 
                                                                                        elemento_ref4.description, elemento_ref4.parent, elemento_ref4.semantic_id, elemento_ref4.qualifier, elemento_ref4.kind)
                                            qosFlowN=QosFlowConnectivity(qfi,qosProfileRequested,qosProfileGuaranteed,pduSessionID, pduSessionType,elemento_ref3.id_short,elemento_ref3.value, elemento_ref3.category, elemento_ref3.description,
                                                                                                elemento_ref3.parent, elemento_ref3.semantic_id, elemento_ref3.qualifier, elemento_ref3.kind)       
                                    qosFlowConnectivityList=QosFlowConnectivityList(elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                    qosFlowConnectivityList.add_qos_flow(qosFlowN)       
                            
                            pduSessionConnectivity=PDUSessionConnectivity(ipAddress,ue,ddnDestination,linkDirection,qosFlowConnectivityList,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                    pduSessionConnectivityList=PDUSessionConnectivityList(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    pduSessionConnectivityList.add_pdu_session(pduSessionConnectivity)
                if elemento_contenido.id_short=="QosMappingFunction":qosMappingFunction=elemento_contenido
                if elemento_contenido.id_short=="GetRANConfiguration":getRANConfiguration=elemento_contenido
                if elemento_contenido.id_short=="SetRANConfiguration":setRANConfiguration=elemento_contenido
                if elemento_contenido.id_short=="EstablishConnectionFunction":establishingConnectionsFunction=elemento_contenido
            connectivity=Connectivity(uesAttachedList,pduSessionConnectivityList, qosMappingFunction, getRANConfiguration, setRANConfiguration,establishingConnectionsFunction, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)                       
        elif(obj.identification.id==qosPerformance):  #QosPerformance Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="LogicalNetworkList": 
                        for elemento_ref in elemento_contenido.value:
                            if elemento_ref.id_short=="LogicalNetworkNPerformance": 
                                for elemento_ref2 in elemento_ref:
                                    if elemento_ref2.id_short=="ActualBitRate":actualBitRate=elemento_ref2
                                    if elemento_ref2.id_short=="PacketLossRate":packetLossRate=elemento_ref2
                                    if elemento_ref2.id_short=="BLER":bler=elemento_ref2
                                    if elemento_ref2.id_short=="Throughput": 
                                        for elemento_ref3 in elemento_ref2:
                                            if elemento_ref3.id_short=="Average":avg=elemento_ref3
                                            if elemento_ref3.id_short=="Max":max=elemento_ref3
                                            if elemento_ref3.id_short=="Min":min=elemento_ref3
                                        throughput=Throughput(avg,max,min,elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                    if elemento_ref2.id_short=="Latency": 
                                        for elemento_ref3 in elemento_ref2:
                                            if elemento_ref3.id_short=="Average":avg=elemento_ref3
                                            if elemento_ref3.id_short=="Max":max=elemento_ref3
                                            if elemento_ref3.id_short=="Min":min=elemento_ref3
                                        latency=Latency(avg,max,min,elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                    if elemento_ref2.id_short=="Reliability":reliability=elemento_ref2
                                    if elemento_ref2.id_short=="CapacityUtilization":capacityUtilization=elemento_ref2
                                    if elemento_ref2.id_short=="SignalLevel": 
                                        for elemento_ref3 in elemento_ref2:
                                            if elemento_ref3.id_short=="SINR":sinr=elemento_ref3
                                            if elemento_ref3.id_short=="RSSI":rssi=elemento_ref3
                                            if elemento_ref3.id_short=="RSRP":rsrp=elemento_ref3
                                            if elemento_ref3.id_short=="RSRQ":rsrq=elemento_ref3
                                        signal_level=NetworkSignalLevel(sinr,rssi,rsrp,rsrq,elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description, elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                logicalNetworkNPerformance=LogicalNetworkNPerformance(actualBitRate,packetLossRate,bler,throughput,latency,reliability,capacityUtilization,signal_level,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                        logicalNetworkList=LogicalNetworkList(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                        logicalNetworkList.add_logicalNetwork(logicalNetworkNPerformance)

                if elemento_contenido.id_short=="ParametersPertainingConnections":
                        for elemento_ref in elemento_contenido.value:                                                                                                   
                            for elemento_ref_2 in elemento_ref.value:   #                                       
                                for elemento_ref_3 in elemento_ref_2.value: 
                                    if elemento_ref_3.id_short=="IPAddress": ip_address=elemento_ref_3 
                                    if elemento_ref_3.id_short=="QosFlowList":
                                        for elemento_ref_4 in elemento_ref_3.value: 
                                            if elemento_ref_4.id_short=="QosFlowN":
                                                for elemento_ref_5 in elemento_ref_4.value:  
                                                    if elemento_ref_5.id_short=="QFI": qfi= elemento_ref_5
                                                    if elemento_ref_5.id_short=="CommunicationServiceAvailability":commservavai=elemento_ref_5
                                                    if elemento_ref_5.id_short=="CommunicationServiceReliability":commservrel=elemento_ref_5
                                                    if elemento_ref_5.id_short=="EndToEndLatency":e2el=elemento_ref_5
                                                    if elemento_ref_5.id_short=="UpdateTime":updateTime=elemento_ref_5
                                                    if elemento_ref_5.id_short=="SurvivalTime":survivalTime=elemento_ref_5
                                                    if elemento_ref_5.id_short=="Latency": 
                                                        for elemento_ref6 in elemento_ref_5:
                                                            if elemento_ref6.id_short=="Average":avg=elemento_ref6
                                                            if elemento_ref6.id_short=="Max":max=elemento_ref6
                                                            if elemento_ref6.id_short=="Min":min=elemento_ref6
                                                        latency=Latency(avg,max,min,elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description, elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                    if elemento_ref_5.id_short=="ServiceBitRate":
                                                        for elemento_ref6 in elemento_ref_5:
                                                            if elemento_ref6.id_short=="Average":avg=elemento_ref6
                                                            if elemento_ref6.id_short=="Max":max=elemento_ref6
                                                            if elemento_ref6.id_short=="Min":min=elemento_ref6
                                                        serviceBitRate=ServiceBitRate(avg,max,min,elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description, elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                    if elemento_ref_5.id_short=="DataThroughput":
                                                        for elemento_ref6 in elemento_ref_5:
                                                            if elemento_ref6.id_short=="Average":avg=elemento_ref6
                                                            if elemento_ref6.id_short=="Max":max=elemento_ref6
                                                            if elemento_ref6.id_short=="Min":min=elemento_ref6
                                                        dataThroughput=DataThroughput(avg,max,min,elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description, elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                    if elemento_ref_5.id_short=="PacketErrorRatio":
                                                        for elemento_ref6 in elemento_ref_5:
                                                            if elemento_ref6.id_short=="Average":avg=elemento_ref6
                                                            if elemento_ref6.id_short=="Max":max=elemento_ref6
                                                            if elemento_ref6.id_short=="Min":min=elemento_ref6
                                                        per=PacketErrorRatio(avg,max,min,elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description, elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                    if elemento_ref_5.id_short=="BLER":
                                                        for elemento_ref6 in elemento_ref_5:
                                                            if elemento_ref6.id_short=="Average":avg=elemento_ref6
                                                            if elemento_ref6.id_short=="Max":max=elemento_ref6
                                                            if elemento_ref6.id_short=="Min":min=elemento_ref6
                                                        bler=BLER(avg,max,min,elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description, elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                qos_flow=QosFlowPerformance(qfi,commservavai,commservrel,e2el,survivalTime,latency, serviceBitRate,per,bler,updateTime,dataThroughput,elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)
                                                                                            
                                        qos_flow_list=QosFlowPerformanceList(elemento_ref_3.id_short,elemento_ref_3.value, elemento_ref_3.category, 
                                                                                            elemento_ref_3.description, elemento_ref_3.parent, elemento_ref_3.semantic_id, elemento_ref_3.qualifier, elemento_ref_3.kind)
                                        qos_flow_list.add_qos_flow(qos_flow)
                                pdu_session=PDUSessionPerformance(ip_address,qos_flow_list,elemento_ref_2.id_short,elemento_ref_2.value, elemento_ref_2.category, 
                                                                                            elemento_ref_2.description, elemento_ref_2.parent, elemento_ref_2.semantic_id, elemento_ref_2.qualifier, elemento_ref_2.kind)
                            pdu_session_list=PDUSessionPerformanceList(elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                            elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            pdu_session_list.add_pdu_session(pdu_session)
                        parameterspertainingConnections=ParametersPertainingConnections(pdu_session_list,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="ListOfSubscriptions":
                        for elemento_ref in elemento_contenido:
                            if elemento_ref.id_short=="ListOfEvents":
                                for elemento_ref2 in elemento_ref:  
                                    if elemento_ref2.id_short=="Event1":event1=elemento_ref2
                                listOfEvents= ListOfNetworkPerformanceEvents(elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description,
                                                                                                        elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                                listOfEvents.add_event(event1)
                            if elemento_ref.id_short=="Subscription1":
                                subscription1=elemento_ref
                        
                        listOfSubscriptions= ListOfNetworkPerformanceSubscriptions(listOfEvents,elemento_ref2.id_short,elemento_ref2.value, elemento_ref2.category, elemento_ref2.description,
                                                                                            elemento_ref2.parent, elemento_ref2.semantic_id, elemento_ref2.qualifier, elemento_ref2.kind)
                        listOfSubscriptions.add_subscription(subscription1)
                if elemento_contenido.id_short=="SubscriptionRequestFunction":subscriptionRequestFunction=elemento_contenido
                if elemento_contenido.id_short=="EstimatePacketTransmissionPerformanceFunction":estimatePacketTransmissionPerformanceFunction=elemento_contenido
                if elemento_contenido.id_short=="EstimateNetworkPerformanceFunction":estimateNetworkPerformanceFunction=elemento_contenido
                if elemento_contenido.id_short=="UpdateTime":updateTime=elemento_contenido
            qosPerformance=QosPerformance(logicalNetworkList, parameterspertainingConnections, listOfSubscriptions, subscriptionRequestFunction, estimatePacketTransmissionPerformanceFunction, estimateNetworkPerformanceFunction,updateTime, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)                                                                           
        elif(obj.identification.id==dataAnalytics):  #DataAnalytics Network
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="Analytics":analytics=elemento_contenido
            dataAnalytics=DataAnalytics(analytics, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind) 

for obj in new_object_store:
    if isinstance(obj,AssetAdministrationShell):
        if obj.id_short=="NETWORK_5G_AAS":
            aasnw5G=AASNetwork5G(network5G,nameplate,identification,documentation,service,technicalDataNetwork,npn5GNWIdentity,assetServiceRegistry,tsnCapabilities,network5GDataSheet,virtualsNetwork,connectivity,qosPerformance,networkLocation,dataAnalytics,obj.asset, obj.identification, obj.id_short, obj.category, obj.description, obj.parent, obj.administration, obj.security, obj.submodel, obj.concept_dictionary, obj.view, obj.derived_from)          
