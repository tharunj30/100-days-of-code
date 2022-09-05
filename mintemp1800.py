from mrjob.job import MRJob

class MRmintemperature(MRJob):
    
    def makefarenheit(self,tenthsofCelcius):
        celcius=float(tenthsofCelcius)/10.0
        farhenheit=celcius*1.8+32.0
        return farhenheit
    
    def mapper(self,_,line):
        (location,date,type,data,x,y,z,w) = line.split(',')
        if(type=='TMIN'):
            temperature=self.makefarenheit(data)
            yield location,temperature
            
    def reducer(self,location,temps):
        yield location, min(temps)
            

if __name__== '__main__':
    MRmintemperature.run()
    
        
        
    
    
