# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

# import arrow
# import dateparser
from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import ValidationAction

timezones = {
    ('Sydney', 'Australia'): 'UTC +10:00',
    ('Lima', 'Peru'): 'UTC -05:00',
    ('Honolulu', 'United States'): 'UTC -10:00',
    ('San Francisco', 'United States'): 'UTC -8:00',
    ('Tijuana', 'Mexico'): 'UTC -8:00',
    ('Boise', 'United States'): 'UTC -7:00',
    ('Cuidad Juarez', 'Mexico'): 'UTC -7:00',
    ('Fort St. John', 'Canada'): 'UTC -7:00',
    ('Denver', 'United States'): 'UTC -7:00',
    ('Phoenix', 'United States'): 'UTC -7:00',
    ('Mexico City', 'Mexico'): 'UTC -6:00',
    ('Cuidad de Mexico', 'Mexico'): 'UTC -6:00',
    ('Belize City', 'Belize'): 'UTC -6:00',
    ('San Ignacio', 'Belize'): 'UTC -6:00',
    ('Chicago', 'United States'): 'UTC -6:00',
    ('Houston', 'United States'): 'UTC -6:00',
    ('Dallas', 'United States'): 'UTC -6:00',
    ('Austin', 'United States'): 'UTC -6:00',
    ('Chihuahua', 'Mexico'): 'UTC -6:00',
    ('San Jose', 'Costa Rica'): 'UTC -6:00',
    ('Limon', 'Costa Rica'): 'UTC -6:00',
    ('San Francisco', 'Costa Rica'): 'UTC -6:00',
    ('San Salvador', 'El Salvador'): 'UTC -6:00',
    ('San Miguel', 'El Salvador'): 'UTC -6:00'
}

# class ValidateCustomSlotMappings(ValidationAction):
#     async def extract_slot_name(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> Dict[Text, Any]:
#         intent_of_last_user_message = tracker.get_intent_of_latest_message()
#         current_count_of_insults = tracker.get_slot("count_of_insults")
#         if intent_of_last_user_message == "insult":
#            current_count_of_insults += 1

#         return {"count_of_insults": current_count_of_insults}

class ActionTimeZone(Action):

    def name(self) -> Text:
        return 'action_time_zone'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot('country')
        city = tracker.get_slot('city')
        timezone = timezones.get(city, country)

        if timezone is None:
            output = 'I could not find the time zone of {}, {}'.format(city, country)
        else:
            output = 'The time zone of {}, {} is {}'.format(city, country, timezone)

        dispatcher.utter_message(text = output)

        return []
