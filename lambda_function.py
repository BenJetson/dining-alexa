from dining import *

with open("buildID", 'r') as build_id:
    print("[INFO] This build's ID is:", build_id.readline())

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
    
    intent_name = intent_request["intent"]["name"]
    
    if intent_name == 'get_menu':

        print("[INFO] Detected that this intent calls for FULL MENU.")

        dining_hall = intent_request["intent"]["slots"]["dining_hall"]["value"]
        url = get_url(dining_hall)
        page = fetch_page(url)
        
        if is_open(page):

            stations = parse_stations(page)

            output = "Today, {} has the following: ".format(dining_hall)

            for station in stations:
                output += station.speak()


            print("[INFO] Output is: \"{}\"".format(output))

            return output

        else:
            print("[INFO] Detected that this dining location is CLOSED.")
            return CLOSED.format(dining_hall)
    
    elif intent_name == "get_station_menu":

        print("[INFO] Detected that this intent calls for STATION MENU.")

        dining_hall = intent_request["intent"]["slots"]["dining_hall"]["value"]
        url = get_url(dining_hall)
        page = fetch_page(url)
        
        if is_open(page):

            print("[INFO] Detected that this dining locatin is OPEN.")

            stations = parse_stations(page)

            query = intent_request["intent"]["slots"]["station"]["value"]

            print("[INFO] User wants information about station with value \"{}\"".format(query))

            for station in stations:
                # TODO: Fix discrepancies between station value and slot value to avoid extra conditions
                if (station.value == query or 
                    (query == "salad bar" and station.value == "salad") or
                    (query == "dessert bar" and station.value == "dessert")):
                    return "Today, " + station.speak()

            return STATION_NO_MATCH.format(query)
        
        else:
            print("[INFO] Detected that this dining location is CLOSED.")
            return CLOSED.format(dining_hall)
    
                





def lambda_handler(event, context):

    request_type = event["request"]["type"]
    print("[INFO] The type of this request is:", request_type)
    print("[INFO] Is this request an intent?", request_type == "IntentRequest")

    if request_type == "LaunchRequest":
        print("[INFO] Detected that this is a LAUNCH request.")
        speech = BANNER
    

    elif request_type == "IntentRequest":
        speech = on_intent(event["request"], event["session"])
        print("[INFO] Detected that this is an INTENT request")

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
    
    
    
    print("[INFO] Returning the following speech:\n", speech)
    

    return returnSpeech(speech)

if __name__ == '__main__':
    pass
