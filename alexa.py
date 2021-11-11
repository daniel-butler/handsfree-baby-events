from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

import actions

sb = SkillBuilder()


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input: HandlerInput) -> Response:
    speech = "Add feedings by saying having a bottle, is on the breast, or is eating."
    handler_input.response_builder\
        .speak(speech)\
        .set_card(SimpleCard("Baby Charlotte", speech))\
        .set_should_end_session(False)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("StartFeedingIntent"))
def start_feeding_intent_handler(handler_input: HandlerInput) -> Response:
    speech, ask = actions.new_feeding(

    )
    handler_input.response_builder\
        .speak(speech)\
        .set_card(SimpleCard("Baby Charlotte", speech))\
        .set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("GetLastFeedingIntent"))
def last_feeding_intent_handler(handler_input: HandlerInput) -> Response:
    speech, ask = actions.last_feeding()
    handler_input.response_builder\
        .speak(speech)\
        .set_card(SimpleCard("Baby Charlotte", speech))\
        .set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_intent_name("NewBabyIntent"))
def add_new_baby(handler_input: HandlerInput) -> Response:
    session_attributes = handler_input.attributes_manager.session_attributes
    speech, ask = actions.new_baby(
        baby_name=session_attributes.get('first_name'),
        birthday=session_attributes.get('birthday'),
    )
    handler_input.response_builder\
        .speak(speech)\
        .set_card(SimpleCard("Baby Events", speech))\
        .set_should_end_session(True)
    return handler_input.response_builder.response

