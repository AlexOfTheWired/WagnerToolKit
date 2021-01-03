"""
Title         : PoseEditor.py

Author        : Alexander Wagner

Description   : This module contains the class and methods for 
                serializing and deserializing animation pose data. 
                i.e. Controls tranform values.  

PATH          : A:\WagnerToolKit\ModularAutoRigger\Utilities

"""


##############################################
# Import 
##############################################

# Pyhton Libraries
import json

# Maya Libraries
import maya.cmds as mc
import maya.OpenMaya as OM

# Package Modules

# Global Variables


################################################
#Utility Functions
################################################


################################################
# Classes 
################################################


class Pose(object):

    """
    Class Name     : Pose
    Description    : Class object for writing/reading pose data to/from disc.
    Notes          : This object can be used to make the animators workflow more efficient.
    """


    def __init__(self, poseName):
        """
        This method is to initialize the object with data passed in as the arguments.
        """
        self.poseName          = poseName # The data will be entered by user in GUI wraper
        self.ctrlList          = None     # 
        self.ctrlTranslateList = None     # 
        self.ctrlRotateList    = None     #
        self.ctrlScaleList     = None     #  Data will be querried by methods 
        self.ctrlNameList      = None     #
        self.ctrlAttributeList = None     #
        self.jsonString        = None     # 

#######################################
# Get Control Methods
#######################################

    def getControlList(self):
        """
        This method fetches all control nodes and populates a list with them.
        """

        # Declare ctrlList as an empty list 
        self.ctrlList = []
        # Get user selected controls
        mSel = mc.ls(sl=True)

        # Iterate through active selection list.
        for idx in range(len(mSel)):
            
            # Append control to list
            self.ctrlList.append(mSel[idx])

        return self.ctrlList


    def getControlTranslate(self):
        """
        This method queries each controls translate values and returns a dictionary
        with ctrl names and their respective translate values.
        """

        # Create an empty dictionary to populate with rotate values
        self.ctrlTranslateList = {}

        try:
            # Iterate through the control list to query translate values.
            for idx in range(len(self.ctrlList)):
                # Query rotate values
                ctrlTranslate = mc.xform(idx, q=True, translate=True, ws=True, a=True)
                # Query control name
                self.ctrlName = '%s' % (self.ctrlList[idx])

                # Add new Key/Value pairs to ctrlTranslateList
                self.ctrlTranslateList[idx] = ctrlTranslate

        except: 
            mc.error("Failed to extract translate values!")

        return self.ctrlTranslate


    def getControlRotate(self):
        """
        This method queries each controls rotate values and returns a dictionary
        with ctrl names and their respective rotate values.
        """    

        # Create an empty dictionary to populate with rotate values
        self.ctrlRotateList = {}

        try:
            # Iterate through the control list to query rotate values.
            for idx in range(len(self.ctrlList)):
                # Query rotate values
                ctrlRotate = mc.xform(idx, q=True, rotate=True, ws=True, a=True)
                # Query control name
                ctrlName = '%s' % (self.ctrlList[idx])

                # Add new Key/Value pairs to ctrlRotateList
                self.ctrlRotateList[ctrlName] = ctrlRotate

        except: 
            mc.error("Failed to extract rotate values!")


        return self.ctrlRotateList


    def getControlScale(self):
        """
        This method queries each controls scale values and returns a dictionary
        with ctrl names and their respective scale values.
        """

        try:
            # Iterate through the control list to query scale values.
            for idx in range(len(self.ctrlList)):
                # Query scale values
                self.ctrlScale = mc.xform(idx, q=True, scale=True, ws=True, a=True)

                # Add new Key/Value pairs to ctrlScaleList
                self.ctrlScaleList[self.ctrlName] = self.ctrlScale

        except:
            mc.error("Failed to exctract scale values")
            
        return self.ctrlScaleList


    def getControlNum(self):
        """
        This method takes the ctrlList as an input and 
        outputs the number of controls in that list.
        """

        try:
            self.ctrlNum = len(ctrlList)

            if self.ctrlNum > 1:
                
                return self.ctrlNum

            else:
                mc.error("User needs to select controls!")
        
        except:
            mc.error("Failed to extract number of controls")


    def getCtrlName(self):
        """
        This method queries the name for each rig control. 
        """

        # Create empty list to populate with control names
        self.ctrlNameList = []

        try:
            for idx in range(len(ctrlList)):
                # Query control name.
                self.ctrlName = '%s' % (ctrlList[idx])
                # Append name to list.
                self.ctrlNameList.append(ctrlName)

        except:
            mc.error("Failed to extract control name.")

        return self.ctrlNameList


    def getControlAttributes(self):
        """
        This method querries each control for custom attribute values
        and populates a list with them.
        """

        # Creat an empty list to populate with custom attribute names and values.
        self.ctrlAttributeList = []
        # Create a list to parse for attrs to ignore
        attrIgnoreList = ['v','tx','ty','tz','rx','ry','rz','sx','sy','sz']      
        
        for idx in range(len(self.ctrlList))

            # Create empty list for custom attrs
            ctrlCustomAttr = []
            # Create list populated with ctrl attributes
            attrList = mc.listAttr(self.ctrlList[idx], k=True, sn=True)
            # Create variable for number of attributes in node
            attr_num = len(attrList)
            # Create empty dict to format custom attr data
            attr_dict = {}

            # Iterate through attr list to filter for custom attriutes
            for attr in attrList:
                # Conditional logic to filter through attributes
                if attr in attrIgnoreList:
                    pass
                else:
                    # Append custom attribute to ctrlCustomAttr
                    ctrlCustomAttr.append(attr)

            # Iterate through custom attr list to format data
            for jdx in range(len(ctrlCustomAttr)):       
                # Query the custom attr values
                attrValue = mc.getAttr('%s.%s'%(m_sel[0],ctrlCustomAttr[jdx]))
                # Add custom attr key and value pairing to attr_dict
                attrDict[ctrlCustomAttr[jdx]] = attr_value
            
            # Add dict to custom ctrlAttributeList
            self.ctrlAttributeList.append(attrDict)

        return self.ctrlAttributeList


#######################################
# Set Control Methods
#######################################

    def setControlTranslate(self):
        """
        This method iterates through ctrlList and sets each controls translate values. 
        """


    def setControlRotate(self):
        """
        This method iterates through ctrlList and sets each controls rotate values. 
        """
    

    def setControlScale(self):
        """
        This method iterates through ctrlList and sets each controls scale values. 
        """


    
    def setControlAttribute(self):
        """
        This method iterates through the ctrlList and sets the 
        custom attributes with new values.
        """


    def dataToWrite(self):
        """
        This method takes the ctrlNum, Translate, Rotate, Scale values and formats
        them into a json object.
        """

        # Create empty json object
        self.jsonString = {}

        # Iterate through ctrlList to format json object.
        for idx in range(len(self.ctrlNum)):
            # Each key will be the control nodes attributes 
            ctrlNode = {
                'Name'      : self.ctrlNameList[idx],
                'Translate' : self.ctrlTranslateList[idx],
                'Rotate'    : self.ctrlRotateList[idx],
                'Scale'     : self.ctrlScaleList[idx],
                
            }
            self.jsonString[self.ctrlNum[idx]] = ctrl.Node

        return self.jsonString


    def exportPose(self):
        """
        This method takes the json object and writes the data to disk.
        """

        # Use context manager to write object data to disk.
        with open(<fileName>, 'w+') as jsonFile:
            json.dump(self.jsonString, jsonFile,sort_keys=True, indent=4, separators=(',' , ':'))

    
    def importPose(self):