"""
    NiDAQ Ni USB-6008
    SetAO(d, c, v) - set V volts on C chanel on D device
    ReadAIChanal(d,c) - read V volts from C chanel on D device
    ReadAIChanals(d, sc, ec) - read V volts from all chanels from SC start chanle to EC end chanel on D device
                    0 <= SC <= EC <= 7
                    example:
                        data = ReadAIChanals(1, 3, 6) - read from chanals 3 to 6 on device 1 
                        data[3] - value from chanal 3
                        data[4] - value from chanal 4
                        data[5] - value from chanal 5
                        data[6] - value from chanal 6
"""
from NIDAQmxConstants import *
import ctypes
import numpy

nidaq = ctypes.windll.nicaiu # load the DLL
##############################
# Setup some typedefs
# to correspond with values in
# C:\Program Files\National Instruments\NI-DAQ\DAQmx ANSI C Dev\include\NIDAQmx.h
# the typedefs
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32

##############################
def CHK(err):
    """a simple error checking routine"""
    if err < 0:
        buf_size = 1
        buf = ctypes.create_string_buffer('\000' * buf_size)
        nidaq.DAQmxGetErrorString(err,ctypes.byref(buf), buf_size)
        #raise RuntimeError('nidaq call failed with error %d: %s'%(err,repr(buf.value)))
        

def SetAO(DevID = 1, AOchanalID = 0, value = 5):
    chanal = "Dev{0}/ao{1}".format(DevID, AOchanalID)
    data = float64(1.0)
    # value range is betwean 0 and 5V
    value = min(max(value,0),5)
    value64 = float64(value)
    #print chanal, value, value64
    taskHandle = TaskHandle(0)
    CHK(nidaq.DAQmxCreateTask("",ctypes.byref(taskHandle)))
    CHK(nidaq.DAQmxCreateAOVoltageChan(taskHandle,
                                       chanal,
                                       "",
                                       float64(0.0),
                                       float64(5.0),
                                       DAQmx_Val_Volts,
                                       ""));
    CHK(nidaq.DAQmxStartTask(taskHandle));
    CHK(nidaq.DAQmxWriteAnalogScalarF64(taskHandle,
                                        1,
                                        float64(10.0),
                                        value64,
                                        None));
    if taskHandle.value != 0:
        nidaq.DAQmxStopTask(taskHandle)
        nidaq.DAQmxClearTask(taskHandle)

def ReadAIChanal(DevID = 1, AIchanalID = 0):
    chanal = "Dev{0}/ai{1}".format(DevID,AIchanalID)
    hi=float64(10.0)
    lo=float64(-10.0)
    #hi=float64(5.0)
    #lo=float64(0.0)

    # initialize variables
    taskHandle = TaskHandle(0)
    max_num_samples = 1000
    data = float64(0.0)
    #data = numpy.zeros((max_num_samples,),dtype=numpy.float64)
    CHK(nidaq.DAQmxCreateTask("",ctypes.byref(taskHandle)))
    CHK(nidaq.DAQmxCreateAIVoltageChan(taskHandle,
                                       chanal,
                                       "",
                                       DAQmx_Val_Diff,
                                       lo,
                                       hi,
                                       DAQmx_Val_Volts,
                                       None))
    CHK(nidaq.DAQmxCfgSampClkTiming(taskHandle,
                                    "",
                                    float64(10000.0),
                                    DAQmx_Val_Rising,
                                    DAQmx_Val_FiniteSamps,
                                    uInt64(max_num_samples)));
    CHK(nidaq.DAQmxStartTask(taskHandle))
    read = int32()
    CHK(nidaq.DAQmxReadAnalogScalarF64(taskHandle,
                                 ctypes.c_double(-1),
                                 ctypes.byref(data),
                                 None))

    #print "Acquired %d points"%(read.value)
    if taskHandle.value != 0:
        nidaq.DAQmxStopTask(taskHandle)
        nidaq.DAQmxClearTask(taskHandle)
    avgData = data.value
    return avgData
        
def ReadAIChanals(DevID = 1, AIchanalIDstart = 0, AIchanalIDend = 7):
    data = {}
    for x in range(AIchanalIDstart, AIchanalIDend+1):
        data[x] = ReadAIChanal(DevID, x)

    return data
    """
    chanal = "Dev{0}/ai{1}:{2}".format(DevID,AIchanalIDstart, AIchanalIDend)
    print chanal
    # initialize variables
    taskHandle = TaskHandle(0)
    max_num_samples =9
    data = numpy.zeros((max_num_samples,),dtype=numpy.float64)   
    # now, on with the program
    CHK(nidaq.DAQmxCreateTask("",ctypes.byref(taskHandle)))
    CHK(nidaq.DAQmxCreateAIVoltageChan(taskHandle,
                                       "Dev1/ai0:2",
                                       "",          
                                       DAQmx_Val_Diff,            #DAQmx_Val_Diff,   #DAQmx_Val_RSE,       #DAQmx_Val_Cfg_Default,
                                       float64(-10.0),
                                       float64(10.0),
                                       DAQmx_Val_Volts,
                                       None))
    CHK(nidaq.DAQmxCfgSampClkTiming(taskHandle,
                                    "",
                                    float64(1000.0),
                                    DAQmx_Val_Rising,
                                    DAQmx_Val_FiniteSamps,
                                    uInt64(max_num_samples)))
              #DAQmxCfgSampClkTiming(taskHandle,"",sampleRate,DAQmx_Val_Rising,DAQmx_Val_FiniteSamps,sampsPerChan);       
    CHK(nidaq.DAQmxStartTask(taskHandle))
    read = int32()
    
    CHK(nidaq.DAQmxReadAnalogF64(taskHandle,
                                 -1,
                                 float64(1.0),    #Timeout in seconds
                                 DAQmx_Val_GroupByChannel,       #DAQmx_Val_GroupByChannel,    #DAQmx_Val_GroupByScanNumber
                                 data.ctypes.data,
                                 max_num_samples,
                                 ctypes.byref(read),
                                 None))
        
    if taskHandle.value != 0:
        nidaq.DAQmxStopTask(taskHandle)
        nidaq.DAQmxClearTask(taskHandle)
    return data
    """
