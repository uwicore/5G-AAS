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

with aasx.AASXReader("5G_UE_AAS.aasx") as reader:
    # Read all contained AAS objects and all referenced auxiliary files
    # In contrast to the AASX Package Explorer, we are not limited to a single XML part in the package, but instead we
    # will read the contents of all included JSON and XML parts into the ObjectStore
    reader.read_into(object_store=new_object_store,
                     file_store=new_file_store)

    # We can also read the meta data
    new_meta_data = reader.get_core_properties()


#It will be neccessary to know the number of Ues stored in the object_store
def assign_IRIs():
    ues_iris=[]
    counters = {
        "Nameplate": 0,
        "Identification": 0,
        "Documentation": 0,
        "Service": 0,
        "TechnicalData": 0,
        "NetworkAccessRestrictions": 0,
        "UE5GIdentification": 0,
        "UEAttachAndConnectionStatus": 0,
        "QosMonitoring": 0,
        "Location": 0,
        "UE5GDatasheet": 0
        }
    iris = {
        "Nameplate": [],
        "Identification": [],
        "Documentation": [],
        "Service": [],
        "TechnicalData": [],

        "NetworkAccessRestrictions": [],
        "UE5GIdentification": [],
        "UEAttachAndConnectionStatus": [],
        "QosMonitoring": [],
        "Location": [],
        "UE5GDatasheet": []
    }
    
    for obj in new_object_store:
        # Check if obj is a Submodel
        if isinstance(obj, Submodel):
            if obj.id_short in counters:
                counters[obj.id_short] += 1
                iris[obj.id_short].append(obj.identification.id)
        num_ues=counters["Nameplate"]

    for i in range(num_ues):
        ue_iris=[iris["Nameplate"][i],iris["Identification"][i],iris["Documentation"][i],iris["Service"][i],iris["TechnicalData"][i],iris["NetworkAccessRestrictions"][i],iris["UE5GIdentification"][i],iris["UEAttachAndConnectionStatus"][i],iris["QosMonitoring"][i],iris["Location"][i], iris["UE5GDatasheet"][i]]
        ues_iris.append(ue_iris)
    return ues_iris, num_ues


# Ejemplo de uso
ues_iris, num_ues = assign_IRIs()


listOfUeAASs=[]

for i in range(num_ues):

    for obj in new_object_store:
        #First the asset
        if isinstance(obj, Asset):
            if i ==0: 
                string_asset = "UE_5G"
            else:
                string_asset = "UE_5G_" + str(i+1)
            
            if obj.id_short==string_asset: 

                print(string_asset)
                ue5G=UE5G(obj.kind, obj.identification, obj.id_short, obj.category, obj.description)

    for obj in new_object_store:
        #Now the submodels
        if isinstance(obj, Submodel):
            if(obj.identification.id==ues_iris[i][0]):    #Nameplate 
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

            elif(obj.identification.id==ues_iris[i][1]):  #Identification
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
                    if element_content.id_short=="ChargeId": chargeId=element_content
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

            elif(obj.identification.id==ues_iris[i][2]):  #Documentation
                documentation= Documentation(obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ues_iris[i][3]):  #Service
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
                            if element_ref.id_short=="Phone": phone=element_ref
                            if element_ref.id_short=="Fax":
                                fax=element_ref
                                contact_info=ContactInfo(nameOfSupplier,contactInfo_role,physical_address,email,url,phone,fax, element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                
                service=Service(contact_info, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ues_iris[i][4]):  #TechnicalData
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
                                        prod_class_system=ProductClassificationItem(productClassificationSystem,classificationSystemVersion,productClassId, element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                            element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)

                                        technicalProperties=TechnicalProperties(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                technicalData=TechnicalData(general_info,prod_class_system,technicalProperties,further_info,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)       
              

            elif(obj.identification.id==ues_iris[i][6]):  #Ue5GIdentification
                for element_content in obj:
                    if element_content.id_short=="PEI": pei=element_content
                    if element_content.id_short=="UEIdentityGPSI": gpsi=element_content
                    if element_content.id_short=="AuthenticationCertificate": authenticationCertificate=element_content
                    if element_content.id_short=="CertificateStatus": certificateStatus=element_content
                    if element_content.id_short=="IPAddress": ipAddress=element_content
                    if element_content.id_short=="MacAddress": macAddress=element_content
                    if element_content.id_short=="IMSI": imsi=element_content
                    if element_content.id_short=="ICCID": iccid=element_content
                    if element_content.id_short=="PIN": pin=element_content
                    if element_content.id_short=="SPN": spn=element_content
                ue5GIdentification=Ue5GIdentification(pei, gpsi, authenticationCertificate,certificateStatus,ipAddress, macAddress, imsi, spn, pin, iccid, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
            elif(obj.identification.id==ues_iris[i][5]):  #NetworkAccessRestrictions
                for element_content in obj:
                    if element_content.id_short=="ListOfCellGlobalIdentifier": 
                        for element_ref in element_content:
                            if element_ref.id_short=="CGI01": cgi01=element_ref
                        listOfCellGlobalIdentifier=ListOfCellGlobalIdentifier(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                        listOfCellGlobalIdentifier.add_cgi(cgi01)
                    if element_content.id_short=="ListOfPermissibleSlices": 
                        for element_ref in element_content:
                            if element_ref.id_short=="SNSSAI01": snssai01=element_ref
                        listOfPermissibleSlices=ListOfPermissibleSlices(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                        listOfPermissibleSlices.add_snssai(snssai01)
                networkAccessRestrictions=NetworkAccessRestrictions(listOfCellGlobalIdentifier,listOfPermissibleSlices,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)


            elif(obj.identification.id==ues_iris[i][7]):  #UeAttachAndConnectionStatus
                for element_content in obj:  
                    if element_content.id_short=="UEAttached": ue_attached=element_content
                    if element_content.id_short=="RRCState": rrc_state=element_content
                    if isinstance(element_content, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                        for element_ref in element_content.value:                                                                                                        
                            if isinstance(element_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                                for element_ref_2 in element_ref.value:   
                                    if element_ref_2.id_short=="IPAddress": ip_address=element_ref_2
                                    if element_ref_2.id_short=="DNN": dnn=element_ref_2
                                    if element_ref_2.id_short=="LinkDirection": linkDirection=element_ref_2

                                    if isinstance(element_ref_2, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):                                        
                                        for element_ref_3 in element_ref_2.value: 
                                            if isinstance(element_ref_3, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):    
                                                for element_ref_4 in element_ref_3.value:  
                                                    if element_ref_4.id_short=="QFI": qfi= element_ref_4
                                                    if isinstance(element_ref_4, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                                                        for element_ref_5 in element_ref_4.value: 
                                                            if element_ref_4.id_short=="RRMParameters":
                                                                        if element_ref_5.id_short=="MCSTable": mcstable=element_ref_5
                                                                        if element_ref_5.id_short=="CQITable": cqitable=element_ref_5
                                                                        if element_ref_5.id_short=="TargetBLER": target_bler=element_ref_5
                                                                        if element_ref_5.id_short=="SchedulingType": scheduling_type=element_ref_5
                                                                        if element_ref_5.id_short=="SchedulingPolicy": scheduling_policy=element_ref_5
                                                                        if element_ref_5.id_short=="HARQMaximumNumberOfRetransmissions": harq_max_num_retransmissions=element_ref_5
                                                                        if element_ref_5.id_short=="KNumber": k_number=element_ref_5
                                                                        if element_ref_5.id_short=="PowerControlPmax": 
                                                                            power_control_pmax=element_ref_5
                                                                            rrm_parameters=RRMParameters(mcstable,cqitable,target_bler, scheduling_type,scheduling_policy, harq_max_num_retransmissions,k_number, power_control_pmax, element_ref_4.id_short,element_ref_4.value, element_ref_4.category, 
                                                                                            element_ref_4.description, element_ref_4.parent, element_ref_4.semantic_id, element_ref_4.qualifier, element_ref_4.kind)

                                                            if element_ref_4.id_short=="QosProfileRequested":                                                            
                                                                for element_ref_6 in element_ref_5.value: 
                                                                    if element_ref_6.id_short=="QosIdentifier": QosIdentifier=element_ref_6
                                                                    if element_ref_6.id_short=="ARP": arp=element_ref_6
                                                                    if element_ref_6.id_short=="RQA": rqa=element_ref_6
                                                                    if element_ref_6.id_short=="NotificationControl": notificationControl=element_ref_6
                                                                    if element_ref_6.id_short=="GFBRUL": gfbr_ul=element_ref_6
                                                                    if element_ref_6.id_short=="GFBRDL": gfbr_dl=element_ref_6
                                                                    if element_ref_6.id_short=="MFBRUL": mfbr_ul=element_ref_6
                                                                    if element_ref_6.id_short=="MFBRDL": mfbr_dl=element_ref_6
                                                                    if element_ref_6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref_6
                                                                    if element_ref_6.id_short=="AggregateBitRates": 
                                                                        AggregateBitRates=element_ref_6
                                                                        
                                                                        qos_parameters_r=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                    element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description,
                                                                                                    element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                                        
                                                                    if element_ref_6.id_short=="ResourceType": ResourceType=element_ref_6
                                                                    if element_ref_6.id_short=="PriorityLevel": PriorityLevel=element_ref_6
                                                                    if element_ref_6.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref_6
                                                                    if element_ref_6.id_short=="PacketErrorRate": PacketErrorRate=element_ref_6
                                                                    if element_ref_6.id_short=="AveragingWindow": AveragingWindow=element_ref_6
                                                                    if element_ref_6.id_short=="MaximumDataBurstVolume": 
                                                                        MaximumDataBurstVolume=element_ref_6
                                                                        
                                                                        qos_characteristics_r=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                    element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description,
                                                                                                    element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)


                                                                if element_ref_5.id_short=="AlternativeQosProfiles":
                                                                    if element_ref_6.id_short=="AlternativeQosProfile01":
                                                                        for element_ref_7 in element_ref_6:  
                                                                            if element_ref_7.id_short=="QosParameters": qosParameters=element_ref_7
                                                                            for element_ref_8 in element_ref_7.value: 
                                                                                if element_ref_8.id_short=="QosIdentifier": QosIdentifier=element_ref_8
                                                                                if element_ref_8.id_short=="ARP": arp=element_ref_8
                                                                                if element_ref_8.id_short=="RQA": rqa=element_ref_8
                                                                                if element_ref_8.id_short=="NotificationControl": notificationControl=element_ref_8
                                                                                if element_ref_8.id_short=="GFBRUL": gfbr_ul=element_ref_8
                                                                                if element_ref_8.id_short=="GFBRDL": gfbr_dl=element_ref_8
                                                                                if element_ref_8.id_short=="MFBRUL": mfbr_ul=element_ref_8
                                                                                if element_ref_8.id_short=="MFBRDL": mfbr_dl=element_ref_8
                                                                                if element_ref_8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref_8
                                                                                if element_ref_8.id_short=="AggregateBitRates": 
                                                                                    AggregateBitRates=element_ref_8
                                                                                    
                                                                                    qos_parameters=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                                element_ref_7.id_short,element_ref_7.value, element_ref_7.category, element_ref_7.description,
                                                                                                                element_ref_7.parent, element_ref_7.semantic_id, element_ref_7.qualifier, element_ref_7.kind)

                                                                            if element_ref_7.id_short=="QosCharacteristics": qosCharacteristics=element_ref_7
                                                                            for element_ref_8 in element_ref_7.value:
                                                                                if element_ref_8.id_short=="ResourceType": ResourceType=element_ref_8
                                                                                if element_ref_8.id_short=="PriorityLevel": PriorityLevel=element_ref_8
                                                                                if element_ref_8.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref_8
                                                                                if element_ref_8.id_short=="PacketErrorRate": PacketErrorRate=element_ref_8
                                                                                if element_ref_8.id_short=="AveragingWindow": AveragingWindow=element_ref_8
                                                                                if element_ref_8.id_short=="MaximumDataBurstVolume": 
                                                                                    MaximumDataBurstVolume=element_ref_8
                                                                                    
                                                                                    qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                                element_ref_7.id_short,element_ref_7.value, element_ref_7.category, element_ref_7.description,
                                                                                                                element_ref_7.parent, element_ref_7.semantic_id, element_ref_7.qualifier, element_ref_7.kind)
                                                                                    
                                                                                    alternativeQosProfile=AlternativeQosProfile(qos_parameters,qos_characteristics,element_ref_6.id_short,element_ref_6.value, element_ref_6.category, element_ref_6.description,
                                                                                                                element_ref_6.parent, element_ref_6.semantic_id, element_ref_6.qualifier, element_ref_6.kind)
                                                                                
                                                                                    alternativeQosProfileList=AlternativeQosProfiles(element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description,
                                                                                                                element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                                                    alternativeQosProfileList.add_alternative_qos_profile(alternativeQosProfile)   

                                                                        qos_profile_requested=QosProfile(qos_parameters_r,qos_characteristics_r, alternativeQosProfileList, element_ref_4.id_short,element_ref_4.value, element_ref_4.category, 
                                                                                            element_ref_4.description, element_ref_4.parent, element_ref_4.semantic_id, element_ref_4.qualifier, element_ref_4.kind)

                                                            if element_ref_4.id_short=="QosProfileGuaranteed":                                                            
                                                                for element_ref_6 in element_ref_5.value: 
                                                                    if element_ref_6.id_short=="QosIdentifier": QosIdentifier=element_ref_6
                                                                    if element_ref_6.id_short=="ARP": arp=element_ref_6
                                                                    if element_ref_6.id_short=="RQA": rqa=element_ref_6
                                                                    if element_ref_6.id_short=="NotificationControl": notificationControl=element_ref_6
                                                                    if element_ref_6.id_short=="GFBRUL": gfbr_ul=element_ref_6
                                                                    if element_ref_6.id_short=="GFBRDL": gfbr_dl=element_ref_6
                                                                    if element_ref_6.id_short=="MFBRUL": mfbr_ul=element_ref_6
                                                                    if element_ref_6.id_short=="MFBRDL": mfbr_dl=element_ref_6
                                                                    if element_ref_6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref_6
                                                                    if element_ref_6.id_short=="AggregateBitRates": 
                                                                        AggregateBitRates=element_ref_6
                                                                        
                                                                        qos_parameters_g=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                    element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description,
                                                                                                    element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                                        
                                                                    if element_ref_6.id_short=="ResourceType": ResourceType=element_ref_6
                                                                    if element_ref_6.id_short=="PriorityLevel": PriorityLevel=element_ref_6
                                                                    if element_ref_6.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref_6
                                                                    if element_ref_6.id_short=="PacketErrorRate": PacketErrorRate=element_ref_6
                                                                    if element_ref_6.id_short=="AveragingWindow": AveragingWindow=element_ref_6
                                                                    if element_ref_6.id_short=="MaximumDataBurstVolume": 
                                                                        MaximumDataBurstVolume=element_ref_6
                                                                        
                                                                        qos_characteristics_g=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                    element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description,
                                                                                                    element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                                if element_ref_5.id_short=="AlternativeQosProfiles":
                                                                    if element_ref_6.id_short=="AlternativeQosProfile01":
                                                                        for element_ref_7 in element_ref_6:  
                                                                            if element_ref_7.id_short=="QosParameters": qosParameters=element_ref_7
                                                                            for element_ref_8 in element_ref_7.value: 
                                                                                if element_ref_8.id_short=="QosIdentifier": QosIdentifier=element_ref_8
                                                                                if element_ref_8.id_short=="ARP": arp=element_ref_8
                                                                                if element_ref_8.id_short=="RQA": rqa=element_ref_8
                                                                                if element_ref_8.id_short=="NotificationControl": notificationControl=element_ref_8
                                                                                if element_ref_8.id_short=="GFBRUL": gfbr_ul=element_ref_8
                                                                                if element_ref_8.id_short=="GFBRDL": gfbr_dl=element_ref_8
                                                                                if element_ref_8.id_short=="MFBRUL": mfbr_ul=element_ref_8
                                                                                if element_ref_8.id_short=="MFBRDL": mfbr_dl=element_ref_8
                                                                                if element_ref_8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=element_ref_8
                                                                                if element_ref_8.id_short=="AggregateBitRates": 
                                                                                    AggregateBitRates=element_ref_8
                                                                                    
                                                                                    qos_parameters=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                                element_ref_7.id_short,element_ref_7.value, element_ref_7.category, element_ref_7.description,
                                                                                                                element_ref_7.parent, element_ref_7.semantic_id, element_ref_7.qualifier, element_ref_7.kind)

                                                                            if element_ref_7.id_short=="QosCharacteristics": qosCharacteristics=element_ref_7
                                                                            for element_ref_8 in element_ref_7.value:
                                                                                if element_ref_8.id_short=="ResourceType": ResourceType=element_ref_8
                                                                                if element_ref_8.id_short=="PriorityLevel": PriorityLevel=element_ref_8
                                                                                if element_ref_8.id_short=="PacketDelayBudget": PacketDelayBudget=element_ref_8
                                                                                if element_ref_8.id_short=="PacketErrorRate": PacketErrorRate=element_ref_8
                                                                                if element_ref_8.id_short=="AveragingWindow": AveragingWindow=element_ref_8
                                                                                if element_ref_8.id_short=="MaximumDataBurstVolume": 
                                                                                    MaximumDataBurstVolume=element_ref_8
                                                                                    
                                                                                    qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                                element_ref_7.id_short,element_ref_7.value, element_ref_7.category, element_ref_7.description,
                                                                                                                element_ref_7.parent, element_ref_7.semantic_id, element_ref_7.qualifier, element_ref_7.kind)
                                                                                    
                                                                                    alternativeQosProfile=AlternativeQosProfile(qos_parameters,qos_characteristics,element_ref_6.id_short,element_ref_6.value, element_ref_6.category, element_ref_6.description,
                                                                                                                element_ref_6.parent, element_ref_6.semantic_id, element_ref_6.qualifier, element_ref_6.kind)
                                                                                
                                                                                    alternativeQosProfileList=AlternativeQosProfiles(element_ref_5.id_short,element_ref_5.value, element_ref_5.category, element_ref_5.description,
                                                                                                                element_ref_5.parent, element_ref_5.semantic_id, element_ref_5.qualifier, element_ref_5.kind)
                                                                                    alternativeQosProfileList.add_alternative_qos_profile(alternativeQosProfile)   

                                                                            
                                                                        qos_profile_guaranteed=QosProfile(qos_parameters_g,qos_characteristics_g, alternativeQosProfileList, element_ref_4.id_short,element_ref_4.value, element_ref_4.category, 
                                                                                            element_ref_4.description, element_ref_4.parent, element_ref_4.semantic_id, element_ref_4.qualifier, element_ref_4.kind)

                                                qos_flow=QosFlowStatus(qfi, qos_profile_requested,qos_profile_guaranteed, rrm_parameters,element_ref_3.id_short,element_ref_3.value, element_ref_3.category, 
                                                                                            element_ref_3.description, element_ref_3.parent, element_ref_3.semantic_id, element_ref_3.qualifier, element_ref_3.kind)
                                            
                                            qos_flow_list=QosFlowStatusList(element_ref_2.id_short,element_ref_2.value, element_ref_2.category, 
                                                                                            element_ref_2.description, element_ref_2.parent, element_ref_2.semantic_id, element_ref_2.qualifier, element_ref_2.kind)
                                            qos_flow_list.add_qos_flow(qos_flow)
                                    
                                pdu_session=PDUSessionStatus(ip_address, dnn, qos_flow_list,linkDirection, element_ref.id_short,element_ref.value, element_ref.category, 
                                                                                            element_ref.description, element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                        
                            pdu_session_list=PDUSessionStatusList(element_content.id_short,element_content.value, element_content.category, 
                                                                                            element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                            pdu_session_list.add_pdu_session(pdu_session)
                    if element_content.id_short=="NewConnectionRequest": newConnectionRequest=element_content
                    if element_content.id_short=="ConnectionModificationRequest": connectionModificationRequest=element_content
                ueAttachAndConnectionStatus=UeAttachAndConnectionStatus(ue_attached,rrc_state, pdu_session_list, newConnectionRequest, connectionModificationRequest, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ues_iris[i][8]):  #QosMonitoring
                for element_content in obj:
                    if element_content.id_short=="GeneralKeyPerformanceIndicators":
                        for element_ref in element_content:
                            if element_ref.id_short=="DroppedConnections": dropped_connections=element_ref
                            if element_ref.id_short=="TrafficVolumeForEach5QIAndAlternativeQosProfiles": trafficVolumeForEach5QIAndAlternativeQosProfile=element_ref
                            if element_ref.id_short=="HandoverSuccessRate": handoverSuccessRate=element_ref
                            if element_ref.id_short=="SINR": sinr=element_ref
                            if element_ref.id_short=="DataThroughput": dataThroughput=element_ref
                            if element_ref.id_short=="BLER": bler=element_ref
                            if element_ref.id_short=="PER": 
                                per=element_ref
                                general_key_performance_indicators=GeneralKeyPerformanceIndicators(dropped_connections, trafficVolumeForEach5QIAndAlternativeQosProfile,handoverSuccessRate,sinr,dataThroughput,bler,per, element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                        element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    if element_content.id_short=="SignalLevel":
                        for element_ref in element_content:
                            if element_ref.id_short=="RSSI": rssi=element_ref
                            if element_ref.id_short=="RSRP": rsrp=element_ref
                            if element_ref.id_short=="RSRQ": 
                                rsrq=element_ref
                                signal_level=SignalLevel(rssi,rsrp,rsrq,element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    if element_content.id_short=="ParametersPertainingConnections":
                        for element_ref in element_content.value:                                                                                                 
                            for element_ref_2 in element_ref.value:                                          
                                for element_ref_3 in element_ref_2.value: 
                                    if element_ref_3.id_short=="IPAddress": ip_address=element_ref_3 
                                    if element_ref_3.id_short=="QosFlowList":
                                        for element_ref_4 in element_ref_3.value: 
                                            if element_ref_4.id_short=="QosFlow01":
                                                for element_ref_5 in element_ref_4.value:  
                                                    if element_ref_5.id_short=="QFI": qfi= element_ref_5
                                                    if element_ref_5.id_short=="CommunicationServiceAvailabilty":commservavai=element_ref_5
                                                    if element_ref_5.id_short=="CommunicationServiceReliability":commservrel=element_ref_5
                                                    if element_ref_5.id_short=="EndToEndLatencyMaximum":e2elm=element_ref_5
                                                    if element_ref_5.id_short=="EndToEndLatencyAVG":e2elavg=element_ref_5
                                                    if element_ref_5.id_short=="SurvivalTime":survivalTime=element_ref_5
                                                    if element_ref_5.id_short=="ServiceBitRate":serviceBitRate=element_ref_5
                                                    if element_ref_5.id_short=="PacketErrorRatio":per=element_ref_5
                                                    if element_ref_5.id_short=="BLER":bler=element_ref_5
                                                    if element_ref_5.id_short=="UpdateTime":updateTime=element_ref_5
                                                    if element_ref_5.id_short=="DataThroughput":dataThroughput=element_ref_5
                                                    if element_ref_5.id_short=="Cause5GSM":
                                                        cause=element_ref_5
                                                        qos_flow=QosFlowMonitoring(qfi,commservavai,commservrel,e2elm,e2elavg,survivalTime,serviceBitRate,per,bler,updateTime,dataThroughput,cause,element_ref_4.id_short,element_ref_4.value, element_ref_4.category, 
                                                                                            element_ref_4.description, element_ref_4.parent, element_ref_4.semantic_id, element_ref_4.qualifier, element_ref_4.kind)
                                        qos_flow_list=QosFlowMonitoringList(element_ref_3.id_short,element_ref_3.value, element_ref_3.category, 
                                                                                            element_ref_3.description, element_ref_3.parent, element_ref_3.semantic_id, element_ref_3.qualifier, element_ref_3.kind)
                                        qos_flow_list.add_qos_flow(qos_flow)
                                pdu_session=PDUSessionMonitoring(ip_address,qos_flow_list,element_ref_2.id_short,element_ref_2.value, element_ref_2.category, 
                                                                                            element_ref_2.description, element_ref_2.parent, element_ref_2.semantic_id, element_ref_2.qualifier, element_ref_2.kind)
                            pdu_session_list=PDUSessionMonitoringList(element_ref.id_short,element_ref.value, element_ref.category, element_ref.description,
                                                                                                            element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            pdu_session_list.add_pdu_session(pdu_session)
                        parameters_pertaining_connections=ParametersPertainingConnections(pdu_session_list,element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)                                    
                    if element_content.id_short=="QosQuery": qosQuery=element_content
                    if element_content.id_short=="SubscriptionRequest": subscriptionRequest=element_content
                    if element_content.id_short=="SubscriptionManagement": subscriptionManagement=element_content
                    if element_content.id_short=="ListOfSubscriptions": listOfMonitoringSubscriptions=ListOfMonitoringSubscriptions(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    if element_content.id_short=="ListOfNWSubscriptions": listOfNWSubscriptions=ListOfMonitoringSubscriptions(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    if element_content.id_short=="UpdateTime":updateTime=element_content
                qos_monitoring=QosMonitoring(general_key_performance_indicators,signal_level,parameters_pertaining_connections,qosQuery,subscriptionRequest,subscriptionManagement,listOfMonitoringSubscriptions, listOfNWSubscriptions, updateTime,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        
        
            elif(obj.identification.id==ues_iris[i][9]):  #Location
                for element_content in obj:
                    if element_content.id_short=="XPosition":xPosition=element_content
                    if element_content.id_short=="YPosition":yPosition=element_content
                    if element_content.id_short=="ZPosition":zPosition=element_content 
                    if element_content.id_short=="Speed":speed=element_content
                    if element_content.id_short=="Acceleration":acceleration=element_content
                    if element_content.id_short=="LCSQosClass": lcsQosClass=element_content
                    if element_content.id_short=="Accuracy": accuracy=element_content
                    if element_content.id_short=="ResponseTime": responseTime=element_content
                    if element_content.id_short=="SubscriptionRequest": subscriptionRequest=element_content
                    if element_content.id_short=="SubscriptionManagement": subscriptionManagement=element_content
                    if element_content.id_short=="ListOfNWSubscriptions": listOfNWSubscriptions=element_content
                    if element_content.id_short=="ListOfSubscriptions": listOfLocalizationSubscriptions=ListOfLocalizationSubscriptions(element_content.id_short,element_content.value, element_content.category, element_content.description,
                                                                                                    element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                locationUE=LocationUE(xPosition, yPosition, zPosition,speed, acceleration, lcsQosClass, accuracy, responseTime,listOfLocalizationSubscriptions, listOfNWSubscriptions, subscriptionRequest, subscriptionManagement,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind) 

            elif(obj.identification.id==ues_iris[i][10]):  #UE5GDataSheet
                for element_content in obj:            
                    if element_content.id_short=="OperatingBands": operatingBands=element_content
                    if element_content.id_short=="UEChannelBandwidth":
                        for element_ref in element_content.value:
                            if element_ref.id_short=="MaximumTransmissionBandwidth": 
                                maxtxbw=element_ref
                                ueChannelBandwidth=UEChannelBandwidth(maxtxbw, element_content.id_short,element_content.value, element_content.category, 
                                                                            element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    if element_content.id_short=="DuplexMode": duplexMode=element_content
                    if element_content.id_short=="TransmitterCharacteristics": 
                        for element_ref in element_content.value:                                
                            if element_ref.id_short=="UEMaximumOutputPower": ueMaxOutPower=element_ref
                            if element_ref.id_short=="OutputPowerDynamics":
                                for element_ref_2 in element_ref.value:
                                    if element_ref_2.id_short=="MinimumOutputPower": minOutPower=element_ref_2
                                    if element_ref_2.id_short=="TransmitOFFPower": 
                                        transmitOFFPower=element_ref_2
                                        output_power_dynamics=OutputPowerDynamics(minOutPower,transmitOFFPower,element_ref.id_short,element_ref.value, element_ref.category, 
                                                                            element_ref.description, element_ref.parent, element_ref.semantic_id, element_ref.qualifier, element_ref.kind)
                            if element_ref.id_short=="TransmitSignalQuality": transmitSignalQuality=element_ref
                            if element_ref.id_short=="OutputRFSpectrumEmissions": outputRFSprectrumEmissions=element_ref
                            if element_ref.id_short=="NumberOfAntennas": numberOfAntennas=element_ref
                            if element_ref.id_short=="NumberOfLayers": numberOfLayers=element_ref 
                            if element_ref.id_short=="MaximumDataUplink": maximumDataUplink=element_ref 
                        transmitterCharacteristics=TransmitterCharacteristics(ueMaxOutPower,output_power_dynamics,transmitSignalQuality,outputRFSprectrumEmissions,numberOfAntennas,numberOfLayers,maximumDataUplink,element_content.id_short,element_content.value, element_content.category, 
                                                                            element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                    if element_content.id_short=="ReceiverCharacteristics": 
                        for element_ref in element_content.value:                                
                            if element_ref.id_short=="ReferenceSensitivityPowerLevel": refsenspowerlvl=element_ref
                            if element_ref.id_short=="MaximumInputLevel": maxInputLevel=element_ref
                            if element_ref.id_short=="AdjacentChannelSelectivity": adjacentChannelSelectivity=element_ref
                            if element_ref.id_short=="NumberOfAntennas": numberOfAntennas=element_ref
                            if element_ref.id_short=="NumberOfLayers": numberOfLayers=element_ref
                            if element_ref.id_short=="MaximumDataDownlink": maximumDataDownlink=element_ref  
                        receiverCharacteristics=ReceiverCharacteristics(refsenspowerlvl,maxInputLevel,adjacentChannelSelectivity,numberOfAntennas,numberOfLayers, maximumDataDownlink,element_content.id_short,element_content.value, element_content.category, 
                                                                            element_content.description, element_content.parent, element_content.semantic_id, element_content.qualifier, element_content.kind)
                ue5GDatasheet=UE5GDataSheet(operatingBands,ueChannelBandwidth,duplexMode,transmitterCharacteristics,receiverCharacteristics,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)  

    for obj in new_object_store:
        #Finally the AAS
        if isinstance(obj,AssetAdministrationShell):
            if i ==0: 
                string_aas = "AAS_UE_5G"
            else:
                string_aas = "AAS_UE_5G_" + str(i+1)

            if obj.id_short==string_aas:
                print(string_aas)
                aasue5G=AASUE5G(ue5G,nameplate,identification,documentation,service,technicalData,ue5GIdentification,networkAccessRestrictions,ueAttachAndConnectionStatus,qos_monitoring, locationUE, ue5GDatasheet, obj.asset, obj.identification, obj.id_short, obj.category, obj.description, obj.parent, obj.administration, obj.security, obj.submodel, obj.concept_dictionary, obj.view, obj.derived_from)
                listOfUeAASs.append(aasue5G)

