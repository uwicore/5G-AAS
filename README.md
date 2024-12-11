# 5G-AAS
This code implements the Asset Administration Shell (AAS) of a 5G User Equipment (UE) and the AAS of a 5G Network (NW) as presented in:

Jorge Gómez-Jerez, Jorge Cañete-Martín, M.Carmen Lucas-Estañ, Javier Gozalvez, “5G UE and Network Asset Administration Shells for the integration of 5G and Industry 4.0 Systems”, submitted to IEEE International Conference on Emerging Technologies and Factory Automation (ETFA 2024), 10th-13th September 2024, Padova, Italy.

The 5G AAS has been defined and implemented at the UWICORE laboratory of the Universidad Miguel Hernandez de Elche (Spain). 

The 5G AASs that we are releasing have been designed following the 5G-ACIA and Plattform Industrie 4.0 guidelines as well as 3GPP standards. They provide and expose the data and capabilities of 5G necessary to facilitate the integration of 5G with Industry 4.0 systems and applications.

We demonstrate the value and interest of this integration in this publication:
Jorge Cañete-Martín, Jorge Gómez-Jerez , M.Carmen Lucas-Estañ, Javier Gozalvez, Fernando Ubis, " Integration of 5G and Industrial Digital Models: A Case Study with AGVs ", IEEE International Conference on Emerging Technologies and Factory Automation (ETFA 2024), 10th-13th September 2024, Padova, Italy.

This paper shows how the integration of the 5G AASs with industrial digital models provide a powerful tool for analyzing how the deployment and configuration of 5G networks impact the operation and productivity of industrial processes, highlighting the importance and necessity of integrating 5G models into industrial digital models for their joint design and optimization. The industrial and 5G digital models are interconnected using OPC-UA, and we used the Visual Components software platform to build our industrial digital models.

In order to comply with our sponsor guidelines, we would appreciate if any publication using this code references the above-mentioned publication.

# Abstract
5G is a fundamental technology for the full digitalization of smart manufacturing. The use of Asset Administration Shells (AAS) can facilitate the integration of 5G with Industry 4.0 systems and applications while minimizing the complexities associated with the 5G network management. This study presents the design and implementation of the first full 5G system AAS that is openly released to the community. It includes a 5G UE (User Equipment) AAS and a 5G NW (network) AAS that have been designed following the 5G-ACIA guidelines as well as the Plattform Industrie 4.0 and 3GPP standards. The AASs have been defined to provide and expose the data and capabilities of 5G necessary to facilitate the integration of 5G with Industry 4.0 systems and applications.


## Features
This code creates 5G NW and UE AASs in python. The AASs has been defined following the 5G-ACIA guidelines as well as the Plattform Industrie 4.0 and 3GPP standards. 
This code uses the Basyx-Python-SDK. The repository also includes the aasx files of the 5G UW and NW AASs implemented in AASX Package Explorer. The code reads the AASs contained in aasx files previously created in AASX Package Explorer. 

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

# Contact 
Feel free to contact the corresponding authors M.Carmen Lucas-Estañ (m.lucas@umh.es) or Javier Gozálvez (j.gozalvez@umh.es) if you have any question about the code.
# Licence 
This code is protected under the GNU license.
# Acknowledgements
This work has been funded by European Union's Horizon Europe Research and Innovation programme under the Re4dy project (No 101058384), by MCIN/AEI/10.13039/ 501100011033 and the “European Union NextGenerationEU
/PRTR” (TED2021-130436B-I00) and by Generalitat Valenciana (CIGE/2022/17), and UMH’s Vicerrectorado de Investigación grants (VIPROAS23/11 and 2024).

