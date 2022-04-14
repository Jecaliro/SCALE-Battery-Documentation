# Configuration of 'IniEditor'

![Ini Editor](./images/MO_Batterie_Config.png)

![Ini Editor](./images/MO_Batterie_selection.png)

```{code-block} python
[DB]
P_DUT.MANUFACTURER=TESLA
P_DUT.SERIAL_NUMBER=84MP-12Q
P_DUT.CAPACITY_NOM=22
P_DUT.CURRENT_NOM=133
P_DUT.CURRENT_MIN=0
P_DUT.CURRENT_MAX=135
P_DUT.CURRENT_CHARGE_MAX=120
P_DUT.CURRENT_DISCHARGE_MAX=-122
P_DUT.POWER_NOM=130
P_DUT.POWER_MIN=0
P_DUT.POWER_MAX=135
P_DUT.VOLTAGE_NOM=180
P_DUT.VOLTAGE_MAX=200
P_DUT.VOLTAGE_MIN=80
P_DUT.VOLTAGE_CHARGE_MAX=175
P_DUT.VOLTAGE_DISCHARGE_MAX=100
P_DUT.TYPE=1
P_DUT.ARCHITECTURE=2
P_DUT.TECHNOLOGY=0
P_DUT.DESCRIPTION=Demonstration batterie 1
P_DUT.OPERATING_TEMP_MIN=-10
P_DUT.OPERATING_TEMP_MAX=55
P_DUT.IDENTIFIER=EXEMPLE_BAT_T001
```

```{code-block} html
<?xml version="1.0" encoding="utf-8" ?>
<ConfigDesc>
	<Group Id="Battery">
		<Category Id="0 - General Configuration">
			<Property Section="DB" Field="P_DUT.MANUFACTURER" Type="NotEmptyString" DisplayName="Manufacturer" Description="Battery manufacturer" />
			<Property Section="DB" Field="P_DUT.SERIAL_NUMBER" Type="NotEmptyString" DisplayName="Serial number" Description="Battery serial number"/>
			<Property Section="DB" Field="P_DUT.IDENTIFIER" Type="NotEmptyString" DisplayName="Identifier" Description="Unique identifier"/>
			<Property Section="DB" Field="P_DUT.DESCRIPTION" Type="String" DisplayName="Description" Description="Free description field"/>
			<Property Section="DB" Field="P_DUT.TECHNOLOGY"  Type="Int[0,3]" DisplayName="Battery technology" Description="Battery technology" DefaultValue="1">
				<TypeConverter Localizable="false">
					<Value Value="0" DisplayValue="Lithium-ion" />
					<Value Value="1" DisplayValue="Lithium-sulphur" />
					<Value Value="2" DisplayValue="Aluminium-air" />
				</TypeConverter>
			</Property>
			<Property Section="DB" Field="P_DUT.TYPE"  Type="Int[0,2]" DisplayName="Battery type" Description="Battery type (A, B or C)" DefaultValue="1">
				<TypeConverter Localizable="false">
					<Value Value="0" DisplayValue="Type A" />
					<Value Value="1" DisplayValue="Type B" />
					<Value Value="2" DisplayValue="Type C" />
				</TypeConverter>
			</Property>
			<Property Section="DB" Field="P_DUT.ARCHITECTURE"  Type="Int[0,2]" DisplayName="Battery architecture" Description="Battery architecture (X, Y or Z)" DefaultValue="0">
				<TypeConverter Localizable="false">
					<Value Value="0" DisplayValue="Type X" />
					<Value Value="1" DisplayValue="Type Y" />
					<Value Value="2" DisplayValue="Type Z" />
				</TypeConverter>
			</Property>
		</Category>
		<Category Id="1 - Temperature">
			<Property Section="DB" Field="P_DUT.OPERATING_TEMP_MIN" Type="Int[-100,100]" DisplayName="Min operating temperature (°C)" Description="Minimum temperature" />
			<Property Section="DB" Field="P_DUT.OPERATING_TEMP_MAX" Type="Int[-100,100]" DisplayName="Max operating temperature (°C)" Description="Maximum temperature"/>
		</Category>
		<Category Id="2 - Capacity">
			<Property Section="DB" Field="P_DUT.CAPACITY_NOM" Type="Int[0,2000]" DisplayName="Nominal capacity (A.h)" Description="Battery capacity" />
		</Category>
		<Category Id="3 - Current">
			<Property Section="DB" Field="P_DUT.CURRENT_NOM" Type="Int[0,1000]" DisplayName="Nominal current (A)" Description="Battery nominal current" />
			<Property Section="DB" Field="P_DUT.CURRENT_MIN" Type="Int[0,1000]" DisplayName="Min current (A)" Description="Battery minimum current" />
			<Property Section="DB" Field="P_DUT.CURRENT_MAX" Type="Int[0,1000]" DisplayName="Max current (A)" Description="Battery maximum current" />
			<Property Section="DB" Field="P_DUT.CURRENT_CHARGE_MAX" Type="Int[0,1000]" DisplayName="Maximum Charge current (A)" Description="Maximum charge current" />
			<Property Section="DB" Field="P_DUT.CURRENT_DISCHARGE_MAX" Type="Int[-1000,0]" DisplayName="Maximum discharge current (A)" Description="Maximum discharge current" />
		</Category>
		<Category Id="4 - Voltage">
			<Property Section="DB" Field="P_DUT.VOLTAGE_NOM" Type="Int[0,1000]" DisplayName="Nominal voltage (V)" Description="Battery nominal voltage" />
			<Property Section="DB" Field="P_DUT.VOLTAGE_MIN" Type="Int[0,1000]" DisplayName="Min voltage (V)" Description="Battery minimum voltage" />
			<Property Section="DB" Field="P_DUT.VOLTAGE_MAX" Type="Int[0,1000]" DisplayName="Max voltage (V)" Description="Battery maximum voltage" />
			<Property Section="DB" Field="P_DUT.VOLTAGE_CHARGE_MAX" Type="Int[0,1000]" DisplayName="Maximum Charge voltage (V)" Description="Maximum charge voltage" />
			<Property Section="DB" Field="P_DUT.VOLTAGE_DISCHARGE_MAX" Type="Int[0,1000]" DisplayName="Maximum discharge voltage (V)" Description="Maximum discharge voltage" />
		</Category>
		<Category Id="5 - Power">
			<Property Section="DB" Field="P_DUT.POWER_NOM" Type="Int[0,1000]" DisplayName="Nominal power (kW)" Description="Battery nominal power" />
			<Property Section="DB" Field="P_DUT.POWER_MIN" Type="Int[0,1000]" DisplayName="Min power (kW)" Description="Battery minimum power" />
			<Property Section="DB" Field="P_DUT.POWER_MAX" Type="Int[0,1000]" DisplayName="Max power (kW)" Description="Battery maximum power" />
		</Category>
	</Group>
</ConfigDesc>
```

