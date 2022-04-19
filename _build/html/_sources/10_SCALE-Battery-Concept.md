# SCALE Battery Concept

## Concept
Software architecture is based in one hand, on a master application managing most Devices, and on another hand, on several procedure executing the test (call instances);

<p align="center"> <img src="./images/Battery_Concept.png" style="width: 100%;" />

Objective is to keep all instances as identical as possible. Only some interfaces can change;
* BMS
* Specif devices.

A specific configuration (hardware connexion) can also be done for every instance.

## Configuration

### Component role

Quick overview of component role:

````{div} full-width

| Component                      |       | Master  | Inst.  | Description                                                                                                                                                                                                                        |
|--------------------------------|:-----:|:---------:|:--------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MANAGEMENT                     | *SCALE* |    **X**    |    **X**   | Global management of all SCALE and non SCALE component in the configuration. Must be in all configuration                                                                                                                          |
| CONTROL_MANAGEMENT.BATTERY     | *SCALE* |         |    **X**   | Management of the different control mode for battery;                                                                                                                                                                              |
| MEASUREMENT_MANAGEMENT.BATTERY | *SCALE* |         |    **X**   | Management of acquisition for battery;                                                                                                                                                                                             |
| MULTIINSTANCE_MANAGEMENT       | *SCALE* |    **X**    |        | Handling of the configuration (see below) and instances                                                                                                                                                                            |
| ACQUISITION                    |       |    **X**    |   (**X**)  | Component for "normed name" customer channels. This is the main place to define: Link to hardware channel Securities Calculation Acquisition plan                                                                                  |
| HARDWARE                       |       |    **X**    |        | Component to place hardware channels of the configuration. Act as a simple passive component to concentrate acquisition channels.                                                                                                  |
| Customer specific component    |       |    **X**    |   (**X**)  | All needed component for customer configuration, such as; PLC Barcode Various interface ...                                                                                                                                        |
| BMS                            | *SCALE* |         |    **X**   | Communication with the battery BMS, adressed either in CAN or FDX protocol. Frame given by SCALE architecture, but possibility to ADD new methods and channels if there is a need to add customer specific command (father method) |
| DUT                            | *SCALE* |         |    **X**   | DUT description. Frame given by SCALE architecture, but possibility to ADD new parameters if needed.                                                                                                                               |
| ENERGY_SYSTEM_SHARING          | *SCALE* | .MASTER | .SLAVE | Management of different ENERGY_SYSTEM; In link with the instance In regards to configuration                                                                                                                                       |
| ENERGY_SYSTEM_X                | *SCALE* |    **X**    |        | SCALE energy system devices                                                                                                                                                                                                        |
| CLIMATIC_CHAMBER_SHARING       | *SCALE* | .MASTER | .SLAVE | Management of different CLIMATIC_CHAMBER; In link with the instance In regards to configuration                                                                                                                                    |
| CLIMATIC_CHAMBER_X             | *SCALE* |    **X**    |        | SCALE climatic chamber devices                                                                                                                                                                                                     |
| COOLAND_COND_SHARING           | *SCALE* | .MASTER | .SLAVE | Management of different COOLAND_COND; In link with the instance In regards to configuration                                                                                                                                        |
| COOLAND_COND_X                 | *SCALE* |    **X**    |        | SCALE coolant conditionning devices                                                                                                                                                                                                |
| SCADA_CLIENT_MASTER            | *SCALE* |    **X**    |        | Can be used only with SCADA                                                                                                                                                                                                        |
| SCADA_CLIENT_INSTANCE          | *SCALE* |         |    **X**   | Can be used only with SCADA                                                                                                                                                                                                        |
````

### Hardware Configuration

Hardware configuration is not different when you have one instance that when you have several instances.

Just note that some MORPHEE® features are multi-instances compliant and some others not;
````{div} full-width

| Feature                                   | Multi-Instance Compatibility | Remark                                                                                                                        |
|-------------------------------------------|:------------------------------:|-------------------------------------------------------------------------------------------------------------------------------|
| Advanced >> ECU Connexion                 |             **X**            |                                                                                                                               |
| Communication >> CAN                      |               **X**              | Possibility to use one CAN channel from one board in one instance and another CAN channel from same board in another instance |
| Communication >> Custom (CSM)             |               **X**              |                                                                                                                               |
| Communication >> EtherCat                 |                              | To share Channels between instance, please have a look to Software Configuration                                              |
| Communication >> Ethernet (SLINK)         |               **X**              |                                                                                                                               |
| Communication >> **F**ast **D**ata E**X**change (**FDX**) |               **X**              |                                                                                                                               |
| Communication >> OBD                      |               ?              |                                                                                                                               |
| Communication >> PFB                      |               ?              |                                                                                                                               |
````

### Software configuration

#### Master and Instance configuration

````{div} full-width

| Master configuration (In Bench cfg)    | Instance 1 configuration (In Test cfg) | Instance n configuration (In Test cfg) |
|----------------------------------------|----------------------------------------|----------------------------------------|
| MANAGEMENT                             |               MANAGEMENT               |               MANAGEMENT               |
| MULTIINSTANCE_MANAGEMENT               |           CONTROL_MANAGEMENT           |           CONTROL_MANAGEMENT           |
| HARDWARE (*Specific*)                  |     MEASUREMENT_MANAGEMENT.BATTERY     |     MEASUREMENT_MANAGEMENT.BATTERY     |
| ACQUISITION (Global)                   |       ACQUISITION (for instance)       |       ACQUISITION (for instance)       |
|                                        |                   DUT                  |                   DUT                  |
|                                        |                   BMS                  |                   BMS                  |
| ENERGY_SYSTEM_SHARING.***MASTER***     |    ENERGY_SYSTEM_SHARING.***SLAVE***   |    ENERGY_SYSTEM_SHARING.***SLAVE***   |
| ENERGY_SYSTEM_1.*{real device}*        |                                        |                                        |
| ...                                    |                                        |                                        |
| ENERGY_SYSTEM_**X**.*{real device}*    |                                        |                                        |
| CLIMATIC_CHAMBER_SHARING.***MASTER***  | CLIMATIC_CHAMBER_SHARING.***SLAVE***   | CLIMATIC_CHAMBER_SHARING.***MASTER***  |
| CLIMATIC_CHAMBER_1.*{real device}*     |                                        |                                        |
| ...                                    |                                        |                                        |
| CLIMATIC_CHAMBER_**X**.*{real device}* |                                        |                                        |
| COOLANT_COND_SHARING.***MASTER***      | COOLANT_COND_SHARING.***SLAVE***       | COOLANT_COND_SHARING.***SLAVE***       |
| COOLANT_COND_1.*{real device}*         |                                        |                                        |
| ...                                    |                                        |                                        |
| COOLANT_COND_**X**.*{real device}*     |                                        |                                        |
````