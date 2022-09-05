# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:34:01 2022

@author: tharu
"""

from mrjob.job import MRJob

class MRmaxtemperature(MRJob):
    
    def makefarenheit(self,tenthsofCelcius):
        celcius=float(tenthsofCelcius)/10.0
        farhenheit=celcius*1.8+32.0
        return farhenheit
    
    def mapper(self,_,line):
        (location,date,type,data,x,y,z,w) = line.split(',')
        if(type=='TMAX'):
            temperature=self.makefarenheit(data)
            yield location,temperature
            
    def reducer(self,location,temps):
        yield location, max(temps)
            

if __name__== '__main__':
    MRmaxtemperature.run()
    
        
        
    
    
