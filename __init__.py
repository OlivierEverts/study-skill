import time
from datetime import datetime, timedelta
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration
from mycroft.util.time import now_local

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
   
        
    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        
        # Get the amount of blocks from the user
        blocks = self.get_response('skill.study')
        
        # To convert  blocks to an int, it first needs to be a string. 
        # The variable must be of type int for further use
        blocks = str(blocks)
        blocks = int(blocks)
        
        # If the user selects one block, Mycroft responds with the singular "block" 
        if blocks == 1:
            amount_of_blocks = "1 block"
        
        # If the user selects multiple blocks, Mycroft responds with the plural "blocks"
        if blocks > 1:
            amount_of_blocks = "{} blocks".format(str(blocks))
            
        # Get the current time to calculate the time when the user will be done in the future
        now = now_local()
        currenttime = now.strftime("%H:%M")
        
        # Calculate the time when the user is done based on the amount of blocks selected
        # Each block is 25 minutes and each break is 5 minutes
        
        minutes = blocks*25 + (blocks-1)*5
        futuretime = now + timedelta(minutes = minutes)
        futuretime = futuretime.strftime("%H:%M")
        
        # Respond to the user with the amount of blocks they have chosen, what the curren time is
        # and when their study session will be finished
        self.speak_dialog('skill.study.confirmation', data={'currenttime': currenttime,
                                                            'amount_of_blocks': amount_of_blocks,
                                                            'futuretime': futuretime})

#The time.sleep() function  takes an input of seconds. So if  you want the code to sleep for several minutes you should multiply the values  witth  60
#Currently everythting is in second for debugging purposes
        for i in range(blocks):
            time.sleep(25)
            if i <  blocks-1:
                self.speak_dialog('skill.breakbegin')
                time.sleep(5)
                self.speak_dialog('skill.breakend') 
            if i == blocks-1:
                break
        self.speak_dialog('skill.end') 



def create_skill():
    return MyFirstSkill()
