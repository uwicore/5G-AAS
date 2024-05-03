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
from AAS5Gsubmodels import *       #Here we have the created structure for the AAS

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



#First we read the assets    
for obj in new_object_store:
    if isinstance(obj, Asset):    
        if obj.id_short=="NETWORK_5G":
            network5G=Network5G(obj.kind, obj.identification, obj.id_short, obj.category, obj.description)

#Now the submodels
for obj in new_object_store:
    if isinstance(obj, Submodel):
        if(obj.id_short=="Nameplate"):  #Nameplate Network
            for element_content in obj:
                if element_content.id_short=="ManufacturerName": manufacturerName=element_content
                if element_content.id_short=="ManufacturerTypName": manufacturerTypName=element_content
                if isinstance(element_content, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for element_ref in element_content.value:  
                        if element_ref.id_short=="CountryCode": countryCode=element_ref
                        if element_ref.id_short=="Street": street=element_ref
                        if element_ref.id_short=="PostalCode": postalCode=element_ref
                        if element_ref.id_short=="City": city=element_ref
                        if element_ref.id_short=="StateCounty": 
                            stateCounty=element_ref
                            physical_address=PhysicalAddress(countryCode,street, postalCode, city, stateCounty, element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                            
                if element_content.id_short=="TypClass": typClass=element_content
                if element_content.id_short=="SerialNo": serialNo=element_content
                if element_content.id_short=="ChargeId": chargeId=element_content
                if element_content.id_short=="CountryOfOrigin": countryOfOrigin=element_content
                if element_content.id_short=="YearOfConstruction": yearOfConstruction=element_content
            nameplate=Nameplate(manufacturerName,manufacturerTypName,physical_address,typClass,serialNo,chargeId,countryOfOrigin,yearOfConstruction, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)       
        elif(obj.id_short=="Identification"):  #Identification Network
            for element_content in obj:
                if element_content.id_short=="ManufacturerName": manufacturerName=element_content
                if element_content.id_short=="ManufacturerId01": manufacturerId01=element_content
                if element_content.id_short=="ManufacturerIdProvider": manufacturerIdProvider=element_content
                if element_content.id_short=="ManufacturerTypId": manufacturerTypId=element_content
                if element_content.id_short=="ManufacturerTypName": manufacturerTypName=element_content
                if element_content.id_short=="ManufacturerTypDescription": manufacturerTypDescription=element_content
                if element_content.id_short=="SupplierName": supplierName=element_content
                if element_content.id_short=="SupplierId": supplierId=element_content
                if element_content.id_short=="SupplierIdProvider": supplierIdProvider=element_content
                if element_content.id_short=="SupplierTypId": supplierTypId=element_content
                if element_content.id_short=="SupplierTypName": supplierTypName=element_content
                if element_content.id_short=="SupplierTypDescription": supplierTypDescription=element_content
                if element_content.id_short=="TypClass": typClass=element_content
                if element_content.id_short=="ClassificationSystem": classificationSystem=element_content
                if element_content.id_short=="SecondaryKeyTyp": secondaryKeyTyp=element_content
                if element_content.id_short=="AssetId": assetId=element_content
                if element_content.id_short=="InstanceId": instanceId=element_content
                if element_content.id_short=="ChargeId": assetId=element_content
                if element_content.id_short=="SecondaryKeyInstance": secondaryKeyInstance=element_content
                if element_content.id_short=="ManufacturingDate": manufacturingDate=element_content
                if element_content.id_short=="DeviceRevision": deviceRevision=element_content
                if element_content.id_short=="SoftwareRevision": softwareRevision=element_content
                if element_content.id_short=="HardwareRevision": hardwareRevision=element_content
                if isinstance(element_content, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for element_ref in element_content.value:   
                        if element_ref.id_short=="Name": name=element_ref
                        if element_ref.id_short=="Role": role=element_ref
                        if isinstance(element_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)): 
                            for element_ref_2 in element_ref.value:
                                if element_ref_2.id_short=="CountryCode": countryCode=element_ref_2
                                if element_ref_2.id_short=="Street": street=element_ref_2
                                if element_ref_2.id_short=="PostalCode": postalCode=element_ref_2
                                if element_ref_2.id_short=="City": city=element_ref_2
                                if element_ref_2.id_short=="StateCounty": 
                                    stateCounty=element_ref_2
                                    physical_address=PhysicalAddress(countryCode,street, postalCode, city, stateCounty, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                        element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)

                        if element_ref.id_short=="Email": email=element_ref
                        if element_ref.id_short=="URL": url=element_ref
                        if element_ref.id_short=="Phone": phone=element_ref
                        if element_ref.id_short=="Fax":
                            fax=element_ref
                            contact_info=ContactInfo(name,role,physical_address,email,url,phone,fax, element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                if element_content.id_short=="URL": url=element_content
            identification=Identification(manufacturerName,manufacturerId01,manufacturerIdProvider,manufacturerTypId,manufacturerTypName,manufacturerTypDescription,supplierName,supplierId,supplierIdProvider,supplierTypId,supplierTypName,supplierTypDescription,typClass,
                                        classificationSystem, secondaryKeyTyp,assetId,instanceId,chargeId,secondaryKeyInstance,manufacturingDate,deviceRevision,softwareRevision,hardwareRevision,contact_info,url,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.id_short=="Documentation"):  #Documentation Network
            documentation= Documentation(obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind) 
        elif(obj.id_short=="Service"):  #Service Network
            for element_content in obj:
                if isinstance(element_content,(SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                    for element_ref in element_content:
                        if element_ref.id_short=="NameOfSupplier": nameOfSupplier=element_ref
                        if element_ref.id_short=="ContactInfo_Role": contactInfo_role=element_ref
                        if isinstance(element_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)): 
                            for element_ref_2 in element_ref.value:
                                if element_ref_2.id_short=="CountryCode": countryCode=element_ref_2
                                if element_ref_2.id_short=="Street": street=element_ref_2
                                if element_ref_2.id_short=="Zip": postalCode=element_ref_2
                                if element_ref_2.id_short=="CityTown": city=element_ref_2
                                if element_ref_2.id_short=="StateCounty": 
                                    stateCounty=element_ref_2
                                    physical_address=PhysicalAddress(countryCode,street, postalCode, city, stateCounty, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                        element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                        if element_ref.id_short=="Email": email=element_ref
                        if element_ref.id_short=="URL": url=element_ref
                        if element_ref.id_short=="PhoneNumber": phone=element_ref
                        if element_ref.id_short=="Fax":
                            fax=element_ref
                            contact_info=ContactInfo(nameOfSupplier,contactInfo_role,physical_address,email,url,phone,fax, element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
            
            service=Service(contact_info, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.id_short=="Location"):  #Location Network
            for element_content in obj:
                if element_content.id_short=="ListOfConnectedUEs": 
                    for element_ref in element_content:
                        if element_ref.id_short=="ConnectedUE01": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="XPosition":xPosition=element_ref2
                                if element_ref2.id_short=="YPosition":yPosition=element_ref2
                                if element_ref2.id_short=="ZPosition":zPosition=element_ref2 
                                if element_ref2.id_short=="Speed":speed=element_ref2
                                if element_ref2.id_short=="Acceleration":acceleration=element_ref2
                                if element_ref2.id_short=="LCSQosClass": lcsQosClass=element_ref2
                                if element_ref2.id_short=="Accuracy": accuracy=element_ref2
                                if element_ref2.id_short=="ResponseTime": responseTime=element_ref2
                            connectedUE1=ConnectedUe(xPosition, yPosition, zPosition, speed, acceleration, lcsQosClass,accuracy, responseTime,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            listOfConnectedUes=ListOfConnectedUes(element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                            listOfConnectedUes.add_ue(connectedUE1)
                        if element_ref.id_short=="ConnectedUE02": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="XPosition":xPosition=element_ref2
                                if element_ref2.id_short=="YPosition":yPosition=element_ref2
                                if element_ref2.id_short=="ZPosition":zPosition=element_ref2 
                                if element_ref2.id_short=="Speed":speed=element_ref2
                                if element_ref2.id_short=="Acceleration":acceleration=element_ref2
                                if element_ref2.id_short=="LCSQosClass": lcsQosClass=element_ref2
                                if element_ref2.id_short=="Accuracy": accuracy=element_ref2
                                if element_ref2.id_short=="ResponseTime": responseTime=element_ref2
                            connectedUE2=ConnectedUe(xPosition, yPosition, zPosition, speed, acceleration, lcsQosClass,accuracy, responseTime, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                    element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            listOfConnectedUes.add_ue(connectedUE2)
                if element_content.id_short=="SubscriptionManagement":subscriptionManagement=element_content

                
                if element_content.id_short=="ListOfSubscriptions":
                    for element_ref in element_content:
                        if element_ref.id_short=="ListOfEvents":
                            for element_ref2 in element_ref:  
                                if element_ref2.id_short=="Event1":
                                        event1=element_ref2
                                        listOfEvents= ListOfNetworkLocationEvents(element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                                    element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                        listOfEvents.add_event(event1)
                        if element_ref.id_short=="Subscription1":
                            subscription1=element_ref
                            listOfSubscriptions= ListOfNetworkLocationSubscriptions(listOfEvents,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                        element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                            listOfSubscriptions.add_subscription(subscription1)

            networkLocation=Location(listOfConnectedUes,subscriptionManagement,listOfSubscriptions,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)       
        elif(obj.id_short=="NPN5GNWIdentity"):  #NPN5GNWIdentity Network
            for element_content in obj:
                if element_content.id_short=="PLMNID": plmnid=element_content
                if element_content.id_short=="NPNID": npnid=element_content
            npn5GNWIdentity=NPN5GNWIdentity(plmnid, npnid,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.id_short=="AssetServiceRegistry"):  #AssetServiceRegistry Network
            for element_content in obj:
                if element_content.id_short=="AssetService": assetService=element_content
                if element_content.id_short=="IntegratorCompany": integratorCompany=element_content
                if element_content.id_short=="PlanningReferences": planningReferences=element_content
                if element_content.id_short=="SLA": sla=element_content
                if element_content.id_short=="CoverageMap5G": coverageMap5G=element_content
            assetServiceRegistry=AssetServiceRegistry(assetService, integratorCompany, planningReferences, sla, coverageMap5G, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.id_short=="TechnicalData"):  #TechnicalData Network
            for element_content in obj:
                if isinstance(element_content, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for element_ref in element_content.value:  
                        if element_ref.id_short=="ManufacturerName": manufacturerName=element_ref
                        if element_ref.id_short=="ManufacturerProductDesignation": manufacturerProductDesignation=element_ref
                        if element_ref.id_short=="ManufacturerPartNumber": manufacturerPartNumber=element_ref
                        if element_ref.id_short=="ManufacturerOrderCode": 
                            manufacturerOrderCode=element_ref
                            general_info=GeneralInformation(manufacturerName,manufacturerProductDesignation,manufacturerPartNumber, manufacturerOrderCode, element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                        if element_ref.id_short=="TextStatement01": textStatement=element_ref
                        if element_ref.id_short=="ValidDate": 
                            
                            validDate=element_ref
                            further_info=FurtherInformation(textStatement,validDate,element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                        if isinstance(element_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                            for element_ref_2 in element_ref.value:   
                                if element_ref_2.id_short=="ProductClassificationSystem": productClassificationSystem=element_ref_2
                                if element_ref_2.id_short=="ClassificationSystemVersion": classificationSystemVersion=element_ref_2
                                if element_ref_2.id_short=="ProductClassId": 
                                    productClassId=element_ref_2
                                    prod_class_system=ProductClassificationItem(productClassificationSystem,classificationSystem,productClassId, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                        element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)

                                    technicalProperties=TechnicalProperties(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
            technicalDataNetwork=TechnicalData(general_info,prod_class_system,technicalProperties,further_info,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)   
        elif(obj.id_short=="TSNCapabilities"):  #TSNCapabilities Network
            for element_content in obj:
                if element_content.id_short=="Bridge5GSDelay":system5GBridgeDelay=element_content
                if element_content.id_short=="Bridge5GS": 
                    for element_ref in element_content:
                        if element_ref.id_short=="Bridge5GSConfiguration": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="BridgeID":bridgeID=element_ref2
                                if element_ref2.id_short=="Ports":ports=element_ref2
                                if element_ref2.id_short=="StreamFilters":streamFilters=element_ref2 
                                if element_ref2.id_short=="UEDsTtResidenceTime":ueDsTtResidenceTime=element_ref2
                                if element_ref2.id_short=="PropagationDelayPerPort":propagationDelayPerPort=element_ref2
                                if element_ref2.id_short=="TrafficClasses":trafficClasses=element_ref2
                                if element_ref2.id_short=="TimeSynchronizationStatus":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="SynchronizationState":synchronizationState=element_ref3
                                        if element_ref3.id_short=="ClockAccuracy":clockAccuracy=element_ref3
                                        if element_ref3.id_short=="FrequencyStability":
                                            frequencyStability=element_ref3
                                            timeSynchronizationStatus= TimeSynchronizationStatus(synchronizationState, clockAccuracy, frequencyStability, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                        element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                            bridge5GSConfiguration=Bridge5GSConfiguration(bridgeID, ports, streamFilters, ueDsTtResidenceTime, propagationDelayPerPort, timeSynchronizationStatus, trafficClasses, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)

                        if element_ref.id_short=="TsnFlowList": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="TsnFlowN":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="DestinationIP":destinationIP=element_ref3
                                        if element_ref3.id_short=="DestinationMacAddress":destinationMacAddress=element_ref3
                                        if element_ref3.id_short=="StreamId":streamId=element_ref3
                                        if element_ref3.id_short=="QosProfileAssociated":qosProfileAssociated=element_ref3
                                        if element_ref3.id_short=="VLANID":vlanID=element_ref3
                                        if element_ref3.id_short=="MaximumLatency":maximumLatency=element_ref3
                                        if element_ref3.id_short=="Reliability":reliability=element_ref3
                                        if element_ref3.id_short=="TSCAI":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="SurvivalTime":survivalTime=element_ref4
                                                if element_ref4.id_short=="PacketArrivalTime":packetArrivalTime=element_ref4
                                                if element_ref4.id_short=="Periodicity":
                                                    periodicity=element_ref4
                                                    tscai= TSCAI(survivalTime, packetArrivalTime, periodicity, element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    tsnFlow=TsnFlowN(destinationIP, destinationMacAddress, streamId, qosProfileAssociated, vlanID, maximumLatency, reliability, tscai, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            tsnFlowList=TsnFlowList(element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)   
                            tsnFlowList.add_tsnFlow(tsnFlow)
                    bridge5GS=Bridge5GS(bridge5GSConfiguration, tsnFlowList, element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
            tsnCapabilities=TSNCapabilities(bridge5GS, system5GBridgeDelay,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        elif(obj.id_short=="Network5GDataSheet"):  #Network5GDataSheet Network
            for element_content in obj:
                if element_content.id_short=="Release3GPP": release3GPP=element_content
                if element_content.id_short=="SupportedNetworkProtocols": supportedNetworkProtocols=element_content
                if element_content.id_short=="SupportedSpectrum": supportedSpectrum=element_content
                if element_content.id_short=="SupportedTransmissionPower": supportedTransmissionPower=element_content
                if element_content.id_short=="SpectrumBandUsed": spectrumBandUsed=element_content
                if element_content.id_short=="MaximumDLDataRate": maximumDLDataRate=element_content
                if element_content.id_short=="MaximumULDataRate": maximumULDataRate=element_content
                if element_content.id_short=="TransmissionModeCharacteristics": 
                    for element_ref in element_content.value: 
                        if element_ref.id_short=="ModulationTypes": modulationTypes=element_ref
                        if element_ref.id_short=="MaximumBitRate": maximumBitRate=element_ref
                    transmissionModeCharacteristics=TransmissionModeCharacteristics(modulationTypes, maximumBitRate,element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                if element_content.id_short=="NetworkTopology": 
                    for element_ref in element_content.value:
                        if element_ref.id_short=="ListOfRanNodes": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="RanNodeN":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Connections":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="UPFByInterfaceN3":upfByInterfaceN3=element_ref4
                                                if element_ref4.id_short=="AMFByInterfaceN2":amfByInterfaceN2=element_ref4
                                                if element_ref4.id_short=="UE": ue=element_ref4
                                            ranConnections=RANConnections(upfByInterfaceN3,amfByInterfaceN2, ue,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)

                                        if element_ref3.id_short=="gNBBasebandUnitResources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            gNBBasebandUnitResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                        if element_ref3.id_short=="gNBRemoteRadioUnitResources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            gNBRemoteRadioUnitResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)

                                        if element_ref3.id_short=="SupportedSpectrum":supportedSpectrum=element_ref3
                                        if element_ref3.id_short=="TransmissionPower":transmissionPower=element_ref3
                                        if element_ref3.id_short=="MaximumTransmissionBandwidth":maximumTransmissionBandwidth=element_ref3
                                        if element_ref3.id_short=="ReceiverSensitivity":receiverSensitivity=element_ref3
                                        if element_ref3.id_short=="TransceiverTiming":transceiverTiming=element_ref3
                                        if element_ref3.id_short=="NumAntennas":numAntennas=element_ref3
                                        if element_ref3.id_short=="NumLayers": numLayers=element_ref3
                                    ranNodeN=RanNodeN(description,ipAddress, ranConnections,gNBBasebandUnitResources,gNBRemoteRadioUnitResources,supportedSpectrum,transmissionPower, maximumTransmissionBandwidth, receiverSensitivity,transceiverTiming,numAntennas, numLayers,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                        element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                            listOfRanNodes=ListOfRanNodes(element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            listOfRanNodes.add_node(ranNodeN)
                        if element_ref.id_short=="ListOfCN": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="LMF":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="LMF_resources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            lmfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    lmf=CoreNetwork(ipAddress, description,lmfResources, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="NSSF":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="NSSF_resources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            nssfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    nssf=CoreNetwork(ipAddress, description,nssfResources, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="AF":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="AF_resources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            afResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    af=CoreNetwork(ipAddress, description,afResources, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="PCF":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="PCF_resources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            pcfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    pcf=CoreNetwork(ipAddress, description,pcfResources, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="SMF":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="SMF_resources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                            smfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    smf=CoreNetwork(ipAddress, description,smfResources, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="AMF":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="IpAddress":ipAddress=element_ref3
                                        if element_ref3.id_short=="Description":description=element_ref3
                                        if element_ref3.id_short=="AMF_resources":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="Position":position=element_ref4
                                                if element_ref4.id_short=="VirtualMachineID":virtualMachineID=element_ref4
                                                if element_ref4.id_short=="StorageMemory":storageMemory=element_ref4
                                                if element_ref4.id_short=="RamMemory":ramMemory=element_ref4
                                        amfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    amf=CoreNetwork(ipAddress, description,amfResources, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="UPFList":
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="UPFn":
                                            for element_ref4 in element_ref3:
                                                if element_ref4.id_short=="IpAddress":ipAddress=element_ref4
                                                if element_ref4.id_short=="Description":description=element_ref4
                                                if element_ref4.id_short=="UPF_resources":
                                                    for element_ref5 in element_ref4:
                                                        if element_ref5.id_short=="Position":position=element_ref5
                                                        if element_ref5.id_short=="VirtualMachineID":virtualMachineID=element_ref5
                                                        if element_ref5.id_short=="StorageMemory":storageMemory=element_ref5
                                                        if element_ref5.id_short=="RamMemory":ramMemory=element_ref5
                                                    upfResources=Resources(position,virtualMachineID,storageMemory, ramMemory,element_ref4.id_short,element_ref4.value, element_ref4.category, element_ref4.description,
                                                                                                element_ref4.parent, element_ref4.semantic_id, element_ref4.qualifier, element_ref4.kind)
                                            upfN=CoreNetwork(ipAddress, description,upfResources, element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)
                                    listOfUPF=ListOfUPF(element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                    listOfUPF.add_upf(upfN)
                            listOfCN=ListOfCN(listOfUPF,af,pcf,smf,amf,nssf,lmf,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                        if element_ref.id_short=="Links": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="N1":n1=element_ref2
                                if element_ref2.id_short=="N2":n2=element_ref2
                                if element_ref2.id_short=="N3":n3=element_ref2
                                if element_ref2.id_short=="N4":n4=element_ref2 
                                if element_ref2.id_short=="N5":n5=element_ref2
                                if element_ref2.id_short=="N6":n6=element_ref2
                                if element_ref2.id_short=="Rx":rx=element_ref2
                                if element_ref2.id_short=="Naf":naf=element_ref2
                                if element_ref2.id_short=="Npcf":npcf=element_ref2
                                if element_ref2.id_short=="Nsmf":nsmf=element_ref2
                                if element_ref2.id_short=="Namf":namf=element_ref2 
                            links=Links(n1,n2,n3,n4,n5,n6,rx,naf,npcf,nsmf,namf,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                    networkTopology=NetworkTopology(listOfRanNodes,listOfCN,links,element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)  
            network5GDataSheet=Network5GDataSheet(release3GPP,supportedSpectrum, spectrumBandUsed, maximumDLDataRate, maximumULDataRate, supportedNetworkProtocols, transmissionModeCharacteristics, supportedTransmissionPower, networkTopology, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)                    
        elif(obj.id_short=="VirtualsNetwork"):  #VirtualsNetwork Network
            for element_content in obj:
                if element_content.id_short=="ListOfVirtualLANs": 
                    for element_ref in element_content.value:
                        if element_ref.id_short=="VirtualLANN": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="VirtualLANId": virtualLANId=element_ref2
                                if element_ref2.id_short=="VLANPriority": vlanPriority=element_ref2
                                if element_ref2.id_short=="VLANTag":vlanTag=element_ref2
                                if element_ref2.id_short=="IpAddress":ipAddress=element_ref2
                                if element_ref2.id_short=="VirtualLANComputingCapability": 
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="VirtualMachineID":virtualMachineID=element_ref3
                                        if element_ref3.id_short=="StorageMemory":storageMemory=element_ref3
                                        if element_ref3.id_short=="RamMemory":ramMemory=element_ref3
                                    virtualLANComputingCapability=ComputingCapability(virtualMachineID, storageMemory, ramMemory, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                            virtualLAN=VirtualLANN(virtualLANId,vlanPriority,vlanTag,virtualLANComputingCapability,ipAddress, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                    virtualLANList=ListOfVirtualLANs(element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    virtualLANList.add_virtualLAN(virtualLAN)
                if element_content.id_short=="ListOfNetworkSlices": 
                    for element_ref in element_content.value:
                        if element_ref.id_short=="NetworkSliceN": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="SNSSAI": 
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="SliceServiceType":sliceServiceType=element_ref3
                                        if element_ref3.id_short=="SliceDifferenciator": sliceDifferenciator=element_ref3
                                    snssai=SNSSAI(sliceServiceType, sliceDifferenciator, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="IpAddress":ipAddress=element_ref2
                                if element_ref2.id_short=="SliceComputingCapability": 
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="VirtualMachineID":virtualMachineID=element_ref3
                                        if element_ref3.id_short=="StorageMemory":storageMemory=element_ref3
                                        if element_ref3.id_short=="RamMemory":ramMemory=element_ref3
                                    sliceComputingCapability=ComputingCapability(virtualMachineID, storageMemory, ramMemory, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                if element_ref2.id_short=="SliceCommunicationAtributes": 
                                    for element_ref3 in element_ref2:
                                        if element_ref3.id_short=="RadioSpectrum":radioSpectrum=element_ref3
                                        if element_ref3.id_short=="Availability":availability=element_ref3
                                        if element_ref3.id_short=="AreaOfService":areaOfService=element_ref3
                                        if element_ref3.id_short=="IsolationLevel":isolationLevel=element_ref3
                                        if element_ref3.id_short=="MaximumSupportedPacketSize":maximumSupportedPacketSize=element_ref3
                                        if element_ref3.id_short=="ServiceCategory":serviceCategory=element_ref3
                                        if element_ref3.id_short=="NetworkSliceEnergyEficiency":networkSliceEnergyEficiency=element_ref3
                                    sliceCommunicationAtributes=SliceCommunicationAtributes(radioSpectrum, availability, areaOfService, isolationLevel, maximumSupportedPacketSize, serviceCategory, networkSliceEnergyEficiency, element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                            networkSliceN=NetworkSliceN(snssai,sliceComputingCapability,ipAddress,sliceCommunicationAtributes,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                    networkSliceList=ListOfNetworkSlices(element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    networkSliceList.add_networkSlice(networkSliceN)
                if element_content.id_short=="NetworkSliceReconfiguration": networkSliceReconfiguration=element_content
                if element_content.id_short=="VLANReconfiguration": vlanReconfiguration=element_content
            virtualsNetwork=VirtualsNetwork(virtualLANList,networkSliceList,networkSliceReconfiguration, vlanReconfiguration, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)              
        elif(obj.id_short=="Connectivity"):  #Connectivity Network
            for element_content in obj:
                if element_content.id_short=="UEsAttachedList": 
                    for element_ref in element_content.value:
                        if element_ref.id_short=="UEAttachedN": 
                            for element_ref2 in element_ref:
                                if element_ref2.id_short=="PEI":pei=element_ref2
                                if element_ref2.id_short=="GPSI": gpsi=element_ref2
                            ueAttachedN=UEAttachedN(pei,gpsi,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                    uesAttachedList=UEAttachedList(element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    uesAttachedList.add_ue(ueAttachedN)
                    
                if element_content.id_short=="PDUSessionList": 
                    for element_ref in element_content.value:
                        if element_ref.id_short=="PDUSessionN":                                                                                
                            for element_ref2 in element_ref.value:
                                if element_ref2.id_short=="IPAddress": ip_address=element_ref2
                                if element_ref2.id_short=="UE": ue=element_ref2
                                if element_ref2.id_short=="DNDestination": dnDestination=element_ref2
                                if element_ref2.id_short=="LinkDirection": linkDirection=element_ref2 
                                if element_ref2.id_short=="QosFlowList":
                                    for element_ref3 in element_ref2.value: 
                                        if element_ref3.id_short=="QosFlowN":
                                            for element_ref4 in element_ref3.value: 
                                                if element_ref4.id_short=="QFI": qfi= element_ref4
                                                if element_ref4.id_short=="PDUSessionID": pduSessionID= element_ref4
                                                if element_ref4.id_short=="PDUSessionType": pduSessionType= element_ref4
                                                if element_ref4.id_short=="QosProfileRequested": 
                                                    for element_ref5 in element_ref4.value: 
                                                        if element_ref5.id_short=="QosParameters":
                                                            for element_ref6 in element_ref5.value: 
                                                                if element_ref6.id_short=="QosIdentifier": qosIdentifier=element_ref6
                                                                if element_ref6.id_short=="ARP": arp=element_ref6
                                                                if element_ref6.id_short=="RQA": rqa=element_ref6
                                                                if element_ref6.id_short=="NotificationControl": notificationControl=element_ref6
                                                                if element_ref6.id_short=="GFBRUL": gfbr_ul=element_ref6
                                                                if element_ref6.id_short=="GFBRDL": gfbr_dl=element_ref6
                                                                if element_ref6.id_short=="MFBRUL": mfbr_ul=element_ref6
                                                                if element_ref6.id_short=="MFBRDL": mfbr_dl=element_ref6
                                                                if element_ref6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref6
                                                                if element_ref6.id_short=="AggregateBitRates": 
                                                                    AggregateBitRates=element_ref6
                                                                    qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                element_ref5.id_short,element_ref5.value, element_ref5.category, element_ref5.description,
                                                                                                element_ref5.parent, element_ref5.semantic_id, element_ref5.qualifier, element_ref5.kind)
                                                                    
                                                        if element_ref5.id_short=="QosCharacteristics":
                                                            for element_ref6 in element_ref5.value: 
                                                                if element_ref6.id_short=="ResourceType": ResourceType=element_ref6
                                                                if element_ref6.id_short=="PriorityLevel": PriorityLevel=element_ref6
                                                                if element_ref6.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref6
                                                                if element_ref6.id_short=="PacketErrorRate": PacketErrorRate=element_ref6
                                                                if element_ref6.id_short=="AveragingWindow": AveragingWindow=element_ref6
                                                                if element_ref6.id_short=="MaximumDataBurstVolume": 
                                                                    MaximumDataBurstVolume=element_ref6
                                                                    qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                element_ref5.id_short,element_ref5.value, element_ref5.category, element_ref5.description,
                                                                                                element_ref5.parent, element_ref5.semantic_id, element_ref5.qualifier, element_ref5.kind)
                                                                    
                                                        if element_ref5.id_short=="AlternativeQosProfiles":
                                                            for element_ref6 in element_ref5.value:
                                                                    if element_ref6.id_short=="AlternativeQosProfileN":
                                                                        for element_ref7 in element_ref6.value:
                                                                            if element_ref7.id_short=="QosParameters":
                                                                                for element_ref8 in element_ref7.value:
                                                                                    if element_ref8.id_short=="QosIdentifier": qosIdentifier=element_ref8
                                                                                    if element_ref8.id_short=="ARP": arp=element_ref8
                                                                                    if element_ref8.id_short=="RQA": rqa=element_ref8
                                                                                    if element_ref8.id_short=="NotificationControl": notificationControl=element_ref8
                                                                                    if element_ref8.id_short=="GFBRUL": gfbr_ul=element_ref8
                                                                                    if element_ref8.id_short=="GFBRDL": gfbr_dl=element_ref8
                                                                                    if element_ref8.id_short=="MFBRUL": mfbr_ul=element_ref8
                                                                                    if element_ref8.id_short=="MFBRDL": mfbr_dl=element_ref8
                                                                                    if element_ref8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref8
                                                                                    if element_ref8.id_short=="AggregateBitRates": 
                                                                                        AggregateBitRates=element_ref8
                                                                                        alternative_qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                                    element_ref7.id_short,element_ref7.value, element_ref7.category, element_ref7.description,
                                                                                                                    element_ref7.parent, element_ref7.semantic_id, element_ref7.qualifier, element_ref7.kind)
                                                                                          
                                                                            if element_ref7.id_short=="QosCharacteristics":
                                                                                for element_ref8 in element_ref7.value:
                                                                                    if element_ref8.id_short=="ResourceType": ResourceType=element_ref8
                                                                                    if element_ref8.id_short=="PriorityLevel": PriorityLevel=element_ref8
                                                                                    if element_ref8.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref8
                                                                                    if element_ref8.id_short=="PacketErrorRate": PacketErrorRate=element_ref8
                                                                                    if element_ref8.id_short=="AveragingWindow": AveragingWindow=element_ref8
                                                                                    if element_ref8.id_short=="MaximumDataBurstVolume": 
                                                                                        MaximumDataBurstVolume=element_ref8
                                                                                        alternative_qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                                    element_ref7.id_short,element_ref7.value, element_ref7.category, element_ref7.description,
                                                                                                                    element_ref7.parent, element_ref7.semantic_id, element_ref7.qualifier, element_ref7.kind)
                                                                        alternativeQosProfile=AlternativeQosProfile(alternative_qos_parameters,alternative_qos_characteristics,
                                                                                                element_ref6.id_short,element_ref6.value, element_ref6.category, element_ref6.description,
                                                                                                element_ref6.parent, element_ref6.semantic_id, element_ref6.qualifier, element_ref6.kind)
                                                            alternativeQosProfiles=AlternativeQosProfiles(element_ref5.id_short,element_ref5.value, element_ref5.category, element_ref5.description,
                                                                                                element_ref5.parent, element_ref5.semantic_id, element_ref5.qualifier, element_ref5.kind)
                                                            alternativeQosProfiles.add_alternative_qos_profile(alternativeQosProfile)
                                                    qosProfileRequested=QosProfileRequested(qos_parameters, qos_characteristics, alternativeQosProfiles, element_ref4.id_short,element_ref4.value, element_ref4.category, 
                                                                                        element_ref4.description, element_ref4.parent, element_ref4.semantic_id, element_ref4.qualifier, element_ref4.kind)                
                                                            
                                                                                    
                                                if element_ref4.id_short=="QosProfileGuaranteed":
                                                    for element_ref5 in element_ref4.value: 
                                                        if element_ref5.id_short=="QosParameters":
                                                            for element_ref6 in element_ref5.value: 
                                                                if element_ref6.id_short=="QosIdentifier": qosIdentifier=element_ref6
                                                                if element_ref6.id_short=="ARP": arp=element_ref6
                                                                if element_ref6.id_short=="RQA": rqa=element_ref6
                                                                if element_ref6.id_short=="NotificationControl": notificationControl=element_ref6
                                                                if element_ref6.id_short=="GFBRUL": gfbr_ul=element_ref6
                                                                if element_ref6.id_short=="GFBRDL": gfbr_dl=element_ref6
                                                                if element_ref6.id_short=="MFBRUL": mfbr_ul=element_ref6
                                                                if element_ref6.id_short=="MFBRDL": mfbr_dl=element_ref6
                                                                if element_ref6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref6
                                                                if element_ref6.id_short=="AggregateBitRates": 
                                                                    AggregateBitRates=element_ref6
                                                                    qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                element_ref5.id_short,element_ref5.value, element_ref5.category, element_ref5.description,
                                                                                                element_ref5.parent, element_ref5.semantic_id, element_ref5.qualifier, element_ref5.kind)
                                                                    
                                                        if element_ref5.id_short=="QosCharacteristics":
                                                            for element_ref6 in element_ref5.value: 
                                                                if element_ref6.id_short=="ResourceType": ResourceType=element_ref6
                                                                if element_ref6.id_short=="PriorityLevel": PriorityLevel=element_ref6
                                                                if element_ref6.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref6
                                                                if element_ref6.id_short=="PacketErrorRate": PacketErrorRate=element_ref6
                                                                if element_ref6.id_short=="AveragingWindow": AveragingWindow=element_ref6
                                                                if element_ref6.id_short=="MaximumDataBurstVolume": 
                                                                    MaximumDataBurstVolume=element_ref6
                                                                    qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                element_ref5.id_short,element_ref5.value, element_ref5.category, element_ref5.description,
                                                                                                element_ref5.parent, element_ref5.semantic_id, element_ref5.qualifier, element_ref5.kind)
                                                                    
                                                        if element_ref5.id_short=="AlternativeQosProfiles":
                                                            for element_ref6 in element_ref5.value:
                                                                    if element_ref6.id_short=="AlternativeQosProfileN":
                                                                        for element_ref7 in element_ref6.value:
                                                                            if element_ref7.id_short=="QosParameters":
                                                                                for element_ref8 in element_ref7.value:
                                                                                    if element_ref8.id_short=="QosIdentifier": qosIdentifier=element_ref8
                                                                                    if element_ref8.id_short=="ARP": arp=element_ref8
                                                                                    if element_ref8.id_short=="RQA": rqa=element_ref8
                                                                                    if element_ref8.id_short=="NotificationControl": notificationControl=element_ref8
                                                                                    if element_ref8.id_short=="GFBRUL": gfbr_ul=element_ref8
                                                                                    if element_ref8.id_short=="GFBRDL": gfbr_dl=element_ref8
                                                                                    if element_ref8.id_short=="MFBRUL": mfbr_ul=element_ref8
                                                                                    if element_ref8.id_short=="MFBRDL": mfbr_dl=element_ref8
                                                                                    if element_ref8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref8
                                                                                    if element_ref8.id_short=="AggregateBitRates": 
                                                                                        AggregateBitRates=element_ref8
                                                                                        alternative_qos_parameters=QosParameters(qosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                                    element_ref7.id_short,element_ref7.value, element_ref7.category, element_ref7.description,
                                                                                                                    element_ref7.parent, element_ref7.semantic_id, element_ref7.qualifier, element_ref7.kind)
                                                                                          
                                                                            if element_ref7.id_short=="QosCharacteristics":
                                                                                for element_ref8 in element_ref7.value:
                                                                                    if element_ref8.id_short=="ResourceType": ResourceType=element_ref8
                                                                                    if element_ref8.id_short=="PriorityLevel": PriorityLevel=element_ref8
                                                                                    if element_ref8.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref8
                                                                                    if element_ref8.id_short=="PacketErrorRate": PacketErrorRate=element_ref8
                                                                                    if element_ref8.id_short=="AveragingWindow": AveragingWindow=element_ref8
                                                                                    if element_ref8.id_short=="MaximumDataBurstVolume": 
                                                                                        MaximumDataBurstVolume=element_ref8
                                                                                        alternative_qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                                    element_ref7.id_short,element_ref7.value, element_ref7.category, element_ref7.description,
                                                                                                                    element_ref7.parent, element_ref7.semantic_id, element_ref7.qualifier, element_ref7.kind)
                                                                        alternativeQosProfile=AlternativeQosProfile(alternative_qos_parameters,alternative_qos_characteristics,
                                                                                                element_ref6.id_short,element_ref6.value, element_ref6.category, element_ref6.description,
                                                                                                element_ref6.parent, element_ref6.semantic_id, element_ref6.qualifier, element_ref6.kind)
                                                            alternativeQosProfiles=AlternativeQosProfiles(element_ref5.id_short,element_ref5.value, element_ref5.category, element_ref5.description,
                                                                                                element_ref5.parent, element_ref5.semantic_id, element_ref5.qualifier, element_ref5.kind)
                                                            alternativeQosProfiles.add_alternative_qos_profile(alternativeQosProfile)
                                                    qosProfileGuaranteed=QosProfileGuaranteed(qos_parameters, qos_characteristics, alternativeQosProfiles, element_ref4.id_short,element_ref4.value, element_ref4.category, 
                                                                                        element_ref4.description, element_ref4.parent, element_ref4.semantic_id, element_ref4.qualifier, element_ref4.kind)
                                            qosFlowN=QosFlowConnectivity(qfi,qosProfileRequested,qosProfileGuaranteed,pduSessionID, pduSessionType,element_ref3.id_short,element_ref3.value, element_ref3.category, element_ref3.description,
                                                                                                element_ref3.parent, element_ref3.semantic_id, element_ref3.qualifier, element_ref3.kind)       
                                    qosFlowConnectivityList=QosFlowConnectivityList(element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                    qosFlowConnectivityList.add_qos_flow(qosFlowN)       
                            
                            pduSessionConnectivity=PDUSessionConnectivity(ipAddress,ue,dnDestination,linkDirection,qosFlowConnectivityList,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                    pduSessionConnectivityList=PDUSessionConnectivityList(element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    pduSessionConnectivityList.add_pdu_session(pduSessionConnectivity)
                if element_content.id_short=="QosMapping":qosMapping=element_content
                if element_content.id_short=="SetRANConfiguration":setRANConfiguration=element_content
                if element_content.id_short=="EstablishConnection":establishConnection=element_content
                if element_content.id_short=="ModifyConnection":modifyConnection=element_content
            connectivity=Connectivity(uesAttachedList,pduSessionConnectivityList, qosMapping, setRANConfiguration,establishConnection, modifyConnection, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)                       
        elif(obj.id_short=="QosPerformance"):  #QosPerformance Network
            for element_content in obj:
                if element_content.id_short=="LogicalNetworkList": 
                        for element_ref in element_content.value:
                            if element_ref.id_short=="LogicalNetworkNPerformance": 
                                for element_ref2 in element_ref:
                                    if element_ref2.id_short=="ActualBitRate":actualBitRate=element_ref2
                                    if element_ref2.id_short=="PacketLossRate":packetLossRate=element_ref2
                                    if element_ref2.id_short=="BLER":bler=element_ref2
                                    if element_ref2.id_short=="Throughput": 
                                        for element_ref3 in element_ref2:
                                            if element_ref3.id_short=="Average":avg=element_ref3
                                            if element_ref3.id_short=="Max":max=element_ref3
                                            if element_ref3.id_short=="Min":min=element_ref3
                                        throughput=Throughput(avg,max,min,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                    if element_ref2.id_short=="Latency": 
                                        for element_ref3 in element_ref2:
                                            if element_ref3.id_short=="Average":avg=element_ref3
                                            if element_ref3.id_short=="Max":max=element_ref3
                                            if element_ref3.id_short=="Min":min=element_ref3
                                        latency=Latency(avg,max,min,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                    if element_ref2.id_short=="Reliability":reliability=element_ref2
                                    if element_ref2.id_short=="CapacityUtilization":capacityUtilization=element_ref2
                                    if element_ref2.id_short=="SignalLevel": 
                                        for element_ref3 in element_ref2:
                                            if element_ref3.id_short=="SINR":sinr=element_ref3
                                            if element_ref3.id_short=="RSSI":rssi=element_ref3
                                            if element_ref3.id_short=="RSRP":rsrp=element_ref3
                                            if element_ref3.id_short=="RSRQ":rsrq=element_ref3
                                        signal_level=NetworkSignalLevel(sinr,rssi,rsrp,rsrq,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description, element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                logicalNetworkNPerformance=LogicalNetworkNPerformance(actualBitRate,packetLossRate,bler,throughput,latency,reliability,capacityUtilization,signal_level,element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                        logicalNetworkList=LogicalNetworkList(element_content.id_short,element_content.value, element_content.category, element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                        logicalNetworkList.add_logicalNetwork(logicalNetworkNPerformance)

                if element_content.id_short=="ParametersPertainingConnections":
                        for element_ref in element_content.value:                                                                                                   
                            for element_ref_2 in element_ref.value:   #                                       
                                for element_ref_3 in element_ref_2.value: 
                                    if element_ref_3.id_short=="IPAddress": ip_address=element_ref_3 
                                    if element_ref_3.id_short=="QosFlowList":
                                        for element_ref_4 in element_ref_3.value: 
                                            if element_ref_4.id_short=="QosFlowN":
                                                for element_ref_5 in element_ref_4.value:  
                                                    if element_ref_5.id_short=="QFI": qfi= element_ref_5
                                                    if element_ref_5.id_short=="CommunicationServiceAvailability":commservavai=element_ref_5
                                                    if element_ref_5.id_short=="CommunicationServiceReliability":commservrel=element_ref_5
                                                    if element_ref_5.id_short=="EndToEndLatency":e2el=element_ref_5
                                                    if element_ref_5.id_short=="UpdateTime":updateTime=element_ref_5
                                                    if element_ref_5.id_short=="SurvivalTime":survivalTime=element_ref_5
                                                    if element_ref_5.id_short=="Latency": 
                                                        for element_ref6 in element_ref_5:
                                                            if element_ref6.id_short=="Average":avg=element_ref6
                                                            if element_ref6.id_short=="Max":max=element_ref6
                                                            if element_ref6.id_short=="Min":min=element_ref6
                                                        latency=Latency(avg,max,min,element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description, element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                    if element_ref_5.id_short=="ServiceBitRate":
                                                        for element_ref6 in element_ref_5:
                                                            if element_ref6.id_short=="Average":avg=element_ref6
                                                            if element_ref6.id_short=="Max":max=element_ref6
                                                            if element_ref6.id_short=="Min":min=element_ref6
                                                        serviceBitRate=ServiceBitRate(avg,max,min,element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description, element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                    if element_ref_5.id_short=="DataThroughput":
                                                        for element_ref6 in element_ref_5:
                                                            if element_ref6.id_short=="Average":avg=element_ref6
                                                            if element_ref6.id_short=="Max":max=element_ref6
                                                            if element_ref6.id_short=="Min":min=element_ref6
                                                        dataThroughput=DataThroughput(avg,max,min,element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description, element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                    if element_ref_5.id_short=="PacketErrorRatio":
                                                        for element_ref6 in element_ref_5:
                                                            if element_ref6.id_short=="Average":avg=element_ref6
                                                            if element_ref6.id_short=="Max":max=element_ref6
                                                            if element_ref6.id_short=="Min":min=element_ref6
                                                        per=PacketErrorRatio(avg,max,min,element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description, element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                    if element_ref_5.id_short=="BLER":
                                                        for element_ref6 in element_ref_5:
                                                            if element_ref6.id_short=="Average":avg=element_ref6
                                                            if element_ref6.id_short=="Max":max=element_ref6
                                                            if element_ref6.id_short=="Min":min=element_ref6
                                                        bler=BLER(avg,max,min,element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description, element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                qos_flow=QosFlowPerformance(qfi,commservavai,commservrel,e2el,survivalTime,latency, serviceBitRate,per,bler,updateTime,dataThroughput,element_ref_4.id_short,element_ref_4.value, element_ref_4.category, element_ref_4.description, element_ref_4.parent, element_ref_4.semantic_id, element_ref_4.qualifier, element_ref_4.kind)
                                                                                            
                                        qos_flow_list=QosFlowPerformanceList(element_ref_3.id_short,element_ref_3.value, element_ref_3.category, 
                                                                                            element_ref_3.description, element_ref_3.parent, element_ref_3.semantic_id, element_ref_3.qualifier, element_ref_3.kind)
                                        qos_flow_list.add_qos_flow(qos_flow)
                                pdu_session=PDUSessionPerformance(ip_address,qos_flow_list,element_ref_2.id_short,element_ref_2.value, element_ref_2.category, 
                                                                                            element_ref_2.description, element_ref_2.parent, element_ref_2.semantic_id, element_ref_2.qualifier, element_ref_2.kind)
                            pdu_session_list=PDUSessionPerformanceList(element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                            element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            pdu_session_list.add_pdu_session(pdu_session)
                        parameterspertainingConnections=ParametersPertainingConnections(pdu_session_list,element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                if element_content.id_short=="ListOfSubscriptions":
                        for element_ref in element_content:
                            if element_ref.id_short=="ListOfEvents":
                                for element_ref2 in element_ref:  
                                    if element_ref2.id_short=="Event1":event1=element_ref2
                                listOfEvents= ListOfNetworkPerformanceEvents(element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                                        element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                listOfEvents.add_event(event1)
                            if element_ref.id_short=="Subscription1":
                                subscription1=element_ref
                        
                        listOfSubscriptions= ListOfNetworkPerformanceSubscriptions(listOfEvents,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                            element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                        listOfSubscriptions.add_subscription(subscription1)
                if element_content.id_short=="SubscriptionManagement":subscriptionManagement=element_content
                if element_content.id_short=="PerformanceOfAPacketTX":performanceOfAPacketTX=element_content
                if element_content.id_short=="PerformanceOfAQosFlow":performanceOfAQosFlow=element_content
                if element_content.id_short=="PerformanceOfAPDUSession":performanceOfAPDUSession=element_content
                if element_content.id_short=="UpdateTime":updateTime=element_content
            qosPerformance=QosPerformance(logicalNetworkList, parameterspertainingConnections, listOfSubscriptions, subscriptionManagement, updateTime, performanceOfAPacketTX, performanceOfAQosFlow, performanceOfAPDUSession, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)                                                                           
        elif(obj.id_short=="QosPrediction"):  #QosPrediction Network
            for element_content in obj:
                if element_content.id_short=="ListOfSubscriptions":
                        for element_ref in element_content:
                            if element_ref.id_short=="ListOfEvents":
                                for element_ref2 in element_ref:  
                                    if element_ref2.id_short=="Event1":event1=element_ref2
                                listOfEvents= ListOfQosPredictionEvents(element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                                        element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                                listOfEvents.add_event(event1)
                            if element_ref.id_short=="Subscription1":
                                subscription1=element_ref
                        
                        listOfSubscriptions= ListOfQosPredictionSubscriptions(listOfEvents,element_ref2.id_short,element_ref2.value, element_ref2.category, element_ref2.description,
                                                                                            element_ref2.parent, element_ref2.semantic_id, element_ref2.qualifier, element_ref2.kind)
                        listOfSubscriptions.add_subscription(subscription1)
                if element_content.id_short=="SubscriptionManagement":subscriptionManagement=element_content
            qosPrediction=QosPrediction(listOfSubscriptions, subscriptionManagement, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind) 

for obj in new_object_store:
    if isinstance(obj,AssetAdministrationShell):
        if obj.id_short=="NETWORK_5G_AAS":
            aasnw5G=AASNetwork5G(network5G,nameplate,identification,documentation,service,technicalDataNetwork,npn5GNWIdentity,assetServiceRegistry,tsnCapabilities,network5GDataSheet,virtualsNetwork,connectivity,qosPerformance,networkLocation,qosPrediction,obj.asset, obj.identification, obj.id_short, obj.category, obj.description, obj.parent, obj.administration, obj.security, obj.submodel, obj.concept_dictionary, obj.view, obj.derived_from)          
