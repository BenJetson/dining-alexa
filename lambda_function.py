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

def get_url(dining_hall):

    print("dining hall: {}".format(dining_hall))

    url = ""

    if dining_hall == "core":
        url = CORE if ONLINE else INFILE_CORE
    elif dining_hall == "schilletter":
        url = SCHILLETTER if ONLINE else INFILE_SCH
    else: 
        print ("AACK")
    
    return url

def on_intent(intent_request, session):
    # This means the person asked the skill to do an action
    intent_name = intent_request["intent"]["name"]
    # This is the name of the intent (Defined in the Alexa Skill Kit)
    if intent_name == 'get_menu':

        dining_hall = intent_request["intent"]["slots"]["dining_hall"]["value"]

        url = get_url(dining_hall)
        
        stations = parse_stations(fetch_page(url))

        output = "Today, {} has the following: ".format(dining_hall)

        for station in stations:
            output += station.speak()

        return output
    
    elif intent_name == "get_station_menu":

        # FIXME static webpage assignment

        dining_hall = intent_request["intent"]["slots"]["dining_hall"]["value"]

        url = get_url(dining_hall)

        stations = parse_stations(fetch_page(url))

        query = intent_request["intent"]["slots"]["station"]["value"]
        print("QUERY: {}".format(query))

        for station in stations:
            # if station.id == intent_request["intent"]["slots"]["station"]["resolutions"]["resolutionsPerAuthority"][0]["values"][0][""]
            if (station.value == query or 
                (query == "salad bar" and station.value == "salad") or
                (query == "dessert bar" and station.value == "dessert")):
                return "Today, " + station.speak()

        return "Sorry, I couldn't find a station that matches the name {}".format(query)
    
                





def lambda_handler(event, context):

    request_type = event["request"]["type"]
    print(request_type)
    print(request_type == "IntentRequest")

    if request_type == "LaunchRequest":
        speech = "Hi! I can help you find out what's on the menu at campus dining halls."
    

    elif request_type == "IntentRequest":
        speech = on_intent(event["request"], event["session"])
        print("INTENT")

    else:
        return {
            "version": "1.0",
            "sessionAttributes": {},
            "response": {
                "outputSpeech": {
                    "type": "Dialog.Delegate",
                    "updatedIntent": {
                        "name": "string",
                        "confirmationStatus": "NONE",
                        "slots": {
                            "string": {
                                "name": "string",
                                "value": "string",
                                "confirmationStatus": "NONE"
                            }
                        }
                    }
                }
            }
        }
    
    
    
    print(speech)
    

    return returnSpeech(speech)

if __name__ == '__main__':
    pass
