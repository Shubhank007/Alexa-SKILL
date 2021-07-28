# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import random
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

facts=[" Great Wall of China. The original wall built under the rule of Emperor Qin Shi Huang of the Win Dynasty took around 20 years to finish. 21,196 kilometres long, the Great Wall witnesses highlands, landscapes, plateaus, natural barriers and more. While it is an architectural marvel alright, did you know that this structure is also considered the longest cemetery on Earth? Over a million people died building it and archaeologists have found human remains buried under parts of the wall. Creepy much?",
    "Christ the Redeemer, Brazil.  Christ the Redeemer is a 125 feet tall statue designed by Heitor da Silva Costa, sculpted by French sculptor Paul Landowski. Since the statue is atop a mountain, it’s prone to getting hit by lightning—in fact it gets hit around three to six times a year. Prior to the FIFA World Cup in 2014, a lightning struck and broke one of the statue’s thumbs. Also, this structure wasn’t originally built in Brazil; it was made in France.",
   "Petra, Jordan. A man made marvel, Petra is known as the Rose City, built out of pink sandstones. This structure, in fact is evidence that the Middle East was the most influential region of the world in the Middle Ages. But this place wasn’t given its due for a long time—did you know that Bedouin of the Arabian Desert destroyed some of the most priceless carvings on the Treasury’s walls? They used the carvings as target during their shooting practice.",
   " Machu Picchu, Peru. One of the most famous lost cities of the world, Machu Picchu, also known as the Lost City of the Incas, was built in 1450 and abandoned a hundred years after that. Declared as a UNESCO Heritage Site in 1983, the structure is built completely out of dry-stone walls. Many of the stones that were used to build the city were more than 50 pounds in weight, but it is said that no wheels were used to transport these rocks up the mountain. In fact it is alleged that hundreds of men pushed the heavy rocks up the steep mountain side.",
   "Colosseum, Italy. Built between 70 AD and 82 AD by Emperor Titus Vespasian, the Colosseum in Rome is the most iconic, ancient amphitheatre in the world. Seating over 50,000 spectators, the amphitheatre was built for public spectacles like the infamous gladiator fights, animal hunts, executions, and dramas. It is said that the events that took place at the Colosseum were graphic and brutal—during certain games around 10,000 animals would be killed in a single day.",
   "Chichen Itza, Mexico. Chichen Itza translates to “At the mouth of the well of Itza”. Believed to be the largest Mayan city ever built, the centre of the Chichen Itza comprises El Castillo, also known as the Temple of Kukulcan. Many travellers aver that the sites in Chichen Itza are known for their unusual sounds. If you clap once from one end of the Ball Court, it reverberates and creates nine echoes in the middle of the court. A clap in front of the Kukulkan Pyramid creates an echo resembling the serpent’s chirp.",
   " Taj Mahal, India. One of the most glorious displays of love in history is the Taj Mahal, built by emperor Shah Jahan in honour of his late wife. One of the most popular legends about the structure is that the emperor had every workers hands cut off so so they couldn’t recreate the design. About 1000 elephants were used to transport construction material to the site.",
    ]

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to facts about seven wonders. We all know the wonders of the world—they're almost on our fingertips. But do you know every little detail about these wonderful structures?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class factsintent(AbstractRequestHandler):
    """Handler for  factsintent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("factsintent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(facts)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(factsintent())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()