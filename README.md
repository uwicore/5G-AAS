# 5G-AAS
This code implements the Asset Administration Shell (AAS) of a 5G User Equipment (UE) and the 5G Network (NW) presented in Jorge Gómez-Jerez, Jorge Cañete-Martín, M.Carmen Lucas-Estañ, Javier Gozalvez. Uwicore laboratory, Universidad Miguel Hernandez de Elche, Elche (Alicante), Spain, "5G UE and Network Asset Administration Shells for the integration of 5G and Industry 4.0 Systems," submitted for participation to IEEE ETFA 2024 - IEEE International Conference on Emerging Technologies and Factory Automation, 10th-13th September 2024, Padova, Italy.

This code has been developed using the Basyx-Python-SDK. Furthermore, you can also find in the repository the aasx files of the 5G UW and NW AASs implemented in AASX Package Explorer. 

In order to comply with our sponsor guidelines, we would appreciate if any publication using this code references the above-mentioned publication.
## Features
5G-AAS creates AAS models in python through reading aasx files created in AASX Package Explorer. This aasx files contains the models created following the principles defined in“5G UE and Network Asset Administration Shells for the integration of 5G and Industry 4.0 Systems”.
## Project Structure
The code from this repository mantains the folder structure of basyx python sdk because it is programmed using it. The main contribution is the code contained in the basyx/aas folder, where we can find the code programmed that will generate this AAS objects in python.
| File                         | Content                                                                                                                     |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| AAS5Gsubmodels.py                     | This script defines the different classes created for the Network and UE AAS programming like the UE5G or the Network5G classes. This classes inherits the Basyx python sdk classes.              |
| NW_5G_AAS.py                           | This script reads the 5G_Network_AAS.aasx file created with AASX Package Explorer and generates the 5G Network AAS python object.                                            |
| UE_5G_AAS.py   | This script reads the 5G_UE_AAS.aasx file created with AAS Package Explorer and generates the 5G UE AAS python object. It generates as many UEs as defined in the AASX file.                                         
| ExampleUse.py   | This script imports the Network and the UEs objects and provides examples of use of the AAS defined.
| 5G_Network_AAS.aasx                           | 5G Network AAS model in an AASX file from AASX Package Explorer.                                                                                                         |
| UE_5G_AAS.aasx  | 5G UE AAS model in an AASX file from AASX Package Explorer. 

## Dependencies
The 5G AAS Python requires the following Python packages to be installed for production usage. These dependencies should be installed with pip:
*	Basyx-python-sdk
*	Math

## Getting Started
### Installation
Clone this repository via download or via git clone.
Terminal commands needed in the python terminal for the creation of AAS.
```bash
pip install basyx-python-sdk
``` 
Complementary command for mathematic operations.
```bash
pip install math
``` 
### Example
Terminal command for moving to the folder
```bash
cd basyx/aas
``` 
If you want to create just a 5G UE AAS and a 5G Network AAS instance, the scripts are already programmed with the default values of identification from the submodels and the AAS from the .aasx models. For this reason, the AAS will be already instanciated in ExampleUse.py and it can be used in any other python script. 
Here we can see some examples of the code of ExampleUse.py. At first, we import the AASs, secondly we print some parameters of the AAS or even about some of their properties. Finally, we change values from some properties of the first 5G UE AAS (contained in listOfUeAASs) the and about the 5G Network AAS.

```python
#Imports
from AAS5Gsubmodels import *       #Here we have the created structure for the AAS
#We need to import the AASs
from NW_5G_AAS import aasnw5G
from UE_5G_AAS import listOfUeAASs
print(listOfUeAASs[0].id_short)
print(aasnw5G.id_short)
print(listOfUeAASs[0].ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0])
#Changing some values
listOfUeAASs[0].ue5GIdentification.permanentEquipmentIdentifier.value=2976
aasnw5G.connectivity.uesAttachedList.uesAttached[0].gpsi.value=8427
```

### Personalized use
The values and the valuetypes of properties must have a value when you personalize an AAS in AASX Package Explorer!
If you want to create more than one AAS for the UE, you can use the AASX Package Explorer with the 5G_UE_AAS file. In Workspace/edit mode, click on the AAS and use "Copy," then in the "Administration Shells" section, choose "Paste into." Do the same with the asset in the "Assets" section and link it with the previous AAS. You should notice that it copies the AAS and the asset entirely, so they will have the same IRIs in the AAS, asset, and the submodels. To ensure each can be uniquely identified, it's necessary to change the IRIs of the AAS and the asset. Changing the IRIs of the submodels is not as direct. To do this, first copy the submodel in the "All Submodels" section, then in the new one, generate a new random IRI. After that, go to the new AAS, delete the "SubmodelReference" of the copied submodel, and then "Add existing." Select the submodel with the new IRI. Repeat this process for every submodel.

Once the AASX file is finished with all the desired instances of 5G_UE_AAS, the code will adapt accordingly. The only difference will be that when using "listOfUeAASs", there will be more indexes, for example, "listOfUeAASs[1]". However, there are some examples of using this list commented below for better understanding.
