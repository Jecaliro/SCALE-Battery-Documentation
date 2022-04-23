# Interfacing with SCADA

The last possibility is to interface **SCALE Battery** with a **FlexLab®** database through the **SCADA** remote controller. In this case, SCADA installation has to be done before doing this configuration.

## Activate the direct access to FlexLab®

To activate the direct access to **FlexLab®**, you need to configure the MULTIINSTANCE_MANAGEMENT component:

![](./images/UEditor_MM_Configuration.png)

And select;
| Parameter           | Description                  | Value      |
|---------------------|------------------------------|------------:|
| P_MIM.DATA_HANDLING |   Management of parameters   | **By Flexlab** |
|  |      |  |


## Adding the component

To activate connection to the **SCADA**, you need:
1. Install the **SCADA** connector by installing folowing MNuGets: 
    - `Morphee.ScadaClient.Connector.Morphee`
    - `Morphee.ScadaClient`
2. Install and use the **SCADA** components by installing folowin MNuGets:
    - `Bench.Scale.SCADA_CLIENT_INSTANCE`
    - `Bench.Scale.SCADA_CLIENT_INSTANCE.BATTERY`
    - `Bench.Scale.SCADA_MASTER_INSTANCE`
    - `Bench.Scale.SCADA_MASTER_INSTANCE.BATTERY`

The `SCADA_MASTER_INSTANCE.BATTERY` has to be included in the Master instance configuration.

The `SCADA_CLIENT_INSTANCE.BATTERY` has to be included in all the others instance configuration.


## Configuration

Configuration is done through config files where you have to configure some fields.

### Server configuration

In `c:\Program Files\FEV\SCADA Client\FEV.Morphee.FlexLab.Framework.dll.config`, configure the server Url:

![](./images/SCADA_Cfg_server.png)

In `c:\Program Files\FEV\SCADA Client\FEV.Morphee.Scada.ScadaClient.exe.config`, configure the network insterface:

![](./images/SCADA_Cfg_Network.png)

### Climatic and channels configuration

In `c:\Program Files\FEV\SCADA Client\Plugins\FEV.Morphee.Scada.Plugins.Morphee.dll.config`, configure channels name and climatic chamber Name:

![](./images/SCADA_Cfg_Channels.png)

```{attention}
Of course, this configuration must meet;
- SCALE Battery configuration (quantity of channel & configuration)
- FlexLab configuration

If not, your configuration will not work properly

```

### Starting the SCADA Client Service

Communication with **SCADA** is done through the SCADA Client Service. Once configured, you have to start it manually and check that status is `Running`.

![](./images/SCADA_Start_Service.png)

You can also restart the computer.

Finaly, if everything is going well, you should see on SCADA side the Green light corresponding to the Cycler connection:

````{div} full-width
```{image} ./images/SCADA_Main_View.png
```
````