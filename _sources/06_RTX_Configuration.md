# RTX configuration

In the global configuration, RTX is a Keypoint becasue:
- It differs from a Single instance configuration
- It allows to specify on which RTX core you want to start which instance.
  
## RTX General configuration

The global RTX configuration is globally identical to the standard configuration except that, because of mutli-instance, Local memory pool and Expend size has to be increased as follow;

```{image} ./images/rtx_config.png
```
Another important point is the number of cores dedicated to RTX and to Windows.

As now, most of computers use several cores, it makes sense to share them between RTX and Windows. Actual experience shows that on a computer with 6 cores or more, **3 cores** can be dedicated to Windows. 

```{attention}
If you encounter any load issue on your computer, it makes sense to study where problems are (Windows side or RTX side), and modify configuration in regard.
```


 
## RTX Core assignation

Inside RTX world, there is also the possibility to distribute the load between the different cores. This can be done through `RTXCPUAssignment.exe`.
You can access this tool directly from **MORPHEE®** toolbar, or in **MORPHEE®** Bin directory:

```{image} ./images/rtx_cpu_assign.png
```
The tool diplay:
- All availble cores
- All available instances

Objective is now to share the load on the different cores, by drag & dropping instances.

General rules are:
- Master Instance is always the heaviest one, then try to dedicate a core to it. If not possible, try to minimize quantity of instances on this core.
- Globally distribute all instances on the others cores.

````{important}
Check that every instance configuration is using only one core:
```{image} ./images/rtx_one_core_cfg.png
```
````
