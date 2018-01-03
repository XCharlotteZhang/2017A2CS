from random import *

joblist=[warrior,sorcerer,bard,thief,adventurer]


class player:
    def __init__(self):
    	self.name=name()
    	jobc=input('your job:')
    	self.job=plyjob()
    	self.stat=plybasestat(jobc)
    	self.level=1
    
    def plyjob(jobc):
    	c=False
    	if jobc in joblist:
    		c=True
    	while c==False:
    		jobc=input('your job:')
      	if jobc in joblist:
      		c=True
      return jobc

    def levelup(self, exp):
        oldlevel=self.level
        exp2level=int(round((self.level**3/12)+self.level*4))
        while exp>=exp2level:
            expcarry=exp-exp2level
            exp=expcarry
            plrlevel+=1
            exp2level=plrlevel
            exp2level=int(round((plrlevel**3/12)+plrlevel*4))
        return plrlevel,exp2level,exp,oldlevel

    def name():
        return input('')

class enemy:
    def __init__(self):
    	self.name=input()
    	self.stats=stats(self.name)
        
    def stats(name):
        #the enemy's stats
        return statslist
        


        
