#!/usr/bin/env python
# coding: utf-8

# # General concept

# ## Multi-Instance... What is it?
# 
# MORPHEE multi-instance makes it possible to run a dedicated number of instances, independent the one from the others, in parallel on one computer. Then, each MORPHEE becomes a complete automation system, with its own acquisition, its own test procedure, its own dashboard, and its own alarms.
# 
# <p align="center"> <img src="./images/Multi-Instance-Global.png" style="width: 15%;" />
# 
# In order to ensure cohabitation, some functions allow to exchange data between the different instances, facilitating measurement, events and equipment sharing.
# 
# To consolidate multi-instance, a new concept of real time load balancing has been developed, allowing to take advantage of existing computer multi-core architecture.
# 

# ## Multi-Instance... Key points
# 
# * One MORPHEE master with **X** MORPHEE instances at the same time
#    * Independent testing procedure
#    * Independent alarms
#    * Independent logging
#    * Independent screens
# * Possibility to use different shared hardware by instance. For example, use of one CAN channels in one instance and another one in another instance. 
# * Possibility to share channels values between instances through shared memory.
# * Possibility to share events between instances for global synchronization, for example stop all instances, or pause all instances. 

# ## Multi-Instance... References
# 
# | Ref                 | Description                                                        |
# |---------------------|--------------------------------------------------------------------|
# | **SA-M64-MULTI-04** |  Possibility to start **1** Master Instance + **4** test instances |
# | **SA-M64-MULTI-08** |  Possibility to start **1** Master Instance + **8** test instances |
# | **SA-M64-MULTI-16** | Possibility to start **1** Master Instance + **16** test instances |
# | **SA-M64-MULTI-24** | Possibility to start **1** Master Instance + **24** test instances |
# | **SA-M64-MULTI-32** | Possibility to start **1** Master Instance + **32** test instances |

# ## Multi-Instance... Limitation
# 
# | Ref                        | Master | Instances |
# |----------------------------|--------|-----------|
# | **Up to 1 + 8 instances**  |  1 kHz | 1 kHz     |
# | **Up to 1 + 16 instances** | 500 Hz | 500 Hz    |
# | **Up to 1 + 32 instances** | 100 Hz | 100 Hz    |
# 
# > [!NOTE]
# > This limitations has been achieved with FEV 8 cores computer.
# 

# ## Software architecture
# 
# Software architecture is based in one hand, on a master application managing most Devices, and on another hand, on several procedure executing the test (call instances);
# 
# <p align="center"> <img src="./images/Battery_Concept.png" style="width: 100%;" />
# 
# Objective is to keep all instances as identical as possible. Only some interfaces can change;
# * BMS
# * Specif devices.
# 
# A specific configuration (hardware connexion) can also be done for every instance.

# ## Configuration
# 
# ### Component role
# 
# Quick overview of component role:
# 
# | Component                      |       | Master  | Inst.  | Description                                                                                                                                                                                                                        |
# |--------------------------------|-------|:---------:|:--------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
# | MANAGEMENT                     | SCALE |    X    |    X   | Global management of all SCALE and non SCALE component in the configuration. Must be in all configuration                                                                                                                          |
# | CONTROL_MANAGEMENT.BATTERY     | SCALE |         |    X   | Management of the different control mode for battery;                                                                                                                                                                              |
# | MEASUREMENT_MANAGEMENT.BATTERY | SCALE |         |    X   | Management of acquisition for battery;                                                                                                                                                                                             |
# | MULTIINSTANCE_MANAGEMENT       | SCALE |    X    |        | Handling of the configuration (see below) and instances                                                                                                                                                                            |
# | ACQUISITION                    |       |    X    |   (X)  | Component for "normed name" customer channels. This is the main place to define: Link to hardware channel Securities Calculation Acquisition plan                                                                                  |
# | HARDWARE                       |       |    X    |        | Component to place hardware channels of the configuration. Act as a simple passive component to concentrate acquisition channels.                                                                                                  |
# | Customer specific component    |       |    X    |   (X)  | All needed component for customer configuration, such as; PLC Barcode Various interface ...                                                                                                                                        |
# | BMS                            | SCALE |         |    X   | Communication with the battery BMS, adressed either in CAN or FDX protocol. Frame given by SCALE architecture, but possibility to ADD new methods and channels if there is a need to add customer specific command (father method) |
# | DUT                            | SCALE |         |    X   | DUT description. Frame given by SCALE architecture, but possibility to ADD new parameters if needed.                                                                                                                               |
# | ENERGY_SYSTEM_SHARING          | SCALE | .MASTER | .SLAVE | Management of different ENERGY_SYSTEM; In link with the instance In regards to configuration                                                                                                                                       |
# | ENERGY_SYSTEM_X                | SCALE |    X    |        | SCALE energy system devices                                                                                                                                                                                                        |
# | CLIMATIC_CHAMBER_SHARING       | SCALE | .MASTER | .SLAVE | Management of different CLIMATIC_CHAMBER; In link with the instance In regards to configuration                                                                                                                                    |
# | CLIMATIC_CHAMBER_X             | SCALE |    X    |        | SCALE climatic chamber devices                                                                                                                                                                                                     |
# | COOLAND_COND_SHARING           | SCALE | .MASTER | .SLAVE | Management of different COOLAND_COND; In link with the instance In regards to configuration                                                                                                                                        |
# | COOLAND_COND_X                 | SCALE |    X    |        | SCALE coolant conditionning devices                                                                                                                                                                                                |
# | SCADA_CLIENT_MASTER            | SCALE |    X    |        | Can be used only with SCADA                                                                                                                                                                                                        |
# | SCADA_CLIENT_INSTANCE          | SCALE |         |    X   | Can be used only with SCADA                                                                                                                                                                                                        |
# 

# ### Hardware Configuration
# 
# Hardware configuration is not different when you have one instance that when you have several instances.
# 
# Just note that some MORPHEE features are multi-instances compliant and some others not;
# 
# | Feature                                   | Multi-Instance Compatibility | Remark                                                                                                                        |
# |-------------------------------------------|:------------------------------:|-------------------------------------------------------------------------------------------------------------------------------|
# | Advanced >> ECU Connexion                 |             **X**            |                                                                                                                               |
# | Communication >> CAN                      |               X              | Possibility to use one CAN channel from one board in one instance and another CAN channel from same board in another instance |
# | Communication >> Custom (CSM)             |               X              |                                                                                                                               |
# | Communication >> EtherCat                 |                              | To share Channels between instance, please have a look to Software Configuration                                              |
# | Communication >> Ethernet (SLINK)         |               X              |                                                                                                                               |
# | Communication >> Fast Data Exchange (FDX) |               X              |                                                                                                                               |
# | Communication >> OBD                      |               ?              |                                                                                                                               |
# | Communication >> PFB                      |               ?              |                                                                                                                               |

# ### Software configuration
# 
# #### Master and Instance configuration
# 
# | Master configuration (In Bench cfg)    | Instance 1 configuration (In Test cfg) | Instance n configuration (In Test cfg) |
# |----------------------------------------|----------------------------------------|----------------------------------------|
# | MANAGEMENT                             |               MANAGEMENT               |               MANAGEMENT               |
# | MULTIINSTANCE_MANAGEMENT               |           CONTROL_MANAGEMENT           |           CONTROL_MANAGEMENT           |
# | HARDWARE (*Specific*)                  |     MEASUREMENT_MANAGEMENT.BATTERY     |     MEASUREMENT_MANAGEMENT.BATTERY     |
# | ACQUISITION (Global)                   |       ACQUISITION (for instance)       |       ACQUISITION (for instance)       |
# |                                        |                   DUT                  |                   DUT                  |
# |                                        |                   BMS                  |                   BMS                  |
# | ENERGY_SYSTEM_SHARING.***MASTER***     |    ENERGY_SYSTEM_SHARING.***SLAVE***   |    ENERGY_SYSTEM_SHARING.***SLAVE***   |
# | ENERGY_SYSTEM_1.*{real device}*        |                                        |                                        |
# | ...                                    |                                        |                                        |
# | ENERGY_SYSTEM_**X**.*{real device}*    |                                        |                                        |
# | CLIMATIC_CHAMBER_SHARING.***MASTER***  | CLIMATIC_CHAMBER_SHARING.***SLAVE***   | CLIMATIC_CHAMBER_SHARING.***MASTER***  |
# | CLIMATIC_CHAMBER_1.*{real device}*     |                                        |                                        |
# | ...                                    |                                        |                                        |
# | CLIMATIC_CHAMBER_**X**.*{real device}* |                                        |                                        |
# | COOLANT_COND_SHARING.***MASTER***      | COOLANT_COND_SHARING.***SLAVE***       | COOLANT_COND_SHARING.***SLAVE***       |
# | COOLANT_COND_1.*{real device}*         |                                        |                                        |
# | ...                                    |                                        |                                        |
# | COOLANT_COND_**X**.*{real device}*     |                                        |                                        |

# 
