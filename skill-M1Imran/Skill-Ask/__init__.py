from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Imran'

LOGGER = getLogger(__name__)


class ResponseTestSkill(MycroftSkill):
    def __init__(self):
        super(ResponseTestSkill, self).__init__(name="ResponseTest")
        self.ask = False
        self.ask_1=False

    def initialize(self):
        
        introduction_intent = IntentBuilder('IntroductionIntent'). \
            require("IntroductionKeyword").build()
        askingname_intent = IntentBuilder('AskingNameIntent'). \
            require("AskingNameKeyword").build()
        askingphone_intent = IntentBuilder('AskingPhoneIntent'). \
            require("AskingPhoneKeyword").build()
 
 
        self.register_intent(introduction_intent, self.handle_introduction_intent)
        self.register_intent(askingname_intent, self.handle_askingname_intent)
        self.register_intent(askingphone_intent, self.handle_askingphone_intent)


    #To activate this say Hey Mycroft I am here to give feedback
    def handle_introduction_intent(self, message):
        self.ask = True
        self.speak_dialog("Introduction",
                   expect_response=True)    

    #To activite this say Imran
    def handle_askingname_intent(self, message):
        if self.ask:
            self.speak_dialog("AskingName")
            self.ask_1 = True
            self.ask = False

    #Activate this say handphone no
    def handle_askingphone_intent(self, message):
        if self.ask_1:
            self.speak_dialog("AskingPhone")
            self.ask_1 = False

    


def create_skill():
    return ResponseTestSkill()
