#Imports
import copy         #To copy nested structures
from AASsubmodels import *       #Here we have the created structure for the AAS

#We need to import the AASs
from NW_5G_AAS import aasnw5G
from UE_5G_AAS import aasue5G


#For make some prints to check it is imported correctly 
print(aasue5G.id_short)
print(aasnw5G.id_short)
print(aasue5G.location.xPosition.id_short)

print(aasue5G.ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0])

#Changing some values in 5G_UE_AAS to understand how it works
aasue5G.qosMonitoring.parametersPertainingConnections.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0].serviceBitRate.value=85
aasue5G.ue5GIdentification.permanentEquipmentIdentifier.value=2976
aasue5G.ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].linkDirection.value="Uplink"

#Same with network
aasnw5G.connectivity.uesAttachedList.uesAttached[0].ueID.gpsi.value=8427
aasnw5G.location.listOfConnectedUes.connectedUes[1].lcsQosClass="Best Effort"
aasnw5G.tsnCapabilities.bridge5GS.parameters5GS.propagationDelayPerPort=8


'''
To use a list of AAS contained in network we should use this commands 
            aasnw5G.add_ueAAS(aasue5G)
            aasnw5G.add_ueAAS(aasue5G_2)


If you have more than one AAS you will need to use this command
from UE_5G_AAS import listOfUeAASs

Example of use of this list could be these:
print(listOfUeAASs[0].location.accuracy.id_short)
listOfUeAASs[1].qosMonitoring.updateTime.value=18

Another example is to use the functions with the list:
asign_qos_characteristics(listOfUeAASs[0],1,1)

'''