import ctypes

int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32

#constats

DAQmx_SelfCal_Supported = int32(0x1860) # Indicates whether the device supports self calibration.
DAQmx_SelfCal_LastTemp = int32(0x1864) # Indicates in degrees Celsius the temperature of the device at the time of the last self calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration.
DAQmx_ExtCal_RecommendedInterval                                 = int32(0x1868) # Indicates in months the National Instruments recommended interval between each external calibration of the device.
DAQmx_ExtCal_LastTemp                                            = int32(0x1867) # Indicates in degrees Celsius the temperature of the device at the time of the last external calibration. Compare this temperature to the current onboard temperature to determine if you should perform another calibration.
DAQmx_Cal_UserDefinedInfo                                        = int32(0x1861) # Specifies a string that contains arbitrary, user-defined information. This number of characters in this string can be no more than Max Size.
DAQmx_Cal_UserDefinedInfo_MaxSize                                = int32(0x191C) # Indicates the maximum length in characters of Information.
DAQmx_Cal_DevTemp                                                = int32(0x223B) # Indicates in degrees Celsius the current temperature of the device.

#********** Channel Attributes **********
DAQmx_ChanType                                                   = int32(0x187F) # Indicates the type of the virtual channel.
DAQmx_PhysicalChanName                                           = int32(0x18F5) # Indicates the name of the physical channel upon which this virtual channel is based.
DAQmx_ChanDescr                                                  = int32(0x1926) # Specifies a user-defined description for the channel.
DAQmx_AI_Max                                                     = int32(0x17DD) # Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the device can measure with the current settings.
DAQmx_AI_Min                                                     = int32(0x17DE) # Specifies the minimum value you expect to measure. This value is in the units you specify with a units property.  When you query this property, it returns the coerced minimum value that the device can measure with the current settings.
DAQmx_AI_CustomScaleName                                         = int32(0x17E0) # Specifies the name of a custom scale for the channel.
DAQmx_AI_MeasType                                                = int32(0x0695) # Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use.
DAQmx_AI_Voltage_Units                                           = int32(0x1094) # Specifies the units to use to return voltage measurements from the channel.
DAQmx_AI_Temp_Units                                              = int32(0x1033) # Specifies the units to use to return temperature measurements from the channel.
DAQmx_AI_Thrmcpl_Type                                            = int32(0x1050) # Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range.
DAQmx_AI_Thrmcpl_CJCSrc                                          = int32(0x1035) # Indicates the source of cold-junction compensation.
DAQmx_AI_Thrmcpl_CJCVal                                          = int32(0x1036) # Specifies the temperature of the cold junction if CJC Source is DAQmx_Val_ConstVal. Specify this value in the units of the measurement.
DAQmx_AI_Thrmcpl_CJCChan                                         = int32(0x1034) # Indicates the channel that acquires the temperature of the cold junction if CJC Source is DAQmx_Val_Chan. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius.
DAQmx_AI_RTD_Type                                                = int32(0x1032) # Specifies the type of RTD connected to the channel.
DAQmx_AI_RTD_R0                                                  = int32(0x1030) # Specifies in ohms the sensor resistance at 0 deg C. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value.
DAQmx_AI_RTD_A                                                   = int32(0x1010) # Specifies the 'A' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD.
DAQmx_AI_RTD_B                                                   = int32(0x1011) # Specifies the 'B' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD.
DAQmx_AI_RTD_C                                                   = int32(0x1013) # Specifies the 'C' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD.
DAQmx_AI_Thrmstr_A                                               = int32(0x18C9) # Specifies the 'A' constant of the Steinhart-Hart thermistor equation.
DAQmx_AI_Thrmstr_B                                               = int32(0x18CB) # Specifies the 'B' constant of the Steinhart-Hart thermistor equation.
DAQmx_AI_Thrmstr_C                                               = int32(0x18CA) # Specifies the 'C' constant of the Steinhart-Hart thermistor equation.
DAQmx_AI_Thrmstr_R1                                              = int32(0x1061) # Specifies in ohms the value of the reference resistor if you use voltage excitation. NI-DAQmx ignores this value for current excitation.
DAQmx_AI_ForceReadFromChan                                       = int32(0x18F8) # Specifies whether to read from the channel if it is a cold-junction compensation channel. By default, an NI-DAQmx Read function does not return data from cold-junction compensation channels.  Setting this property to TRUE forces read operations to return the cold-junction compensation channel data with the other channels in the task.
DAQmx_AI_Current_Units                                           = int32(0x0701) # Specifies the units to use to return current measurements from the channel.
DAQmx_AI_Strain_Units                                            = int32(0x0981) # Specifies the units to use to return strain measurements from the channel.
DAQmx_AI_StrainGage_GageFactor                                   = int32(0x0994) # Specifies the sensitivity of the strain gage.  Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value.
DAQmx_AI_StrainGage_PoissonRatio                                 = int32(0x0998) # Specifies the ratio of lateral strain to axial strain in the material you are measuring.
DAQmx_AI_StrainGage_Cfg                                          = int32(0x0982) # Specifies the bridge configuration of the strain gages.
DAQmx_AI_Resistance_Units                                        = int32(0x0955) # Specifies the units to use to return resistance measurements.
DAQmx_AI_Freq_Units                                              = int32(0x0806) # Specifies the units to use to return frequency measurements from the channel.
DAQmx_AI_Freq_ThreshVoltage                                      = int32(0x0815) # Specifies the voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.
DAQmx_AI_Freq_Hyst                                               = int32(0x0814) # Specifies in volts a window below Threshold Level. The input voltage must pass below Threshold Level minus this value before NI-DAQmx recognizes a waveform repetition at Threshold Level. Hysteresis can improve the measurement accuracy when the signal contains noise or jitter.
DAQmx_AI_LVDT_Units                                              = int32(0x0910) # Specifies the units to use to return linear position measurements from the channel.
DAQmx_AI_LVDT_Sensitivity                                        = int32(0x0939) # Specifies the sensitivity of the LVDT. This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value.
DAQmx_AI_LVDT_SensitivityUnits                                   = int32(0x219A) # Specifies the units of Sensitivity.
DAQmx_AI_RVDT_Units                                              = int32(0x0877) # Specifies the units to use to return angular position measurements from the channel.
DAQmx_AI_RVDT_Sensitivity                                        = int32(0x0903) # Specifies the sensitivity of the RVDT. This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value.
DAQmx_AI_RVDT_SensitivityUnits                                   = int32(0x219B) # Specifies the units of Sensitivity.
DAQmx_AI_SoundPressure_MaxSoundPressureLvl                       = int32(0x223A) # Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for Maximum Value and Minimum Value for the channel.
DAQmx_AI_SoundPressure_Units                                     = int32(0x1528) # Specifies the units to use to return sound pressure measurements from the channel.
DAQmx_AI_Microphone_Sensitivity                                  = int32(0x1536) # Specifies the sensitivity of the microphone. This value is in mV/Pa. Refer to the sensor documentation to determine this value.
DAQmx_AI_Accel_Units                                             = int32(0x0673) # Specifies the units to use to return acceleration measurements from the channel.
DAQmx_AI_Accel_Sensitivity                                       = int32(0x0692) # Specifies the sensitivity of the accelerometer. This value is in the units you specify with Sensitivity Units. Refer to the sensor documentation to determine this value.
DAQmx_AI_Accel_SensitivityUnits                                  = int32(0x219C) # Specifies the units of Sensitivity.
DAQmx_AI_TEDS_Units                                              = int32(0x21E0) # Indicates the units defined by TEDS information associated with the channel.
DAQmx_AI_Coupling                                                = int32(0x0064) # Specifies the coupling for the channel.
DAQmx_AI_Impedance                                               = int32(0x0062) # Specifies the input impedance of the channel.
DAQmx_AI_TermCfg                                                 = int32(0x1097) # Specifies the terminal configuration for the channel.
DAQmx_AI_InputSrc                                                = int32(0x2198) # Specifies the source of the channel. You can use the signal from the I/O connector or one of several calibration signals. Certain devices have a single calibration signal bus. For these devices, you must specify the same calibration signal for all channels you connect to a calibration signal.
DAQmx_AI_ResistanceCfg                                           = int32(0x1881) # Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD.
DAQmx_AI_LeadWireResistance                                      = int32(0x17EE) # Specifies in ohms the resistance of the wires that lead to the sensor.
DAQmx_AI_Bridge_Cfg                                              = int32(0x0087) # Specifies the type of Wheatstone bridge that the sensor is.
DAQmx_AI_Bridge_NomResistance                                    = int32(0x17EC) # Specifies in ohms the resistance across each arm of the bridge in an unloaded position.
DAQmx_AI_Bridge_InitialVoltage                                   = int32(0x17ED) # Specifies in volts the output voltage of the bridge in the unloaded condition. NI-DAQmx subtracts this value from any measurements before applying scaling equations.
DAQmx_AI_Bridge_ShuntCal_Enable                                  = int32(0x0094) # Specifies whether to enable a shunt calibration switch. Use Shunt Cal Select to select the switch(es) to enable.
DAQmx_AI_Bridge_ShuntCal_Select                                  = int32(0x21D5) # Specifies which shunt calibration switch(es) to enable.  Use Shunt Cal Enable to enable the switch(es) you specify with this property.
DAQmx_AI_Bridge_ShuntCal_GainAdjust                              = int32(0x193F) # Specifies the result of a shunt calibration. NI-DAQmx multiplies data read from the channel by the value of this property. This value should be close to 1.0.
DAQmx_AI_Bridge_Balance_CoarsePot                                = int32(0x17F1) # Specifies by how much to compensate for offset in the signal. This value can be between 0 and 127.
DAQmx_AI_Bridge_Balance_FinePot                                  = int32(0x18F4) # Specifies by how much to compensate for offset in the signal. This value can be between 0 and 4095.
DAQmx_AI_CurrentShunt_Loc                                        = int32(0x17F2) # Specifies the shunt resistor location for current measurements.
DAQmx_AI_CurrentShunt_Resistance                                 = int32(0x17F3) # Specifies in ohms the external shunt resistance for current measurements.
DAQmx_AI_Excit_Src                                               = int32(0x17F4) # Specifies the source of excitation.
DAQmx_AI_Excit_Val                                               = int32(0x17F5) # Specifies the amount of excitation that the sensor requires. If Voltage or Current is  DAQmx_Val_Voltage, this value is in volts. If Voltage or Current is  DAQmx_Val_Current, this value is in amperes.
DAQmx_AI_Excit_UseForScaling                                     = int32(0x17FC) # Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set this property to TRUE for ratiometric transducers. If you set this property to TRUE, set Maximum Value and Minimum Value to reflect the scaling.
DAQmx_AI_Excit_UseMultiplexed                                    = int32(0x2180) # Specifies if the SCXI-1122 multiplexes the excitation to the upper half of the channels as it advances through the scan list.
DAQmx_AI_Excit_ActualVal                                         = int32(0x1883) # Specifies the actual amount of excitation supplied by an internal excitation source.  If you read an internal excitation source more precisely with an external device, set this property to the value you read.  NI-DAQmx ignores this value for external excitation.
DAQmx_AI_Excit_DCorAC                                            = int32(0x17FB) # Specifies if the excitation supply is DC or AC.
DAQmx_AI_Excit_VoltageOrCurrent                                  = int32(0x17F6) # Specifies if the channel uses current or voltage excitation.
DAQmx_AI_ACExcit_Freq                                            = int32(0x0101) # Specifies the AC excitation frequency in Hertz.
DAQmx_AI_ACExcit_SyncEnable                                      = int32(0x0102) # Specifies whether to synchronize the AC excitation source of the channel to that of another channel. Synchronize the excitation sources of multiple channels to use multichannel sensors. Set this property to FALSE for the master channel and to TRUE for the slave channels.
DAQmx_AI_ACExcit_WireMode                                        = int32(0x18CD) # Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.
DAQmx_AI_Atten                                                   = int32(0x1801) # Specifies the amount of attenuation to use.
DAQmx_AI_Lowpass_Enable                                          = int32(0x1802) # Specifies whether to enable the lowpass filter of the channel.
DAQmx_AI_Lowpass_CutoffFreq                                      = int32(0x1803) # Specifies the frequency in Hertz that corresponds to the -3dB cutoff of the filter.
DAQmx_AI_Lowpass_SwitchCap_ClkSrc                                = int32(0x1884) # Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information.
DAQmx_AI_Lowpass_SwitchCap_ExtClkFreq                            = int32(0x1885) # Specifies the frequency of the external clock when you set Clock Source to DAQmx_Val_External.  NI-DAQmx uses this frequency to set the pre- and post- filters on the SCXI-1141, SCXI-1142, and SCXI-1143. On those devices, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer to the SCXI-1141/1142/1143 User Manual for more...
DAQmx_AI_Lowpass_SwitchCap_ExtClkDiv                             = int32(0x1886) # Specifies the divisor for the external clock when you set Clock Source to DAQmx_Val_External. On the SCXI-1141, SCXI-1142, and SCXI-1143, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer to the SCXI-1141/1142/1143 User Manual for more information.
DAQmx_AI_Lowpass_SwitchCap_OutClkDiv                             = int32(0x1887) # Specifies the divisor for the output clock.  NI-DAQmx uses the cutoff frequency to determine the output clock frequency. Refer to the SCXI-1141/1142/1143 User Manual for more information.
DAQmx_AI_ResolutionUnits                                         = int32(0x1764) # Indicates the units of Resolution Value.
DAQmx_AI_Resolution                                              = int32(0x1765) # Indicates the resolution of the analog-to-digital converter of the channel. This value is in the units you specify with Resolution Units.
DAQmx_AI_Dither_Enable                                           = int32(0x0068) # Specifies whether to enable dithering.  Dithering adds Gaussian noise to the input signal. You can use dithering to achieve higher resolution measurements by over sampling the input signal and averaging the results.
DAQmx_AI_Rng_High                                                = int32(0x1815) # Specifies the upper limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.
DAQmx_AI_Rng_Low                                                 = int32(0x1816) # Specifies the lower limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.
DAQmx_AI_Gain                                                    = int32(0x1818) # Specifies a gain factor to apply to the channel.
DAQmx_AI_SampAndHold_Enable                                      = int32(0x181A) # Specifies whether to enable the sample and hold circuitry of the device. When you disable sample and hold circuitry, a small voltage offset might be introduced into the signal.  You can eliminate this offset by using Auto Zero Mode to perform an auto zero on the channel.
DAQmx_AI_AutoZeroMode                                            = int32(0x1760) # Specifies when to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample.
DAQmx_AI_DataXferMech                                            = int32(0x1821) # Specifies the data transfer mode for the device.
DAQmx_AI_DataXferReqCond                                         = int32(0x188B) # Specifies under what condition to transfer data from the onboard memory of the device to the buffer.
DAQmx_AI_MemMapEnable                                            = int32(0x188C) # Specifies for NI-DAQmx to map hardware registers to the memory space of the customer process, if possible. Mapping to the memory space of the customer process increases performance. However, memory mapping can adversely affect the operation of the device and possibly result in a system crash if software in the process unintentionally accesses the mapped registers.
DAQmx_AI_DevScalingCoeff                                         = int32(0x1930) # Indicates the coefficients of a polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Each element of the array corresponds to a term of the equation. For example, if index two of the array is 4, the third term of the equation is 4x^2. Scaling coefficients do not account for any custom scales or sensors contained by the channel.
DAQmx_AO_Max                                                     = int32(0x1186) # Specifies the maximum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value larger than the maximum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a smaller value if other task settings restrict the device from generating the desired maximum.
DAQmx_AO_Min                                                     = int32(0x1187) # Specifies the minimum value you expect to generate. The value is in the units you specify with a units property. If you try to write a value smaller than the minimum value, NI-DAQmx generates an error. NI-DAQmx might coerce this value to a larger value if other task settings restrict the device from generating the desired minimum.
DAQmx_AO_CustomScaleName                                         = int32(0x1188) # Specifies the name of a custom scale for the channel.
DAQmx_AO_OutputType                                              = int32(0x1108) # Indicates whether the channel generates voltage or current.
DAQmx_AO_Voltage_Units                                           = int32(0x1184) # Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select.
DAQmx_AO_Current_Units                                           = int32(0x1109) # Specifies in what units to generate current on the channel. Write data to the channel is in the units you select.
DAQmx_AO_OutputImpedance                                         = int32(0x1490) # Specifies in ohms the impedance of the analog output stage of the device.
DAQmx_AO_LoadImpedance                                           = int32(0x0121) # Specifies in ohms the load impedance connected to the analog output channel.
DAQmx_AO_IdleOutputBehavior                                      = int32(0x2240) # Specifies the state of the channel when no generation is in progress.
DAQmx_AO_TermCfg                                                 = int32(0x188E) # Specifies the terminal configuration of the channel.
DAQmx_AO_ResolutionUnits                                         = int32(0x182B) # Specifies the units of Resolution Value.
DAQmx_AO_Resolution                                              = int32(0x182C) # Indicates the resolution of the digital-to-analog converter of the channel. This value is in the units you specify with Resolution Units.
DAQmx_AO_DAC_Rng_High                                            = int32(0x182E) # Specifies the upper limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.
DAQmx_AO_DAC_Rng_Low                                             = int32(0x182D) # Specifies the lower limit of the output range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.
DAQmx_AO_DAC_Ref_ConnToGnd                                       = int32(0x0130) # Specifies whether to ground the internal DAC reference. Grounding the internal DAC reference has the effect of grounding all analog output channels and stopping waveform generation across all analog output channels regardless of whether the channels belong to the current task. You can ground the internal DAC reference only when Source is DAQmx_Val_Internal and Allow Connecting DAC Reference to Ground at Runtime is...
DAQmx_AO_DAC_Ref_AllowConnToGnd                                  = int32(0x1830) # Specifies whether to allow grounding the internal DAC reference at run time. You must set this property to TRUE and set Source to DAQmx_Val_Internal before you can set Connect DAC Reference to Ground to TRUE.
DAQmx_AO_DAC_Ref_Src                                             = int32(0x0132) # Specifies the source of the DAC reference voltage. The value of this voltage source determines the full-scale value of the DAC.
DAQmx_AO_DAC_Ref_ExtSrc                                          = int32(0x2252) # Specifies the source of the DAC reference voltage if Source is DAQmx_Val_External.
DAQmx_AO_DAC_Ref_Val                                             = int32(0x1832) # Specifies in volts the value of the DAC reference voltage. This voltage determines the full-scale range of the DAC. Smaller reference voltages result in smaller ranges, but increased resolution.
DAQmx_AO_DAC_Offset_Src                                          = int32(0x2253) # Specifies the source of the DAC offset voltage. The value of this voltage source determines the full-scale value of the DAC.
DAQmx_AO_DAC_Offset_ExtSrc                                       = int32(0x2254) # Specifies the source of the DAC offset voltage if Source is DAQmx_Val_External.
DAQmx_AO_DAC_Offset_Val                                          = int32(0x2255) # Specifies in volts the value of the DAC offset voltage.
DAQmx_AO_ReglitchEnable                                          = int32(0x0133) # Specifies whether to enable reglitching.  The output of a DAC normally glitches whenever the DAC is updated with a new value. The amount of glitching differs from code to code and is generally largest at major code transitions.  Reglitching generates uniform glitch energy at each code transition and provides for more uniform glitches.  Uniform glitch energy makes it easier to filter out the noise introduced from g...
DAQmx_AO_InterpEnable                                            = int32(0x2241) # Specifies whether to enable the DAC interpolation filter. Disable the interpolation filter to improve DAC signal-to-noise ratio and reduce filter latency at the expense of degraded image rejection.
DAQmx_AO_Gain                                                    = int32(0x0118) # Specifies in decibels the gain factor to apply to the channel.
DAQmx_AO_UseOnlyOnBrdMem                                         = int32(0x183A) # Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs.
DAQmx_AO_DataXferMech                                            = int32(0x0134) # Specifies the data transfer mode for the device.
DAQmx_AO_DataXferReqCond                                         = int32(0x183C) # Specifies under what condition to transfer data from the buffer to the onboard memory of the device.
DAQmx_AO_MemMapEnable                                            = int32(0x188F) # Specifies if NI-DAQmx maps hardware registers to the memory space of the customer process, if possible. Mapping to the memory space of the customer process increases performance. However, memory mapping can adversely affect the operation of the device and possibly result in a system crash if software in the process unintentionally accesses the mapped registers.
DAQmx_AO_DevScalingCoeff                                         = int32(0x1931) # Indicates the coefficients of a linear equation that NI-DAQmx uses to scale values from a voltage to the native format of the device.  Each element of the array corresponds to a term of the equation. For example, if index two of the array is 4, the third term of the equation is 4x^2.  Scaling coefficients do not account for any custom scales that may be applied to the channel.
DAQmx_DI_InvertLines                                             = int32(0x0793) # Specifies whether to invert the lines in the channel. If you set this property to TRUE, the lines are at high logic when off and at low logic when on.
DAQmx_DI_NumLines                                                = int32(0x2178) # Indicates the number of digital lines in the channel.
DAQmx_DI_DigFltr_Enable                                          = int32(0x21D6) # Specifies whether to enable the digital filter for the line(s) or port(s). You can enable the filter on a line-by-line basis. You do not have to enable the filter for all lines in a channel.
DAQmx_DI_DigFltr_MinPulseWidth                                   = int32(0x21D7) # Specifies in seconds the minimum pulse width the filter recognizes as a valid high or low state transition.
DAQmx_DI_Tristate                                                = int32(0x1890) # Specifies whether to tristate the lines in the channel. If you set this property to TRUE, NI-DAQmx tristates the lines in the channel. If you set this property to FALSE, NI-DAQmx does not modify the configuration of the lines even if the lines were previously tristated. Set this property to FALSE to read lines in other tasks or to read output-only lines.
DAQmx_DI_DataXferMech                                            = int32(0x2263) # Specifies the data transfer mode for the device.
DAQmx_DI_DataXferReqCond                                         = int32(0x2264) # Specifies under what condition to transfer data from the onboard memory of the device to the buffer.
DAQmx_DO_InvertLines                                             = int32(0x1133) # Specifies whether to invert the lines in the channel. If you set this property to TRUE, the lines are at high logic when off and at low logic when on.
DAQmx_DO_NumLines                                                = int32(0x2179) # Indicates the number of digital lines in the channel.
DAQmx_DO_Tristate                                                = int32(0x18F3) # Specifies whether to stop driving the channel and set it to a Hi-Z state.
DAQmx_DO_UseOnlyOnBrdMem                                         = int32(0x2265) # Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory after you start the task. Onboard memory includes data FIFOs.
DAQmx_DO_DataXferMech                                            = int32(0x2266) # Specifies the data transfer mode for the device.
DAQmx_DO_DataXferReqCond                                         = int32(0x2267) # Specifies under what condition to transfer data from the buffer to the onboard memory of the device.
DAQmx_CI_Max                                                     = int32(0x189C) # Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings.
DAQmx_CI_Min                                                     = int32(0x189D) # Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings.
DAQmx_CI_CustomScaleName                                         = int32(0x189E) # Specifies the name of a custom scale for the channel.
DAQmx_CI_MeasType                                                = int32(0x18A0) # Indicates the measurement to take with the channel.
DAQmx_CI_Freq_Units                                              = int32(0x18A1) # Specifies the units to use to return frequency measurements.
DAQmx_CI_Freq_Term                                               = int32(0x18A2) # Specifies the input terminal of the signal to measure.
DAQmx_CI_Freq_StartingEdge                                       = int32(0x0799) # Specifies between which edges to measure the frequency of the signal.
DAQmx_CI_Freq_MeasMeth                                           = int32(0x0144) # Specifies the method to use to measure the frequency of the signal.
DAQmx_CI_Freq_MeasTime                                           = int32(0x0145) # Specifies in seconds the length of time to measure the frequency of the signal if Method is DAQmx_Val_HighFreq2Ctr. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement.
DAQmx_CI_Freq_Div                                                = int32(0x0147) # Specifies the value by which to divide the input signal if  Method is DAQmx_Val_LargeRng2Ctr. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement.
DAQmx_CI_Freq_DigFltr_Enable                                     = int32(0x21E7) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_Freq_DigFltr_MinPulseWidth                              = int32(0x21E8) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_Freq_DigFltr_TimebaseSrc                                = int32(0x21E9) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_Freq_DigFltr_TimebaseRate                               = int32(0x21EA) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_Freq_DigSync_Enable                                     = int32(0x21EB) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_Period_Units                                            = int32(0x18A3) # Specifies the unit to use to return period measurements.
DAQmx_CI_Period_Term                                             = int32(0x18A4) # Specifies the input terminal of the signal to measure.
DAQmx_CI_Period_StartingEdge                                     = int32(0x0852) # Specifies between which edges to measure the period of the signal.
DAQmx_CI_Period_MeasMeth                                         = int32(0x192C) # Specifies the method to use to measure the period of the signal.
DAQmx_CI_Period_MeasTime                                         = int32(0x192D) # Specifies in seconds the length of time to measure the period of the signal if Method is DAQmx_Val_HighFreq2Ctr. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement.
DAQmx_CI_Period_Div                                              = int32(0x192E) # Specifies the value by which to divide the input signal if Method is DAQmx_Val_LargeRng2Ctr. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement.
DAQmx_CI_Period_DigFltr_Enable                                   = int32(0x21EC) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_Period_DigFltr_MinPulseWidth                            = int32(0x21ED) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_Period_DigFltr_TimebaseSrc                              = int32(0x21EE) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_Period_DigFltr_TimebaseRate                             = int32(0x21EF) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_Period_DigSync_Enable                                   = int32(0x21F0) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_CountEdges_Term                                         = int32(0x18C7) # Specifies the input terminal of the signal to measure.
DAQmx_CI_CountEdges_Dir                                          = int32(0x0696) # Specifies whether to increment or decrement the counter on each edge.
DAQmx_CI_CountEdges_DirTerm                                      = int32(0x21E1) # Specifies the source terminal of the digital signal that controls the count direction if Direction is DAQmx_Val_ExtControlled.
DAQmx_CI_CountEdges_CountDir_DigFltr_Enable                      = int32(0x21F1) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_CountEdges_CountDir_DigFltr_MinPulseWidth               = int32(0x21F2) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseSrc                 = int32(0x21F3) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_CountEdges_CountDir_DigFltr_TimebaseRate                = int32(0x21F4) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_CountEdges_CountDir_DigSync_Enable                      = int32(0x21F5) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_CountEdges_InitialCnt                                   = int32(0x0698) # Specifies the starting value from which to count.
DAQmx_CI_CountEdges_ActiveEdge                                   = int32(0x0697) # Specifies on which edges to increment or decrement the counter.
DAQmx_CI_CountEdges_DigFltr_Enable                               = int32(0x21F6) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_CountEdges_DigFltr_MinPulseWidth                        = int32(0x21F7) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_CountEdges_DigFltr_TimebaseSrc                          = int32(0x21F8) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_CountEdges_DigFltr_TimebaseRate                         = int32(0x21F9) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_CountEdges_DigSync_Enable                               = int32(0x21FA) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_AngEncoder_Units                                        = int32(0x18A6) # Specifies the units to use to return angular position measurements from the channel.
DAQmx_CI_AngEncoder_PulsesPerRev                                 = int32(0x0875) # Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B.
DAQmx_CI_AngEncoder_InitialAngle                                 = int32(0x0881) # Specifies the starting angle of the encoder. This value is in the units you specify with Units.
DAQmx_CI_LinEncoder_Units                                        = int32(0x18A9) # Specifies the units to use to return linear encoder measurements from the channel.
DAQmx_CI_LinEncoder_DistPerPulse                                 = int32(0x0911) # Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with Units.
DAQmx_CI_LinEncoder_InitialPos                                   = int32(0x0915) # Specifies the position of the encoder when the measurement begins. This value is in the units you specify with Units.
DAQmx_CI_Encoder_DecodingType                                    = int32(0x21E6) # Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. DAQmx_Val_X1, DAQmx_Val_X2, and DAQmx_Val_X4 are valid for quadrature encoders only. DAQmx_Val_TwoPulseCounting is valid for two-pulse encoders only.
DAQmx_CI_Encoder_AInputTerm                                      = int32(0x219D) # Specifies the terminal to which signal A is connected.
DAQmx_CI_Encoder_AInput_DigFltr_Enable                           = int32(0x21FB) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_Encoder_AInput_DigFltr_MinPulseWidth                    = int32(0x21FC) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_Encoder_AInput_DigFltr_TimebaseSrc                      = int32(0x21FD) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_Encoder_AInput_DigFltr_TimebaseRate                     = int32(0x21FE) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_Encoder_AInput_DigSync_Enable                           = int32(0x21FF) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_Encoder_BInputTerm                                      = int32(0x219E) # Specifies the terminal to which signal B is connected.
DAQmx_CI_Encoder_BInput_DigFltr_Enable                           = int32(0x2200) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_Encoder_BInput_DigFltr_MinPulseWidth                    = int32(0x2201) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_Encoder_BInput_DigFltr_TimebaseSrc                      = int32(0x2202) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_Encoder_BInput_DigFltr_TimebaseRate                     = int32(0x2203) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_Encoder_BInput_DigSync_Enable                           = int32(0x2204) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_Encoder_ZInputTerm                                      = int32(0x219F) # Specifies the terminal to which signal Z is connected.
DAQmx_CI_Encoder_ZInput_DigFltr_Enable                           = int32(0x2205) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_Encoder_ZInput_DigFltr_MinPulseWidth                    = int32(0x2206) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_Encoder_ZInput_DigFltr_TimebaseSrc                      = int32(0x2207) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_Encoder_ZInput_DigFltr_TimebaseRate                     = int32(0x2208) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_Encoder_ZInput_DigSync_Enable                           = int32(0x2209) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_Encoder_ZIndexEnable                                    = int32(0x0890) # Specifies whether to use Z indexing for the channel.
DAQmx_CI_Encoder_ZIndexVal                                       = int32(0x0888) # Specifies the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with Z Index Phase. Specify this value in the units of the measurement.
DAQmx_CI_Encoder_ZIndexPhase                                     = int32(0x0889) # Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than DAQmx_Val_AHighBHigh.
DAQmx_CI_PulseWidth_Units                                        = int32(0x0823) # Specifies the units to use to return pulse width measurements.
DAQmx_CI_PulseWidth_Term                                         = int32(0x18AA) # Specifies the input terminal of the signal to measure.
DAQmx_CI_PulseWidth_StartingEdge                                 = int32(0x0825) # Specifies on which edge of the input signal to begin each pulse width measurement.
DAQmx_CI_PulseWidth_DigFltr_Enable                               = int32(0x220A) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_PulseWidth_DigFltr_MinPulseWidth                        = int32(0x220B) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_PulseWidth_DigFltr_TimebaseSrc                          = int32(0x220C) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_PulseWidth_DigFltr_TimebaseRate                         = int32(0x220D) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_PulseWidth_DigSync_Enable                               = int32(0x220E) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_TwoEdgeSep_Units                                        = int32(0x18AC) # Specifies the units to use to return two-edge separation measurements from the channel.
DAQmx_CI_TwoEdgeSep_FirstTerm                                    = int32(0x18AD) # Specifies the source terminal of the digital signal that starts each measurement.
DAQmx_CI_TwoEdgeSep_FirstEdge                                    = int32(0x0833) # Specifies on which edge of the first signal to start each measurement.
DAQmx_CI_TwoEdgeSep_First_DigFltr_Enable                         = int32(0x220F) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_TwoEdgeSep_First_DigFltr_MinPulseWidth                  = int32(0x2210) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_TwoEdgeSep_First_DigFltr_TimebaseSrc                    = int32(0x2211) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_TwoEdgeSep_First_DigFltr_TimebaseRate                   = int32(0x2212) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_TwoEdgeSep_First_DigSync_Enable                         = int32(0x2213) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_TwoEdgeSep_SecondTerm                                   = int32(0x18AE) # Specifies the source terminal of the digital signal that stops each measurement.
DAQmx_CI_TwoEdgeSep_SecondEdge                                   = int32(0x0834) # Specifies on which edge of the second signal to stop each measurement.
DAQmx_CI_TwoEdgeSep_Second_DigFltr_Enable                        = int32(0x2214) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_TwoEdgeSep_Second_DigFltr_MinPulseWidth                 = int32(0x2215) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_TwoEdgeSep_Second_DigFltr_TimebaseSrc                   = int32(0x2216) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_TwoEdgeSep_Second_DigFltr_TimebaseRate                  = int32(0x2217) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_TwoEdgeSep_Second_DigSync_Enable                        = int32(0x2218) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_SemiPeriod_Units                                        = int32(0x18AF) # Specifies the units to use to return semi-period measurements.
DAQmx_CI_SemiPeriod_Term                                         = int32(0x18B0) # Specifies the input terminal of the signal to measure.
DAQmx_CI_SemiPeriod_DigFltr_Enable                               = int32(0x2219) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_SemiPeriod_DigFltr_MinPulseWidth                        = int32(0x221A) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_SemiPeriod_DigFltr_TimebaseSrc                          = int32(0x221B) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_SemiPeriod_DigFltr_TimebaseRate                         = int32(0x221C) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_SemiPeriod_DigSync_Enable                               = int32(0x221D) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_CtrTimebaseSrc                                          = int32(0x0143) # Specifies the terminal of the timebase to use for the counter.
DAQmx_CI_CtrTimebaseRate                                         = int32(0x18B2) # Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can take measurements only in terms of ticks of the timebase.
DAQmx_CI_CtrTimebaseActiveEdge                                   = int32(0x0142) # Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge.
DAQmx_CI_CtrTimebase_DigFltr_Enable                              = int32(0x2271) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CI_CtrTimebase_DigFltr_MinPulseWidth                       = int32(0x2272) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CI_CtrTimebase_DigFltr_TimebaseSrc                         = int32(0x2273) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CI_CtrTimebase_DigFltr_TimebaseRate                        = int32(0x2274) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CI_CtrTimebase_DigSync_Enable                              = int32(0x2275) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CI_Count                                                   = int32(0x0148) # Indicates the current value of the count register.
DAQmx_CI_OutputState                                             = int32(0x0149) # Indicates the current state of the out terminal of the counter.
DAQmx_CI_TCReached                                               = int32(0x0150) # Indicates whether the counter rolled over. When you query this property, NI-DAQmx resets it to FALSE.
DAQmx_CI_CtrTimebaseMasterTimebaseDiv                            = int32(0x18B3) # Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to measure slower signals without causing the count register to roll over.
DAQmx_CI_DataXferMech                                            = int32(0x0200) # Specifies the data transfer mode for the channel.
DAQmx_CI_NumPossiblyInvalidSamps                                 = int32(0x193C) # Indicates the number of samples that the device might have overwritten before it could transfer them to the buffer.
DAQmx_CI_DupCountPrevent                                         = int32(0x21AC) # Specifies whether to enable duplicate count prevention for the channel.
DAQmx_CI_Prescaler                                               = int32(0x2239) # Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase.
DAQmx_CO_OutputType                                              = int32(0x18B5) # Indicates how to define pulses generated on the channel.
DAQmx_CO_Pulse_IdleState                                         = int32(0x1170) # Specifies the resting state of the output terminal.
DAQmx_CO_Pulse_Term                                              = int32(0x18E1) # Specifies on which terminal to generate pulses.
DAQmx_CO_Pulse_Time_Units                                        = int32(0x18D6) # Specifies the units in which to define high and low pulse time.
DAQmx_CO_Pulse_HighTime                                          = int32(0x18BA) # Specifies the amount of time that the pulse is at a high voltage. This value is in the units you specify with Units or when you create the channel.
DAQmx_CO_Pulse_LowTime                                           = int32(0x18BB) # Specifies the amount of time that the pulse is at a low voltage. This value is in the units you specify with Units or when you create the channel.
DAQmx_CO_Pulse_Time_InitialDelay                                 = int32(0x18BC) # Specifies in seconds the amount of time to wait before generating the first pulse.
DAQmx_CO_Pulse_DutyCyc                                           = int32(0x1176) # Specifies the duty cycle of the pulses. The duty cycle of a signal is the width of the pulse divided by period. NI-DAQmx uses this ratio and the pulse frequency to determine the width of the pulses and the delay between pulses.
DAQmx_CO_Pulse_Freq_Units                                        = int32(0x18D5) # Specifies the units in which to define pulse frequency.
DAQmx_CO_Pulse_Freq                                              = int32(0x1178) # Specifies the frequency of the pulses to generate. This value is in the units you specify with Units or when you create the channel.
DAQmx_CO_Pulse_Freq_InitialDelay                                 = int32(0x0299) # Specifies in seconds the amount of time to wait before generating the first pulse.
DAQmx_CO_Pulse_HighTicks                                         = int32(0x1169) # Specifies the number of ticks the pulse is high.
DAQmx_CO_Pulse_LowTicks                                          = int32(0x1171) # Specifies the number of ticks the pulse is low.
DAQmx_CO_Pulse_Ticks_InitialDelay                                = int32(0x0298) # Specifies the number of ticks to wait before generating the first pulse.
DAQmx_CO_CtrTimebaseSrc                                          = int32(0x0339) # Specifies the terminal of the timebase to use for the counter. Typically, NI-DAQmx uses one of the internal counter timebases when generating pulses. Use this property to specify an external timebase and produce custom pulse widths that are not possible using the internal timebases.
DAQmx_CO_CtrTimebaseRate                                         = int32(0x18C2) # Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to define output pulses in seconds rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can define output pulses only in ticks of the timebase.
DAQmx_CO_CtrTimebaseActiveEdge                                   = int32(0x0341) # Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge.
DAQmx_CO_CtrTimebase_DigFltr_Enable                              = int32(0x2276) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_CO_CtrTimebase_DigFltr_MinPulseWidth                       = int32(0x2277) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_CO_CtrTimebase_DigFltr_TimebaseSrc                         = int32(0x2278) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_CO_CtrTimebase_DigFltr_TimebaseRate                        = int32(0x2279) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_CO_CtrTimebase_DigSync_Enable                              = int32(0x227A) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_CO_Count                                                   = int32(0x0293) # Indicates the current value of the count register.
DAQmx_CO_OutputState                                             = int32(0x0294) # Indicates the current state of the output terminal of the counter.
DAQmx_CO_AutoIncrCnt                                             = int32(0x0295) # Specifies a number of timebase ticks by which to increment each successive pulse.
DAQmx_CO_CtrTimebaseMasterTimebaseDiv                            = int32(0x18C3) # Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to generate slower signals without causing the count register to roll over.
DAQmx_CO_PulseDone                                               = int32(0x190E) # Indicates if the task completed pulse generation. Use this value for retriggerable pulse generation when you need to determine if the device generated the current pulse. When you query this property, NI-DAQmx resets it to FALSE.
DAQmx_CO_Prescaler                                               = int32(0x226D) # Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase.

#********** Export Signal Attributes **********
DAQmx_Exported_AIConvClk_OutputTerm                              = int32(0x1687) # Specifies the terminal to which to route the AI Convert Clock.
DAQmx_Exported_AIConvClk_Pulse_Polarity                          = int32(0x1688) # Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock.
DAQmx_Exported_10MHzClk_OutputTerm                               = int32(0x226E) # Specifies the terminal to which to route the 10MHz Clock.
DAQmx_Exported_20MHzTimebase_OutputTerm                          = int32(0x1657) # Specifies the terminal to which to route the 20MHz Timebase.
DAQmx_Exported_SampClk_OutputBehavior                            = int32(0x186B) # Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample.
DAQmx_Exported_SampClk_OutputTerm                                = int32(0x1663) # Specifies the terminal to which to route the Sample Clock.
DAQmx_Exported_SampClkTimebase_OutputTerm                        = int32(0x18F9) # Specifies the terminal to which to route the Sample Clock Timebase.
DAQmx_Exported_DividedSampClkTimebase_OutputTerm                 = int32(0x21A1) # Specifies the terminal to which to route the Divided Sample Clock Timebase.
DAQmx_Exported_AdvTrig_OutputTerm                                = int32(0x1645) # Specifies the terminal to which to route the Advance Trigger.
DAQmx_Exported_AdvTrig_Pulse_Polarity                            = int32(0x1646) # Indicates the polarity of the exported Advance Trigger.
DAQmx_Exported_AdvTrig_Pulse_WidthUnits                          = int32(0x1647) # Specifies the units of Width Value.
DAQmx_Exported_AdvTrig_Pulse_Width                               = int32(0x1648) # Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with Width Units.
DAQmx_Exported_RefTrig_OutputTerm                                = int32(0x0590) # Specifies the terminal to which to route the Reference Trigger.
DAQmx_Exported_StartTrig_OutputTerm                              = int32(0x0584) # Specifies the terminal to which to route the Start Trigger.
DAQmx_Exported_AdvCmpltEvent_OutputTerm                          = int32(0x1651) # Specifies the terminal to which to route the Advance Complete Event.
DAQmx_Exported_AdvCmpltEvent_Delay                               = int32(0x1757) # Specifies the output signal delay in periods of the sample clock.
DAQmx_Exported_AdvCmpltEvent_Pulse_Polarity                      = int32(0x1652) # Specifies the polarity of the exported Advance Complete Event.
DAQmx_Exported_AdvCmpltEvent_Pulse_Width                         = int32(0x1654) # Specifies the width of the exported Advance Complete Event pulse.
DAQmx_Exported_AIHoldCmpltEvent_OutputTerm                       = int32(0x18ED) # Specifies the terminal to which to route the AI Hold Complete Event.
DAQmx_Exported_AIHoldCmpltEvent_PulsePolarity                    = int32(0x18EE) # Specifies the polarity of an exported AI Hold Complete Event pulse.
DAQmx_Exported_ChangeDetectEvent_OutputTerm                      = int32(0x2197) # Specifies the terminal to which to route the Change Detection Event.
DAQmx_Exported_CtrOutEvent_OutputTerm                            = int32(0x1717) # Specifies the terminal to which to route the Counter Output Event.
DAQmx_Exported_CtrOutEvent_OutputBehavior                        = int32(0x174F) # Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.
DAQmx_Exported_CtrOutEvent_Pulse_Polarity                        = int32(0x1718) # Specifies the polarity of the pulses at the output terminal of the counter when Output Behavior is DAQmx_Val_Pulse. NI-DAQmx ignores this property if Output Behavior is DAQmx_Val_Toggle.
DAQmx_Exported_CtrOutEvent_Toggle_IdleState                      = int32(0x186A) # Specifies the initial state of the output terminal of the counter when Output Behavior is DAQmx_Val_Toggle. The terminal enters this state when NI-DAQmx commits the task.
DAQmx_Exported_SyncPulseEvent_OutputTerm                         = int32(0x223C) # Specifies the terminal to which to route the Synchronization Pulse Event.
DAQmx_Exported_WatchdogExpiredEvent_OutputTerm                   = int32(0x21AA) # Specifies the terminal  to which to route the Watchdog Timer Expired Event.

#********** Device Attributes **********
DAQmx_Dev_ProductType                                            = int32(0x0631) # Indicates the product name of the device.
DAQmx_Dev_SerialNum                                              = int32(0x0632) # Indicates the serial number of the device. This value is zero if the device does not have a serial number.

#********** Read Attributes **********
DAQmx_Read_RelativeTo                                            = int32(0x190A) # Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with Offset, the read operation begins at that offset relative to the point you select with this property. The default value is DAQmx_Val_CurrReadPos unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is DAQmx_Val_FirstPretrigSamp.
DAQmx_Read_Offset                                                = int32(0x190B) # Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with RelativeTo.
DAQmx_Read_ChannelsToRead                                        = int32(0x1823) # Specifies a subset of channels in the task from which to read.
DAQmx_Read_ReadAllAvailSamp                                      = int32(0x1215) # Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer.
DAQmx_Read_AutoStart                                             = int32(0x1826) # Specifies if an NI-DAQmx Read function automatically starts the task  if you did not start the task explicitly by using DAQmxStartTask(). The default value is TRUE. When  an NI-DAQmx Read function starts a finite acquisition task, it also stops the task after reading the last sample.
DAQmx_Read_OverWrite                                             = int32(0x1211) # Specifies whether to overwrite samples in the buffer that you have not yet read.
DAQmx_Read_CurrReadPos                                           = int32(0x1221) # Indicates in samples per channel the current position in the buffer.
DAQmx_Read_AvailSampPerChan                                      = int32(0x1223) # Indicates the number of samples available to read per channel. This value is the same for all channels in the task.
DAQmx_Read_TotalSampPerChanAcquired                              = int32(0x192A) # Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels.
DAQmx_Read_OverloadedChansExist                                  = int32(0x2174) # Indicates if the device detected an overload in any channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read Overloaded Channels. Otherwise, you will receive an error.
DAQmx_Read_OverloadedChans                                       = int32(0x2175) # Indicates the names of any overloaded virtual channels in the task. You must read Overloaded Channels Exist before you read this property. Otherwise, you will receive an error.
DAQmx_Read_ChangeDetect_HasOverflowed                            = int32(0x2194) # Indicates if samples were missed because change detection events occurred faster than the device could handle them. Some devices detect overflows differently than others.
DAQmx_Read_RawDataWidth                                          = int32(0x217A) # Indicates in bytes the size of a raw sample from the task.
DAQmx_Read_NumChans                                              = int32(0x217B) # Indicates the number of channels that an NI-DAQmx Read function reads from the task. This value is the number of channels in the task or the number of channels you specify with Channels to Read.
DAQmx_Read_DigitalLines_BytesPerChan                             = int32(0x217C) # Indicates the number of bytes per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra bytes are FALSE.
DAQmx_ReadWaitMode                                               = int32(0x2232) # Specifies how an NI-DAQmx Read function waits for samples to become available.

#********** Switch Channel Attributes **********
DAQmx_SwitchChan_Usage                                           = int32(0x18E4) # Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.
DAQmx_SwitchChan_MaxACCarryCurrent                               = int32(0x0648) # Indicates in amperes the maximum AC current that the device can carry.
DAQmx_SwitchChan_MaxACSwitchCurrent                              = int32(0x0646) # Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level.
DAQmx_SwitchChan_MaxACCarryPwr                                   = int32(0x0642) # Indicates in watts the maximum AC power that the device can carry.
DAQmx_SwitchChan_MaxACSwitchPwr                                  = int32(0x0644) # Indicates in watts the maximum AC power that the device can switch.
DAQmx_SwitchChan_MaxDCCarryCurrent                               = int32(0x0647) # Indicates in amperes the maximum DC current that the device can carry.
DAQmx_SwitchChan_MaxDCSwitchCurrent                              = int32(0x0645) # Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level.
DAQmx_SwitchChan_MaxDCCarryPwr                                   = int32(0x0643) # Indicates in watts the maximum DC power that the device can carry.
DAQmx_SwitchChan_MaxDCSwitchPwr                                  = int32(0x0649) # Indicates in watts the maximum DC power that the device can switch.
DAQmx_SwitchChan_MaxACVoltage                                    = int32(0x0651) # Indicates in volts the maximum AC RMS voltage that the device can switch.
DAQmx_SwitchChan_MaxDCVoltage                                    = int32(0x0650) # Indicates in volts the maximum DC voltage that the device can switch.
DAQmx_SwitchChan_WireMode                                        = int32(0x18E5) # Indicates the number of wires that the channel switches.
DAQmx_SwitchChan_Bandwidth                                       = int32(0x0640) # Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration.
DAQmx_SwitchChan_Impedance                                       = int32(0x0641) # Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads.

#********** Switch Device Attributes **********
DAQmx_SwitchDev_SettlingTime                                     = int32(0x1244) # Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times.
DAQmx_SwitchDev_AutoConnAnlgBus                                  = int32(0x17DA) # Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property.
DAQmx_SwitchDev_Settled                                          = int32(0x1243) # Indicates when Settling Time expires.
DAQmx_SwitchDev_RelayList                                        = int32(0x17DC) # Indicates a comma-delimited list of relay names.
DAQmx_SwitchDev_NumRelays                                        = int32(0x18E6) # Indicates the number of relays on the device. This value matches the number of relay names in Relay List.
DAQmx_SwitchDev_SwitchChanList                                   = int32(0x18E7) # Indicates a comma-delimited list of channel names for the current topology of the device.
DAQmx_SwitchDev_NumSwitchChans                                   = int32(0x18E8) # Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in Switch Channel List.
DAQmx_SwitchDev_NumRows                                          = int32(0x18E9) # Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology.
DAQmx_SwitchDev_NumColumns                                       = int32(0x18EA) # Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology.
DAQmx_SwitchDev_Topology                                         = int32(0x193D) # Indicates the current topology of the device. This value is one of the topology options in DAQmxSwitchSetTopologyAndReset().

#********** Switch Scan Attributes **********
DAQmx_SwitchScan_BreakMode                                       = int32(0x1247) # Specifies the break mode between each entry in a scan list.
DAQmx_SwitchScan_RepeatMode                                      = int32(0x1248) # Specifies if the task advances through the scan list multiple times.
DAQmx_SwitchScan_WaitingForAdv                                   = int32(0x17D9) # Indicates if the switch hardware is waiting for an  Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list.

#********** Scale Attributes **********
DAQmx_Scale_Descr                                                = int32(0x1226) # Specifies a description for the scale.
DAQmx_Scale_ScaledUnits                                          = int32(0x191B) # Specifies the units to use for scaled values. You can use an arbitrary string.
DAQmx_Scale_PreScaledUnits                                       = int32(0x18F7) # Specifies the units of the values that you want to scale.
DAQmx_Scale_Type                                                 = int32(0x1929) # Indicates the method or equation form that the custom scale uses.
DAQmx_Scale_Lin_Slope                                            = int32(0x1227) # Specifies the slope, m, in the equation y=mx+b.
DAQmx_Scale_Lin_YIntercept                                       = int32(0x1228) # Specifies the y-intercept, b, in the equation y=mx+b.
DAQmx_Scale_Map_ScaledMax                                        = int32(0x1229) # Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to Pre-Scaled Maximum Value. Reads clip samples that are larger than this value. Writes generate errors for samples that are larger than this value.
DAQmx_Scale_Map_PreScaledMax                                     = int32(0x1231) # Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to Scaled Maximum Value.
DAQmx_Scale_Map_ScaledMin                                        = int32(0x1230) # Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to Pre-Scaled Minimum Value. Reads clip samples that are smaller than this value. Writes generate errors for samples that are smaller than this value.
DAQmx_Scale_Map_PreScaledMin                                     = int32(0x1232) # Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to Scaled Minimum Value.
DAQmx_Scale_Poly_ForwardCoeff                                    = int32(0x1234) # Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.
DAQmx_Scale_Poly_ReverseCoeff                                    = int32(0x1235) # Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3.
DAQmx_Scale_Table_ScaledVals                                     = int32(0x1236) # Specifies an array of scaled values. These values map directly to the values in Pre-Scaled Values.
DAQmx_Scale_Table_PreScaledVals                                  = int32(0x1237) # Specifies an array of pre-scaled values. These values map directly to the values in Scaled Values.

#********** System Attributes **********
DAQmx_Sys_GlobalChans                                            = int32(0x1265) # Indicates an array that contains the names of all global channels saved on the system.
DAQmx_Sys_Scales                                                 = int32(0x1266) # Indicates an array that contains the names of all custom scales saved on the system.
DAQmx_Sys_Tasks                                                  = int32(0x1267) # Indicates an array that contains the names of all tasks saved on the system.
DAQmx_Sys_DevNames                                               = int32(0x193B) # Indicates an array that contains the names of all devices installed in the system.
DAQmx_Sys_NIDAQMajorVersion                                      = int32(0x1272) # Indicates the major portion of the installed version of NI-DAQ, such as 7 for version 7.0.
DAQmx_Sys_NIDAQMinorVersion                                      = int32(0x1923) # Indicates the minor portion of the installed version of NI-DAQ, such as 0 for version 7.0.

#********** Task Attributes **********
DAQmx_Task_Name                                                  = int32(0x1276) # Indicates the name of the task.
DAQmx_Task_Channels                                              = int32(0x1273) # Indicates the names of all virtual channels in the task.
DAQmx_Task_NumChans                                              = int32(0x2181) # Indicates the number of virtual channels in the task.
DAQmx_Task_Complete                                              = int32(0x1274) # Indicates whether the task completed execution.

#********** Timing Attributes **********
DAQmx_SampQuant_SampMode                                         = int32(0x1300) # Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples.
DAQmx_SampQuant_SampPerChan                                      = int32(0x1310) # Specifies the number of samples to acquire or generate for each channel if Sample Mode is finite.
DAQmx_SampTimingType                                             = int32(0x1347) # Specifies the type of sample timing to use for the task.
DAQmx_SampClk_Rate                                               = int32(0x1344) # Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.
DAQmx_SampClk_Src                                                = int32(0x1852) # Specifies the terminal of the signal to use as the Sample Clock.
DAQmx_SampClk_ActiveEdge                                         = int32(0x1301) # Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.
DAQmx_SampClk_TimebaseDiv                                        = int32(0x18EB) # Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse.
DAQmx_SampClk_Timebase_Rate                                      = int32(0x1303) # Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters.
DAQmx_SampClk_Timebase_Src                                       = int32(0x1308) # Specifies the terminal of the signal to use as the Sample Clock Timebase.
DAQmx_SampClk_Timebase_ActiveEdge                                = int32(0x18EC) # Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.
DAQmx_SampClk_Timebase_MasterTimebaseDiv                         = int32(0x1305) # Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase.
DAQmx_SampClk_DigFltr_Enable                                     = int32(0x221E) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_SampClk_DigFltr_MinPulseWidth                              = int32(0x221F) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_SampClk_DigFltr_TimebaseSrc                                = int32(0x2220) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_SampClk_DigFltr_TimebaseRate                               = int32(0x2221) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_SampClk_DigSync_Enable                                     = int32(0x2222) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_ChangeDetect_DI_RisingEdgePhysicalChans                    = int32(0x2195) # Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports.
DAQmx_ChangeDetect_DI_FallingEdgePhysicalChans                   = int32(0x2196) # Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports.
DAQmx_OnDemand_SimultaneousAOEnable                              = int32(0x21A0) # Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel.
DAQmx_AIConv_Rate                                                = int32(0x1848) # Specifies the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of an E Series device.
DAQmx_AIConv_Src                                                 = int32(0x1502) # Specifies the terminal of the signal to use as the AI Convert Clock.
DAQmx_AIConv_ActiveEdge                                          = int32(0x1853) # Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.
DAQmx_AIConv_TimebaseDiv                                         = int32(0x1335) # Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse.
DAQmx_AIConv_Timebase_Src                                        = int32(0x1339) # Specifies the terminal  of the signal to use as the AI Convert Clock Timebase.
DAQmx_MasterTimebase_Rate                                        = int32(0x1495) # Specifies the rate of the Master Timebase.
DAQmx_MasterTimebase_Src                                         = int32(0x1343) # Specifies the terminal of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal.
DAQmx_RefClk_Rate                                                = int32(0x1315) # Specifies the frequency of the Reference Clock.
DAQmx_RefClk_Src                                                 = int32(0x1316) # Specifies the terminal of the signal to use as the Reference Clock.
DAQmx_SyncPulse_Src                                              = int32(0x223D) # Specifies the terminal of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device.
DAQmx_SyncPulse_SyncTime                                         = int32(0x223E) # Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse.
DAQmx_SyncPulse_MinDelayToStart                                  = int32(0x223F) # Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts.
DAQmx_DelayFromSampClk_DelayUnits                                = int32(0x1304) # Specifies the units of Delay.
DAQmx_DelayFromSampClk_Delay                                     = int32(0x1317) # Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with Delay Units.

#********** Trigger Attributes **********
DAQmx_StartTrig_Type                                             = int32(0x1393) # Specifies the type of trigger to use to start a task.
DAQmx_DigEdge_StartTrig_Src                                      = int32(0x1407) # Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger.
DAQmx_DigEdge_StartTrig_Edge                                     = int32(0x1404) # Specifies on which edge of a digital pulse to start acquiring or generating samples.
DAQmx_DigEdge_StartTrig_DigFltr_Enable                           = int32(0x2223) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_DigEdge_StartTrig_DigFltr_MinPulseWidth                    = int32(0x2224) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_DigEdge_StartTrig_DigFltr_TimebaseSrc                      = int32(0x2225) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_DigEdge_StartTrig_DigFltr_TimebaseRate                     = int32(0x2226) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_DigEdge_StartTrig_DigSync_Enable                           = int32(0x2227) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_AnlgEdge_StartTrig_Src                                     = int32(0x1398) # Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger.
DAQmx_AnlgEdge_StartTrig_Slope                                   = int32(0x1397) # Specifies on which slope of the trigger signal to start acquiring or generating samples.
DAQmx_AnlgEdge_StartTrig_Lvl                                     = int32(0x1396) # Specifies at what threshold in the units of the measurement or generation to start acquiring or generating samples. Use Slope to specify on which slope to trigger on this threshold.
DAQmx_AnlgEdge_StartTrig_Hyst                                    = int32(0x1395) # Specifies a hysteresis level in the units of the measurement or generation. If Slope is DAQmx_Val_RisingSlope, the trigger does not deassert until the source signal passes below  Level minus the hysteresis. If Slope is DAQmx_Val_FallingSlope, the trigger does not deassert until the source signal passes above Level plus the hysteresis.
DAQmx_AnlgEdge_StartTrig_Coupling                                = int32(0x2233) # Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.
DAQmx_AnlgWin_StartTrig_Src                                      = int32(0x1400) # Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Start Trigger.
DAQmx_AnlgWin_StartTrig_When                                     = int32(0x1401) # Specifies whether the task starts acquiring or generating samples when the signal enters or leaves the window you specify with Bottom and Top.
DAQmx_AnlgWin_StartTrig_Top                                      = int32(0x1403) # Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.
DAQmx_AnlgWin_StartTrig_Btm                                      = int32(0x1402) # Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.
DAQmx_AnlgWin_StartTrig_Coupling                                 = int32(0x2234) # Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.
DAQmx_StartTrig_Delay                                            = int32(0x1856) # Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with Delay Units.
DAQmx_StartTrig_DelayUnits                                       = int32(0x18C8) # Specifies the units of Delay.
DAQmx_StartTrig_Retriggerable                                    = int32(0x190F) # Specifies whether to enable retriggerable counter pulse generation. When you set this property to TRUE, the device generates pulses each time it receives a trigger. The device ignores a trigger if it is in the process of generating pulses.
DAQmx_RefTrig_Type                                               = int32(0x1419) # Specifies the type of trigger to use to mark a reference point for the measurement.
DAQmx_RefTrig_PretrigSamples                                     = int32(0x1445) # Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger. Post-trigger samples per channel are equal to Samples Per Channel minus the number of pretrigger samples per channel.
DAQmx_DigEdge_RefTrig_Src                                        = int32(0x1434) # Specifies the name of a terminal where there is a digital signal to use as the source of the Reference Trigger.
DAQmx_DigEdge_RefTrig_Edge                                       = int32(0x1430) # Specifies on what edge of a digital pulse the Reference Trigger occurs.
DAQmx_AnlgEdge_RefTrig_Src                                       = int32(0x1424) # Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger.
DAQmx_AnlgEdge_RefTrig_Slope                                     = int32(0x1423) # Specifies on which slope of the source signal the Reference Trigger occurs.
DAQmx_AnlgEdge_RefTrig_Lvl                                       = int32(0x1422) # Specifies in the units of the measurement the threshold at which the Reference Trigger occurs.  Use Slope to specify on which slope to trigger at this threshold.
DAQmx_AnlgEdge_RefTrig_Hyst                                      = int32(0x1421) # Specifies a hysteresis level in the units of the measurement. If Slope is DAQmx_Val_RisingSlope, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Slope is DAQmx_Val_FallingSlope, the trigger does not deassert until the source signal passes above Level plus the hysteresis.
DAQmx_AnlgEdge_RefTrig_Coupling                                  = int32(0x2235) # Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.
DAQmx_AnlgWin_RefTrig_Src                                        = int32(0x1426) # Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the Reference Trigger.
DAQmx_AnlgWin_RefTrig_When                                       = int32(0x1427) # Specifies whether the Reference Trigger occurs when the source signal enters the window or when it leaves the window. Use Bottom and Top to specify the window.
DAQmx_AnlgWin_RefTrig_Top                                        = int32(0x1429) # Specifies the upper limit of the window. Specify this value in the units of the measurement.
DAQmx_AnlgWin_RefTrig_Btm                                        = int32(0x1428) # Specifies the lower limit of the window. Specify this value in the units of the measurement.
DAQmx_AnlgWin_RefTrig_Coupling                                   = int32(0x1857) # Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.
DAQmx_AdvTrig_Type                                               = int32(0x1365) # Specifies the type of trigger to use to advance to the next entry in a scan list.
DAQmx_DigEdge_AdvTrig_Src                                        = int32(0x1362) # Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger.
DAQmx_DigEdge_AdvTrig_Edge                                       = int32(0x1360) # Specifies on which edge of a digital signal to advance to the next entry in a scan list.
DAQmx_DigEdge_AdvTrig_DigFltr_Enable                             = int32(0x2238) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_PauseTrig_Type                                             = int32(0x1366) # Specifies the type of trigger to use to pause a task.
DAQmx_AnlgLvl_PauseTrig_Src                                      = int32(0x1370) # Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.
DAQmx_AnlgLvl_PauseTrig_When                                     = int32(0x1371) # Specifies whether the task pauses above or below the threshold you specify with Level.
DAQmx_AnlgLvl_PauseTrig_Lvl                                      = int32(0x1369) # Specifies the threshold at which to pause the task. Specify this value in the units of the measurement or generation. Use Pause When to specify whether the task pauses above or below this threshold.
DAQmx_AnlgLvl_PauseTrig_Hyst                                     = int32(0x1368) # Specifies a hysteresis level in the units of the measurement or generation. If Pause When is DAQmx_Val_AboveLvl, the trigger does not deassert until the source signal passes below Level minus the hysteresis. If Pause When is DAQmx_Val_BelowLvl, the trigger does not deassert until the source signal passes above Level plus the hysteresis.
DAQmx_AnlgLvl_PauseTrig_Coupling                                 = int32(0x2236) # Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.
DAQmx_AnlgWin_PauseTrig_Src                                      = int32(0x1373) # Specifies the name of a virtual channel or terminal where there is an analog signal to use as the source of the trigger.
DAQmx_AnlgWin_PauseTrig_When                                     = int32(0x1374) # Specifies whether the task pauses while the trigger signal is inside or outside the window you specify with Bottom and Top.
DAQmx_AnlgWin_PauseTrig_Top                                      = int32(0x1376) # Specifies the upper limit of the window. Specify this value in the units of the measurement or generation.
DAQmx_AnlgWin_PauseTrig_Btm                                      = int32(0x1375) # Specifies the lower limit of the window. Specify this value in the units of the measurement or generation.
DAQmx_AnlgWin_PauseTrig_Coupling                                 = int32(0x2237) # Specifies the coupling for the source signal of the trigger if the source is a terminal rather than a virtual channel.
DAQmx_DigLvl_PauseTrig_Src                                       = int32(0x1379) # Specifies the name of a terminal where there is a digital signal to use as the source of the Pause Trigger.
DAQmx_DigLvl_PauseTrig_When                                      = int32(0x1380) # Specifies whether the task pauses while the signal is high or low.
DAQmx_DigLvl_PauseTrig_DigFltr_Enable                            = int32(0x2228) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_DigLvl_PauseTrig_DigFltr_MinPulseWidth                     = int32(0x2229) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_DigLvl_PauseTrig_DigFltr_TimebaseSrc                       = int32(0x222A) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_DigLvl_PauseTrig_DigFltr_TimebaseRate                      = int32(0x222B) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_DigLvl_PauseTrig_DigSync_Enable                            = int32(0x222C) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
DAQmx_ArmStartTrig_Type                                          = int32(0x1414) # Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.
DAQmx_DigEdge_ArmStartTrig_Src                                   = int32(0x1417) # Specifies the name of a terminal where there is a digital signal to use as the source of the Arm Start Trigger.
DAQmx_DigEdge_ArmStartTrig_Edge                                  = int32(0x1415) # Specifies on which edge of a digital signal to arm the task for a Start Trigger.
DAQmx_DigEdge_ArmStartTrig_DigFltr_Enable                        = int32(0x222D) # Specifies whether to apply the pulse width filter to the signal.
DAQmx_DigEdge_ArmStartTrig_DigFltr_MinPulseWidth                 = int32(0x222E) # Specifies in seconds the minimum pulse width the filter recognizes.
DAQmx_DigEdge_ArmStartTrig_DigFltr_TimebaseSrc                   = int32(0x222F) # Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
DAQmx_DigEdge_ArmStartTrig_DigFltr_TimebaseRate                  = int32(0x2230) # Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
DAQmx_DigEdge_ArmStartTrig_DigSync_Enable                        = int32(0x2231) # Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#********** Watchdog Attributes **********
DAQmx_Watchdog_Timeout                                           = int32(0x21A9) # Specifies in seconds the amount of time until the watchdog timer expires. A value of -1 means the internal timer never expires. Set this input to -1 if you use an Expiration Trigger to expire the watchdog task.
DAQmx_WatchdogExpirTrig_Type                                     = int32(0x21A3) # Specifies the type of trigger to use to expire a watchdog task.
DAQmx_DigEdge_WatchdogExpirTrig_Src                              = int32(0x21A4) # Specifies the name of a terminal where a digital signal exists to use as the source of the Expiration Trigger.
DAQmx_DigEdge_WatchdogExpirTrig_Edge                             = int32(0x21A5) # Specifies on which edge of a digital signal to expire the watchdog task.
DAQmx_Watchdog_DO_ExpirState                                     = int32(0x21A7) # Specifies the state to which to set the digital physical channels when the watchdog task expires.  You cannot modify the expiration state of dedicated digital input physical channels.
DAQmx_Watchdog_HasExpired                                        = int32(0x21A8) # Indicates if the watchdog timer expired. You can read this property only while the task is running.

#********** Write Attributes **********
DAQmx_Write_RelativeTo                                           = int32(0x190C) # Specifies the point in the buffer at which to write data. If you also specify an offset with Offset, the write operation begins at that offset relative to this point you select with this property.
DAQmx_Write_Offset                                               = int32(0x190D) # Specifies in samples per channel an offset at which a write operation begins. This offset is relative to the location you specify with Relative To.
DAQmx_Write_RegenMode                                            = int32(0x1453) # Specifies whether to allow NI-DAQmx to generate the same data multiple times.
DAQmx_Write_CurrWritePos                                         = int32(0x1458) # Indicates the number of the next sample for the device to generate. This value is identical for all channels in the task.
DAQmx_Write_SpaceAvail                                           = int32(0x1460) # Indicates in samples per channel the amount of available space in the buffer.
DAQmx_Write_TotalSampPerChanGenerated                            = int32(0x192B) # Indicates the total number of samples generated by each channel in the task. This value is identical for all channels in the task.
DAQmx_Write_RawDataWidth                                         = int32(0x217D) # Indicates in bytes the required size of a raw sample to write to the task.
DAQmx_Write_NumChans                                             = int32(0x217E) # Indicates the number of channels that an NI-DAQmx Write function writes to the task. This value is the number of channels in the task.
DAQmx_Write_DigitalLines_BytesPerChan                            = int32(0x217F) # Indicates the number of bytes expected per channel in a sample for line-based writes. If a channel has fewer lines than this number, NI-DAQmx ignores the extra bytes.

#********** Physical Channel Attributes **********
DAQmx_PhysicalChan_TEDS_MfgID                                    = int32(0x21DA) # Indicates the manufacturer ID of the sensor.
DAQmx_PhysicalChan_TEDS_ModelNum                                 = int32(0x21DB) # Indicates the model number of the sensor.
DAQmx_PhysicalChan_TEDS_SerialNum                                = int32(0x21DC) # Indicates the serial number of the sensor.
DAQmx_PhysicalChan_TEDS_VersionNum                               = int32(0x21DD) # Indicates the version number of the sensor.
DAQmx_PhysicalChan_TEDS_VersionLetter                            = int32(0x21DE) # Indicates the version letter of the sensor.
DAQmx_PhysicalChan_TEDS_BitStream                                = int32(0x21DF) # Indicates the TEDS binary bitstream without checksums.
DAQmx_PhysicalChan_TEDS_TemplateIDs                              = int32(0x228F) # Indicates the IDs of the templates in the bitstream in BitStream.

"""
/******************************************************************************
 *** NI-DAQmx Values **********************************************************
 ******************************************************************************/

/******************************************************/
/***    Non-Attribute Function Parameter Values     ***/
/******************************************************/
"""
#*** Values for the Mode parameter of DAQmxTaskControl ***  
DAQmx_Val_Task_Start                                              =int32(0) # Start
DAQmx_Val_Task_Stop                                               =int32(1) # Stop
DAQmx_Val_Task_Verify                                             =int32(2) # Verify
DAQmx_Val_Task_Commit                                             =int32(3) # Commit
DAQmx_Val_Task_Reserve                                            =int32(4) # Reserve
DAQmx_Val_Task_Unreserve                                          =int32(5) # Unreserve
DAQmx_Val_Task_Abort                                              =int32(6) # Abort

#*** Values for the Action parameter of DAQmxControlWatchdogTask ***
DAQmx_Val_ResetTimer                                              =int32(0) # Reset Timer
DAQmx_Val_ClearExpiration                                         =int32(1) # Clear Expiration

#*** Values for the Line Grouping parameter of DAQmxCreateDIChan and DAQmxCreateDOChan ***
DAQmx_Val_ChanPerLine                                             =int32(0) # One Channel For Each Line
DAQmx_Val_ChanForAllLines                                         =int32(1) # One Channel For All Lines

#*** Values for the Fill Mode parameter of DAQmxReadAnalogF64, DAQmxReadBinaryI16, DAQmxReadBinaryU16, DAQmxReadBinaryI32, DAQmxReadBinaryU32,
#    DAQmxReadDigitalU8, DAQmxReadDigitalU32, DAQmxReadDigitalLines ***
#*** Values for the Data Layout parameter of DAQmxWriteAnalogF64, DAQmxWriteBinaryI16, DAQmxWriteDigitalU8, DAQmxWriteDigitalU32, DAQmxWriteDigitalLines ***
DAQmx_Val_GroupByChannel                                          =int32(0) # Group by Channel
DAQmx_Val_GroupByScanNumber                                       =int32(1) # Group by Scan Number

#*** Values for the Signal Modifiers parameter of DAQmxConnectTerms ***/
DAQmx_Val_DoNotInvertPolarity                                     =int32(0) # Do not invert polarity
DAQmx_Val_InvertPolarity                                          =int32(1) # Invert polarity

#*** Values for the Action paramter of DAQmxCloseExtCal ***
DAQmx_Val_Action_Commit                                           =int32(0) # Commit
DAQmx_Val_Action_Cancel                                           =int32(1) # Cancel

#*** Values for the Trigger ID parameter of DAQmxSendSoftwareTrigger ***
DAQmx_Val_AdvanceTrigger                                        =int32(12488) # Advance Trigger

#*** Value set for the ActiveEdge parameter of DAQmxCfgSampClkTiming ***
DAQmx_Val_Rising                                                =int32(10280) # Rising
DAQmx_Val_Falling                                               =int32(10171) # Falling

#*** Value set SwitchPathType ***
#*** Value set for the output Path Status parameter of DAQmxSwitchFindPath ***
DAQmx_Val_PathStatus_Available                                  =int32(10431) # Path Available
DAQmx_Val_PathStatus_AlreadyExists                              =int32(10432) # Path Already Exists
DAQmx_Val_PathStatus_Unsupported                                =int32(10433) # Path Unsupported
DAQmx_Val_PathStatus_ChannelInUse                               =int32(10434) # Channel In Use
DAQmx_Val_PathStatus_SourceChannelConflict                      =int32(10435) # Channel Source Conflict
DAQmx_Val_PathStatus_ChannelReservedForRouting                  =int32(10436) # Channel Reserved for Routing

#*** Value set for the Units parameter of DAQmxCreateAIThrmcplChan, DAQmxCreateAIRTDChan, DAQmxCreateAIThrmstrChanIex, DAQmxCreateAIThrmstrChanVex and DAQmxCreateAITempBuiltInSensorChan ***
DAQmx_Val_DegC                                                  =int32(10143) # Deg C
DAQmx_Val_DegF                                                  =int32(10144) # Deg F
DAQmx_Val_Kelvins                                               =int32(10325) # Kelvins
DAQmx_Val_DegR                                                  =int32(10145) # Deg R

#*** Value set for the state parameter of DAQmxSetDigitalPowerUpStates ***
DAQmx_Val_High                                                  =int32(10192) # High
DAQmx_Val_Low                                                   =int32(10214) # Low
DAQmx_Val_Tristate                                              =int32(10310) # Tristate

#*** Value set RelayPos ***
#*** Value set for the state parameter of DAQmxSwitchGetSingleRelayPos and DAQmxSwitchGetMultiRelayPos ***
DAQmx_Val_Open                                                  =int32(10437) # Open
DAQmx_Val_Closed                                                =int32(10438) # Closed

#*** Value for the Terminal Config parameter of DAQmxCreateAIVoltageChan, DAQmxCreateAICurrentChan and DAQmxCreateAIVoltageChanWithExcit ***
DAQmx_Val_Cfg_Default                                             =int32(-1) # Default

#*** Value for the Timeout parameter of DAQmxWaitUntilTaskDone
DAQmx_Val_WaitInfinitely                                          =float64(-1.0)

#*** Value for the Number of Samples per Channel parameter of DAQmxReadAnalogF64, DAQmxReadBinaryI16, DAQmxReadBinaryU16,
#    DAQmxReadBinaryI32, DAQmxReadBinaryU32, DAQmxReadDigitalU8, DAQmxReadDigitalU32,
#    DAQmxReadDigitalLines, DAQmxReadCounterF64, DAQmxReadCounterU32 and DAQmxReadRaw ***
DAQmx_Val_Auto                                                    =int32(-1)
"""
/******************************************************/
/***              Attribute Values                  ***/
/******************************************************/
"""
#*** Values for DAQmx_AI_ACExcit_WireMode ***
#*** Value set ACExcitWireMode ***
DAQmx_Val_4Wire                                                       =int32(4) # 4-Wire
DAQmx_Val_5Wire                                                       =int32(5) # 5-Wire

#*** Values for DAQmx_AI_MeasType ***
#*** Value set AIMeasurementType ***
DAQmx_Val_Voltage                                               =int32(10322) # Voltage
DAQmx_Val_Current                                               =int32(10134) # Current
DAQmx_Val_Voltage_CustomWithExcitation                          =int32(10323) # More:Voltage:Custom with Excitation
DAQmx_Val_Freq_Voltage                                          =int32(10181) # Frequency
DAQmx_Val_Resistance                                            =int32(10278) # Resistance
DAQmx_Val_Temp_TC                                               =int32(10303) # Temperature:Thermocouple
DAQmx_Val_Temp_Thrmstr                                          =int32(10302) # Temperature:Thermistor
DAQmx_Val_Temp_RTD                                              =int32(10301) # Temperature:RTD
DAQmx_Val_Temp_BuiltInSensor                                    =int32(10311) # Temperature:Built-in Sensor
DAQmx_Val_Strain_Gage                                           =int32(10300) # Strain Gage
DAQmx_Val_Position_LVDT                                         =int32(10352) # Position:LVDT
DAQmx_Val_Position_RVDT                                         =int32(10353) # Position:RVDT
DAQmx_Val_Accelerometer                                         =int32(10356) # Accelerometer
DAQmx_Val_SoundPressure_Microphone                              =int32(10354) # Sound Pressure:Microphone
DAQmx_Val_TEDS_Sensor                                           =int32(12531) # TEDS Sensor

#*** Values for DAQmx_AO_IdleOutputBehavior ***
#*** Value set AOIdleOutputBehavior ***
DAQmx_Val_ZeroVolts                                             =int32(12526) # Zero Volts
DAQmx_Val_HighImpedance                                         =int32(12527) # High Impedance
DAQmx_Val_MaintainExistingValue                                 =int32(12528) # Maintain Existing Value

#*** Values for DAQmx_AO_OutputType ***
#*** Value set AOOutputChannelType ***
DAQmx_Val_Voltage                                               =int32(10322) # Voltage
DAQmx_Val_Current                                               =int32(10134) # Current

#*** Values for DAQmx_AI_Accel_SensitivityUnits ***
#*** Value set AccelSensitivityUnits1 ***
DAQmx_Val_mVoltsPerG                                            =int32(12509) # mVolts/g
DAQmx_Val_VoltsPerG                                             =int32(12510) # Volts/g

#*** Values for DAQmx_AI_Accel_Units ***
#*** Value set AccelUnits2 ***
DAQmx_Val_AccelUnit_g                                           =int32(10186) # g
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_SampQuant_SampMode ***
#*** Value set AcquisitionType ***
DAQmx_Val_FiniteSamps                                           =int32(10178) # Finite Samples
DAQmx_Val_ContSamps                                             =int32(10123) # Continuous Samples
DAQmx_Val_HWTimedSinglePoint                                    =int32(12522) # Hardware Timed Single Point

#*** Values for DAQmx_AnlgLvl_PauseTrig_When ***
#*** Value set ActiveLevel ***
DAQmx_Val_AboveLvl                                              =int32(10093) # Above Level
DAQmx_Val_BelowLvl                                              =int32(10107) # Below Level

#*** Values for DAQmx_AI_RVDT_Units ***
#*** Value set AngleUnits1 ***
DAQmx_Val_Degrees                                               =int32(10146) # Degrees
DAQmx_Val_Radians                                               =int32(10273) # Radians
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_CI_AngEncoder_Units ***
#*** Value set AngleUnits2 ***
DAQmx_Val_Degrees                                               =int32(10146) # Degrees
DAQmx_Val_Radians                                               =int32(10273) # Radians
DAQmx_Val_Ticks                                                 =int32(10304) # Ticks
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_AI_AutoZeroMode ***
#*** Value set AutoZeroType1 ***
DAQmx_Val_None                                                  =int32(10230) # None
DAQmx_Val_Once                                                  =int32(10244) # Once

#*** Values for DAQmx_SwitchScan_BreakMode ***
#*** Value set BreakMode ***
DAQmx_Val_NoAction                                              =int32(10227) # No Action
DAQmx_Val_BreakBeforeMake                                       =int32(10110) # Break Before Make

#*** Values for DAQmx_AI_Bridge_Cfg ***
#*** Value set BridgeConfiguration1 ***
DAQmx_Val_FullBridge                                            =int32(10182) # Full Bridge
DAQmx_Val_HalfBridge                                            =int32(10187) # Half Bridge
DAQmx_Val_QuarterBridge                                         =int32(10270) # Quarter Bridge
DAQmx_Val_NoBridge                                              =int32(10228) # No Bridge

#*** Values for DAQmx_CI_MeasType ***
#*** Value set CIMeasurementType ***
DAQmx_Val_CountEdges                                            =int32(10125) # Count Edges
DAQmx_Val_Freq                                                  =int32(10179) # Frequency
DAQmx_Val_Period                                                =int32(10256) # Period
DAQmx_Val_PulseWidth                                            =int32(10359) # Pulse Width
DAQmx_Val_SemiPeriod                                            =int32(10289) # Semi Period
DAQmx_Val_Position_AngEncoder                                   =int32(10360) # Position:Angular Encoder
DAQmx_Val_Position_LinEncoder                                   =int32(10361) # Position:Linear Encoder
DAQmx_Val_TwoEdgeSep                                            =int32(10267) # Two Edge Separation

#*** Values for DAQmx_AI_Thrmcpl_CJCSrc ***
#*** Value set CJCSource1 ***
DAQmx_Val_BuiltIn                                               =int32(10200) # Built-In
DAQmx_Val_ConstVal                                              =int32(10116) # Constant Value
DAQmx_Val_Chan                                                  =int32(10113) # Channel

#*** Values for DAQmx_CO_OutputType ***
#*** Value set COOutputType ***
DAQmx_Val_Pulse_Time                                            =int32(10269) # Pulse:Time
DAQmx_Val_Pulse_Freq                                            =int32(10119) # Pulse:Frequency
DAQmx_Val_Pulse_Ticks                                           =int32(10268) # Pulse:Ticks

#*** Values for DAQmx_ChanType ***
#*** Value set ChannelType ***
DAQmx_Val_AI                                                    =int32(10100) # Analog Input
DAQmx_Val_AO                                                    =int32(10102) # Analog Output
DAQmx_Val_DI                                                    =int32(10151) # Digital Input
DAQmx_Val_DO                                                    =int32(10153) # Digital Output
DAQmx_Val_CI                                                    =int32(10131) # Counter Input
DAQmx_Val_CO                                                    =int32(10132) # Counter Output

#*** Values for DAQmx_CI_CountEdges_Dir ***
#*** Value set CountDirection1 ***
DAQmx_Val_CountUp                                               =int32(10128) # Count Up
DAQmx_Val_CountDown                                             =int32(10124) # Count Down
DAQmx_Val_ExtControlled                                         =int32(10326) # Externally Controlled

#*** Values for DAQmx_CI_Freq_MeasMeth ***
#*** Values for DAQmx_CI_Period_MeasMeth ***
#*** Value set CounterFrequencyMethod ***
DAQmx_Val_LowFreq1Ctr                                           =int32(10105) # Low Frequency with 1 Counter
DAQmx_Val_HighFreq2Ctr                                          =int32(10157) # High Frequency with 2 Counters
DAQmx_Val_LargeRng2Ctr                                          =int32(10205) # Large Range with 2 Counters

#*** Values for DAQmx_AI_Coupling ***
#*** Value set Coupling1 ***
DAQmx_Val_AC                                                    =int32(10045) # AC
DAQmx_Val_DC                                                    =int32(10050) # DC
DAQmx_Val_GND                                                   =int32(10066) # GND

#*** Values for DAQmx_AnlgEdge_StartTrig_Coupling ***
#*** Values for DAQmx_AnlgWin_StartTrig_Coupling ***
#*** Values for DAQmx_AnlgEdge_RefTrig_Coupling ***
#*** Values for DAQmx_AnlgWin_RefTrig_Coupling ***
#*** Values for DAQmx_AnlgLvl_PauseTrig_Coupling ***
#*** Values for DAQmx_AnlgWin_PauseTrig_Coupling ***
#*** Value set Coupling2 ***
DAQmx_Val_AC                                                    =int32(10045) # AC
DAQmx_Val_DC                                                    =int32(10050) # DC

#*** Values for DAQmx_AI_CurrentShunt_Loc ***
#*** Value set CurrentShuntResistorLocation1 ***
DAQmx_Val_Internal                                              =int32(10200) # Internal
DAQmx_Val_External                                              =int32(10167) # External

#*** Values for DAQmx_AI_Current_Units ***
#*** Values for DAQmx_AO_Current_Units ***
#*** Value set CurrentUnits1 ***
DAQmx_Val_Amps                                                  =int32(10342) # Amps
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale
DAQmx_Val_FromTEDS                                              =int32(12516) # From TEDS

#*** Value set CurrentUnits2 ***
DAQmx_Val_Amps                                                  =int32(10342) # Amps
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_AI_DataXferMech ***
#*** Values for DAQmx_AO_DataXferMech ***
#*** Values for DAQmx_DI_DataXferMech ***
#*** Values for DAQmx_DO_DataXferMech ***
#*** Values for DAQmx_CI_DataXferMech ***
#*** Value set DataTransferMechanism ***
DAQmx_Val_DMA                                                   =int32(10054) # DMA
DAQmx_Val_Interrupts                                            =int32(10204) # Interrupts
DAQmx_Val_ProgrammedIO                                          =int32(10264) # Programmed I/O

#*** Values for DAQmx_Watchdog_DO_ExpirState ***
#*** Value set DigitalLineState ***
DAQmx_Val_High                                                  =int32(10192) # High
DAQmx_Val_Low                                                   =int32(10214) # Low
DAQmx_Val_Tristate                                              =int32(10310) # Tristate
DAQmx_Val_NoChange                                              =int32(10160) # No Change

#*** Values for DAQmx_StartTrig_DelayUnits ***
#*** Value set DigitalWidthUnits1 ***
DAQmx_Val_SampClkPeriods                                        =int32(10286) # Sample Clock Periods
DAQmx_Val_Seconds                                               =int32(10364) # Seconds
DAQmx_Val_Ticks                                                 =int32(10304) # Ticks

#*** Values for DAQmx_DelayFromSampClk_DelayUnits ***
#*** Value set DigitalWidthUnits2 ***
DAQmx_Val_Seconds                                               =int32(10364) # Seconds
DAQmx_Val_Ticks                                                 =int32(10304) # Ticks

#*** Values for DAQmx_Exported_AdvTrig_Pulse_WidthUnits ***
#*** Value set DigitalWidthUnits3 ***
DAQmx_Val_Seconds                                               =int32(10364) # Seconds

#*** Values for DAQmx_CI_Freq_StartingEdge ***
#*** Values for DAQmx_CI_Period_StartingEdge ***
#*** Values for DAQmx_CI_CountEdges_ActiveEdge ***
#*** Values for DAQmx_CI_PulseWidth_StartingEdge ***
#*** Values for DAQmx_CI_TwoEdgeSep_FirstEdge ***
#*** Values for DAQmx_CI_TwoEdgeSep_SecondEdge ***
#*** Values for DAQmx_CI_CtrTimebaseActiveEdge ***
#*** Values for DAQmx_CO_CtrTimebaseActiveEdge ***
#*** Values for DAQmx_SampClk_ActiveEdge ***
#*** Values for DAQmx_SampClk_Timebase_ActiveEdge ***
#*** Values for DAQmx_AIConv_ActiveEdge ***
#*** Values for DAQmx_DigEdge_StartTrig_Edge ***
#*** Values for DAQmx_DigEdge_RefTrig_Edge ***
#*** Values for DAQmx_DigEdge_AdvTrig_Edge ***
#*** Values for DAQmx_DigEdge_ArmStartTrig_Edge ***
#*** Values for DAQmx_DigEdge_WatchdogExpirTrig_Edge ***
#*** Value set Edge1 ***
DAQmx_Val_Rising                                                =int32(10280) # Rising
DAQmx_Val_Falling                                               =int32(10171) # Falling

#*** Values for DAQmx_CI_Encoder_DecodingType ***
#*** Value set EncoderType2 ***
DAQmx_Val_X1                                                    =int32(10090) # X1
DAQmx_Val_X2                                                    =int32(10091) # X2
DAQmx_Val_X4                                                    =int32(10092) # X4
DAQmx_Val_TwoPulseCounting                                      =int32(10313) # Two Pulse Counting

#*** Values for DAQmx_CI_Encoder_ZIndexPhase ***
#*** Value set EncoderZIndexPhase1 ***
DAQmx_Val_AHighBHigh                                            =int32(10040) # A High B High
DAQmx_Val_AHighBLow                                             =int32(10041) # A High B Low
DAQmx_Val_ALowBHigh                                             =int32(10042) # A Low B High
DAQmx_Val_ALowBLow                                              =int32(10043) # A Low B Low

#*** Values for DAQmx_AI_Excit_DCorAC ***
#*** Value set ExcitationDCorAC ***
DAQmx_Val_DC                                                    =int32(10050) # DC
DAQmx_Val_AC                                                    =int32(10045) # AC

#*** Values for DAQmx_AI_Excit_Src ***
#*** Value set ExcitationSource ***
DAQmx_Val_Internal                                              =int32(10200) # Internal
DAQmx_Val_External                                              =int32(10167) # External
DAQmx_Val_None                                                  =int32(10230) # None

#*** Values for DAQmx_AI_Excit_VoltageOrCurrent ***
#*** Value set ExcitationVoltageOrCurrent ***
DAQmx_Val_Voltage                                               =int32(10322) # Voltage
DAQmx_Val_Current                                               =int32(10134) # Current

#*** Values for DAQmx_Exported_CtrOutEvent_OutputBehavior ***
#*** Value set ExportActions2 ***
DAQmx_Val_Pulse                                                 =int32(10265) # Pulse
DAQmx_Val_Toggle                                                =int32(10307) # Toggle

#*** Values for DAQmx_Exported_SampClk_OutputBehavior ***
#*** Value set ExportActions3 ***
DAQmx_Val_Pulse                                                 =int32(10265) # Pulse
DAQmx_Val_Lvl                                                   =int32(10210) # Level

#*** Values for DAQmx_AI_Freq_Units ***
#*** Value set FrequencyUnits ***
DAQmx_Val_Hz                                                    =int32(10373) # Hz
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_CO_Pulse_Freq_Units ***
#*** Value set FrequencyUnits2 ***
DAQmx_Val_Hz                                                    =int32(10373) # Hz

#*** Values for DAQmx_CI_Freq_Units ***
#*** Value set FrequencyUnits3 ***
DAQmx_Val_Hz                                                    =int32(10373) # Hz
DAQmx_Val_Ticks                                                 =int32(10304) # Ticks
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale


#*** Values for DAQmx_AI_DataXferReqCond ***
#*** Values for DAQmx_DI_DataXferReqCond ***
#*** Value set InputDataTransferCondition ***
DAQmx_Val_OnBrdMemMoreThanHalfFull                              =int32(10237) # On Board Memory More than Half Full
DAQmx_Val_OnBrdMemNotEmpty                                      =int32(10241) # On Board Memory Not Empty

#*** Values for DAQmx_AI_TermCfg ***
#*** Value set InputTermCfg ***
DAQmx_Val_RSE                                                   =int32(10083) # RSE
DAQmx_Val_NRSE                                                  =int32(10078) # NRSE
DAQmx_Val_Diff                                                  =int32(10106) # Differential
DAQmx_Val_PseudoDiff                                            =int32(12529) # Pseudodifferential

#*** Values for DAQmx_AI_LVDT_SensitivityUnits ***
#*** Value set LVDTSensitivityUnits1 ***
DAQmx_Val_mVoltsPerVoltPerMillimeter                            =int32(12506) # mVolts/Volt/mMeter
DAQmx_Val_mVoltsPerVoltPerMilliInch                             =int32(12505) # mVolts/Volt/0.001 Inch

#*** Values for DAQmx_AI_LVDT_Units ***
#*** Value set LengthUnits2 ***
DAQmx_Val_Meters                                                =int32(10219) # Meters
DAQmx_Val_Inches                                                =int32(10379) # Inches
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_CI_LinEncoder_Units ***
#*** Value set LengthUnits3 ***
DAQmx_Val_Meters                                                =int32(10219) # Meters
DAQmx_Val_Inches                                                =int32(10379) # Inches
DAQmx_Val_Ticks                                                 =int32(10304) # Ticks
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_CI_OutputState ***
#*** Values for DAQmx_CO_Pulse_IdleState ***
#*** Values for DAQmx_CO_OutputState ***
#*** Values for DAQmx_Exported_CtrOutEvent_Toggle_IdleState ***
#*** Values for DAQmx_DigLvl_PauseTrig_When ***
#*** Value set Level1 ***
DAQmx_Val_High                                                  =int32(10192) # High
DAQmx_Val_Low                                                   =int32(10214) # Low

#*** Values for DAQmx_AIConv_Timebase_Src ***
#*** Value set MIOAIConvertTbSrc ***
DAQmx_Val_SameAsSampTimebase                                    =int32(10284) # Same as Sample Timebase
DAQmx_Val_SameAsMasterTimebase                                  =int32(10282) # Same as Master Timebase

#*** Values for DAQmx_AO_DataXferReqCond ***
#*** Values for DAQmx_DO_DataXferReqCond ***
#*** Value set OutputDataTransferCondition ***
DAQmx_Val_OnBrdMemEmpty                                         =int32(10235) # On Board Memory Empty
DAQmx_Val_OnBrdMemHalfFullOrLess                                =int32(10239) # On Board Memory Half Full or Less
DAQmx_Val_OnBrdMemNotFull                                       =int32(10242) # On Board Memory Less than Full

#*** Values for DAQmx_AO_TermCfg ***
#*** Value set OutputTermCfg ***
DAQmx_Val_RSE                                                   =int32(10083) # RSE
DAQmx_Val_Diff                                                  =int32(10106) # Differential
DAQmx_Val_PseudoDiff                                            =int32(12529) # Pseudodifferential

#*** Values for DAQmx_Read_OverWrite ***
#*** Value set OverwriteMode1 ***
DAQmx_Val_OverwriteUnreadSamps                                  =int32(10252) # Overwrite Unread Samples
DAQmx_Val_DoNotOverwriteUnreadSamps                             =int32(10159) # Do Not Overwrite Unread Samples

#*** Values for DAQmx_Exported_AIConvClk_Pulse_Polarity ***
#*** Values for DAQmx_Exported_AdvTrig_Pulse_Polarity ***
#*** Values for DAQmx_Exported_AdvCmpltEvent_Pulse_Polarity ***
#*** Values for DAQmx_Exported_AIHoldCmpltEvent_PulsePolarity ***
#*** Values for DAQmx_Exported_CtrOutEvent_Pulse_Polarity ***
#*** Value set Polarity2 ***
DAQmx_Val_ActiveHigh                                            =int32(10095) # Active High
DAQmx_Val_ActiveLow                                             =int32(10096) # Active Low


#*** Values for DAQmx_AI_RTD_Type ***
#*** Value set RTDType1 ***
DAQmx_Val_Pt3750                                                =int32(12481) # Pt3750
DAQmx_Val_Pt3851                                                =int32(10071) # Pt3851
DAQmx_Val_Pt3911                                                =int32(12482) # Pt3911
DAQmx_Val_Pt3916                                                =int32(10069) # Pt3916
DAQmx_Val_Pt3920                                                =int32(10053) # Pt3920
DAQmx_Val_Pt3928                                                =int32(12483) # Pt3928
DAQmx_Val_Custom                                                =int32(10137) # Custom

#*** Values for DAQmx_AI_RVDT_SensitivityUnits ***
#*** Value set RVDTSensitivityUnits1 ***
DAQmx_Val_mVoltsPerVoltPerDegree                                =int32(12507) # mVolts/Volt/Degree
DAQmx_Val_mVoltsPerVoltPerRadian                                =int32(12508) # mVolts/Volt/Radian

#*** Values for DAQmx_Read_RelativeTo ***
#*** Value set ReadRelativeTo ***
DAQmx_Val_FirstSample                                           =int32(10424) # First Sample
DAQmx_Val_CurrReadPos                                           =int32(10425) # Current Read Position
DAQmx_Val_RefTrig                                               =int32(10426) # Reference Trigger
DAQmx_Val_FirstPretrigSamp                                      =int32(10427) # First Pretrigger Sample
DAQmx_Val_MostRecentSamp                                        =int32(10428) # Most Recent Sample


#*** Values for DAQmx_Write_RegenMode ***
#*** Value set RegenerationMode1 ***
DAQmx_Val_AllowRegen                                            =int32(10097) # Allow Regeneration
DAQmx_Val_DoNotAllowRegen                                       =int32(10158) # Do Not Allow Regeneration

#*** Values for DAQmx_AI_ResistanceCfg ***
#*** Value set ResistanceConfiguration ***
DAQmx_Val_2Wire                                                       =int32(2) # 2-Wire
DAQmx_Val_3Wire                                                       =int32(3) # 3-Wire
DAQmx_Val_4Wire                                                       =int32(4) # 4-Wire

#*** Values for DAQmx_AI_Resistance_Units ***
#*** Value set ResistanceUnits1 ***
DAQmx_Val_Ohms                                                  =int32(10384) # Ohms
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale
DAQmx_Val_FromTEDS                                              =int32(12516) # From TEDS

#*** Value set ResistanceUnits2 ***
DAQmx_Val_Ohms                                                  =int32(10384) # Ohms
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_AI_ResolutionUnits ***
#*** Values for DAQmx_AO_ResolutionUnits ***
#*** Value set ResolutionType1 ***
DAQmx_Val_Bits                                                  =int32(10109) # Bits

#*** Values for DAQmx_SampTimingType ***
#*** Value set SampleTimingType ***
DAQmx_Val_SampClk                                               =int32(10388) # Sample Clock
DAQmx_Val_Handshake                                             =int32(10389) # Handshake
DAQmx_Val_Implicit                                              =int32(10451) # Implicit
DAQmx_Val_OnDemand                                              =int32(10390) # On Demand
DAQmx_Val_ChangeDetection                                       =int32(12504) # Change Detection

#*** Values for DAQmx_Scale_Type ***
#*** Value set ScaleType ***
DAQmx_Val_Linear                                                =int32(10447) # Linear
DAQmx_Val_MapRanges                                             =int32(10448) # Map Ranges
DAQmx_Val_Polynomial                                            =int32(10449) # Polynomial
DAQmx_Val_Table                                                 =int32(10450) # Table

#*** Values for DAQmx_AI_Bridge_ShuntCal_Select ***
#*** Value set ShuntCalSelect ***
DAQmx_Val_A                                                     =int32(12513) # A
DAQmx_Val_B                                                     =int32(12514) # B
DAQmx_Val_AandB                                                 =int32(12515) # A and B

#*** Value set Signal ***
DAQmx_Val_AIConvertClock                                        =int32(12484) # AI Convert Clock
DAQmx_Val_10MHzClock                                            =int32(12536) # 10MHz Clock
DAQmx_Val_20MHzTimebaseClock                                    =int32(12486) # 20MHz Timebase Clock
DAQmx_Val_SampleClock                                           =int32(12487) # Sample Clock
DAQmx_Val_AdvanceTrigger                                        =int32(12488) # Advance Trigger
DAQmx_Val_ReferenceTrigger                                      =int32(12490) # Reference Trigger
DAQmx_Val_StartTrigger                                          =int32(12491) # Start Trigger
DAQmx_Val_AdvCmpltEvent                                         =int32(12492) # Advance Complete Event
DAQmx_Val_AIHoldCmpltEvent                                      =int32(12493) # AI Hold Complete Event
DAQmx_Val_CounterOutputEvent                                    =int32(12494) # Counter Output Event
DAQmx_Val_ChangeDetectionEvent                                  =int32(12511) # Change Detection Event
DAQmx_Val_WDTExpiredEvent                                       =int32(12512) # Watchdog Timer Expired Event

#*** Values for DAQmx_AnlgEdge_StartTrig_Slope ***
#*** Values for DAQmx_AnlgEdge_RefTrig_Slope ***
#*** Value set Slope1 ***
DAQmx_Val_RisingSlope                                           =int32(10280) # Rising
DAQmx_Val_FallingSlope                                          =int32(10171) # Falling

#*** Values for DAQmx_AI_SoundPressure_Units ***
#*** Value set SoundPressureUnits1 ***
DAQmx_Val_Pascals                                               =int32(10081) # Pascals
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_AI_Lowpass_SwitchCap_ClkSrc ***
#*** Values for DAQmx_AO_DAC_Ref_Src ***
#*** Values for DAQmx_AO_DAC_Offset_Src ***
#*** Value set SourceSelection ***
DAQmx_Val_Internal                                              =int32(10200) # Internal
DAQmx_Val_External                                              =int32(10167) # External

#*** Values for DAQmx_AI_StrainGage_Cfg ***
#*** Value set StrainGageBridgeType1 ***
DAQmx_Val_FullBridgeI                                           =int32(10183) # Full Bridge I
DAQmx_Val_FullBridgeII                                          =int32(10184) # Full Bridge II
DAQmx_Val_FullBridgeIII                                         =int32(10185) # Full Bridge III
DAQmx_Val_HalfBridgeI                                           =int32(10188) # Half Bridge I
DAQmx_Val_HalfBridgeII                                          =int32(10189) # Half Bridge II
DAQmx_Val_QuarterBridgeI                                        =int32(10271) # Quarter Bridge I
DAQmx_Val_QuarterBridgeII                                       =int32(10272) # Quarter Bridge II

#*** Values for DAQmx_AI_Strain_Units ***
#*** Value set StrainUnits1 ***
DAQmx_Val_Strain                                                =int32(10299) # Strain
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_SwitchScan_RepeatMode ***
#*** Value set SwitchScanRepeatMode ***
DAQmx_Val_Finite                                                =int32(10172) # Finite
DAQmx_Val_Cont                                                  =int32(10117) # Continuous

#*** Values for DAQmx_SwitchChan_Usage ***
#*** Value set SwitchUsageTypes ***
DAQmx_Val_Source                                                =int32(10439) # Source
DAQmx_Val_Load                                                  =int32(10440) # Load
DAQmx_Val_ReservedForRouting                                    =int32(10441) # Reserved for Routing

#*** Value set TEDSUnits ***
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale
DAQmx_Val_FromTEDS                                              =int32(12516) # From TEDS

#*** Values for DAQmx_AI_Temp_Units ***
#*** Value set TemperatureUnits1 ***
DAQmx_Val_DegC                                                  =int32(10143) # Deg C
DAQmx_Val_DegF                                                  =int32(10144) # Deg F
DAQmx_Val_Kelvins                                               =int32(10325) # Kelvins
DAQmx_Val_DegR                                                  =int32(10145) # Deg R
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_AI_Thrmcpl_Type ***
#*** Value set ThermocoupleType1 ***
DAQmx_Val_J_Type_TC                                             =int32(10072) # J
DAQmx_Val_K_Type_TC                                             =int32(10073) # K
DAQmx_Val_N_Type_TC                                             =int32(10077) # N
DAQmx_Val_R_Type_TC                                             =int32(10082) # R
DAQmx_Val_S_Type_TC                                             =int32(10085) # S
DAQmx_Val_T_Type_TC                                             =int32(10086) # T
DAQmx_Val_B_Type_TC                                             =int32(10047) # B
DAQmx_Val_E_Type_TC                                             =int32(10055) # E

#*** Values for DAQmx_CO_Pulse_Time_Units ***
#*** Value set TimeUnits2 ***
DAQmx_Val_Seconds                                               =int32(10364) # Seconds

#*** Values for DAQmx_CI_Period_Units ***
#*** Values for DAQmx_CI_PulseWidth_Units ***
#*** Values for DAQmx_CI_TwoEdgeSep_Units ***
#*** Values for DAQmx_CI_SemiPeriod_Units ***
#*** Value set TimeUnits3 ***
DAQmx_Val_Seconds                                               =int32(10364) # Seconds
DAQmx_Val_Ticks                                                 =int32(10304) # Ticks
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_RefTrig_Type ***
#*** Value set TriggerType1 ***
DAQmx_Val_AnlgEdge                                              =int32(10099) # Analog Edge
DAQmx_Val_DigEdge                                               =int32(10150) # Digital Edge
DAQmx_Val_AnlgWin                                               =int32(10103) # Analog Window
DAQmx_Val_None                                                  =int32(10230) # None

#*** Values for DAQmx_ArmStartTrig_Type ***
#*** Values for DAQmx_WatchdogExpirTrig_Type ***
#*** Value set TriggerType4 ***
DAQmx_Val_DigEdge                                               =int32(10150) # Digital Edge
DAQmx_Val_None                                                  =int32(10230) # None

#*** Values for DAQmx_AdvTrig_Type ***
#*** Value set TriggerType5 ***
DAQmx_Val_DigEdge                                               =int32(10150) # Digital Edge
DAQmx_Val_Software                                              =int32(10292) # Software
DAQmx_Val_None                                                  =int32(10230) # None

#*** Values for DAQmx_PauseTrig_Type ***
#*** Value set TriggerType6 ***
DAQmx_Val_AnlgLvl                                               =int32(10101) # Analog Level
DAQmx_Val_AnlgWin                                               =int32(10103) # Analog Window
DAQmx_Val_DigLvl                                                =int32(10152) # Digital Level
DAQmx_Val_None                                                  =int32(10230) # None

#*** Values for DAQmx_StartTrig_Type ***
#*** Value set TriggerType8 ***
DAQmx_Val_AnlgEdge                                              =int32(10099) # Analog Edge
DAQmx_Val_DigEdge                                               =int32(10150) # Digital Edge
DAQmx_Val_AnlgWin                                               =int32(10103) # Analog Window
DAQmx_Val_None                                                  =int32(10230) # None

#*** Values for DAQmx_Scale_PreScaledUnits ***
#*** Value set UnitsPreScaled ***
DAQmx_Val_Volts                                                 =int32(10348) # Volts
DAQmx_Val_Amps                                                  =int32(10342) # Amps
DAQmx_Val_DegF                                                  =int32(10144) # Deg F
DAQmx_Val_DegC                                                  =int32(10143) # Deg C
DAQmx_Val_DegR                                                  =int32(10145) # Deg R
DAQmx_Val_Kelvins                                               =int32(10325) # Kelvins
DAQmx_Val_Strain                                                =int32(10299) # Strain
DAQmx_Val_Ohms                                                  =int32(10384) # Ohms
DAQmx_Val_Hz                                                    =int32(10373) # Hz
DAQmx_Val_Seconds                                               =int32(10364) # Seconds
DAQmx_Val_Meters                                                =int32(10219) # Meters
DAQmx_Val_Inches                                                =int32(10379) # Inches
DAQmx_Val_Degrees                                               =int32(10146) # Degrees
DAQmx_Val_Radians                                               =int32(10273) # Radians
DAQmx_Val_g                                                     =int32(10186) # g
DAQmx_Val_Pascals                                               =int32(10081) # Pascals
DAQmx_Val_FromTEDS                                              =int32(12516) # From TEDS

#*** Values for DAQmx_AI_Voltage_Units ***
#*** Value set VoltageUnits1 ***
DAQmx_Val_Volts                                                 =int32(10348) # Volts
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale
DAQmx_Val_FromTEDS                                              =int32(12516) # From TEDS

#*** Values for DAQmx_AO_Voltage_Units ***
#*** Value set VoltageUnits2 ***
DAQmx_Val_Volts                                                 =int32(10348) # Volts
DAQmx_Val_FromCustomScale                                       =int32(10065) # From Custom Scale

#*** Values for DAQmx_ReadWaitMode ***
#*** Value set WaitMode ***
DAQmx_Val_WaitForInterrupt                                      =int32(12523) # Wait For Interrupt
DAQmx_Val_Poll                                                  =int32(12524) # Poll
DAQmx_Val_Yield                                                 =int32(12525) # Yield

#*** Values for DAQmx_AnlgWin_StartTrig_When ***
#*** Values for DAQmx_AnlgWin_RefTrig_When ***
#*** Value set WindowTriggerCondition1 ***
DAQmx_Val_EnteringWin                                           =int32(10163) # Entering Window
DAQmx_Val_LeavingWin                                            =int32(10208) # Leaving Window

#*** Values for DAQmx_AnlgWin_PauseTrig_When ***
#*** Value set WindowTriggerCondition2 ***
DAQmx_Val_InsideWin                                             =int32(10199) # Inside Window
DAQmx_Val_OutsideWin                                            =int32(10251) # Outside Window

#*** Values for DAQmx_Write_RelativeTo ***
#*** Value set WriteRelativeTo ***
DAQmx_Val_FirstSample                                           =int32(10424) # First Sample
DAQmx_Val_CurrWritePos                                          =int32(10430) # Current Write Position



# Switch Topologies
DAQmx_Val_Switch_Topology_1127_1_Wire_64x1_Mux            ="1127/1-Wire 64x1 Mux"              # 1127/1-Wire 64x1 Mux
DAQmx_Val_Switch_Topology_1127_2_Wire_32x1_Mux            ="1127/2-Wire 32x1 Mux"              # 1127/2-Wire 32x1 Mux
DAQmx_Val_Switch_Topology_1127_2_Wire_4x8_Matrix          ="1127/2-Wire 4x8 Matrix"            # 1127/2-Wire 4x8 Matrix
DAQmx_Val_Switch_Topology_1127_4_Wire_16x1_Mux            ="1127/4-Wire 16x1 Mux"              # 1127/4-Wire 16x1 Mux
DAQmx_Val_Switch_Topology_1127_Independent                ="1127/Independent"                  # 1127/Independent
DAQmx_Val_Switch_Topology_1128_1_Wire_64x1_Mux            ="1128/1-Wire 64x1 Mux"              # 1128/1-Wire 64x1 Mux
DAQmx_Val_Switch_Topology_1128_2_Wire_32x1_Mux            ="1128/2-Wire 32x1 Mux"              # 1128/2-Wire 32x1 Mux
DAQmx_Val_Switch_Topology_1128_2_Wire_4x8_Matrix          ="1128/2-Wire 4x8 Matrix"            # 1128/2-Wire 4x8 Matrix
DAQmx_Val_Switch_Topology_1128_4_Wire_16x1_Mux            ="1128/4-Wire 16x1 Mux"              # 1128/4-Wire 16x1 Mux
DAQmx_Val_Switch_Topology_1128_Independent                ="1128/Independent"                  # 1128/Independent
DAQmx_Val_Switch_Topology_1129_2_Wire_16x16_Matrix        ="1129/2-Wire 16x16 Matrix"          # 1129/2-Wire 16x16 Matrix
DAQmx_Val_Switch_Topology_1129_2_Wire_8x32_Matrix         ="1129/2-Wire 8x32 Matrix"           # 1129/2-Wire 8x32 Matrix
DAQmx_Val_Switch_Topology_1129_2_Wire_4x64_Matrix         ="1129/2-Wire 4x64 Matrix"           # 1129/2-Wire 4x64 Matrix
DAQmx_Val_Switch_Topology_1129_2_Wire_Dual_8x16_Matrix    ="1129/2-Wire Dual 8x16 Matrix"      # 1129/2-Wire Dual 8x16 Matrix
DAQmx_Val_Switch_Topology_1129_2_Wire_Dual_4x32_Matrix    ="1129/2-Wire Dual 4x32 Matrix"      # 1129/2-Wire Dual 4x32 Matrix
DAQmx_Val_Switch_Topology_1129_2_Wire_Quad_4x16_Matrix    ="1129/2-Wire Quad 4x16 Matrix"      # 1129/2-Wire Quad 4x16 Matrix
DAQmx_Val_Switch_Topology_1130_1_Wire_256x1_Mux           ="1130/1-Wire 256x1 Mux"             # 1130/1-Wire 256x1 Mux
DAQmx_Val_Switch_Topology_1130_2_Wire_128x1_Mux           ="1130/2-Wire 128x1 Mux"             # 1130/2-Wire 128x1 Mux
DAQmx_Val_Switch_Topology_1130_4_Wire_64x1_Mux            ="1130/4-Wire 64x1 Mux"              # 1130/4-Wire 64x1 Mux
DAQmx_Val_Switch_Topology_1130_1_Wire_4x64_Matrix         ="1130/1-Wire 4x64 Matrix"           # 1130/1-Wire 4x64 Matrix
DAQmx_Val_Switch_Topology_1130_1_Wire_8x32_Matrix         ="1130/1-Wire 8x32 Matrix"           # 1130/1-Wire 8x32 Matrix
DAQmx_Val_Switch_Topology_1130_2_Wire_4x32_Matrix         ="1130/2-Wire 4x32 Matrix"           # 1130/2-Wire 4x32 Matrix
DAQmx_Val_Switch_Topology_1130_Independent                ="1130/Independent"                  # 1130/Independent
DAQmx_Val_Switch_Topology_1160_16_SPDT                    ="1160/16-SPDT"                      # 1160/16-SPDT
DAQmx_Val_Switch_Topology_1161_8_SPDT                     ="1161/8-SPDT"                       # 1161/8-SPDT
DAQmx_Val_Switch_Topology_1163R_Octal_4x1_Mux             ="1163R/Octal 4x1 Mux"               # 1163R/Octal 4x1 Mux
DAQmx_Val_Switch_Topology_1166_32_SPDT                    ="1166/32-SPDT"                      # 1166/32-SPDT
DAQmx_Val_Switch_Topology_1167_Independent                ="1167/Independent"                  # 1167/Independent
DAQmx_Val_Switch_Topology_1169_100_SPST                   ="1169/100-SPST"                     # 1169/100-SPST
DAQmx_Val_Switch_Topology_1190_Quad_4x1_Mux               ="1190/Quad 4x1 Mux"                 # 1190/Quad 4x1 Mux
DAQmx_Val_Switch_Topology_1191_Quad_4x1_Mux               ="1191/Quad 4x1 Mux"                 # 1191/Quad 4x1 Mux
DAQmx_Val_Switch_Topology_1192_8_SPDT                     ="1192/8-SPDT"                       # 1192/8-SPDT
DAQmx_Val_Switch_Topology_1193_32x1_Mux                   ="1193/32x1 Mux"                     # 1193/32x1 Mux
DAQmx_Val_Switch_Topology_1193_Dual_16x1_Mux              ="1193/Dual 16x1 Mux"                # 1193/Dual 16x1 Mux
DAQmx_Val_Switch_Topology_1193_Quad_8x1_Mux               ="1193/Quad 8x1 Mux"                 # 1193/Quad 8x1 Mux
DAQmx_Val_Switch_Topology_1193_16x1_Terminated_Mux        ="1193/16x1 Terminated Mux"          # 1193/16x1 Terminated Mux
DAQmx_Val_Switch_Topology_1193_Dual_8x1_Terminated_Mux    ="1193/Dual 8x1 Terminated Mux"      # 1193/Dual 8x1 Terminated Mux
DAQmx_Val_Switch_Topology_1193_Quad_4x1_Terminated_Mux    ="1193/Quad 4x1 Terminated Mux"      # 1193/Quad 4x1 Terminated Mux
DAQmx_Val_Switch_Topology_1193_Independent                ="1193/Independent"                  # 1193/Independent
DAQmx_Val_Switch_Topology_2501_1_Wire_48x1_Mux            ="2501/1-Wire 48x1 Mux"              # 2501/1-Wire 48x1 Mux
DAQmx_Val_Switch_Topology_2501_1_Wire_48x1_Amplified_Mux  ="2501/1-Wire 48x1 Amplified Mux"    # 2501/1-Wire 48x1 Amplified Mux
DAQmx_Val_Switch_Topology_2501_2_Wire_24x1_Mux            ="2501/2-Wire 24x1 Mux"              # 2501/2-Wire 24x1 Mux
DAQmx_Val_Switch_Topology_2501_2_Wire_24x1_Amplified_Mux  ="2501/2-Wire 24x1 Amplified Mux"    # 2501/2-Wire 24x1 Amplified Mux
DAQmx_Val_Switch_Topology_2501_2_Wire_Dual_12x1_Mux       ="2501/2-Wire Dual 12x1 Mux"         # 2501/2-Wire Dual 12x1 Mux
DAQmx_Val_Switch_Topology_2501_2_Wire_Quad_6x1_Mux        ="2501/2-Wire Quad 6x1 Mux"          # 2501/2-Wire Quad 6x1 Mux
DAQmx_Val_Switch_Topology_2501_2_Wire_4x6_Matrix          ="2501/2-Wire 4x6 Matrix"            # 2501/2-Wire 4x6 Matrix
DAQmx_Val_Switch_Topology_2501_4_Wire_12x1_Mux            ="2501/4-Wire 12x1 Mux"              # 2501/4-Wire 12x1 Mux
DAQmx_Val_Switch_Topology_2503_1_Wire_48x1_Mux            ="2503/1-Wire 48x1 Mux"              # 2503/1-Wire 48x1 Mux
DAQmx_Val_Switch_Topology_2503_2_Wire_24x1_Mux            ="2503/2-Wire 24x1 Mux"              # 2503/2-Wire 24x1 Mux
DAQmx_Val_Switch_Topology_2503_2_Wire_Dual_12x1_Mux       ="2503/2-Wire Dual 12x1 Mux"         # 2503/2-Wire Dual 12x1 Mux
DAQmx_Val_Switch_Topology_2503_2_Wire_Quad_6x1_Mux        ="2503/2-Wire Quad 6x1 Mux"          # 2503/2-Wire Quad 6x1 Mux
DAQmx_Val_Switch_Topology_2503_2_Wire_4x6_Matrix          ="2503/2-Wire 4x6 Matrix"            # 2503/2-Wire 4x6 Matrix
DAQmx_Val_Switch_Topology_2503_4_Wire_12x1_Mux            ="2503/4-Wire 12x1 Mux"              # 2503/4-Wire 12x1 Mux
DAQmx_Val_Switch_Topology_2529_2_Wire_8x16_Matrix         ="2529/2-Wire 8x16 Matrix"           # 2529/2-Wire 8x16 Matrix
DAQmx_Val_Switch_Topology_2529_2_Wire_4x32_Matrix         ="2529/2-Wire 4x32 Matrix"           # 2529/2-Wire 4x32 Matrix
DAQmx_Val_Switch_Topology_2529_2_Wire_Dual_4x16_Matrix    ="2529/2-Wire Dual 4x16 Matrix"      # 2529/2-Wire Dual 4x16 Matrix
DAQmx_Val_Switch_Topology_2530_1_Wire_128x1_Mux           ="2530/1-Wire 128x1 Mux"             # 2530/1-Wire 128x1 Mux
DAQmx_Val_Switch_Topology_2530_2_Wire_64x1_Mux            ="2530/2-Wire 64x1 Mux"              # 2530/2-Wire 64x1 Mux
DAQmx_Val_Switch_Topology_2530_4_Wire_32x1_Mux            ="2530/4-Wire 32x1 Mux"              # 2530/4-Wire 32x1 Mux
DAQmx_Val_Switch_Topology_2530_1_Wire_4x32_Matrix         ="2530/1-Wire 4x32 Matrix"           # 2530/1-Wire 4x32 Matrix
DAQmx_Val_Switch_Topology_2530_1_Wire_8x16_Matrix         ="2530/1-Wire 8x16 Matrix"           # 2530/1-Wire 8x16 Matrix
DAQmx_Val_Switch_Topology_2530_2_Wire_4x16_Matrix         ="2530/2-Wire 4x16 Matrix"           # 2530/2-Wire 4x16 Matrix
DAQmx_Val_Switch_Topology_2530_Independent                ="2530/Independent"                  # 2530/Independent
DAQmx_Val_Switch_Topology_2532_1_Wire_4x128_Matrix        ="2532/1-Wire 4x128 Matrix"          # 2532/1-Wire 4x128 Matrix
DAQmx_Val_Switch_Topology_2532_1_Wire_8x64_Matrix         ="2532/1-Wire 8x64 Matrix"           # 2532/1-Wire 8x64 Matrix
DAQmx_Val_Switch_Topology_2532_1_Wire_Sixteen_2x16_Matrix ="2532/1-Wire Sixteen 2x16 Matrix"   # 2532/1-Wire Sixteen 2x16 Matrix
DAQmx_Val_Switch_Topology_2565_16_SPST                    ="2565/16-SPST"                      # 2565/16-SPST
DAQmx_Val_Switch_Topology_2566_16_SPDT                    ="2566/16-SPDT"                      # 2566/16-SPDT
DAQmx_Val_Switch_Topology_2567_Independent                ="2567/Independent"                  # 2567/Independent
DAQmx_Val_Switch_Topology_2568_31_SPST                    ="2568/31-SPST"                      # 2568/31-SPST
DAQmx_Val_Switch_Topology_2569_100_SPST                   ="2569/100-SPST"                     # 2569/100-SPST
DAQmx_Val_Switch_Topology_2570_40_SPDT                    ="2570/40-SPDT"                      # 2570/40-SPDT
DAQmx_Val_Switch_Topology_2590_4x1_Mux                    ="2590/4x1 Mux"                      # 2590/4x1 Mux
DAQmx_Val_Switch_Topology_2591_4x1_Mux                    ="2591/4x1 Mux"                      # 2591/4x1 Mux
DAQmx_Val_Switch_Topology_2593_16x1_Mux                   ="2593/16x1 Mux"                     # 2593/16x1 Mux
DAQmx_Val_Switch_Topology_2593_Dual_8x1_Mux               ="2593/Dual 8x1 Mux"                 # 2593/Dual 8x1 Mux
DAQmx_Val_Switch_Topology_2593_8x1_Terminated_Mux         ="2593/8x1 Terminated Mux"           # 2593/8x1 Terminated Mux
DAQmx_Val_Switch_Topology_2593_Dual_4x1_Terminated_Mux    ="2593/Dual 4x1 Terminated Mux"      # 2593/Dual 4x1 Terminated Mux
DAQmx_Val_Switch_Topology_2593_Independent                ="2593/Independent"                  # 2593/Independent






"""
/******************************************************************************
 *** NI-DAQmx Error Codes *****************************************************
 ******************************************************************************/
"""
DAQmxSuccess                                  =int32(0)

def DAQmxFailed(error):
    return error<0

# Error and Warning Codes
DAQmxErrorWriteNotCompleteBeforeSampClk                                    =int32(-209801)
DAQmxErrorReadNotCompleteBeforeSampClk                                     =int32(-209800)
DAQmxErrorDAQmxCantUseStringDueToUnknownChar                               =int32(-200811)
DAQmxErrorDAQmxCantRetrieveStringDueToUnknownChar                          =int32(-200810)
DAQmxErrorClearTEDSNotSupportedOnRT                                        =int32(-200809)
DAQmxErrorCfgTEDSNotSupportedOnRT                                          =int32(-200808)
DAQmxErrorProgFilterClkCfgdToDifferentMinPulseWidthBySameTask1PerDev       =int32(-200807)
DAQmxErrorProgFilterClkCfgdToDifferentMinPulseWidthByAnotherTask1PerDev    =int32(-200806)
DAQmxErrorNoLastExtCalDateTimeLastExtCalNotDAQmx                           =int32(-200804)
DAQmxErrorCannotWriteNotStartedAutoStartFalseNotOnDemandHWTimedSglPt       =int32(-200803)
DAQmxErrorCannotWriteNotStartedAutoStartFalseNotOnDemandBufSizeZero        =int32(-200802)
DAQmxErrorCOInvalidTimingSrcDueToSignal                                    =int32(-200801)
DAQmxErrorCIInvalidTimingSrcForSampClkDueToSampTimingType                  =int32(-200800)
DAQmxErrorCIInvalidTimingSrcForEventCntDueToSampMode                       =int32(-200799)
DAQmxErrorNoChangeDetectOnNonInputDigLineForDev                            =int32(-200798)
DAQmxErrorEmptyStringTermNameNotSupported                                  =int32(-200797)
DAQmxErrorMemMapEnabledForHWTimedNonBufferedAO                             =int32(-200796)
DAQmxErrorDevOnboardMemOverflowDuringHWTimedNonBufferedGen                 =int32(-200795)
DAQmxErrorCODAQmxWriteMultipleChans                                        =int32(-200794)
DAQmxErrorCantMaintainExistingValueAOSync                                  =int32(-200793)
DAQmxErrorMStudioMultiplePhysChansNotSupported                             =int32(-200792)
DAQmxErrorCantConfigureTEDSForChan                                         =int32(-200791)
DAQmxErrorWriteDataTypeTooSmall                                            =int32(-200790)
DAQmxErrorReadDataTypeTooSmall                                             =int32(-200789)
DAQmxErrorMeasuredBridgeOffsetTooHigh                                      =int32(-200788)
DAQmxErrorStartTrigConflictWithCOHWTimedSinglePt                           =int32(-200787)
DAQmxErrorSampClkRateExtSampClkTimebaseRateMismatch                        =int32(-200786)
DAQmxErrorInvalidTimingSrcDueToSampTimingType                              =int32(-200785)
DAQmxErrorVirtualTEDSFileNotFound                                          =int32(-200784)
DAQmxErrorMStudioNoForwardPolyScaleCoeffs                                  =int32(-200783)
DAQmxErrorMStudioNoReversePolyScaleCoeffs                                  =int32(-200782)
DAQmxErrorMStudioNoPolyScaleCoeffsUseCalc                                  =int32(-200781)
DAQmxErrorMStudioNoForwardPolyScaleCoeffsUseCalc                           =int32(-200780)
DAQmxErrorMStudioNoReversePolyScaleCoeffsUseCalc                           =int32(-200779)
DAQmxErrorCOSampModeSampTimingTypeSampClkConflict                          =int32(-200778)
DAQmxErrorDevCannotProduceMinPulseWidth                                    =int32(-200777)
DAQmxErrorCannotProduceMinPulseWidthGivenPropertyValues                    =int32(-200776)
DAQmxErrorTermCfgdToDifferentMinPulseWidthByAnotherTask                    =int32(-200775)
DAQmxErrorTermCfgdToDifferentMinPulseWidthByAnotherProperty                =int32(-200774)
DAQmxErrorDigSyncNotAvailableOnTerm                                        =int32(-200773)
DAQmxErrorDigFilterNotAvailableOnTerm                                      =int32(-200772)
DAQmxErrorDigFilterEnabledMinPulseWidthNotCfg                              =int32(-200771)
DAQmxErrorDigFilterAndSyncBothEnabled                                      =int32(-200770)
DAQmxErrorHWTimedSinglePointAOAndDataXferNotProgIO                         =int32(-200769)
DAQmxErrorNonBufferedAOAndDataXferNotProgIO                                =int32(-200768)
DAQmxErrorProgIODataXferForBufferedAO                                      =int32(-200767)
DAQmxErrorTEDSLegacyTemplateIDInvalidOrUnsupported                         =int32(-200766)
DAQmxErrorTEDSMappingMethodInvalidOrUnsupported                            =int32(-200765)
DAQmxErrorTEDSLinearMappingSlopeZero                                       =int32(-200764)
DAQmxErrorAIInputBufferSizeNotMultOfXferSize                               =int32(-200763)
DAQmxErrorNoSyncPulseExtSampClkTimebase                                    =int32(-200762)
DAQmxErrorNoSyncPulseAnotherTaskRunning                                    =int32(-200761)
DAQmxErrorAOMinMaxNotInGainRange                                           =int32(-200760)
DAQmxErrorAOMinMaxNotInDACRange                                            =int32(-200759)
DAQmxErrorDevOnlySupportsSampClkTimingAO                                   =int32(-200758)
DAQmxErrorDevOnlySupportsSampClkTimingAI                                   =int32(-200757)
DAQmxErrorTEDSIncompatibleSensorAndMeasType                                =int32(-200756)
DAQmxErrorTEDSMultipleCalTemplatesNotSupported                             =int32(-200755)
DAQmxErrorTEDSTemplateParametersNotSupported                               =int32(-200754)
DAQmxErrorParsingTEDSData                                                  =int32(-200753)
DAQmxErrorMultipleActivePhysChansNotSupported                              =int32(-200752)
DAQmxErrorNoChansSpecdForChangeDetect                                      =int32(-200751)
DAQmxErrorInvalidCalVoltageForGivenGain                                    =int32(-200750)
DAQmxErrorInvalidCalGain                                                   =int32(-200749)
DAQmxErrorMultipleWritesBetweenSampClks                                    =int32(-200748)
DAQmxErrorInvalidAcqTypeForFREQOUT                                         =int32(-200747)
DAQmxErrorSuitableTimebaseNotFoundTimeCombo2                               =int32(-200746)
DAQmxErrorSuitableTimebaseNotFoundFrequencyCombo2                          =int32(-200745)
DAQmxErrorRefClkRateRefClkSrcMismatch                                      =int32(-200744)
DAQmxErrorNoTEDSTerminalBlock                                              =int32(-200743)
DAQmxErrorCorruptedTEDSMemory                                              =int32(-200742)
DAQmxErrorTEDSNotSupported                                                 =int32(-200741)
DAQmxErrorTimingSrcTaskStartedBeforeTimedLoop                              =int32(-200740)
DAQmxErrorPropertyNotSupportedForTimingSrc                                 =int32(-200739)
DAQmxErrorTimingSrcDoesNotExist                                            =int32(-200738)
DAQmxErrorInputBufferSizeNotEqualSampsPerChanForFiniteSampMode             =int32(-200737)
DAQmxErrorFREQOUTCannotProduceDesiredFrequency2                            =int32(-200736)
DAQmxErrorExtRefClkRateNotSpecified                                        =int32(-200735)
DAQmxErrorDeviceDoesNotSupportDMADataXferForNonBufferedAcq                 =int32(-200734)
DAQmxErrorDigFilterMinPulseWidthSetWhenTristateIsFalse                     =int32(-200733)
DAQmxErrorDigFilterEnableSetWhenTristateIsFalse                            =int32(-200732)
DAQmxErrorNoHWTimingWithOnDemand                                           =int32(-200731)
DAQmxErrorCannotDetectChangesWhenTristateIsFalse                           =int32(-200730)
DAQmxErrorCannotHandshakeWhenTristateIsFalse                               =int32(-200729)
DAQmxErrorLinesUsedForStaticInputNotForHandshakingControl                  =int32(-200728)
DAQmxErrorLinesUsedForHandshakingControlNotForStaticInput                  =int32(-200727)
DAQmxErrorLinesUsedForStaticInputNotForHandshakingInput                    =int32(-200726)
DAQmxErrorLinesUsedForHandshakingInputNotForStaticInput                    =int32(-200725)
DAQmxErrorDifferentDITristateValsForChansInTask                            =int32(-200724)
DAQmxErrorTimebaseCalFreqVarianceTooLarge                                  =int32(-200723)
DAQmxErrorTimebaseCalFailedToConverge                                      =int32(-200722)
DAQmxErrorInadequateResolutionForTimebaseCal                               =int32(-200721)
DAQmxErrorInvalidAOGainCalConst                                            =int32(-200720)
DAQmxErrorInvalidAOOffsetCalConst                                          =int32(-200719)
DAQmxErrorInvalidAIGainCalConst                                            =int32(-200718)
DAQmxErrorInvalidAIOffsetCalConst                                          =int32(-200717)
DAQmxErrorDigOutputOverrun                                                 =int32(-200716)
DAQmxErrorDigInputOverrun                                                  =int32(-200715)
DAQmxErrorAcqStoppedDriverCantXferDataFastEnough                           =int32(-200714)
DAQmxErrorChansCantAppearInSameTask                                        =int32(-200713)
DAQmxErrorInputCfgFailedBecauseWatchdogExpired                             =int32(-200712)
DAQmxErrorAnalogTrigChanNotExternal                                        =int32(-200711)
DAQmxErrorTooManyChansForInternalAIInputSrc                                =int32(-200710)
DAQmxErrorTEDSSensorNotDetected                                            =int32(-200709)
DAQmxErrorPrptyGetSpecdActiveItemFailedDueToDifftValues                    =int32(-200708)
DAQmxErrorRoutingDestTermPXIClk10InNotInSlot2                              =int32(-200706)
DAQmxErrorRoutingDestTermPXIStarXNotInSlot2                                =int32(-200705)
DAQmxErrorRoutingSrcTermPXIStarXNotInSlot2                                 =int32(-200704)
DAQmxErrorRoutingSrcTermPXIStarInSlot16AndAbove                            =int32(-200703)
DAQmxErrorRoutingDestTermPXIStarInSlot16AndAbove                           =int32(-200702)
DAQmxErrorRoutingDestTermPXIStarInSlot2                                    =int32(-200701)
DAQmxErrorRoutingSrcTermPXIStarInSlot2                                     =int32(-200700)
DAQmxErrorRoutingDestTermPXIChassisNotIdentified                           =int32(-200699)
DAQmxErrorRoutingSrcTermPXIChassisNotIdentified                            =int32(-200698)
DAQmxErrorFailedToAcquireCalData                                           =int32(-200697)
DAQmxErrorBridgeOffsetNullingCalNotSupported                               =int32(-200696)
DAQmxErrorAIMaxNotSpecified                                                =int32(-200695)
DAQmxErrorAIMinNotSpecified                                                =int32(-200694)
DAQmxErrorOddTotalBufferSizeToWrite                                        =int32(-200693)
DAQmxErrorOddTotalNumSampsToWrite                                          =int32(-200692)
DAQmxErrorBufferWithWaitMode                                               =int32(-200691)
DAQmxErrorBufferWithHWTimedSinglePointSampMode                             =int32(-200690)
DAQmxErrorCOWritePulseLowTicksNotSupported                                 =int32(-200689)
DAQmxErrorCOWritePulseHighTicksNotSupported                                =int32(-200688)
DAQmxErrorCOWritePulseLowTimeOutOfRange                                    =int32(-200687)
DAQmxErrorCOWritePulseHighTimeOutOfRange                                   =int32(-200686)
DAQmxErrorCOWriteFreqOutOfRange                                            =int32(-200685)
DAQmxErrorCOWriteDutyCycleOutOfRange                                       =int32(-200684)
DAQmxErrorInvalidInstallation                                              =int32(-200683)
DAQmxErrorRefTrigMasterSessionUnavailable                                  =int32(-200682)
DAQmxErrorRouteFailedBecauseWatchdogExpired                                =int32(-200681)
DAQmxErrorDeviceShutDownDueToHighTemp                                      =int32(-200680)
DAQmxErrorNoMemMapWhenHWTimedSinglePoint                                   =int32(-200679)
DAQmxErrorWriteFailedBecauseWatchdogExpired                                =int32(-200678)
DAQmxErrorDifftInternalAIInputSrcs                                         =int32(-200677)
DAQmxErrorDifftAIInputSrcInOneChanGroup                                    =int32(-200676)
DAQmxErrorInternalAIInputSrcInMultChanGroups                               =int32(-200675)
DAQmxErrorSwitchOpFailedDueToPrevError                                     =int32(-200674)
DAQmxErrorWroteMultiSampsUsingSingleSampWrite                              =int32(-200673)
DAQmxErrorMismatchedInputArraySizes                                        =int32(-200672)
DAQmxErrorCantExceedRelayDriveLimit                                        =int32(-200671)
DAQmxErrorDACRngLowNotEqualToMinusRefVal                                   =int32(-200670)
DAQmxErrorCantAllowConnectDACToGnd                                         =int32(-200669)
DAQmxErrorWatchdogTimeoutOutOfRangeAndNotSpecialVal                        =int32(-200668)
DAQmxErrorNoWatchdogOutputOnPortReservedForInput                           =int32(-200667)
DAQmxErrorNoInputOnPortCfgdForWatchdogOutput                               =int32(-200666)
DAQmxErrorWatchdogExpirationStateNotEqualForLinesInPort                    =int32(-200665)
DAQmxErrorCannotPerformOpWhenTaskNotReserved                               =int32(-200664)
DAQmxErrorPowerupStateNotSupported                                         =int32(-200663)
DAQmxErrorWatchdogTimerNotSupported                                        =int32(-200662)
DAQmxErrorOpNotSupportedWhenRefClkSrcNone                                  =int32(-200661)
DAQmxErrorSampClkRateUnavailable                                           =int32(-200660)
DAQmxErrorPrptyGetSpecdSingleActiveChanFailedDueToDifftVals                =int32(-200659)
DAQmxErrorPrptyGetImpliedActiveChanFailedDueToDifftVals                    =int32(-200658)
DAQmxErrorPrptyGetSpecdActiveChanFailedDueToDifftVals                      =int32(-200657)
DAQmxErrorNoRegenWhenUsingBrdMem                                           =int32(-200656)
DAQmxErrorNonbufferedReadMoreThanSampsPerChan                              =int32(-200655)
DAQmxErrorWatchdogExpirationTristateNotSpecdForEntirePort                  =int32(-200654)
DAQmxErrorPowerupTristateNotSpecdForEntirePort                             =int32(-200653)
DAQmxErrorPowerupStateNotSpecdForEntirePort                                =int32(-200652)
DAQmxErrorCantSetWatchdogExpirationOnDigInChan                             =int32(-200651)
DAQmxErrorCantSetPowerupStateOnDigInChan                                   =int32(-200650)
DAQmxErrorPhysChanNotInTask                                                =int32(-200649)
DAQmxErrorPhysChanDevNotInTask                                             =int32(-200648)
DAQmxErrorDigInputNotSupported                                             =int32(-200647)
DAQmxErrorDigFilterIntervalNotEqualForLines                                =int32(-200646)
DAQmxErrorDigFilterIntervalAlreadyCfgd                                     =int32(-200645)
DAQmxErrorCantResetExpiredWatchdog                                         =int32(-200644)
DAQmxErrorActiveChanTooManyLinesSpecdWhenGettingPrpty                      =int32(-200643)
DAQmxErrorActiveChanNotSpecdWhenGetting1LinePrpty                          =int32(-200642)
DAQmxErrorDigPrptyCannotBeSetPerLine                                       =int32(-200641)
DAQmxErrorSendAdvCmpltAfterWaitForTrigInScanlist                           =int32(-200640)
DAQmxErrorDisconnectionRequiredInScanlist                                  =int32(-200639)
DAQmxErrorTwoWaitForTrigsAfterConnectionInScanlist                         =int32(-200638)
DAQmxErrorActionSeparatorRequiredAfterBreakingConnectionInScanlist         =int32(-200637)
DAQmxErrorConnectionInScanlistMustWaitForTrig                              =int32(-200636)
DAQmxErrorActionNotSupportedTaskNotWatchdog                                =int32(-200635)
DAQmxErrorWfmNameSameAsScriptName                                          =int32(-200634)
DAQmxErrorScriptNameSameAsWfmName                                          =int32(-200633)
DAQmxErrorDSFStopClock                                                     =int32(-200632)
DAQmxErrorDSFReadyForStartClock                                            =int32(-200631)
DAQmxErrorWriteOffsetNotMultOfIncr                                         =int32(-200630)
DAQmxErrorDifferentPrptyValsNotSupportedOnDev                              =int32(-200629)
DAQmxErrorRefAndPauseTrigConfigured                                        =int32(-200628)
DAQmxErrorFailedToEnableHighSpeedInputClock                                =int32(-200627)
DAQmxErrorEmptyPhysChanInPowerUpStatesArray                                =int32(-200626)
DAQmxErrorActivePhysChanTooManyLinesSpecdWhenGettingPrpty                  =int32(-200625)
DAQmxErrorActivePhysChanNotSpecdWhenGetting1LinePrpty                      =int32(-200624)
DAQmxErrorPXIDevTempCausedShutDown                                         =int32(-200623)
DAQmxErrorInvalidNumSampsToWrite                                           =int32(-200622)
DAQmxErrorOutputFIFOUnderflow2                                             =int32(-200621)
DAQmxErrorRepeatedAIPhysicalChan                                           =int32(-200620)
DAQmxErrorMultScanOpsInOneChassis                                          =int32(-200619)
DAQmxErrorInvalidAIChanOrder                                               =int32(-200618)
DAQmxErrorReversePowerProtectionActivated                                  =int32(-200617)
DAQmxErrorInvalidAsynOpHandle                                              =int32(-200616)
DAQmxErrorFailedToEnableHighSpeedOutput                                    =int32(-200615)
DAQmxErrorCannotReadPastEndOfRecord                                        =int32(-200614)
DAQmxErrorAcqStoppedToPreventInputBufferOverwriteOneDataXferMech           =int32(-200613)
DAQmxErrorZeroBasedChanIndexInvalid                                        =int32(-200612)
DAQmxErrorNoChansOfGivenTypeInTask                                         =int32(-200611)
DAQmxErrorSampClkSrcInvalidForOutputValidForInput                          =int32(-200610)
DAQmxErrorOutputBufSizeTooSmallToStartGen                                  =int32(-200609)
DAQmxErrorInputBufSizeTooSmallToStartAcq                                   =int32(-200608)
DAQmxErrorExportTwoSignalsOnSameTerminal                                   =int32(-200607)
DAQmxErrorChanIndexInvalid                                                 =int32(-200606)
DAQmxErrorRangeSyntaxNumberTooBig                                          =int32(-200605)
DAQmxErrorNULLPtr                                                          =int32(-200604)
DAQmxErrorScaledMinEqualMax                                                =int32(-200603)
DAQmxErrorPreScaledMinEqualMax                                             =int32(-200602)
DAQmxErrorPropertyNotSupportedForScaleType                                 =int32(-200601)
DAQmxErrorChannelNameGenerationNumberTooBig                                =int32(-200600)
DAQmxErrorRepeatedNumberInScaledValues                                     =int32(-200599)
DAQmxErrorRepeatedNumberInPreScaledValues                                  =int32(-200598)
DAQmxErrorLinesAlreadyReservedForOutput                                    =int32(-200597)
DAQmxErrorSwitchOperationChansSpanMultipleDevsInList                       =int32(-200596)
DAQmxErrorInvalidIDInListAtBeginningOfSwitchOperation                      =int32(-200595)
DAQmxErrorMStudioInvalidPolyDirection                                      =int32(-200594)
DAQmxErrorMStudioPropertyGetWhileTaskNotVerified                           =int32(-200593)
DAQmxErrorRangeWithTooManyObjects                                          =int32(-200592)
DAQmxErrorCppDotNetAPINegativeBufferSize                                   =int32(-200591)
DAQmxErrorCppCantRemoveInvalidEventHandler                                 =int32(-200590)
DAQmxErrorCppCantRemoveEventHandlerTwice                                   =int32(-200589)
DAQmxErrorCppCantRemoveOtherObjectsEventHandler                            =int32(-200588)
DAQmxErrorDigLinesReservedOrUnavailable                                    =int32(-200587)
DAQmxErrorDSFFailedToResetStream                                           =int32(-200586)
DAQmxErrorDSFReadyForOutputNotAsserted                                     =int32(-200585)
DAQmxErrorSampToWritePerChanNotMultipleOfIncr                              =int32(-200584)
DAQmxErrorAOPropertiesCauseVoltageBelowMin                                 =int32(-200583)
DAQmxErrorAOPropertiesCauseVoltageOverMax                                  =int32(-200582)
DAQmxErrorPropertyNotSupportedWhenRefClkSrcNone                            =int32(-200581)
DAQmxErrorAIMaxTooSmall                                                    =int32(-200580)
DAQmxErrorAIMaxTooLarge                                                    =int32(-200579)
DAQmxErrorAIMinTooSmall                                                    =int32(-200578)
DAQmxErrorAIMinTooLarge                                                    =int32(-200577)
DAQmxErrorBuiltInCJCSrcNotSupported                                        =int32(-200576)
DAQmxErrorTooManyPostTrigSampsPerChan                                      =int32(-200575)
DAQmxErrorTrigLineNotFoundSingleDevRoute                                   =int32(-200574)
DAQmxErrorDifferentInternalAIInputSources                                  =int32(-200573)
DAQmxErrorDifferentAIInputSrcInOneChanGroup                                =int32(-200572)
DAQmxErrorInternalAIInputSrcInMultipleChanGroups                           =int32(-200571)
DAQmxErrorCAPIChanIndexInvalid                                             =int32(-200570)
DAQmxErrorCollectionDoesNotMatchChanType                                   =int32(-200569)
DAQmxErrorOutputCantStartChangedRegenerationMode                           =int32(-200568)
DAQmxErrorOutputCantStartChangedBufferSize                                 =int32(-200567)
DAQmxErrorChanSizeTooBigForU32PortWrite                                    =int32(-200566)
DAQmxErrorChanSizeTooBigForU8PortWrite                                     =int32(-200565)
DAQmxErrorChanSizeTooBigForU32PortRead                                     =int32(-200564)
DAQmxErrorChanSizeTooBigForU8PortRead                                      =int32(-200563)
DAQmxErrorInvalidDigDataWrite                                              =int32(-200562)
DAQmxErrorInvalidAODataWrite                                               =int32(-200561)
DAQmxErrorWaitUntilDoneDoesNotIndicateDone                                 =int32(-200560)
DAQmxErrorMultiChanTypesInTask                                             =int32(-200559)
DAQmxErrorMultiDevsInTask                                                  =int32(-200558)
DAQmxErrorCannotSetPropertyWhenTaskRunning                                 =int32(-200557)
DAQmxErrorCannotGetPropertyWhenTaskNotCommittedOrRunning                   =int32(-200556)
DAQmxErrorLeadingUnderscoreInString                                        =int32(-200555)
DAQmxErrorTrailingSpaceInString                                            =int32(-200554)
DAQmxErrorLeadingSpaceInString                                             =int32(-200553)
DAQmxErrorInvalidCharInString                                              =int32(-200552)
DAQmxErrorDLLBecameUnlocked                                                =int32(-200551)
DAQmxErrorDLLLock                                                          =int32(-200550)
DAQmxErrorSelfCalConstsInvalid                                             =int32(-200549)
DAQmxErrorInvalidTrigCouplingExceptForExtTrigChan                          =int32(-200548)
DAQmxErrorWriteFailsBufferSizeAutoConfigured                               =int32(-200547)
DAQmxErrorExtCalAdjustExtRefVoltageFailed                                  =int32(-200546)
DAQmxErrorSelfCalFailedExtNoiseOrRefVoltageOutOfCal                        =int32(-200545)
DAQmxErrorExtCalTemperatureNotDAQmx                                        =int32(-200544)
DAQmxErrorExtCalDateTimeNotDAQmx                                           =int32(-200543)
DAQmxErrorSelfCalTemperatureNotDAQmx                                       =int32(-200542)
DAQmxErrorSelfCalDateTimeNotDAQmx                                          =int32(-200541)
DAQmxErrorDACRefValNotSet                                                  =int32(-200540)
DAQmxErrorAnalogMultiSampWriteNotSupported                                 =int32(-200539)
DAQmxErrorInvalidActionInControlTask                                       =int32(-200538)
DAQmxErrorPolyCoeffsInconsistent                                           =int32(-200537)
DAQmxErrorSensorValTooLow                                                  =int32(-200536)
DAQmxErrorSensorValTooHigh                                                 =int32(-200535)
DAQmxErrorWaveformNameTooLong                                              =int32(-200534)
DAQmxErrorIdentifierTooLongInScript                                        =int32(-200533)
DAQmxErrorUnexpectedIDFollowingSwitchChanName                              =int32(-200532)
DAQmxErrorRelayNameNotSpecifiedInList                                      =int32(-200531)
DAQmxErrorUnexpectedIDFollowingRelayNameInList                             =int32(-200530)
DAQmxErrorUnexpectedIDFollowingSwitchOpInList                              =int32(-200529)
DAQmxErrorInvalidLineGrouping                                              =int32(-200528)
DAQmxErrorCtrMinMax                                                        =int32(-200527)
DAQmxErrorWriteChanTypeMismatch                                            =int32(-200526)
DAQmxErrorReadChanTypeMismatch                                             =int32(-200525)
DAQmxErrorWriteNumChansMismatch                                            =int32(-200524)
DAQmxErrorOneChanReadForMultiChanTask                                      =int32(-200523)
DAQmxErrorCannotSelfCalDuringExtCal                                        =int32(-200522)
DAQmxErrorMeasCalAdjustOscillatorPhaseDAC                                  =int32(-200521)
DAQmxErrorInvalidCalConstCalADCAdjustment                                  =int32(-200520)
DAQmxErrorInvalidCalConstOscillatorFreqDACValue                            =int32(-200519)
DAQmxErrorInvalidCalConstOscillatorPhaseDACValue                           =int32(-200518)
DAQmxErrorInvalidCalConstOffsetDACValue                                    =int32(-200517)
DAQmxErrorInvalidCalConstGainDACValue                                      =int32(-200516)
DAQmxErrorInvalidNumCalADCReadsToAverage                                   =int32(-200515)
DAQmxErrorInvalidCfgCalAdjustDirectPathOutputImpedance                     =int32(-200514)
DAQmxErrorInvalidCfgCalAdjustMainPathOutputImpedance                       =int32(-200513)
DAQmxErrorInvalidCfgCalAdjustMainPathPostAmpGainAndOffset                  =int32(-200512)
DAQmxErrorInvalidCfgCalAdjustMainPathPreAmpGain                            =int32(-200511)
DAQmxErrorInvalidCfgCalAdjustMainPreAmpOffset                              =int32(-200510)
DAQmxErrorMeasCalAdjustCalADC                                              =int32(-200509)
DAQmxErrorMeasCalAdjustOscillatorFrequency                                 =int32(-200508)
DAQmxErrorMeasCalAdjustDirectPathOutputImpedance                           =int32(-200507)
DAQmxErrorMeasCalAdjustMainPathOutputImpedance                             =int32(-200506)
DAQmxErrorMeasCalAdjustDirectPathGain                                      =int32(-200505)
DAQmxErrorMeasCalAdjustMainPathPostAmpGainAndOffset                        =int32(-200504)
DAQmxErrorMeasCalAdjustMainPathPreAmpGain                                  =int32(-200503)
DAQmxErrorMeasCalAdjustMainPathPreAmpOffset                                =int32(-200502)
DAQmxErrorInvalidDateTimeInEEPROM                                          =int32(-200501)
DAQmxErrorUnableToLocateErrorResources                                     =int32(-200500)
DAQmxErrorDotNetAPINotUnsigned32BitNumber                                  =int32(-200499)
DAQmxErrorInvalidRangeOfObjectsSyntaxInString                              =int32(-200498)
DAQmxErrorAttemptToEnableLineNotPreviouslyDisabled                         =int32(-200497)
DAQmxErrorInvalidCharInPattern                                             =int32(-200496)
DAQmxErrorIntermediateBufferFull                                           =int32(-200495)
DAQmxErrorLoadTaskFailsBecauseNoTimingOnDev                                =int32(-200494)
DAQmxErrorCAPIReservedParamNotNULLNorEmpty                                 =int32(-200493)
DAQmxErrorCAPIReservedParamNotNULL                                         =int32(-200492)
DAQmxErrorCAPIReservedParamNotZero                                         =int32(-200491)
DAQmxErrorSampleValueOutOfRange                                            =int32(-200490)
DAQmxErrorChanAlreadyInTask                                                =int32(-200489)
DAQmxErrorVirtualChanDoesNotExist                                          =int32(-200488)
DAQmxErrorChanNotInTask                                                    =int32(-200486)
DAQmxErrorTaskNotInDataNeighborhood                                        =int32(-200485)
DAQmxErrorCantSaveTaskWithoutReplace                                       =int32(-200484)
DAQmxErrorCantSaveChanWithoutReplace                                       =int32(-200483)
DAQmxErrorDevNotInTask                                                     =int32(-200482)
DAQmxErrorDevAlreadyInTask                                                 =int32(-200481)
DAQmxErrorCanNotPerformOpWhileTaskRunning                                  =int32(-200479)
DAQmxErrorCanNotPerformOpWhenNoChansInTask                                 =int32(-200478)
DAQmxErrorCanNotPerformOpWhenNoDevInTask                                   =int32(-200477)
DAQmxErrorCannotPerformOpWhenTaskNotRunning                                =int32(-200475)
DAQmxErrorOperationTimedOut                                                =int32(-200474)
DAQmxErrorCannotReadWhenAutoStartFalseAndTaskNotRunningOrCommitted         =int32(-200473)
DAQmxErrorCannotWriteWhenAutoStartFalseAndTaskNotRunningOrCommitted        =int32(-200472)
DAQmxErrorTaskVersionNew                                                   =int32(-200470)
DAQmxErrorChanVersionNew                                                   =int32(-200469)
DAQmxErrorEmptyString                                                      =int32(-200467)
DAQmxErrorChannelSizeTooBigForPortReadType                                 =int32(-200466)
DAQmxErrorChannelSizeTooBigForPortWriteType                                =int32(-200465)
DAQmxErrorExpectedNumberOfChannelsVerificationFailed                       =int32(-200464)
DAQmxErrorNumLinesMismatchInReadOrWrite                                    =int32(-200463)
DAQmxErrorOutputBufferEmpty                                                =int32(-200462)
DAQmxErrorInvalidChanName                                                  =int32(-200461)
DAQmxErrorReadNoInputChansInTask                                           =int32(-200460)
DAQmxErrorWriteNoOutputChansInTask                                         =int32(-200459)
DAQmxErrorPropertyNotSupportedNotInputTask                                 =int32(-200457)
DAQmxErrorPropertyNotSupportedNotOutputTask                                =int32(-200456)
DAQmxErrorGetPropertyNotInputBufferedTask                                  =int32(-200455)
DAQmxErrorGetPropertyNotOutputBufferedTask                                 =int32(-200454)
DAQmxErrorInvalidTimeoutVal                                                =int32(-200453)
DAQmxErrorAttributeNotSupportedInTaskContext                               =int32(-200452)
DAQmxErrorAttributeNotQueryableUnlessTaskIsCommitted                       =int32(-200451)
DAQmxErrorAttributeNotSettableWhenTaskIsRunning                            =int32(-200450)
DAQmxErrorDACRngLowNotMinusRefValNorZero                                   =int32(-200449)
DAQmxErrorDACRngHighNotEqualRefVal                                         =int32(-200448)
DAQmxErrorUnitsNotFromCustomScale                                          =int32(-200447)
DAQmxErrorInvalidVoltageReadingDuringExtCal                                =int32(-200446)
DAQmxErrorCalFunctionNotSupported                                          =int32(-200445)
DAQmxErrorInvalidPhysicalChanForCal                                        =int32(-200444)
DAQmxErrorExtCalNotComplete                                                =int32(-200443)
DAQmxErrorCantSyncToExtStimulusFreqDuringCal                               =int32(-200442)
DAQmxErrorUnableToDetectExtStimulusFreqDuringCal                           =int32(-200441)
DAQmxErrorInvalidCloseAction                                               =int32(-200440)
DAQmxErrorExtCalFunctionOutsideExtCalSession                               =int32(-200439)
DAQmxErrorInvalidCalArea                                                   =int32(-200438)
DAQmxErrorExtCalConstsInvalid                                              =int32(-200437)
DAQmxErrorStartTrigDelayWithExtSampClk                                     =int32(-200436)
DAQmxErrorDelayFromSampClkWithExtConv                                      =int32(-200435)
DAQmxErrorFewerThan2PreScaledVals                                          =int32(-200434)
DAQmxErrorFewerThan2ScaledValues                                           =int32(-200433)
DAQmxErrorPhysChanOutputType                                               =int32(-200432)
DAQmxErrorPhysChanMeasType                                                 =int32(-200431)
DAQmxErrorInvalidPhysChanType                                              =int32(-200430)
DAQmxErrorLabVIEWEmptyTaskOrChans                                          =int32(-200429)
DAQmxErrorLabVIEWInvalidTaskOrChans                                        =int32(-200428)
DAQmxErrorInvalidRefClkRate                                                =int32(-200427)
DAQmxErrorInvalidExtTrigImpedance                                          =int32(-200426)
DAQmxErrorHystTrigLevelAIMax                                               =int32(-200425)
DAQmxErrorLineNumIncompatibleWithVideoSignalFormat                         =int32(-200424)
DAQmxErrorTrigWindowAIMinAIMaxCombo                                        =int32(-200423)
DAQmxErrorTrigAIMinAIMax                                                   =int32(-200422)
DAQmxErrorHystTrigLevelAIMin                                               =int32(-200421)
DAQmxErrorInvalidSampRateConsiderRIS                                       =int32(-200420)
DAQmxErrorInvalidReadPosDuringRIS                                          =int32(-200419)
DAQmxErrorImmedTrigDuringRISMode                                           =int32(-200418)
DAQmxErrorTDCNotEnabledDuringRISMode                                       =int32(-200417)
DAQmxErrorMultiRecWithRIS                                                  =int32(-200416)
DAQmxErrorInvalidRefClkSrc                                                 =int32(-200415)
DAQmxErrorInvalidSampClkSrc                                                =int32(-200414)
DAQmxErrorInsufficientOnBoardMemForNumRecsAndSamps                         =int32(-200413)
DAQmxErrorInvalidAIAttenuation                                             =int32(-200412)
DAQmxErrorACCouplingNotAllowedWith50OhmImpedance                           =int32(-200411)
DAQmxErrorInvalidRecordNum                                                 =int32(-200410)
DAQmxErrorZeroSlopeLinearScale                                             =int32(-200409)
DAQmxErrorZeroReversePolyScaleCoeffs                                       =int32(-200408)
DAQmxErrorZeroForwardPolyScaleCoeffs                                       =int32(-200407)
DAQmxErrorNoReversePolyScaleCoeffs                                         =int32(-200406)
DAQmxErrorNoForwardPolyScaleCoeffs                                         =int32(-200405)
DAQmxErrorNoPolyScaleCoeffs                                                =int32(-200404)
DAQmxErrorReversePolyOrderLessThanNumPtsToCompute                          =int32(-200403)
DAQmxErrorReversePolyOrderNotPositive                                      =int32(-200402)
DAQmxErrorNumPtsToComputeNotPositive                                       =int32(-200401)
DAQmxErrorWaveformLengthNotMultipleOfIncr                                  =int32(-200400)
DAQmxErrorCAPINoExtendedErrorInfoAvailable                                 =int32(-200399)
DAQmxErrorCVIFunctionNotFoundInDAQmxDLL                                    =int32(-200398)
DAQmxErrorCVIFailedToLoadDAQmxDLL                                          =int32(-200397)
DAQmxErrorNoCommonTrigLineForImmedRoute                                    =int32(-200396)
DAQmxErrorNoCommonTrigLineForTaskRoute                                     =int32(-200395)
DAQmxErrorF64PrptyValNotUnsignedInt                                        =int32(-200394)
DAQmxErrorRegisterNotWritable                                              =int32(-200393)
DAQmxErrorInvalidOutputVoltageAtSampClkRate                                =int32(-200392)
DAQmxErrorStrobePhaseShiftDCMBecameUnlocked                                =int32(-200391)
DAQmxErrorDrivePhaseShiftDCMBecameUnlocked                                 =int32(-200390)
DAQmxErrorClkOutPhaseShiftDCMBecameUnlocked                                =int32(-200389)
DAQmxErrorOutputBoardClkDCMBecameUnlocked                                  =int32(-200388)
DAQmxErrorInputBoardClkDCMBecameUnlocked                                   =int32(-200387)
DAQmxErrorInternalClkDCMBecameUnlocked                                     =int32(-200386)
DAQmxErrorDCMLock                                                          =int32(-200385)
DAQmxErrorDataLineReservedForDynamicOutput                                 =int32(-200384)
DAQmxErrorInvalidRefClkSrcGivenSampClkSrc                                  =int32(-200383)
DAQmxErrorNoPatternMatcherAvailable                                        =int32(-200382)
DAQmxErrorInvalidDelaySampRateBelowPhaseShiftDCMThresh                     =int32(-200381)
DAQmxErrorStrainGageCalibration                                            =int32(-200380)
DAQmxErrorInvalidExtClockFreqAndDivCombo                                   =int32(-200379)
DAQmxErrorCustomScaleDoesNotExist                                          =int32(-200378)
DAQmxErrorOnlyFrontEndChanOpsDuringScan                                    =int32(-200377)
DAQmxErrorInvalidOptionForDigitalPortChannel                               =int32(-200376)
DAQmxErrorUnsupportedSignalTypeExportSignal                                =int32(-200375)
DAQmxErrorInvalidSignalTypeExportSignal                                    =int32(-200374)
DAQmxErrorUnsupportedTrigTypeSendsSWTrig                                   =int32(-200373)
DAQmxErrorInvalidTrigTypeSendsSWTrig                                       =int32(-200372)
DAQmxErrorRepeatedPhysicalChan                                             =int32(-200371)
DAQmxErrorResourcesInUseForRouteInTask                                     =int32(-200370)
DAQmxErrorResourcesInUseForRoute                                           =int32(-200369)
DAQmxErrorRouteNotSupportedByHW                                            =int32(-200368)
DAQmxErrorResourcesInUseForExportSignalPolarity                            =int32(-200367)
DAQmxErrorResourcesInUseForInversionInTask                                 =int32(-200366)
DAQmxErrorResourcesInUseForInversion                                       =int32(-200365)
DAQmxErrorExportSignalPolarityNotSupportedByHW                             =int32(-200364)
DAQmxErrorInversionNotSupportedByHW                                        =int32(-200363)
DAQmxErrorOverloadedChansExistNotRead                                      =int32(-200362)
DAQmxErrorInputFIFOOverflow2                                               =int32(-200361)
DAQmxErrorCJCChanNotSpecd                                                  =int32(-200360)
DAQmxErrorCtrExportSignalNotPossible                                       =int32(-200359)
DAQmxErrorRefTrigWhenContinuous                                            =int32(-200358)
DAQmxErrorIncompatibleSensorOutputAndDeviceInputRanges                     =int32(-200357)
DAQmxErrorCustomScaleNameUsed                                              =int32(-200356)
DAQmxErrorPropertyValNotSupportedByHW                                      =int32(-200355)
DAQmxErrorPropertyValNotValidTermName                                      =int32(-200354)
DAQmxErrorResourcesInUseForProperty                                        =int32(-200353)
DAQmxErrorCJCChanAlreadyUsed                                               =int32(-200352)
DAQmxErrorForwardPolynomialCoefNotSpecd                                    =int32(-200351)
DAQmxErrorTableScaleNumPreScaledAndScaledValsNotEqual                      =int32(-200350)
DAQmxErrorTableScalePreScaledValsNotSpecd                                  =int32(-200349)
DAQmxErrorTableScaleScaledValsNotSpecd                                     =int32(-200348)
DAQmxErrorIntermediateBufferSizeNotMultipleOfIncr                          =int32(-200347)
DAQmxErrorEventPulseWidthOutOfRange                                        =int32(-200346)
DAQmxErrorEventDelayOutOfRange                                             =int32(-200345)
DAQmxErrorSampPerChanNotMultipleOfIncr                                     =int32(-200344)
DAQmxErrorCannotCalculateNumSampsTaskNotStarted                            =int32(-200343)
DAQmxErrorScriptNotInMem                                                   =int32(-200342)
DAQmxErrorOnboardMemTooSmall                                               =int32(-200341)
DAQmxErrorReadAllAvailableDataWithoutBuffer                                =int32(-200340)
DAQmxErrorPulseActiveAtStart                                               =int32(-200339)
DAQmxErrorCalTempNotSupported                                              =int32(-200338)
DAQmxErrorDelayFromSampClkTooLong                                          =int32(-200337)
DAQmxErrorDelayFromSampClkTooShort                                         =int32(-200336)
DAQmxErrorAIConvRateTooHigh                                                =int32(-200335)
DAQmxErrorDelayFromStartTrigTooLong                                        =int32(-200334)
DAQmxErrorDelayFromStartTrigTooShort                                       =int32(-200333)
DAQmxErrorSampRateTooHigh                                                  =int32(-200332)
DAQmxErrorSampRateTooLow                                                   =int32(-200331)
DAQmxErrorPFI0UsedForAnalogAndDigitalSrc                                   =int32(-200330)
DAQmxErrorPrimingCfgFIFO                                                   =int32(-200329)
DAQmxErrorCannotOpenTopologyCfgFile                                        =int32(-200328)
DAQmxErrorInvalidDTInsideWfmDataType                                       =int32(-200327)
DAQmxErrorRouteSrcAndDestSame                                              =int32(-200326)
DAQmxErrorReversePolynomialCoefNotSpecd                                    =int32(-200325)
DAQmxErrorDevAbsentOrUnavailable                                           =int32(-200324)
DAQmxErrorNoAdvTrigForMultiDevScan                                         =int32(-200323)
DAQmxErrorInterruptsInsufficientDataXferMech                               =int32(-200322)
DAQmxErrorInvalidAttentuationBasedOnMinMax                                 =int32(-200321)
DAQmxErrorCabledModuleCannotRouteSSH                                       =int32(-200320)
DAQmxErrorCabledModuleCannotRouteConvClk                                   =int32(-200319)
DAQmxErrorInvalidExcitValForScaling                                        =int32(-200318)
DAQmxErrorNoDevMemForScript                                                =int32(-200317)
DAQmxErrorScriptDataUnderflow                                              =int32(-200316)
DAQmxErrorNoDevMemForWaveform                                              =int32(-200315)
DAQmxErrorStreamDCMBecameUnlocked                                          =int32(-200314)
DAQmxErrorStreamDCMLock                                                    =int32(-200313)
DAQmxErrorWaveformNotInMem                                                 =int32(-200312)
DAQmxErrorWaveformWriteOutOfBounds                                         =int32(-200311)
DAQmxErrorWaveformPreviouslyAllocated                                      =int32(-200310)
DAQmxErrorSampClkTbMasterTbDivNotAppropriateForSampTbSrc                   =int32(-200309)
DAQmxErrorSampTbRateSampTbSrcMismatch                                      =int32(-200308)
DAQmxErrorMasterTbRateMasterTbSrcMismatch                                  =int32(-200307)
DAQmxErrorSampsPerChanTooBig                                               =int32(-200306)
DAQmxErrorFinitePulseTrainNotPossible                                      =int32(-200305)
DAQmxErrorExtMasterTimebaseRateNotSpecified                                =int32(-200304)
DAQmxErrorExtSampClkSrcNotSpecified                                        =int32(-200303)
DAQmxErrorInputSignalSlowerThanMeasTime                                    =int32(-200302)
DAQmxErrorCannotUpdatePulseGenProperty                                     =int32(-200301)
DAQmxErrorInvalidTimingType                                                =int32(-200300)
DAQmxErrorPropertyUnavailWhenUsingOnboardMemory                            =int32(-200297)
DAQmxErrorCannotWriteAfterStartWithOnboardMemory                           =int32(-200295)
DAQmxErrorNotEnoughSampsWrittenForInitialXferRqstCondition                 =int32(-200294)
DAQmxErrorNoMoreSpace                                                      =int32(-200293)
DAQmxErrorSamplesCanNotYetBeWritten                                        =int32(-200292)
DAQmxErrorGenStoppedToPreventIntermediateBufferRegenOfOldSamples           =int32(-200291)
DAQmxErrorGenStoppedToPreventRegenOfOldSamples                             =int32(-200290)
DAQmxErrorSamplesNoLongerWriteable                                         =int32(-200289)
DAQmxErrorSamplesWillNeverBeGenerated                                      =int32(-200288)
DAQmxErrorNegativeWriteSampleNumber                                        =int32(-200287)
DAQmxErrorNoAcqStarted                                                     =int32(-200286)
DAQmxErrorSamplesNotYetAvailable                                           =int32(-200284)
DAQmxErrorAcqStoppedToPreventIntermediateBufferOverflow                    =int32(-200283)
DAQmxErrorNoRefTrigConfigured                                              =int32(-200282)
DAQmxErrorCannotReadRelativeToRefTrigUntilDone                             =int32(-200281)
DAQmxErrorSamplesNoLongerAvailable                                         =int32(-200279)
DAQmxErrorSamplesWillNeverBeAvailable                                      =int32(-200278)
DAQmxErrorNegativeReadSampleNumber                                         =int32(-200277)
DAQmxErrorExternalSampClkAndRefClkThruSameTerm                             =int32(-200276)
DAQmxErrorExtSampClkRateTooLowForClkIn                                     =int32(-200275)
DAQmxErrorExtSampClkRateTooHighForBackplane                                =int32(-200274)
DAQmxErrorSampClkRateAndDivCombo                                           =int32(-200273)
DAQmxErrorSampClkRateTooLowForDivDown                                      =int32(-200272)
DAQmxErrorProductOfAOMinAndGainTooSmall                                    =int32(-200271)
DAQmxErrorInterpolationRateNotPossible                                     =int32(-200270)
DAQmxErrorOffsetTooLarge                                                   =int32(-200269)
DAQmxErrorOffsetTooSmall                                                   =int32(-200268)
DAQmxErrorProductOfAOMaxAndGainTooLarge                                    =int32(-200267)
DAQmxErrorMinAndMaxNotSymmetric                                            =int32(-200266)
DAQmxErrorInvalidAnalogTrigSrc                                             =int32(-200265)
DAQmxErrorTooManyChansForAnalogRefTrig                                     =int32(-200264)
DAQmxErrorTooManyChansForAnalogPauseTrig                                   =int32(-200263)
DAQmxErrorTrigWhenOnDemandSampTiming                                       =int32(-200262)
DAQmxErrorInconsistentAnalogTrigSettings                                   =int32(-200261)
DAQmxErrorMemMapDataXferModeSampTimingCombo                                =int32(-200260)
DAQmxErrorInvalidJumperedAttr                                              =int32(-200259)
DAQmxErrorInvalidGainBasedOnMinMax                                         =int32(-200258)
DAQmxErrorInconsistentExcit                                                =int32(-200257)
DAQmxErrorTopologyNotSupportedByCfgTermBlock                               =int32(-200256)
DAQmxErrorBuiltInTempSensorNotSupported                                    =int32(-200255)
DAQmxErrorInvalidTerm                                                      =int32(-200254)
DAQmxErrorCannotTristateTerm                                               =int32(-200253)
DAQmxErrorCannotTristateBusyTerm                                           =int32(-200252)
DAQmxErrorNoDMAChansAvailable                                              =int32(-200251)
DAQmxErrorInvalidWaveformLengthWithinLoopInScript                          =int32(-200250)
DAQmxErrorInvalidSubsetLengthWithinLoopInScript                            =int32(-200249)
DAQmxErrorMarkerPosInvalidForLoopInScript                                  =int32(-200248)
DAQmxErrorIntegerExpectedInScript                                          =int32(-200247)
DAQmxErrorPLLBecameUnlocked                                                =int32(-200246)
DAQmxErrorPLLLock                                                          =int32(-200245)
DAQmxErrorDDCClkOutDCMBecameUnlocked                                       =int32(-200244)
DAQmxErrorDDCClkOutDCMLock                                                 =int32(-200243)
DAQmxErrorClkDoublerDCMBecameUnlocked                                      =int32(-200242)
DAQmxErrorClkDoublerDCMLock                                                =int32(-200241)
DAQmxErrorSampClkDCMBecameUnlocked                                         =int32(-200240)
DAQmxErrorSampClkDCMLock                                                   =int32(-200239)
DAQmxErrorSampClkTimebaseDCMBecameUnlocked                                 =int32(-200238)
DAQmxErrorSampClkTimebaseDCMLock                                           =int32(-200237)
DAQmxErrorAttrCannotBeReset                                                =int32(-200236)
DAQmxErrorExplanationNotFound                                              =int32(-200235)
DAQmxErrorWriteBufferTooSmall                                              =int32(-200234)
DAQmxErrorSpecifiedAttrNotValid                                            =int32(-200233)
DAQmxErrorAttrCannotBeRead                                                 =int32(-200232)
DAQmxErrorAttrCannotBeSet                                                  =int32(-200231)
DAQmxErrorNULLPtrForC_Api                                                  =int32(-200230)
DAQmxErrorReadBufferTooSmall                                               =int32(-200229)
DAQmxErrorBufferTooSmallForString                                          =int32(-200228)
DAQmxErrorNoAvailTrigLinesOnDevice                                         =int32(-200227)
DAQmxErrorTrigBusLineNotAvail                                              =int32(-200226)
DAQmxErrorCouldNotReserveRequestedTrigLine                                 =int32(-200225)
DAQmxErrorTrigLineNotFound                                                 =int32(-200224)
DAQmxErrorSCXI1126ThreshHystCombination                                    =int32(-200223)
DAQmxErrorAcqStoppedToPreventInputBufferOverwrite                          =int32(-200222)
DAQmxErrorTimeoutExceeded                                                  =int32(-200221)
DAQmxErrorInvalidDeviceID                                                  =int32(-200220)
DAQmxErrorInvalidAOChanOrder                                               =int32(-200219)
DAQmxErrorSampleTimingTypeAndDataXferMode                                  =int32(-200218)
DAQmxErrorBufferWithOnDemandSampTiming                                     =int32(-200217)
DAQmxErrorBufferAndDataXferMode                                            =int32(-200216)
DAQmxErrorMemMapAndBuffer                                                  =int32(-200215)
DAQmxErrorNoAnalogTrigHW                                                   =int32(-200214)
DAQmxErrorTooManyPretrigPlusMinPostTrigSamps                               =int32(-200213)
DAQmxErrorInconsistentUnitsSpecified                                       =int32(-200212)
DAQmxErrorMultipleRelaysForSingleRelayOp                                   =int32(-200211)
DAQmxErrorMultipleDevIDsPerChassisSpecifiedInList                          =int32(-200210)
DAQmxErrorDuplicateDevIDInList                                             =int32(-200209)
DAQmxErrorInvalidRangeStatementCharInList                                  =int32(-200208)
DAQmxErrorInvalidDeviceIDInList                                            =int32(-200207)
DAQmxErrorTriggerPolarityConflict                                          =int32(-200206)
DAQmxErrorCannotScanWithCurrentTopology                                    =int32(-200205)
DAQmxErrorUnexpectedIdentifierInFullySpecifiedPathInList                   =int32(-200204)
DAQmxErrorSwitchCannotDriveMultipleTrigLines                               =int32(-200203)
DAQmxErrorInvalidRelayName                                                 =int32(-200202)
DAQmxErrorSwitchScanlistTooBig                                             =int32(-200201)
DAQmxErrorSwitchChanInUse                                                  =int32(-200200)
DAQmxErrorSwitchNotResetBeforeScan                                         =int32(-200199)
DAQmxErrorInvalidTopology                                                  =int32(-200198)
DAQmxErrorAttrNotSupported                                                 =int32(-200197)
DAQmxErrorUnexpectedEndOfActionsInList                                     =int32(-200196)
DAQmxErrorPowerBudgetExceeded                                              =int32(-200195)
DAQmxErrorHWUnexpectedlyPoweredOffAndOn                                    =int32(-200194)
DAQmxErrorSwitchOperationNotSupported                                      =int32(-200193)
DAQmxErrorOnlyContinuousScanSupported                                      =int32(-200192)
DAQmxErrorSwitchDifferentTopologyWhenScanning                              =int32(-200191)
DAQmxErrorDisconnectPathNotSameAsExistingPath                              =int32(-200190)
DAQmxErrorConnectionNotPermittedOnChanReservedForRouting                   =int32(-200189)
DAQmxErrorCannotConnectSrcChans                                            =int32(-200188)
DAQmxErrorCannotConnectChannelToItself                                     =int32(-200187)
DAQmxErrorChannelNotReservedForRouting                                     =int32(-200186)
DAQmxErrorCannotConnectChansDirectly                                       =int32(-200185)
DAQmxErrorChansAlreadyConnected                                            =int32(-200184)
DAQmxErrorChanDuplicatedInPath                                             =int32(-200183)
DAQmxErrorNoPathToDisconnect                                               =int32(-200182)
DAQmxErrorInvalidSwitchChan                                                =int32(-200181)
DAQmxErrorNoPathAvailableBetween2SwitchChans                               =int32(-200180)
DAQmxErrorExplicitConnectionExists                                         =int32(-200179)
DAQmxErrorSwitchDifferentSettlingTimeWhenScanning                          =int32(-200178)
DAQmxErrorOperationOnlyPermittedWhileScanning                              =int32(-200177)
DAQmxErrorOperationNotPermittedWhileScanning                               =int32(-200176)
DAQmxErrorHardwareNotResponding                                            =int32(-200175)
DAQmxErrorInvalidSampAndMasterTimebaseRateCombo                            =int32(-200173)
DAQmxErrorNonZeroBufferSizeInProgIOXfer                                    =int32(-200172)
DAQmxErrorVirtualChanNameUsed                                              =int32(-200171)
DAQmxErrorPhysicalChanDoesNotExist                                         =int32(-200170)
DAQmxErrorMemMapOnlyForProgIOXfer                                          =int32(-200169)
DAQmxErrorTooManyChans                                                     =int32(-200168)
DAQmxErrorCannotHaveCJTempWithOtherChans                                   =int32(-200167)
DAQmxErrorOutputBufferUnderwrite                                           =int32(-200166)
DAQmxErrorSensorInvalidCompletionResistance                                =int32(-200163)
DAQmxErrorVoltageExcitIncompatibleWith2WireCfg                             =int32(-200162)
DAQmxErrorIntExcitSrcNotAvailable                                          =int32(-200161)
DAQmxErrorCannotCreateChannelAfterTaskVerified                             =int32(-200160)
DAQmxErrorLinesReservedForSCXIControl                                      =int32(-200159)
DAQmxErrorCouldNotReserveLinesForSCXIControl                               =int32(-200158)
DAQmxErrorCalibrationFailed                                                =int32(-200157)
DAQmxErrorReferenceFrequencyInvalid                                        =int32(-200156)
DAQmxErrorReferenceResistanceInvalid                                       =int32(-200155)
DAQmxErrorReferenceCurrentInvalid                                          =int32(-200154)
DAQmxErrorReferenceVoltageInvalid                                          =int32(-200153)
DAQmxErrorEEPROMDataInvalid                                                =int32(-200152)
DAQmxErrorCabledModuleNotCapableOfRoutingAI                                =int32(-200151)
DAQmxErrorChannelNotAvailableInParallelMode                                =int32(-200150)
DAQmxErrorExternalTimebaseRateNotKnownForDelay                             =int32(-200149)
DAQmxErrorFREQOUTCannotProduceDesiredFrequency                             =int32(-200148)
DAQmxErrorMultipleCounterInputTask                                         =int32(-200147)
DAQmxErrorCounterStartPauseTriggerConflict                                 =int32(-200146)
DAQmxErrorCounterInputPauseTriggerAndSampleClockInvalid                    =int32(-200145)
DAQmxErrorCounterOutputPauseTriggerInvalid                                 =int32(-200144)
DAQmxErrorCounterTimebaseRateNotSpecified                                  =int32(-200143)
DAQmxErrorCounterTimebaseRateNotFound                                      =int32(-200142)
DAQmxErrorCounterOverflow                                                  =int32(-200141)
DAQmxErrorCounterNoTimebaseEdgesBetweenGates                               =int32(-200140)
DAQmxErrorCounterMaxMinRangeFreq                                           =int32(-200139)
DAQmxErrorCounterMaxMinRangeTime                                           =int32(-200138)
DAQmxErrorSuitableTimebaseNotFoundTimeCombo                                =int32(-200137)
DAQmxErrorSuitableTimebaseNotFoundFrequencyCombo                           =int32(-200136)
DAQmxErrorInternalTimebaseSourceDivisorCombo                               =int32(-200135)
DAQmxErrorInternalTimebaseSourceRateCombo                                  =int32(-200134)
DAQmxErrorInternalTimebaseRateDivisorSourceCombo                           =int32(-200133)
DAQmxErrorExternalTimebaseRateNotknownForRate                              =int32(-200132)
DAQmxErrorAnalogTrigChanNotFirstInScanList                                 =int32(-200131)
DAQmxErrorNoDivisorForExternalSignal                                       =int32(-200130)
DAQmxErrorAttributeInconsistentAcrossRepeatedPhysicalChannels              =int32(-200128)
DAQmxErrorCannotHandshakeWithPort0                                         =int32(-200127)
DAQmxErrorControlLineConflictOnPortC                                       =int32(-200126)
DAQmxErrorLines4To7ConfiguredForOutput                                     =int32(-200125)
DAQmxErrorLines4To7ConfiguredForInput                                      =int32(-200124)
DAQmxErrorLines0To3ConfiguredForOutput                                     =int32(-200123)
DAQmxErrorLines0To3ConfiguredForInput                                      =int32(-200122)
DAQmxErrorPortConfiguredForOutput                                          =int32(-200121)
DAQmxErrorPortConfiguredForInput                                           =int32(-200120)
DAQmxErrorPortConfiguredForStaticDigitalOps                                =int32(-200119)
DAQmxErrorPortReservedForHandshaking                                       =int32(-200118)
DAQmxErrorPortDoesNotSupportHandshakingDataIO                              =int32(-200117)
DAQmxErrorCannotTristate8255OutputLines                                    =int32(-200116)
DAQmxErrorTemperatureOutOfRangeForCalibration                              =int32(-200113)
DAQmxErrorCalibrationHandleInvalid                                         =int32(-200112)
DAQmxErrorPasswordRequired                                                 =int32(-200111)
DAQmxErrorIncorrectPassword                                                =int32(-200110)
DAQmxErrorPasswordTooLong                                                  =int32(-200109)
DAQmxErrorCalibrationSessionAlreadyOpen                                    =int32(-200108)
DAQmxErrorSCXIModuleIncorrect                                              =int32(-200107)
DAQmxErrorAttributeInconsistentAcrossChannelsOnDevice                      =int32(-200106)
DAQmxErrorSCXI1122ResistanceChanNotSupportedForCfg                         =int32(-200105)
DAQmxErrorBracketPairingMismatchInList                                     =int32(-200104)
DAQmxErrorInconsistentNumSamplesToWrite                                    =int32(-200103)
DAQmxErrorIncorrectDigitalPattern                                          =int32(-200102)
DAQmxErrorIncorrectNumChannelsToWrite                                      =int32(-200101)
DAQmxErrorIncorrectReadFunction                                            =int32(-200100)
DAQmxErrorPhysicalChannelNotSpecified                                      =int32(-200099)
DAQmxErrorMoreThanOneTerminal                                              =int32(-200098)
DAQmxErrorMoreThanOneActiveChannelSpecified                                =int32(-200097)
DAQmxErrorInvalidNumberSamplesToRead                                       =int32(-200096)
DAQmxErrorAnalogWaveformExpected                                           =int32(-200095)
DAQmxErrorDigitalWaveformExpected                                          =int32(-200094)
DAQmxErrorActiveChannelNotSpecified                                        =int32(-200093)
DAQmxErrorFunctionNotSupportedForDeviceTasks                               =int32(-200092)
DAQmxErrorFunctionNotInLibrary                                             =int32(-200091)
DAQmxErrorLibraryNotPresent                                                =int32(-200090)
DAQmxErrorDuplicateTask                                                    =int32(-200089)
DAQmxErrorInvalidTask                                                      =int32(-200088)
DAQmxErrorInvalidChannel                                                   =int32(-200087)
DAQmxErrorInvalidSyntaxForPhysicalChannelRange                             =int32(-200086)
DAQmxErrorMinNotLessThanMax                                                =int32(-200082)
DAQmxErrorSampleRateNumChansConvertPeriodCombo                             =int32(-200081)
DAQmxErrorAODuringCounter1DMAConflict                                      =int32(-200079)
DAQmxErrorAIDuringCounter0DMAConflict                                      =int32(-200078)
DAQmxErrorInvalidAttributeValue                                            =int32(-200077)
DAQmxErrorSuppliedCurrentDataOutsideSpecifiedRange                         =int32(-200076)
DAQmxErrorSuppliedVoltageDataOutsideSpecifiedRange                         =int32(-200075)
DAQmxErrorCannotStoreCalConst                                              =int32(-200074)
DAQmxErrorSCXIModuleNotFound                                               =int32(-200073)
DAQmxErrorDuplicatePhysicalChansNotSupported                               =int32(-200072)
DAQmxErrorTooManyPhysicalChansInList                                       =int32(-200071)
DAQmxErrorInvalidAdvanceEventTriggerType                                   =int32(-200070)
DAQmxErrorDeviceIsNotAValidSwitch                                          =int32(-200069)
DAQmxErrorDeviceDoesNotSupportScanning                                     =int32(-200068)
DAQmxErrorScanListCannotBeTimed                                            =int32(-200067)
DAQmxErrorConnectOperatorInvalidAtPointInList                              =int32(-200066)
DAQmxErrorUnexpectedSwitchActionInList                                     =int32(-200065)
DAQmxErrorUnexpectedSeparatorInList                                        =int32(-200064)
DAQmxErrorExpectedTerminatorInList                                         =int32(-200063)
DAQmxErrorExpectedConnectOperatorInList                                    =int32(-200062)
DAQmxErrorExpectedSeparatorInList                                          =int32(-200061)
DAQmxErrorFullySpecifiedPathInListContainsRange                            =int32(-200060)
DAQmxErrorConnectionSeparatorAtEndOfList                                   =int32(-200059)
DAQmxErrorIdentifierInListTooLong                                          =int32(-200058)
DAQmxErrorDuplicateDeviceIDInListWhenSettling                              =int32(-200057)
DAQmxErrorChannelNameNotSpecifiedInList                                    =int32(-200056)
DAQmxErrorDeviceIDNotSpecifiedInList                                       =int32(-200055)
DAQmxErrorSemicolonDoesNotFollowRangeInList                                =int32(-200054)
DAQmxErrorSwitchActionInListSpansMultipleDevices                           =int32(-200053)
DAQmxErrorRangeWithoutAConnectActionInList                                 =int32(-200052)
DAQmxErrorInvalidIdentifierFollowingSeparatorInList                        =int32(-200051)
DAQmxErrorInvalidChannelNameInList                                         =int32(-200050)
DAQmxErrorInvalidNumberInRepeatStatementInList                             =int32(-200049)
DAQmxErrorInvalidTriggerLineInList                                         =int32(-200048)
DAQmxErrorInvalidIdentifierInListFollowingDeviceID                         =int32(-200047)
DAQmxErrorInvalidIdentifierInListAtEndOfSwitchAction                       =int32(-200046)
DAQmxErrorDeviceRemoved                                                    =int32(-200045)
DAQmxErrorRoutingPathNotAvailable                                          =int32(-200044)
DAQmxErrorRoutingHardwareBusy                                              =int32(-200043)
DAQmxErrorRequestedSignalInversionForRoutingNotPossible                    =int32(-200042)
DAQmxErrorInvalidRoutingDestinationTerminalName                            =int32(-200041)
DAQmxErrorInvalidRoutingSourceTerminalName                                 =int32(-200040)
DAQmxErrorRoutingNotSupportedForDevice                                     =int32(-200039)
DAQmxErrorWaitIsLastInstructionOfLoopInScript                              =int32(-200038)
DAQmxErrorClearIsLastInstructionOfLoopInScript                             =int32(-200037)
DAQmxErrorInvalidLoopIterationsInScript                                    =int32(-200036)
DAQmxErrorRepeatLoopNestingTooDeepInScript                                 =int32(-200035)
DAQmxErrorMarkerPositionOutsideSubsetInScript                              =int32(-200034)
DAQmxErrorSubsetStartOffsetNotAlignedInScript                              =int32(-200033)
DAQmxErrorInvalidSubsetLengthInScript                                      =int32(-200032)
DAQmxErrorMarkerPositionNotAlignedInScript                                 =int32(-200031)
DAQmxErrorSubsetOutsideWaveformInScript                                    =int32(-200030)
DAQmxErrorMarkerOutsideWaveformInScript                                    =int32(-200029)
DAQmxErrorWaveformInScriptNotInMem                                         =int32(-200028)
DAQmxErrorKeywordExpectedInScript                                          =int32(-200027)
DAQmxErrorBufferNameExpectedInScript                                       =int32(-200026)
DAQmxErrorProcedureNameExpectedInScript                                    =int32(-200025)
DAQmxErrorScriptHasInvalidIdentifier                                       =int32(-200024)
DAQmxErrorScriptHasInvalidCharacter                                        =int32(-200023)
DAQmxErrorResourceAlreadyReserved                                          =int32(-200022)
DAQmxErrorSelfTestFailed                                                   =int32(-200020)
DAQmxErrorADCOverrun                                                       =int32(-200019)
DAQmxErrorDACUnderflow                                                     =int32(-200018)
DAQmxErrorInputFIFOUnderflow                                               =int32(-200017)
DAQmxErrorOutputFIFOUnderflow                                              =int32(-200016)
DAQmxErrorSCXISerialCommunication                                          =int32(-200015)
DAQmxErrorDigitalTerminalSpecifiedMoreThanOnce                             =int32(-200014)
DAQmxErrorDigitalOutputNotSupported                                        =int32(-200012)
DAQmxErrorInconsistentChannelDirections                                    =int32(-200011)
DAQmxErrorInputFIFOOverflow                                                =int32(-200010)
DAQmxErrorTimeStampOverwritten                                             =int32(-200009)
DAQmxErrorStopTriggerHasNotOccurred                                        =int32(-200008)
DAQmxErrorRecordNotAvailable                                               =int32(-200007)
DAQmxErrorRecordOverwritten                                                =int32(-200006)
DAQmxErrorDataNotAvailable                                                 =int32(-200005)
DAQmxErrorDataOverwrittenInDeviceMemory                                    =int32(-200004)
DAQmxErrorDuplicatedChannel                                                =int32(-200003)
DAQmxWarningTimestampCounterRolledOver                                      =int32(200003)
DAQmxWarningInputTerminationOverloaded                                      =int32(200004)
DAQmxWarningADCOverloaded                                                   =int32(200005)
DAQmxWarningPLLUnlocked                                                     =int32(200007)
DAQmxWarningCounter0DMADuringAIConflict                                     =int32(200008)
DAQmxWarningCounter1DMADuringAOConflict                                     =int32(200009)
DAQmxWarningStoppedBeforeDone                                               =int32(200010)
DAQmxWarningRateViolatesSettlingTime                                        =int32(200011)
DAQmxWarningRateViolatesMaxADCRate                                          =int32(200012)
DAQmxWarningUserDefInfoStringTooLong                                        =int32(200013)
DAQmxWarningTooManyInterruptsPerSecond                                      =int32(200014)
DAQmxWarningPotentialGlitchDuringWrite                                      =int32(200015)
DAQmxWarningDevNotSelfCalibratedWithDAQmx                                   =int32(200016)
DAQmxWarningAISampRateTooLow                                                =int32(200017)
DAQmxWarningAIConvRateTooLow                                                =int32(200018)
DAQmxWarningReadOffsetCoercion                                              =int32(200019)
DAQmxWarningPretrigCoercion                                                 =int32(200020)
DAQmxWarningSampValCoercedToMax                                             =int32(200021)
DAQmxWarningSampValCoercedToMin                                             =int32(200022)
DAQmxWarningPropertyVersionNew                                              =int32(200024)
DAQmxWarningUserDefinedInfoTooLong                                          =int32(200025)
DAQmxWarningCAPIStringTruncatedToFitBuffer                                  =int32(200026)
DAQmxWarningSampClkRateTooLow                                               =int32(200027)
DAQmxWarningPossiblyInvalidCTRSampsInFiniteDMAAcq                           =int32(200028)
DAQmxWarningRISAcqCompletedSomeBinsNotFilled                                =int32(200029)
DAQmxWarningPXIDevTempExceedsMaxOpTemp                                      =int32(200030)
DAQmxWarningOutputGainTooLowForRFFreq                                       =int32(200031)
DAQmxWarningOutputGainTooHighForRFFreq                                      =int32(200032)
DAQmxWarningMultipleWritesBetweenSampClks                                   =int32(200033)
DAQmxWarningDeviceMayShutDownDueToHighTemp                                  =int32(200034)
DAQmxWarningRateViolatesMinADCRate                                          =int32(200035)
DAQmxWarningSampClkRateAboveDevSpecs                                        =int32(200036)
DAQmxWarningCOPrevDAQmxWriteSettingsOverwrittenForHWTimedSinglePoint        =int32(200037)
DAQmxWarningReadNotCompleteBeforeSampClk                                    =int32(209800)
DAQmxWarningWriteNotCompleteBeforeSampClk                                   =int32(209801)
DAQmxErrorInvalidSignalModifier_Routing                                     =int32(-89150)
DAQmxErrorRoutingDestTermPXIClk10InNotInSlot2_Routing                       =int32(-89149)
DAQmxErrorRoutingDestTermPXIStarXNotInSlot2_Routing                         =int32(-89148)
DAQmxErrorRoutingSrcTermPXIStarXNotInSlot2_Routing                          =int32(-89147)
DAQmxErrorRoutingSrcTermPXIStarInSlot16AndAbove_Routing                     =int32(-89146)
DAQmxErrorRoutingDestTermPXIStarInSlot16AndAbove_Routing                    =int32(-89145)
DAQmxErrorRoutingDestTermPXIStarInSlot2_Routing                             =int32(-89144)
DAQmxErrorRoutingSrcTermPXIStarInSlot2_Routing                              =int32(-89143)
DAQmxErrorRoutingDestTermPXIChassisNotIdentified_Routing                    =int32(-89142)
DAQmxErrorRoutingSrcTermPXIChassisNotIdentified_Routing                     =int32(-89141)
DAQmxErrorTrigLineNotFoundSingleDevRoute_Routing                            =int32(-89140)
DAQmxErrorNoCommonTrigLineForRoute_Routing                                  =int32(-89139)
DAQmxErrorResourcesInUseForRouteInTask_Routing                              =int32(-89138)
DAQmxErrorResourcesInUseForRoute_Routing                                    =int32(-89137)
DAQmxErrorRouteNotSupportedByHW_Routing                                     =int32(-89136)
DAQmxErrorResourcesInUseForInversionInTask_Routing                          =int32(-89135)
DAQmxErrorResourcesInUseForInversion_Routing                                =int32(-89134)
DAQmxErrorInversionNotSupportedByHW_Routing                                 =int32(-89133)
DAQmxErrorResourcesInUseForProperty_Routing                                 =int32(-89132)
DAQmxErrorRouteSrcAndDestSame_Routing                                       =int32(-89131)
DAQmxErrorDevAbsentOrUnavailable_Routing                                    =int32(-89130)
DAQmxErrorInvalidTerm_Routing                                               =int32(-89129)
DAQmxErrorCannotTristateTerm_Routing                                        =int32(-89128)
DAQmxErrorCannotTristateBusyTerm_Routing                                    =int32(-89127)
DAQmxErrorCouldNotReserveRequestedTrigLine_Routing                          =int32(-89126)
DAQmxErrorTrigLineNotFound_Routing                                          =int32(-89125)
DAQmxErrorRoutingPathNotAvailable_Routing                                   =int32(-89124)
DAQmxErrorRoutingHardwareBusy_Routing                                       =int32(-89123)
DAQmxErrorRequestedSignalInversionForRoutingNotPossible_Routing             =int32(-89122)
DAQmxErrorInvalidRoutingDestinationTerminalName_Routing                     =int32(-89121)
DAQmxErrorInvalidRoutingSourceTerminalName_Routing                          =int32(-89120)
DAQmxStatusCouldNotConnectToServer_Routing                                  =int32(-88900)
DAQmxStatusDeviceNameNotFound_Routing                                       =int32(-88717)
DAQmxStatusLocalRemoteDriverVersionMismatch_Routing                         =int32(-88716)
DAQmxStatusDuplicateDeviceName_Routing                                      =int32(-88715)
DAQmxStatusRuntimeAborting_Routing                                          =int32(-88710)
DAQmxStatusRuntimeAborted_Routing                                           =int32(-88709)
DAQmxStatusResourceNotInPool_Routing                                        =int32(-88708)
DAQmxStatusDriverDeviceGUIDNotFound_Routing                                 =int32(-88705)
