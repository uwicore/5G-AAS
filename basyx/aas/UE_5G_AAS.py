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

with aasx.AASXReader("5G_UE_AAS.aasx") as reader:
    # Read all contained AAS objects and all referenced auxiliary files
    # In contrast to the AASX Package Explorer, we are not limited to a single XML part in the package, but instead we
    # will read the contents of all included JSON and XML parts into the ObjectStore
    reader.read_into(object_store=new_object_store,
                     file_store=new_file_store)

    # We can also read the meta data
    new_meta_data = reader.get_core_properties()


#Configuration of IRIs
#Here we have to configurate our IRIs based on our AASX file
nameplate_IRI= "https://example.com/ids/sm/8342_3111_1042_3026"
identification_IRI= "https://example.com/ids/sm/1074_5111_1042_7646"
documentation_IRI= "https://example.com/ids/sm/5542_3111_1042_4014"
service_IRI= "https://example.com/ids/sm/4572_3111_1042_7525"
technicalData_IRI= "https://example.com/ids/sm/5372_3111_1042_7577"                
ue5GIdentification_IRI= "https://example.com/ids/sm/6092_3111_1042_0266"
networkAccessRestrictions_IRI= "https://example.com/ids/sm/5282_3111_1042_5880"
ueAttachAndConnectionStatus_IRI= "https://example.com/ids/sm/4382_3111_1042_2974"
qosMonitoring_IRI= "https://example.com/ids/sm/8482_3111_1042_7222"
location_IRI= "https://example.com/ids/sm/0092_3111_1042_1275"
ue5GDataSheet_IRI= "https://example.com/ids/sm/7423_4122_4042_5354"
asset_idShort= "UE_5G"
AAS_idShort= "AAS_UE_5G"
#CAMBIAR UE1 IRIS Y LO OTRO PORQUE SE ELIMINA SIM CARD
ue1_IRIS=[nameplate_IRI, identification_IRI, documentation_IRI, service_IRI, technicalData_IRI, ue5GDataSheet_IRI, ue5GIdentification_IRI, networkAccessRestrictions_IRI,ueAttachAndConnectionStatus_IRI,qosMonitoring_IRI, location_IRI,  asset_idShort,AAS_idShort]


#This is for a single 5G UE AAS, if you will use more than one you need to use the code commented below

for obj in new_object_store:
    #First the asset
    if isinstance(obj, Asset):
        if obj.id_short==ue1_IRIS[11]: 
            ue5G=UE5G(obj.kind, obj.identification, obj.id_short, obj.category, obj.description)

for obj in new_object_store:
    #Now the submodels
    if isinstance(obj, Submodel):
        if(obj.identification.id==ue1_IRIS[0]):    #Nameplate 
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

        elif(obj.identification.id==ue1_IRIS[1]):  #Identification
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
                if elemento_contenido.id_short=="ChargeId": chargeId=elemento_contenido
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

        elif(obj.identification.id==ue1_IRIS[2]):  #Documentation
            documentation= Documentation(obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[3]):  #Service
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
                        if elemento_ref.id_short=="Phone": phone=elemento_ref
                        if elemento_ref.id_short=="Fax":
                            fax=elemento_ref
                            contact_info=ContactInfo(nameOfSupplier,contactInfo_role,physical_address,email,url,phone,fax, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            
            service=Service(contact_info, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[4]):  #TechnicalData
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
                                    prod_class_system=ProductClassificationItem(productClassificationSystem,classificationSystemVersion,productClassId, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                        elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)

                                    technicalProperties=TechnicalProperties(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            technicalData=TechnicalData(general_info,prod_class_system,technicalProperties,further_info,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)          

        elif(obj.identification.id==ue1_IRIS[5]):   #UE5GDatasheet
            for elemento_contenido in obj:            
                if elemento_contenido.id_short=="OperatingBands": operatingBands=elemento_contenido
                if elemento_contenido.id_short=="UEChannelBandwidth":
                    for elemento_ref in elemento_contenido.value:
                        if elemento_ref.id_short=="MaximumTransmissionBandwidth": 
                            maxtxbw=elemento_ref
                            ueChannelBandwidth=UEChannelBandwidth(maxtxbw, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                        elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="DuplexMode": duplexMode=elemento_contenido
                if elemento_contenido.id_short=="TransmitterCharacteristics": 
                    for elemento_ref in elemento_contenido.value:                                
                        if elemento_ref.id_short=="UEMaximumOutputPower": ueMaxOutPower=elemento_ref
                        if elemento_ref.id_short=="OutputPowerDynamics":
                            for elemento_ref_2 in elemento_ref.value:
                                if elemento_ref_2.id_short=="MinimumOutputPower": minOutPower=elemento_ref_2
                                if elemento_ref_2.id_short=="TransmitOFFPower": 
                                    transmitOFFPower=elemento_ref_2
                                    output_power_dynamics=OutputPowerDynamics(minOutPower,transmitOFFPower,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, 
                                                                        elemento_ref.description, elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                        if elemento_ref.id_short=="TransmitSignalQuality": transmitSignalQuality=elemento_ref
                        if elemento_ref.id_short=="OutputRFSpectrumEmissions": outputRFSprectrumEmissions=elemento_ref
                        if elemento_ref.id_short=="NumberOfAntennas": numberOfAntennas=elemento_ref
                        if elemento_ref.id_short=="NumberOfLayers": numberOfLayers=elemento_ref 
                        if elemento_ref.id_short=="MaximumDataUplink": maximumDataUplink=elemento_ref 
                    transmitterCharacteristics=TransmitterCharacteristics(ueMaxOutPower,output_power_dynamics,transmitSignalQuality,outputRFSprectrumEmissions,numberOfAntennas,numberOfLayers,maximumDataUplink,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                        elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="ReceiverCharacteristics": 
                    for elemento_ref in elemento_contenido.value:                                
                        if elemento_ref.id_short=="ReferenceSensitivityPowerLevel": refsenspowerlvl=elemento_ref
                        if elemento_ref.id_short=="MaximumInputLevel": maxInputLevel=elemento_ref
                        if elemento_ref.id_short=="AdjacentChannelSelectivity": adjacentChannelSelectivity=elemento_ref
                        if elemento_ref.id_short=="NumberOfAntennas": numberOfAntennas=elemento_ref
                        if elemento_ref.id_short=="NumberOfLayers": numberOfLayers=elemento_ref
                        if elemento_ref.id_short=="MaximumDataDownlink": maximumDataDownlink=elemento_ref  
                    receiverCharacteristics=ReceiverCharacteristics(refsenspowerlvl,maxInputLevel,adjacentChannelSelectivity,numberOfAntennas,numberOfLayers, maximumDataDownlink,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                        elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            ue5GDatasheet=UE5GDataSheet(operatingBands,ueChannelBandwidth,duplexMode,transmitterCharacteristics,receiverCharacteristics,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[6]):  #Ue5GIdentification
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="PEI": pei=elemento_contenido
                if elemento_contenido.id_short=="UEIdentityGPSI": gpsi=elemento_contenido
                if elemento_contenido.id_short=="AuthenticationCertificate": authenticationCertificate=elemento_contenido
                if elemento_contenido.id_short=="CertificateStatus": certificateStatus=elemento_contenido
                if elemento_contenido.id_short=="IPAddress": ipAddress=elemento_contenido
                if elemento_contenido.id_short=="MacAddress": macAddress=elemento_contenido
                if elemento_contenido.id_short=="IMSI": imsi=elemento_contenido
                if elemento_contenido.id_short=="ICCID": iccid=elemento_contenido
                if elemento_contenido.id_short=="PIN": pin=elemento_contenido
                if elemento_contenido.id_short=="SPN": spn=elemento_contenido
            ue5GIdentification=Ue5GIdentification(pei, gpsi, authenticationCertificate,certificateStatus,ipAddress, macAddress, imsi, spn, pin, iccid, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[7]):  #NetworkAccessRestrictions
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="ListOfCellGlobalIdentifier": 
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="CGI01": cgi01=elemento_ref
                    listOfCellGlobalIdentifier=ListOfCellGlobalIdentifier(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    listOfCellGlobalIdentifier.add_cgi(cgi01)
                if elemento_contenido.id_short=="ListOfPermissibleSlices": 
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="SNSSAI01": snssai01=elemento_ref
                    listOfPermissibleSlices=ListOfPermissibleSlices(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    listOfPermissibleSlices.add_snssai(snssai01)
            networkAccessRestrictions=NetworkAccessRestrictions(listOfCellGlobalIdentifier,listOfPermissibleSlices,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[8]):  #UeAttachAndConnectionStatus
            for elemento_contenido in obj:  
                if elemento_contenido.id_short=="UEAttached": ue_attached=elemento_contenido
                if elemento_contenido.id_short=="RRCState": rrc_state=elemento_contenido
                if isinstance(elemento_contenido, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                    for elemento_ref in elemento_contenido.value:                                                                                                        
                        if isinstance(elemento_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                            for elemento_ref_2 in elemento_ref.value:   
                                if elemento_ref_2.id_short=="IPAddress": ip_address=elemento_ref_2
                                if elemento_ref_2.id_short=="DNN": dnn=elemento_ref_2
                                if elemento_ref_2.id_short=="LinkDirection": linkDirection=elemento_ref_2

                                if isinstance(elemento_ref_2, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):                                        
                                    for elemento_ref_3 in elemento_ref_2.value: 
                                        if isinstance(elemento_ref_3, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):    
                                            for elemento_ref_4 in elemento_ref_3.value:  
                                                if elemento_ref_4.id_short=="QFI": qfi= elemento_ref_4
                                                if isinstance(elemento_ref_4, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                                                    for elemento_ref_5 in elemento_ref_4.value: 
                                                        if elemento_ref_4.id_short=="RRMParameters":
                                                                    if elemento_ref_5.id_short=="MCSTable": mcstable=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="CQITable": cqitable=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="TargetBLER": target_bler=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="SchedulingType": scheduling_type=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="SchedulingPolicy": scheduling_policy=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="HARQMaximumNumberOfRetransmissions": harq_max_num_retransmissions=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="KNumber": k_number=elemento_ref_5
                                                                    if elemento_ref_5.id_short=="PowerControlPmax": 
                                                                        power_control_pmax=elemento_ref_5
                                                                        rrm_parameters=RRMParameters(mcstable,cqitable,target_bler, scheduling_type,scheduling_policy, harq_max_num_retransmissions,k_number, power_control_pmax, elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                        elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)

                                                        if elemento_ref_4.id_short=="QosProfileRequested":                                                            
                                                            for elemento_ref_6 in elemento_ref_5.value: 
                                                                if elemento_ref_6.id_short=="QosIdentifier": QosIdentifier=elemento_ref_6
                                                                if elemento_ref_6.id_short=="ARP": arp=elemento_ref_6
                                                                if elemento_ref_6.id_short=="RQA": rqa=elemento_ref_6
                                                                if elemento_ref_6.id_short=="NotificationControl": notificationControl=elemento_ref_6
                                                                if elemento_ref_6.id_short=="GFBRUL": gfbr_ul=elemento_ref_6
                                                                if elemento_ref_6.id_short=="GFBRDL": gfbr_dl=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MFBRUL": mfbr_ul=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MFBRDL": mfbr_dl=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_6
                                                                if elemento_ref_6.id_short=="AggregateBitRates": 
                                                                    AggregateBitRates=elemento_ref_6
                                                                    
                                                                    qos_parameters_r=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                    
                                                                if elemento_ref_6.id_short=="ResourceType": ResourceType=elemento_ref_6
                                                                if elemento_ref_6.id_short=="PriorityLevel": PriorityLevel=elemento_ref_6
                                                                if elemento_ref_6.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_6
                                                                if elemento_ref_6.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_6
                                                                if elemento_ref_6.id_short=="AveragingWindow": AveragingWindow=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MaximumDataBurstVolume": 
                                                                    MaximumDataBurstVolume=elemento_ref_6
                                                                    
                                                                    qos_characteristics_r=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)


                                                            if elemento_ref_5.id_short=="AlternativeQosProfiles":
                                                                if elemento_ref_6.id_short=="AlternativeQosProfile01":
                                                                    for elemento_ref_7 in elemento_ref_6:  
                                                                        if elemento_ref_7.id_short=="QosParameters": qosParameters=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value: 
                                                                            if elemento_ref_8.id_short=="QosIdentifier": QosIdentifier=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="ARP": arp=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="RQA": rqa=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="NotificationControl": notificationControl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRUL": gfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRDL": gfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRUL": mfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRDL": mfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AggregateBitRates": 
                                                                                AggregateBitRates=elemento_ref_8
                                                                                
                                                                                qos_parameters=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)

                                                                        if elemento_ref_7.id_short=="QosCharacteristics": qosCharacteristics=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value:
                                                                            if elemento_ref_8.id_short=="ResourceType": ResourceType=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PriorityLevel": PriorityLevel=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AveragingWindow": AveragingWindow=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumDataBurstVolume": 
                                                                                MaximumDataBurstVolume=elemento_ref_8
                                                                                
                                                                                qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)
                                                                                
                                                                                alternativeQosProfile=AlternativeQosProfile(qos_parameters,qos_characteristics,elemento_ref_6.id_short,elemento_ref_6.value, elemento_ref_6.category, elemento_ref_6.description,
                                                                                                            elemento_ref_6.parent, elemento_ref_6.semantic_id, elemento_ref_6.qualifier, elemento_ref_6.kind)
                                                                            
                                                                                alternativeQosProfileList=AlternativeQosProfiles(elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                            elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                                alternativeQosProfileList.add_alternative_qos_profile(alternativeQosProfile)   

                                                                    qos_profile_requested=QosProfile(qos_parameters_r,qos_characteristics_r, alternativeQosProfileList, elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                        elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)

                                                        if elemento_ref_4.id_short=="QosProfileGuaranteed":                                                            
                                                            for elemento_ref_6 in elemento_ref_5.value: 
                                                                if elemento_ref_6.id_short=="QosIdentifier": QosIdentifier=elemento_ref_6
                                                                if elemento_ref_6.id_short=="ARP": arp=elemento_ref_6
                                                                if elemento_ref_6.id_short=="RQA": rqa=elemento_ref_6
                                                                if elemento_ref_6.id_short=="NotificationControl": notificationControl=elemento_ref_6
                                                                if elemento_ref_6.id_short=="GFBRUL": gfbr_ul=elemento_ref_6
                                                                if elemento_ref_6.id_short=="GFBRDL": gfbr_dl=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MFBRUL": mfbr_ul=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MFBRDL": mfbr_dl=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_6
                                                                if elemento_ref_6.id_short=="AggregateBitRates": 
                                                                    AggregateBitRates=elemento_ref_6
                                                                    
                                                                    qos_parameters_g=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                    
                                                                if elemento_ref_6.id_short=="ResourceType": ResourceType=elemento_ref_6
                                                                if elemento_ref_6.id_short=="PriorityLevel": PriorityLevel=elemento_ref_6
                                                                if elemento_ref_6.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_6
                                                                if elemento_ref_6.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_6
                                                                if elemento_ref_6.id_short=="AveragingWindow": AveragingWindow=elemento_ref_6
                                                                if elemento_ref_6.id_short=="MaximumDataBurstVolume": 
                                                                    MaximumDataBurstVolume=elemento_ref_6
                                                                    
                                                                    qos_characteristics_g=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                            if elemento_ref_5.id_short=="AlternativeQosProfiles":
                                                                if elemento_ref_6.id_short=="AlternativeQosProfile01":
                                                                    for elemento_ref_7 in elemento_ref_6:  
                                                                        if elemento_ref_7.id_short=="QosParameters": qosParameters=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value: 
                                                                            if elemento_ref_8.id_short=="QosIdentifier": QosIdentifier=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="ARP": arp=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="RQA": rqa=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="NotificationControl": notificationControl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRUL": gfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRDL": gfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRUL": mfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRDL": mfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AggregateBitRates": 
                                                                                AggregateBitRates=elemento_ref_8
                                                                                
                                                                                qos_parameters=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)

                                                                        if elemento_ref_7.id_short=="QosCharacteristics": qosCharacteristics=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value:
                                                                            if elemento_ref_8.id_short=="ResourceType": ResourceType=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PriorityLevel": PriorityLevel=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AveragingWindow": AveragingWindow=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumDataBurstVolume": 
                                                                                MaximumDataBurstVolume=elemento_ref_8
                                                                                
                                                                                qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)
                                                                                
                                                                                alternativeQosProfile=AlternativeQosProfile(qos_parameters,qos_characteristics,elemento_ref_6.id_short,elemento_ref_6.value, elemento_ref_6.category, elemento_ref_6.description,
                                                                                                            elemento_ref_6.parent, elemento_ref_6.semantic_id, elemento_ref_6.qualifier, elemento_ref_6.kind)
                                                                            
                                                                                alternativeQosProfileList=AlternativeQosProfiles(elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                            elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                                alternativeQosProfileList.add_alternative_qos_profile(alternativeQosProfile)   

                                                                        
                                                                    qos_profile_guaranteed=QosProfile(qos_parameters_g,qos_characteristics_g, alternativeQosProfileList, elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                        elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)

                                            qos_flow=QosFlowStatus(qfi, qos_profile_requested,qos_profile_guaranteed, rrm_parameters,elemento_ref_3.id_short,elemento_ref_3.value, elemento_ref_3.category, 
                                                                                        elemento_ref_3.description, elemento_ref_3.parent, elemento_ref_3.semantic_id, elemento_ref_3.qualifier, elemento_ref_3.kind)
                                        
                                        qos_flow_list=QosFlowStatusList(elemento_ref_2.id_short,elemento_ref_2.value, elemento_ref_2.category, 
                                                                                        elemento_ref_2.description, elemento_ref_2.parent, elemento_ref_2.semantic_id, elemento_ref_2.qualifier, elemento_ref_2.kind)
                                        qos_flow_list.add_qos_flow(qos_flow)
                                
                            pdu_session=PDUSessionStatus(ip_address, dnn, qos_flow_list,linkDirection, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, 
                                                                                        elemento_ref.description, elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                    
                        pdu_session_list=PDUSessionStatusList(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                                        elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                        pdu_session_list.add_pdu_session(pdu_session)
                if elemento_contenido.id_short=="NewConnectionRequest": newConnectionRequest=elemento_contenido
                if elemento_contenido.id_short=="ConnectionModificationRequest": connectionModificationRequest=elemento_contenido
                if elemento_contenido.id_short=="QoSRequest": qoSRequest=elemento_contenido
            ueAttachAndConnectionStatus=UeAttachAndConnectionStatus(ue_attached,rrc_state, pdu_session_list, newConnectionRequest, connectionModificationRequest, qoSRequest, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[9]):  #QosMonitoring
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="GeneralKeyPerformanceIndicators":
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="DroppedConnections": dropped_connections=elemento_ref
                        if elemento_ref.id_short=="TrafficVolumeForEach5QIAndAlternativeQosProfiles": trafficVolumeForEach5QIAndAlternativeQosProfile=elemento_ref
                        if elemento_ref.id_short=="HandoverSuccessRate": handoverSuccessRate=elemento_ref
                        if elemento_ref.id_short=="SINR": sinr=elemento_ref
                        if elemento_ref.id_short=="DataThroughput": dataThroughput=elemento_ref
                        if elemento_ref.id_short=="BLER": bler=elemento_ref
                        if elemento_ref.id_short=="PER": 
                            per=elemento_ref
                            general_key_performance_indicators=GeneralKeyPerformanceIndicators(dropped_connections, trafficVolumeForEach5QIAndAlternativeQosProfile,handoverSuccessRate,sinr,dataThroughput,bler,per, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="SignalLevel":
                    for elemento_ref in elemento_contenido:
                        if elemento_ref.id_short=="RSSI": rssi=elemento_ref
                        if elemento_ref.id_short=="RSRP": rsrp=elemento_ref
                        if elemento_ref.id_short=="RSRQ": 
                            rsrq=elemento_ref
                            signal_level=SignalLevel(rssi,rsrp,rsrq,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="ParametersPertainingConnections":
                    for elemento_ref in elemento_contenido.value:                                                                                                 
                        for elemento_ref_2 in elemento_ref.value:                                          
                            for elemento_ref_3 in elemento_ref_2.value: 
                                if elemento_ref_3.id_short=="IPAddress": ip_address=elemento_ref_3 
                                if elemento_ref_3.id_short=="QosFlowList":
                                    for elemento_ref_4 in elemento_ref_3.value: 
                                        if elemento_ref_4.id_short=="QosFlow01":
                                            for elemento_ref_5 in elemento_ref_4.value:  
                                                if elemento_ref_5.id_short=="QFI": qfi= elemento_ref_5
                                                if elemento_ref_5.id_short=="CommunicationServiceAvailabilty":commservavai=elemento_ref_5
                                                if elemento_ref_5.id_short=="CommunicationServiceReliability":commservrel=elemento_ref_5
                                                if elemento_ref_5.id_short=="EndToEndLatencyMaximum":e2elm=elemento_ref_5
                                                if elemento_ref_5.id_short=="EndToEndLatencyAVG":e2elavg=elemento_ref_5
                                                if elemento_ref_5.id_short=="SurvivalTime":survivalTime=elemento_ref_5
                                                if elemento_ref_5.id_short=="ServiceBitRate":serviceBitRate=elemento_ref_5
                                                if elemento_ref_5.id_short=="PacketErrorRatio":per=elemento_ref_5
                                                if elemento_ref_5.id_short=="BLER":bler=elemento_ref_5
                                                if elemento_ref_5.id_short=="UpdateTime":updateTime=elemento_ref_5
                                                if elemento_ref_5.id_short=="DataThroughput":dataThroughput=elemento_ref_5
                                                if elemento_ref_5.id_short=="Cause5GSM":
                                                    cause=elemento_ref_5
                                                    qos_flow=QosFlowMonitoring(qfi,commservavai,commservrel,e2elm,e2elavg,survivalTime,serviceBitRate,per,bler,updateTime,dataThroughput,cause,elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                        elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)
                                    qos_flow_list=QosFlowMonitoringList(elemento_ref_3.id_short,elemento_ref_3.value, elemento_ref_3.category, 
                                                                                        elemento_ref_3.description, elemento_ref_3.parent, elemento_ref_3.semantic_id, elemento_ref_3.qualifier, elemento_ref_3.kind)
                                    qos_flow_list.add_qos_flow(qos_flow)
                            pdu_session=PDUSessionMonitoring(ip_address,qos_flow_list,elemento_ref_2.id_short,elemento_ref_2.value, elemento_ref_2.category, 
                                                                                        elemento_ref_2.description, elemento_ref_2.parent, elemento_ref_2.semantic_id, elemento_ref_2.qualifier, elemento_ref_2.kind)
                        pdu_session_list=PDUSessionMonitoringList(elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                        elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                        pdu_session_list.add_pdu_session(pdu_session)
                    parameters_pertaining_connections=ParametersPertainingConnections(pdu_session_list,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)                                    
                if elemento_contenido.id_short=="QosQuery": qosQuery=elemento_contenido
                if elemento_contenido.id_short=="SubscriptionRequest": subscriptionRequest=elemento_contenido
                if elemento_contenido.id_short=="EventNotificationAction": eventNotificationAction=elemento_contenido
                if elemento_contenido.id_short=="ListOfSubscriptions": listOfMonitoringSubscriptions=ListOfMonitoringSubscriptions(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                if elemento_contenido.id_short=="UpdateTime":updateTime=elemento_contenido
            qos_monitoring=QosMonitoring(general_key_performance_indicators,signal_level,parameters_pertaining_connections,qosQuery,subscriptionRequest,eventNotificationAction,listOfMonitoringSubscriptions,updateTime,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

        elif(obj.identification.id==ue1_IRIS[10]):  #Location
            for elemento_contenido in obj:
                if elemento_contenido.id_short=="XPosition":xPosition=elemento_contenido
                if elemento_contenido.id_short=="YPosition":yPosition=elemento_contenido
                if elemento_contenido.id_short=="ZPosition":zPosition=elemento_contenido 
                if elemento_contenido.id_short=="Speed":speed=elemento_contenido
                if elemento_contenido.id_short=="Acceleration":acceleration=elemento_contenido
                if elemento_contenido.id_short=="LCSQosClass": lcsQosClass=elemento_contenido
                if elemento_contenido.id_short=="Accuracy": accuracy=elemento_contenido
                if elemento_contenido.id_short=="ResponseTime": responseTime=elemento_contenido
                if elemento_contenido.id_short=="SubscriptionRequest": subscriptionRequest=elemento_contenido
                if elemento_contenido.id_short=="EventNotificationAction": eventNotificationAction=elemento_contenido
                if elemento_contenido.id_short=="ListOfSubscriptions": listOfLocalizationSubscriptions=ListOfLocalizationSubscriptions(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
            locationUE=LocationUE(xPosition, yPosition, zPosition,speed, acceleration, lcsQosClass, accuracy, responseTime,listOfLocalizationSubscriptions,subscriptionRequest,eventNotificationAction,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)    

for obj in new_object_store:
    #Finally the AAS
    if isinstance(obj,AssetAdministrationShell):
        if obj.id_short==ue1_IRIS[12]:
            aasue5G=AASUE5G(ue5G,nameplate,identification,documentation,service,technicalData,ue5GIdentification,networkAccessRestrictions,ueAttachAndConnectionStatus,qos_monitoring, locationUE, ue5GDatasheet, obj.asset, obj.identification, obj.id_short, obj.category, obj.description, obj.parent, obj.administration, obj.security, obj.submodel, obj.concept_dictionary, obj.view, obj.derived_from)




#If there are more than one 5G UE AAS then you should use this code
#Here we have an example of use with 2 AAS, but if you need multiple AASs you only have to repeat the configuration of IRIs step and change the Ues list

'''


#Configuration of IRIs
#Here we have to configurate our IRIs based on our AASX file
nameplate_IRI= "https://example.com/ids/sm/1482_2111_1052_6324"
identification_IRI= "https://example.com/ids/sm/8580_0160_4032_4523"
documentation_IRI= "https://example.com/ids/sm/4590_0160_4032_7169"
service_IRI= "https://example.com/ids/sm/0464_0160_4032_2624"
technicalData_IRI= "https://example.com/ids/sm/0201_0160_4032_9321"
ue5GIdentification_IRI= "https://example.com/ids/sm/1451_2120_5032_6719"
networkAccessRestrictions_IRI= "https://example.com/ids/sm/9374_0160_4032_3879"
ueAttachAndConnectionStatus_IRI= "https://example.com/ids/sm/3513_1160_4032_9468"
qosMonitoring_IRI= "https://example.com/ids/sm/6135_1160_4032_3954"
location_IRI= "https://example.com/ids/sm/2161_6162_4032_6231"
ue5GDataSheet_IRI= "https://example.com/ids/sm/6553_4122_4042_8971"
asset_idShort= "UE_5G_2"
AAS_idShort= "AAS_UE_5G_2"
ue2_IRIS=[nameplate_IRI, identification_IRI, documentation_IRI, service_IRI, technicalData_IRI, ue5GDataSheet_IRI, ue5GIdentification_IRI, networkAccessRestrictions_IRI,ueAttachAndConnectionStatus_IRI,qosMonitoring_IRI, location_IRI, asset_idShort,AAS_idShort]


Ues = [ue1_IRIS, ue2_IRIS]

listOfUeAASs=[]

for ue in Ues:

    for obj in new_object_store:
        #First the asset
        if isinstance(obj, Asset):
            if obj.id_short==ue[11]: 
                ue5G=UE5G(obj.kind, obj.identification, obj.id_short, obj.category, obj.description)

    for obj in new_object_store:
        #Now the submodels
        if isinstance(obj, Submodel):
            if(obj.identification.id==ue[0]):    #Nameplate 
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

            elif(obj.identification.id==ue[1]):  #Identification
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
                    if elemento_contenido.id_short=="ChargeId": chargeId=elemento_contenido
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

            elif(obj.identification.id==ue[2]):  #Documentation
                documentation= Documentation(obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ue[3]):  #Service
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
                            if elemento_ref.id_short=="Phone": phone=elemento_ref
                            if elemento_ref.id_short=="Fax":
                                fax=elemento_ref
                                contact_info=ContactInfo(nameOfSupplier,contactInfo_role,physical_address,email,url,phone,fax, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                
                service=Service(contact_info, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ue[4]):  #TechnicalData
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
                                        prod_class_system=ProductClassificationItem(productClassificationSystem,classificationSystemVersion,productClassId, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                            elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)

                                        technicalProperties=TechnicalProperties(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                technicalData=TechnicalData(general_info,prod_class_system,technicalProperties,further_info,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)       
    
            elif(obj.identification.id==ue[5]):  #UE5GDataSheet
                for elemento_contenido in obj:            
                    if elemento_contenido.id_short=="OperatingBands": operatingBands=elemento_contenido
                    if elemento_contenido.id_short=="UEChannelBandwidth":
                        for elemento_ref in elemento_contenido.value:
                            if elemento_ref.id_short=="MaximumTransmissionBandwidth": 
                                maxtxbw=elemento_ref
                                ueChannelBandwidth=UEChannelBandwidth(maxtxbw, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                            elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    if elemento_contenido.id_short=="DuplexMode": duplexMode=elemento_contenido
                    if elemento_contenido.id_short=="TransmitterCharacteristics": 
                        for elemento_ref in elemento_contenido.value:                                
                            if elemento_ref.id_short=="UeMaximumOutputPower": ueMaxOutPower=elemento_ref
                            if elemento_ref.id_short=="OutputPowerDynamics":
                                for elemento_ref_2 in elemento_ref.value:
                                    if elemento_ref_2.id_short=="MinimumOutputPower": minOutPower=elemento_ref_2
                                    if elemento_ref_2.id_short=="TransmitOFFPower": 
                                        transmitOFFPower=elemento_ref_2
                                        output_power_dynamics=OutputPowerDynamics(minOutPower,transmitOFFPower,elemento_ref.id_short,elemento_ref.value, elemento_ref.category, 
                                                                            elemento_ref.description, elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            if elemento_ref.id_short=="TransmitSignalQuality": transmitSignalQuality=elemento_ref
                            if elemento_ref.id_short=="OutputRFSpectrumEmissions": outputRFSprectrumEmissions=elemento_ref
                            if elemento_ref.id_short=="NumberOfAntennas": numberOfAntennas=elemento_ref
                            if elemento_ref.id_short=="NumberOfLayers": numberOfLayers=elemento_ref 
                            if elemento_ref.id_short=="MaximumDataUplink": maximumDataUplink=elemento_ref 
                        transmitterCharacteristics=TransmitterCharacteristics(ueMaxOutPower,output_power_dynamics,transmitSignalQuality,outputRFSprectrumEmissions,numberOfAntennas,numberOfLayers,maximumDataUplink,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                            elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    if elemento_contenido.id_short=="ReceiverCharacteristics": 
                        for elemento_ref in elemento_contenido.value:                                
                            if elemento_ref.id_short=="ReferenceSensitivityPowerLevel": refsenspowerlvl=elemento_ref
                            if elemento_ref.id_short=="MaximumInputLevel": maxInputLevel=elemento_ref
                            if elemento_ref.id_short=="AdjacentChannelSelectivity": adjacentChannelSelectivity=elemento_ref
                            if elemento_ref.id_short=="NumberOfAntennas": numberOfAntennas=elemento_ref
                            if elemento_ref.id_short=="NumberOfLayers": numberOfLayers=elemento_ref
                            if elemento_ref.id_short=="MaximumDataDownlink": maximumDataDownlink=elemento_ref  
                        receiverCharacteristics=ReceiverCharacteristics(refsenspowerlvl,maxInputLevel,adjacentChannelSelectivity,numberOfAntennas,numberOfLayers, maximumDataDownlink,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                            elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                ue5GDatasheet=UE5GDataSheet(operatingBands,ueChannelBandwidth,duplexMode,transmitterCharacteristics,receiverCharacteristics,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)              

            elif(obj.identification.id==ue[6]):  #Ue5GIdentification
                for elemento_contenido in obj:
                    if elemento_contenido.id_short=="PermanentEquipmentIdentifier": pei=elemento_contenido
                    if elemento_contenido.id_short=="UeIdentityGPSI": gpsi=elemento_contenido
                    if elemento_contenido.id_short=="AuthenticationCertificate": authenticationCertificate=elemento_contenido
                    if elemento_contenido.id_short=="CertificateStatus": certificateStatus=elemento_contenido
                    if elemento_contenido.id_short=="IPAddress": ipAddress=elemento_contenido
                    if elemento_contenido.id_short=="MacAddress": macAddress=elemento_contenido
                    if elemento_contenido.id_short=="IMSI": imsi=elemento_contenido
                    if elemento_contenido.id_short=="ICCID": iccid=elemento_contenido
                    if elemento_contenido.id_short=="PIN": pin=elemento_contenido
                    if elemento_contenido.id_short=="SPN": spn=elemento_contenido
                ue5GIdentification=Ue5GIdentification(pei, gpsi, authenticationCertificate,certificateStatus,ipAddress, macAddress, imsi, spn, pin, iccid obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
                
            elif(obj.identification.id==ue[7]):  #NetworkAccessRestrictions
                for elemento_contenido in obj:
                    if elemento_contenido.id_short=="ListOfCellGlobalIdentifier": 
                        for elemento_ref in elemento_contenido:
                            if elemento_ref.id_short=="CGI01": cgi01=elemento_ref
                        listOfCellGlobalIdentifier=ListOfCellGlobalIdentifier(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                        listOfCellGlobalIdentifier.add_cgi(cgi01)
                    if elemento_contenido.id_short=="ListOfPermissibleSlices": 
                        for elemento_ref in elemento_contenido:
                            if elemento_ref.id_short=="SNSSAI01": snssai01=elemento_ref
                        listOfPermissibleSlices=ListOfPermissibleSlices(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                        listOfPermissibleSlices.add_snssai(snssai01)
                networkAccessRestrictions=NetworkAccessRestrictions(listOfCellGlobalIdentifier,listOfPermissibleSlices,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ue[8]):  #UeAttachAndConnectionStatus
                for elemento_contenido in obj:  
                    if elemento_contenido.id_short=="UeAttached": ue_attached=elemento_contenido
                    if elemento_contenido.id_short=="RRCState": rrc_state=elemento_contenido
                    if isinstance(elemento_contenido, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):       
                        for elemento_ref in elemento_contenido.value:                                                                                                        
                            if isinstance(elemento_ref, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                                for elemento_ref_2 in elemento_ref.value:   
                                    if elemento_ref_2.id_short=="IPAddress": ip_address=elemento_ref_2
                                    if elemento_ref_2.id_short=="DNN": dnn=elemento_ref_2
                                    if elemento_ref_2.id_short=="LinkDirection": linkDirection=elemento_ref_2

                                    if isinstance(elemento_ref_2, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):                                        
                                        for elemento_ref_3 in elemento_ref_2.value: 
                                            if isinstance(elemento_ref_3, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):    
                                                for elemento_ref_4 in elemento_ref_3.value:  
                                                    if elemento_ref_4.id_short=="QFI": qfi= elemento_ref_4
                                                    if isinstance(elemento_ref_4, (SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered)):
                                                        for elemento_ref_5 in elemento_ref_4.value: 
                                                            if elemento_ref_4.id_short=="RRMParameters":
                                                                        if elemento_ref_5.id_short=="MCSTable": mcstable=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="CQITable": cqitable=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="TargetBLER": target_bler=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="SchedulingType": scheduling_type=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="SchedulingPolicy": scheduling_policy=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="HARQMaximumNumberOfRetransmissions": harq_max_num_retransmissions=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="KNumber": k_number=elemento_ref_5
                                                                        if elemento_ref_5.id_short=="PowerControlPmax": 
                                                                            power_control_pmax=elemento_ref_5
                                                                            rrm_parameters=RRMParameters(mcstable,cqitable,target_bler, scheduling_type,scheduling_policy, harq_max_num_retransmissions,k_number, power_control_pmax, elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                            elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)

                                                            if elemento_ref_4.id_short=="QosProfileRequested":                                                            
                                                                for elemento_ref_6 in elemento_ref_5.value: 
                                                                    if elemento_ref_6.id_short=="QosIdentifier": QosIdentifier=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="ARP": arp=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="RQA": rqa=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="NotificationControl": notificationControl=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="GFBRUL": gfbr_ul=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="GFBRDL": gfbr_dl=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MFBRUL": mfbr_ul=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MFBRDL": mfbr_dl=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="AggregateBitRates": 
                                                                        AggregateBitRates=elemento_ref_6
                                                                        
                                                                        qos_parameters_r=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                    elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                    elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                        
                                                                    if elemento_ref_6.id_short=="ResourceType": ResourceType=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="PriorityLevel": PriorityLevel=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="AveragingWindow": AveragingWindow=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MaximumDataBurstVolume": 
                                                                        MaximumDataBurstVolume=elemento_ref_6
                                                                        
                                                                        qos_characteristics_r=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                    elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                    elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)


                                                                if elemento_ref_5.id_short=="AlternativeQosProfiles":
                                                                    if elemento_ref_6.id_short=="AlternativeQosProfile01":
            
                                                                        if elemento_ref_7.id_short=="QosParameters": qosParameters=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value: 
                                                                            if elemento_ref_8.id_short=="QosIdentifier": QosIdentifier=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="ARP": arp=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="RQA": rqa=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="NotificationControl": notificationControl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRUL": gfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRDL": gfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRUL": mfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRDL": mfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AggregateBitRates": 
                                                                                AggregateBitRates=elemento_ref_8
                                                                                
                                                                                qos_parameters=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)

                                                                        if elemento_ref_7.id_short=="QosCharacteristics": qosCharacteristics=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value:
                                                                            if elemento_ref_8.id_short=="ResourceType": ResourceType=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PriorityLevel": PriorityLevel=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AveragingWindow": AveragingWindow=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumDataBurstVolume": 
                                                                                MaximumDataBurstVolume=elemento_ref_8
                                                                                
                                                                                qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)
                                                                                
                                                                                alternativeQosProfile=AlternativeQosProfile(qos_parameters,qos_characteristics,elemento_ref_6.id_short,elemento_ref_6.value, elemento_ref_6.category, elemento_ref_6.description,
                                                                                                            elemento_ref_6.parent, elemento_ref_6.semantic_id, elemento_ref_6.qualifier, elemento_ref_6.kind)
                                                                            
                                                                                alternativeQosProfileList=AlternativeQosProfiles(elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                            elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                                alternativeQosProfileList.add_alternative_qos_profile(alternativeQosProfile)   

                                                                        qos_profile_requested=QosProfile(qos_parameters_r,qos_characteristics_r, alternativeQosProfileList, elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                            elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)

                                                            if elemento_ref_4.id_short=="QosProfileGuaranteed":                                                            
                                                                for elemento_ref_6 in elemento_ref_5.value: 
                                                                    if elemento_ref_6.id_short=="QosIdentifier": QosIdentifier=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="ARP": arp=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="RQA": rqa=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="NotificationControl": notificationControl=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="GFBRUL": gfbr_ul=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="GFBRDL": gfbr_dl=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MFBRUL": mfbr_ul=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MFBRDL": mfbr_dl=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="AggregateBitRates": 
                                                                        AggregateBitRates=elemento_ref_6
                                                                        
                                                                        qos_parameters_g=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                    elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                    elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                        
                                                                    if elemento_ref_6.id_short=="ResourceType": ResourceType=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="PriorityLevel": PriorityLevel=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="AveragingWindow": AveragingWindow=elemento_ref_6
                                                                    if elemento_ref_6.id_short=="MaximumDataBurstVolume": 
                                                                        MaximumDataBurstVolume=elemento_ref_6
                                                                        
                                                                        qos_characteristics_g=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                    elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                    elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                if elemento_ref_5.id_short=="AlternativeQosProfiles":
                                                                    if elemento_ref_6.id_short=="AlternativeQosProfile01":
            
                                                                        if elemento_ref_7.id_short=="QosParameters": qosParameters=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value: 
                                                                            if elemento_ref_8.id_short=="QosIdentifier": QosIdentifier=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="ARP": arp=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="RQA": rqa=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="NotificationControl": notificationControl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRUL": gfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="GFBRDL": gfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRUL": mfbr_ul=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MFBRDL": mfbr_dl=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumPacketLossRate": MaximumPacketLossRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AggregateBitRates": 
                                                                                AggregateBitRates=elemento_ref_8
                                                                                
                                                                                qos_parameters=QosParameters(QosIdentifier,arp, rqa,notificationControl,gfbr_ul,gfbr_dl,mfbr_ul, mfbr_dl,MaximumPacketLossRate,AggregateBitRates,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)

                                                                        if elemento_ref_7.id_short=="QosCharacteristics": qosCharacteristics=elemento_ref_7
                                                                        for elemento_ref_8 in elemento_ref_7.value:
                                                                            if elemento_ref_8.id_short=="ResourceType": ResourceType=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PriorityLevel": PriorityLevel=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketDelayBudget": PacketDelayBudget=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="PacketErrorRate": PacketErrorRate=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="AveragingWindow": AveragingWindow=elemento_ref_8
                                                                            if elemento_ref_8.id_short=="MaximumDataBurstVolume": 
                                                                                MaximumDataBurstVolume=elemento_ref_8
                                                                                
                                                                                qos_characteristics=QosCharacteristics(ResourceType, PriorityLevel, PacketDelayBudget, PacketErrorRate,AveragingWindow, MaximumDataBurstVolume,
                                                                                                            elemento_ref_7.id_short,elemento_ref_7.value, elemento_ref_7.category, elemento_ref_7.description,
                                                                                                            elemento_ref_7.parent, elemento_ref_7.semantic_id, elemento_ref_7.qualifier, elemento_ref_7.kind)
                                                                                
                                                                                alternativeQosProfile=AlternativeQosProfile(qos_parameters,qos_characteristics,elemento_ref_6.id_short,elemento_ref_6.value, elemento_ref_6.category, elemento_ref_6.description,
                                                                                                            elemento_ref_6.parent, elemento_ref_6.semantic_id, elemento_ref_6.qualifier, elemento_ref_6.kind)
                                                                            
                                                                                alternativeQosProfileList=AlternativeQosProfiles(elemento_ref_5.id_short,elemento_ref_5.value, elemento_ref_5.category, elemento_ref_5.description,
                                                                                                            elemento_ref_5.parent, elemento_ref_5.semantic_id, elemento_ref_5.qualifier, elemento_ref_5.kind)
                                                                                alternativeQosProfileList.add_alternative_qos_profile(alternativeQosProfile)   

                                                                        
                                                                        qos_profile_guaranteed=QosProfile(qos_parameters_g,qos_characteristics_g, alternativeQosProfileList, elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                            elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)

                                                qos_flow=QosFlowStatus(qfi, qos_profile_requested,qos_profile_guaranteed, rrm_parameters,elemento_ref_3.id_short,elemento_ref_3.value, elemento_ref_3.category, 
                                                                                            elemento_ref_3.description, elemento_ref_3.parent, elemento_ref_3.semantic_id, elemento_ref_3.qualifier, elemento_ref_3.kind)
                                            
                                            qos_flow_list=QosFlowStatusList(elemento_ref_2.id_short,elemento_ref_2.value, elemento_ref_2.category, 
                                                                                            elemento_ref_2.description, elemento_ref_2.parent, elemento_ref_2.semantic_id, elemento_ref_2.qualifier, elemento_ref_2.kind)
                                            qos_flow_list.add_qos_flow(qos_flow)
                                    
                                pdu_session=PDUSessionStatus(ip_address, dnn, qos_flow_list,linkDirection, elemento_ref.id_short,elemento_ref.value, elemento_ref.category, 
                                                                                            elemento_ref.description, elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                        
                            pdu_session_list=PDUSessionStatusList(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, 
                                                                                            elemento_contenido.description, elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                            pdu_session_list.add_pdu_session(pdu_session)
                    if elemento_contenido.id_short=="NewConnectionRequest": newConnectionRequest=elemento_contenido
                    if elemento_contenido.id_short=="ConnectionModificationRequest": connectionModificationRequest=elemento_contenido
                    if elemento_contenido.id_short=="QoSRequest": qoSRequest=elemento_contenido
                ueAttachAndConnectionStatus=UeAttachAndConnectionStatus(ue_attached,rrc_state, pdu_session_list, newConnectionRequest, connectionModificationRequest, qoSRequest, obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

            elif(obj.identification.id==ue[9]):  #QosMonitoring
                for elemento_contenido in obj:
                    if elemento_contenido.id_short=="GeneralKeyPerformanceIndicators":
                        for elemento_ref in elemento_contenido:
                            if elemento_ref.id_short=="DroppedConnections": dropped_connections=elemento_ref
                            if elemento_ref.id_short=="TrafficVolumeForEach5QIAndAlternativeQosProfiles": trafficVolumeForEach5QIAndAlternativeQosProfile=elemento_ref
                            if elemento_ref.id_short=="HandoverSuccessRate": handoverSuccessRate=elemento_ref
                            if elemento_ref.id_short=="SINR": sinr=elemento_ref
                            if elemento_ref.id_short=="DataThroughput": dataThroughput=elemento_ref
                            if elemento_ref.id_short=="BLER": bler=elemento_ref
                            if elemento_ref.id_short=="PER": 
                                per=elemento_ref
                                general_key_performance_indicators=GeneralKeyPerformanceIndicators(dropped_connections, trafficVolumeForEach5QIAndAlternativeQosProfile,handoverSuccessRate,sinr,dataThroughput,bler,per, elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                        elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    if elemento_contenido.id_short=="SignalLevel":
                        for elemento_ref in elemento_contenido:
                            if elemento_ref.id_short=="RSSI": rssi=elemento_ref
                            if elemento_ref.id_short=="RSRP": rsrp=elemento_ref
                            if elemento_ref.id_short=="RSRQ": 
                                rsrq=elemento_ref
                                signal_level=SignalLevel(rssi,rsrp,rsrq,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    if elemento_contenido.id_short=="ParametersPertainingConnections":
                        for elemento_ref in elemento_contenido.value:                                                                                                 
                            for elemento_ref_2 in elemento_ref.value:                                          
                                for elemento_ref_3 in elemento_ref_2.value: 
                                    if elemento_ref_3.id_short=="IPAddress": ip_address=elemento_ref_3 
                                    if elemento_ref_3.id_short=="QosFlowList":
                                        for elemento_ref_4 in elemento_ref_3.value: 
                                            if elemento_ref_4.id_short=="QosFlow01":
                                                for elemento_ref_5 in elemento_ref_4.value:  
                                                    if elemento_ref_5.id_short=="QFI": qfi= elemento_ref_5
                                                    if elemento_ref_5.id_short=="CommunicationServiceAvailabilty":commservavai=elemento_ref_5
                                                    if elemento_ref_5.id_short=="CommunicationServiceReliability":commservrel=elemento_ref_5
                                                    if elemento_ref_5.id_short=="EndToEndLatencyMaximum":e2elm=elemento_ref_5
                                                    if elemento_ref_5.id_short=="EndToEndLatencyAVG":e2elavg=elemento_ref_5
                                                    if elemento_ref_5.id_short=="SurvivalTime":survivalTime=elemento_ref_5
                                                    if elemento_ref_5.id_short=="ServiceBitRate":serviceBitRate=elemento_ref_5
                                                    if elemento_ref_5.id_short=="PacketErrorRatio":per=elemento_ref_5
                                                    if elemento_ref_5.id_short=="BLER":bler=elemento_ref_5
                                                    if elemento_ref_5.id_short=="UpdateTime":updateTime=elemento_ref_5
                                                    if elemento_ref_5.id_short=="DataThroughput":dataThroughput=elemento_ref_5
                                                    if elemento_ref_5.id_short=="Cause5GSM":
                                                        cause=elemento_ref_5
                                                        qos_flow=QosFlowMonitoring(qfi,commservavai,commservrel,e2elm,e2elavg,survivalTime,serviceBitRate,per,bler,updateTime,dataThroughput,cause,elemento_ref_4.id_short,elemento_ref_4.value, elemento_ref_4.category, 
                                                                                            elemento_ref_4.description, elemento_ref_4.parent, elemento_ref_4.semantic_id, elemento_ref_4.qualifier, elemento_ref_4.kind)
                                        qos_flow_list=QosFlowMonitoringList(elemento_ref_3.id_short,elemento_ref_3.value, elemento_ref_3.category, 
                                                                                            elemento_ref_3.description, elemento_ref_3.parent, elemento_ref_3.semantic_id, elemento_ref_3.qualifier, elemento_ref_3.kind)
                                        qos_flow_list.add_qos_flow(qos_flow)
                                pdu_session=PDUSessionMonitoring(ip_address,qos_flow_list,elemento_ref_2.id_short,elemento_ref_2.value, elemento_ref_2.category, 
                                                                                            elemento_ref_2.description, elemento_ref_2.parent, elemento_ref_2.semantic_id, elemento_ref_2.qualifier, elemento_ref_2.kind)
                            pdu_session_list=PDUSessionMonitoringList(elemento_ref.id_short,elemento_ref.value, elemento_ref.category, elemento_ref.description,
                                                                                                            elemento_ref.parent, elemento_ref.semantic_id, elemento_ref.qualifier, elemento_ref.kind)
                            pdu_session_list.add_pdu_session(pdu_session)
                        parameters_pertaining_connections=ParametersPertainingConnections(pdu_session_list,elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)                                    
                    if elemento_contenido.id_short=="QosQuery": qosQuery=elemento_contenido
                    if elemento_contenido.id_short=="SubscriptionRequest": subscriptionRequest=elemento_contenido
                    if elemento_contenido.id_short=="EventNotificationAction": eventNotificationAction=elemento_contenido
                    if elemento_contenido.id_short=="ListOfSubscriptions": listOfMonitoringSubscriptions=ListOfMonitoringSubscriptions(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                    if elemento_contenido.id_short=="UpdateTime":updateTime=elemento_contenido
                qos_monitoring=QosMonitoring(general_key_performance_indicators,signal_level,parameters_pertaining_connections,qosQuery,subscriptionRequest,eventNotificationAction,listOfMonitoringSubscriptions,updateTime,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)
        
        
            elif(obj.identification.id==ue[10]):  #Location
                for elemento_contenido in obj:
                    if elemento_contenido.id_short=="XPosition":xPosition=elemento_contenido
                    if elemento_contenido.id_short=="YPosition":yPosition=elemento_contenido
                    if elemento_contenido.id_short=="ZPosition":zPosition=elemento_contenido 
                    if elemento_contenido.id_short=="Speed":speed=elemento_contenido
                    if elemento_contenido.id_short=="Acceleration":acceleration=elemento_contenido
                    if elemento_contenido.id_short=="LCSQosClass": lcsQosClass=elemento_contenido
                    if elemento_contenido.id_short=="Accuracy": accuracy=elemento_contenido
                    if elemento_contenido.id_short=="ResponseTime": responseTime=elemento_contenido
                    if elemento_contenido.id_short=="SubscriptionRequest": subscriptionRequest=elemento_contenido
                    if elemento_contenido.id_short=="EventNotificationAction": eventNotificationAction=elemento_contenido
                    if elemento_contenido.id_short=="ListOfSubscriptions": listOfLocalizationSubscriptions=ListOfLocalizationSubscriptions(elemento_contenido.id_short,elemento_contenido.value, elemento_contenido.category, elemento_contenido.description,
                                                                                                    elemento_contenido.parent, elemento_contenido.semantic_id, elemento_contenido.qualifier, elemento_contenido.kind)
                locationUE=LocationUE(xPosition, yPosition, zPosition,speed, acceleration, lcsQosClass, accuracy, responseTime,listOfLocalizationSubscriptions,subscriptionRequest,eventNotificationAction,obj.identification,obj.submodel_element,obj.id_short,obj.category,obj.description,obj.parent,obj.administration,obj.semantic_id,obj.qualifier,obj.kind)

    for obj in new_object_store:
        #Finally the AAS
        if isinstance(obj,AssetAdministrationShell):
            if obj.id_short==ue[12]:
                aasue5G=AASUE5G(ue5G,nameplate,identification,documentation,service,technicalData,simCard,ue5GIdentification,networkAccessRestrictions,ueAttachAndConnectionStatus,qos_monitoring, locationUE, ue5GDatasheet, obj.asset, obj.identification, obj.id_short, obj.category, obj.description, obj.parent, obj.administration, obj.security, obj.submodel, obj.concept_dictionary, obj.view, obj.derived_from)
                listOfUeAASs.append(aasue5G)
        

'''
