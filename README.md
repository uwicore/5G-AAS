# 5G-AAS
The 1st version of 5G AAS Python offers the python models for 5G UE AAS and 5G Network AAS. These python models are programmed using the Basyx-Python-SDK github. Previously, AAS models in .aasx format have been created using AASX Package Explorer github.
## Features
Reading AASX package files to create AAS objects in python.
Creating 5G UE AAS and 5G Network AAS templates in python following the [paper] model. Despite being able to create various 5G UE AAS instances, only one 5G Network AAS can be created.
## Project Structure
The 5G AAS Python have a similar structure that the basyx python sdk github. The active folder of the project is basyx/aas, where we can find the AAS models programming. In this folder we can find the 5G_UE_AAS.aasx and the 5G_Network_AAS.aasx models as templates. 

| File                         | Content                                                                                                                     |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| AASsubmodels.py                     | It will be the different classes that will be present in the python AAS created. This script inherits from the Basyx-Python-SDK classes.                |
| NW_5G_AAS.py                           | Script that will read the 5G_Network_AAS.aasx model and will create the 5G Network AAS model in python. It Should be executed from the basyx/aas folder.                                                                                                        |
| UE_5G_AAS.py   | Script that will read the 5G_UE_AAS.aasx model and will create the 5G UE AAS model in python. It Should be executed from the basyx/aas folder. 
| ExampleUse.py   | Script that will import the AAS createds in NW_5G_AAS.py and UE_5G_AAS.py and will show some examples of how they can be used. It Should be executed from the basyx/aas folder. 
| 5G_Network_AAS.aasx                           | 5G Network AAS model in an AASX file from AASX Package Explorer.                                                                                                         |
| UE_5G_AAS.aasx  | 5G UE AAS model in an AASX file from AASX Package Explorer. 

## Dependencies
The 5G AAS Python requires the following Python packages to be installed for production usage. These dependencies should be installed with pip:
*	Basyx-python-sdk
*	Math

## Getting Started
### Instalation
Clone this repository via download or via git clone.
Terminal commands needed in the python terminal for the creation of AAS.
```bash
pip install basyx-python-sdk
``` 
Complementary command for mathematic operations
```bash
pip install math
``` 
### Normal use
Terminal command for moving to the folder
```bash
cd basyx/aas
``` 
If you want to create just a 5G UE AAS and a 5G Network AAS instance, the scripts are already programmed with the default values of identification from the submodels and the AAS from the .aasx models. For this reason, the AAS will be already instanciated in ExampleUse.py and are ready for using in any other python script.

### Personalized use
If you want to create more than one AAS for the UE, you can use the AASX Package Explorer with the 5G_UE_AAS file. In Workspace/edit mode, click on the AAS and use "Copy," then in the "Administration Shells" section, choose "Paste into." Do the same with the asset in the "Assets" section and link it with the previous AAS. You should notice that it copies the AAS and the asset entirely, so they will have the same IRIs in the AAS, asset, and the submodels. To ensure each can be uniquely identified, it's necessary to change the IRIs of the AAS and the asset. Changing the IRIs of the submodels is not as direct. To do this, first copy the submodel in the "All Submodels" section, then in the new one, generate a new random IRI. After that, go to the new AAS, delete the "SubmodelReference" of the copied submodel, and then "Add existing." Select the submodel with the new IRI. Repeat this process for every submodel.

Once the AASX file is finished with all the 5G_UE_AAS instances desired, if multiple 5G_UE_AAS instances exist, modify the last part of the code in UE_5G_AAS.py. Replace the code meant for a single 5G_UE_AAS with the commented code, which despite being designed for two 5G_UE_AAS instances, it could easily be adapted to multiple instances. Also, update the imports in ExampleUse.py, replacing "aasue5G" with "listOfUeAASs," a list containing all the 5G_UE_AAS instances created before in AASX Package Explorer. Additionally, ExampleUse.py includes some commented usage examples of "listOfUeAASs" at the end of the file.


## Future versions
In future versions, additional functions will be included to streamline the utilization of our 5G_UE_AAS and 5G_NW_AAS structure. These functions will simplify the process of adding new PDU Sessions or QoS Flows, as well as deleting them. Furthermore, a function to assign QoS characteristics based on the 5QI standard outlined in 3GPP specification 23.501 will also be incorporated.
