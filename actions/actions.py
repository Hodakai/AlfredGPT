from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime

# Example of a custom action for checking table availability
class ActionCheckAvailability(Action):

    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Example: Extracting date and people from slots
        booking_date = tracker.get_slot('date')
        people = tracker.get_slot('people')

        # Hypothetical function to check availability
        available = self.check_database_for_availability(booking_date, people)

        if available:
            dispatcher.utter_message(text="Yes, we have a table available for you!")
        else:
            dispatcher.utter_message(text="Sorry, we don't have a table available for that date and time.")
        return []

    def check_database_for_availability(self, date: str, people: int) -> bool:
        # Dummy function for database check
        # You need to implement actual checking logic here
        # TODO : Implement Supabase db here
        return True

# Custom action to add a comment to a reservation
class ActionAddComment(Action):

    def name(self) -> Text:
        return "action_add_comment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        comment = tracker.get_slot('comment')
        # Function to add comment to DB or service
        # add_comment_to_reservation(comment)
        dispatcher.utter_message(text=f"Comment added: {comment}")
        return []

# Custom action to provide menu details
class ActionProvideMenu(Action):

    def name(self) -> Text:
        return "action_provide_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        menu = self.get_todays_menu()  # Assume this function fetches the daily menu
        dispatcher.utter_message(text=f"Today's menu is: {menu}")
        return []

    def get_todays_menu(self) -> str:
        # Dummy content for today's menu
        return "Chef's special: Grilled Salmon, Vegan Pizza, and Tiramisu"

# Remember to uncomment the necessary imports and implement or integrate actual business logic/database queries as needed.

