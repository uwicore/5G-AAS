#Imports
from AAS5Gsubmodels import *       #Here we have the created structure for the AAS


#We need to import the AASs
from NW_5G_AAS import aasnw5G
from UE_5G_AAS import listOfUeAASs


#For make some prints to check it is imported correctly 
print(listOfUeAASs[0].id_short)
print(aasnw5G.id_short)
print(listOfUeAASs[0].location.xPosition.id_short)

print(listOfUeAASs[0].ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0])

#Changing some values in 5G_UE_AAS to understand how it works
listOfUeAASs[0].qosMonitoring.parametersPertainingConnections.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0].serviceBitRate.value=85
listOfUeAASs[0].ue5GIdentification.permanentEquipmentIdentifier.value=2976
listOfUeAASs[0].ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].linkDirection.value="Uplink"

#Same with network
aasnw5G.connectivity.uesAttachedList.uesAttached[0].gpsi.value=8427
aasnw5G.location.listOfConnectedUes.connectedUes[1].lcsQosClass="Best Effort"
aasnw5G.tsnCapabilities.bridge5GS.bridge5GSConfiguration.propagationDelayPerPort=8


'''
If you want to use a list of AAS contained in network we should use this commands 
            aasnw5G.add_ueAAS(listOfUeAASs[0])
            aasnw5G.add_ueAAS(listOfUeAASs[1])

If there is more than one 5G UE AAS you can use the list of Ues like these examples:
listOfUeAASs[1].qosMonitoring.updateTime.value=18
print(listOfUeAASs[1].qosMonitoring.generalKeyPerformanceIndicators.bler.value)
'''
