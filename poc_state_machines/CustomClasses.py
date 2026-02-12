from typing import Literal

class State:
    def __init__(self,id:str="", read:str="", write:str="", moveDirection: Literal["L", "R"]="Left", nextStateId:str=""):
        self.id = id
        self.read = read
        self.write = write
        self.moveDirection = moveDirection
        self.nextStateId = nextStateId
    def __str__(self, isJson=False):
        stringReadJson = "null" if self.read==None else f'"{self.read}"'
        stringWriteJson = "null" if self.write==None else f'"{self.write}"'
        
        stringReadClass = "None" if self.read==None else f'"{self.read}"'
        stringWriteClass = "None" if self.write==None else f'"{self.write}"'
        
        jsonFormat = '{"id":"'+self.id+'","read":'+stringReadJson+',"write":'+stringWriteJson+',"move":"'+self.moveDirection+'","nextStateId":"'+self.nextStateId+'"}'
        classFormat = f'State("{self.id}", {stringReadClass}, {stringWriteClass}, "{self.moveDirection}", "{self.nextStateId}")'
        
        if isJson: return jsonFormat
        else: return classFormat
    def __eq__(self, value):
        if isinstance(value, State):
            return (self.id == value.id and
                    self.read == value.read and
                    self.write == value.write and
                    self.moveDirection == value.moveDirection and
                    self.nextStateId == value.nextStateId)
        
        return False

def statesArrayToJson(states: list[State], isJson=True):
    print(f"Converting {len(states)} States to json")
    out = "["
    for i,state in enumerate(states):
        out += state.__str__(isJson=isJson)
        if i != len(states)-1: out += ","
    out += "]"
    return out