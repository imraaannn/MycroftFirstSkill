# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Imran'

LOGGER = getLogger(__name__)


class HelloWorldSkill(MycroftSkill):

    def __init__(self):

        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

        self.intent2_flag = False

        self.intent3_flag = False

        self.intent4_flag = False
        

    def initialize(self):

        thank_you_intent = IntentBuilder("ThankYouIntent"). \

            require("ThankYouKeyword").build()

        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \

            require("HowAreYouKeyword").build()

        self.register_intent(how_are_you_intent,self.handle_how_are_you_intent)

        

        hello_world_intent = IntentBuilder("HelloWorldIntent"). \

            require("HelloWorldKeyword").build()

        self.register_intent(hello_world_intent,self.handle_hello_world_intent)

        

        rajni_intent = IntentBuilder("RajniIntent"). \

            require("RajniKeyword").build()

        self.register_intent(rajni_intent,self.handle_rajni_intent)


    def handle_rajni_intent(self, message):
		# when you say RajniKeyword, this method is called
		# this enables intent2 (thank you)
        self.intent2_flag=True;
		# this speaks, and tells mycroft to listen without wakeword
        self.speak("Rajni is the best",expect_response=True) 

    
    def handle_thank_you_intent(self, message):
		# this is triggered if you say thank you
        if self.intent2_flag=True:

            self.speak("Welcome Man",expect_response=True)
			# activates how are you intent
            self.intent3_flag = True
			# deactivates thank you intent
			self.intent2_flag = False
		else:
			# if you said thank you but it wasnt expected (no intent 1 called)
			self.speak("what are you thanking me for?")

 

       
    def handle_how_are_you_intent(self, message):

        if intent3_flag=True;
            self.speak("how.are.you",expect_response=True)



    def stop(self):
        pass


def create_skill():

    return HelloWorldSkill()
