from dining import *


def returnSpeech(speech, endSession=True):
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
        "outputSpeech": {
        "type": "PlainText",
        "text": speech
            },
            "shouldEndSession": endSession
          }
    }



def on_intent(intent_request, session):
    # This means the person asked the skill to do an action
    intent_name = intent_request["intent"]["name"]
    # This is the name of the intent (Defined in the Alexa Skill Kit)
    if intent_name == 'get_menu':

        dining_hall = intent_request["intent"]["slots"]["dining_hall"]["value"]

        if dining_hall == "core":
            url = CORE
        elif dining_hall == "schilletter":
            url = SCHILLETTER

        stations = parse_stations(fetch_page(url))

        return stations[0]
    
    elif intent_name == "get_station_menu":

        stations = parse_stations(fetch_page(url))

        query = intent_request["intent"]["slots"]["station"]["value"].title()

        for station in stations:
            # if station.id == intent_request["intent"]["slots"]["station"]["resolutions"]["resolutionsPerAuthority"][0]["values"][0][""]
            if station.value == query:
                return station.speak()
            else:
                return "Sorry, I couldn't find a station that matches the name {}".format(query)





def lambda_handler(event, context):

    if event["request"]["type"] == "LaunchRequest":
        speech = "Hi! I can help you find out what's on the menu at campus dining halls."
    

    elif event["request"]["type"] == "IntentRequest":
        speech = on_intent(event["request"], event["session"])
    

    return returnSpeech(speech)

if __name__ == '__main__':
    pass
