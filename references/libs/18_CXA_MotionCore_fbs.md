# 18 CXA_MotionCore_fbs

## 18.1 Introduction and overview

Nodes in the Data Layer can include complex data. This data is serialized data
and can be read out and written consistently.
These data structures are based on the FlatBuffer (Google project). The Flat‐
Buffer is intended to represent complex data structures platform- and pro‐
gramming language-comprehensively.
The basic concept is that a type description is written on a complex date.
From this type description, access methods to a date of this type are provided
for different programming languages.
The PLC is not an exception: The Data Layer can read out a complex date as
a whole and analyze it with access methods. A complex date can also be com‐
posed in the PLC and it can be written to it. During all these operations, the
FlatBuffer is very efficient on how to work on this data. When working with a
date, it is worked directly on the transferred memory or on the memory to be
transferred. Thus, a (de)serialization before or afterwards is not required.
The CXA_MotionCore_fbs library is the PLC library to work with the FlatBuffer
from the Motion app. It includes function blocks allowing access from the IEC
program to complex data structures of the Data Layer of the Motion.
The library provides a function block and subordinate methods for each indi‐
vidual data type to ensure that the individual elements of the data structure
can be read or a FlatBuffer can be created for this data type.

Example

There is a test program below the "_Examples” folder. It can be used to access
the configuration of the Motion in read-only and write mode.

The axis configuration and their axis limits exemplarily show how this Flat‐
Buffer can be read and written. This example is exemplary for all other Flat‐
Buffer included in the CXA_MotionCore_fbs.

## 18.2 Reading axis configuration

The FlatBuffer "motion_core_fbtypes_AxsCfg" and "motion_core_fbtypes_AxsCf‐
gLimits” are exemplarily used to explain how to access this data.
● Retrieving an axis configuration from the ctrlX
  The function block DL_ReadNodeValue from the CXA_Datalayer library can
  retrieve data consistently and completely without interruptions.

VAR
m_NodeValue: DL_NodeValue;
MyReadNodeValue: DL_ReadNodeValue;
m_Execute : BOOL;

    m_data: POINTER TO BYTE;
    m_size: UDINT;
  END_VAR

MyReadNodeValue(Execute:=m_Execute, NodeName:='/motion/axs/Axis_1/cfg', NodeValue:=m_NodeValue);

● Interpreting retrieved data
  The complete data structure is now in the PLC. The retrieved data is of the
  complex data type motion_core_fbTypes_AxsCfg and can be interpreted as
  a complex data type. Thus, there is a "getRootAs_xxx” method in each func‐
  tion block. Call this method once to retrieve further FlatBuffer elements.

VAR
    MyAxsCfg: motion_core_fbtypes_AxsCfg;
END_VAR

MyAxsCfg.getRootAsAxsCfg(m_NodeValue.getData(), m_nodeValue.getSize());

● Retrieving FlatBuffer elements
  There are further "get_xxx” methods in each function block of the
  “motion_core_fbtypes_xxx“. Individual elements can be retrieved with these
  methods.

VAR
    MyAxsProfileName: STRING;
END_VAR

MyAxsProfileName:= MyAxsCfg.getAxisProfileName();

● Accesses to substructures (motion_core_fbs_AxsCfgLimits) in the FlatBuffer
  (motion_core_fbs_AxsCfg)
  Substructures can be included in each FlatBuffer. An entry in a FlatBuffer
  is not mandatory. Thus, only one pointer is returned when accessing such
  elements. If the element is not included in the FlatBuffer, this pointer is
  NULL. It is thus recommended to check the state before it is accessed
  further.

VAR
ptr_AxsLimits : POINTER TO motion_core_fbtypes_AxsCfgLimits;
AxsAcc : LREAL;
  END_VAR

  ptr_AxsLimits := MyAxsCfg.getLimits();
    IF ptr_AxsLimits <> 0 THEN
    ptr_AxsAcc := ptr_AxsLimits^.getAcc();
  END_IF

## 18.3 Writing an axis configuration

To write an axis configuration, create a FlatBuffer of this type in the IEC pro‐
gram first and then transfer this type to the ctrlX CORE. A date is composed
in the memory. When setting the value, individual elements are positioned
directly in the memory in a way that they do not have to be recopied later on.
Use the "FlatBufferBuilder".
● Creating a new FlatBuffer of the type "motion_core_fbs_AxsCfg"

VAR
    builder : CXA_Datalayer.FlatBufferBuilder;
END_VAR

//create an empty flatbuffer – remove previous data from the flatbuffer
builder();

● Writing on the individual FlatBuffer elements (example of the axis limits of
the axis configuration)
Use the methods "add_xxx” to write on the individual elements of a
data structure. These methods always have to be embedded between the
methods "start_xxx" and "end_xxx”.

VAR
    Write_AxsCfgLimits : motion_core_fbtypes_AxsCfgLimits;
    Offset_AxscfgLimits : UDINT;
END_VAR

Write_AxsCfgLimits.startAxsCfgLimits(builder:=MyFbs_AxsCfg);
Write_AxsCfgLimits.addAcc(2000);

Write_AxsCfgLimits.addDec(2000);
Write_AxsCfgLimits.addJrkAcc(4000);
Write_AxsCfgLimits.addJrkDec(4000);
Write_AxsCfgLimits.addPosMax(1000);
Write_AxsCfgLimits.addPosMin(-1000);
Write_AxsCfgLimits.addVelNeg(1000);
Write_AxsCfgLimits.addVelPos(1000);

Offset_AxscfgLimits := Write_AxsCfgLimits.endAxsCfgLimits();
Write_AxsCfg.startAxsCfg(builder:= MyFbs_AxsCfg);
Write_AxsCfg.addLimits(Offset_AxscfgLimits);
End_AxsCfg:=Write_AxsCfg.endAxsCfg();

● Axis limits with a method call (alternative to “Writing on axis limits individ‐
ually”)
Alternatively, there are the "create_xxx" methods in each function block.
These methods can be used to directly set all FlatBufferelements without
using the methods "start_xxx" and "end_xxx”. When these methods are
used, individual elements of the data structure are omitted and cannot be
set.

VAR
  Write_AxsCfgLimits : motion_core_fbtypes_AxsCfgLimits;
Offset_AxscfgLimits : UDINT;

END_VAR

Offset_AxscfgLimits:= Write_AxsCfgLimits.createAxsCfgLimits( builder:=MyFbs_AxsCfg,posMin := -1000,
posMax := 1000, velPos := 1000 , velNeg := 1000, acc := 2000, dec := 2000, jrkAcc :=4000 , jrkDec :=4000 );

Write_AxsCfg.startAxsCfg(builder:= MyFbs_AxsCfg);
Write_AxsCfg.addLimits(Offset_AxscfgLimits);
End_AxsCfg:=Write_AxsCfg.endAxsCfg();

● FlatBuffer completion
First, create the FlatBuffer again and write on the elements (individually
or completely) and then complete the FlatBuffer with the finish“ method
(CXA_Datalayer -> function block “FlatBufferBuilder”). Only a completed
FlatBuffer can be written to a node of the Data Layer.

MyFbs_AxsCfg.finish(root_table:=End_AxsCfg);

● Transferring the FlatBuffer to the ctrlX CORE
To transfer the FlatBuffer (here “Axis configuration”), the function block
"DL_WriteNodeValue" is used from the CXA_Datalayer library. The FlatBuffer
is written to a “NodeValue” and then transferred to the ctrlX.

VAR
    MyWriteAxsCfg : DL_WriteNodeValue;
NodeValue_Fbs_AxsCfg : DL_NodeValue;
    m_NodeValueOut : DL_NodeValue;
    m_WriteExecute : BOOL;

  END_VAR

NodeValue_Fbs_AxsCfg.SetFlatbuffer(MyFbs_AxsCfg);
MyWriteNodeValue(Execute:= m_WriteExecute, NodeName:='/motion/axs/Axis_1/cfg' ,
NodeValueIn:= NodeValue_Fbs_AxsCfg , NodeValueOut:= m_NodeValueOut);
