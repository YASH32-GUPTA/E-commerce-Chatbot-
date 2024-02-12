from fastapi import FastAPI, HTTPException
from fastapi import Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import DatbaseConnector  as db
import HelperFunctions as extract


app = FastAPI()

# Accepting Data Globally -----
inprogress_orders = {}


class DialogflowRequest(BaseModel):
    responseId: str
    queryResult: dict
    originalDetectIntentRequest: dict
    session: str


@app.post("/")
async def handle_request(request:Request):
    # getting tha data from the json  :
    payload = await request.json()


    # taking out the info from the JSON DATA :

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']


    #  Extracting the Interacting User Session ID
    session_id = extract.extract_session_id(output_contexts[0]["name"])



    # Checking the Model : Giving Back -  Intents :

    intent_handler_dict = {
        'order.add - context ; ongoing-order': add_to_order,
        # 'order.remove - context: ongoing-order': remove_from_order,
        'order.complete - context : ongoing-order': complete_order,
        'track.order - context ; ongoing-tracking': track_order
    }

    return intent_handler_dict[intent](parameters,session_id)




#---------------------------------------------------- TRACK ORDER ------------------------------------------------------------------------------
def track_order(parameters : dict,session_id : str ):
    order_id = int( parameters['number'])

    # Order status  :

    order_status = get_order_status(order_id)

    if order_status :
        fulfillmentText  = f"The Order Status for Order Id : {order_id} is {order_status}"
    else :
        fulfillmentText  = f"No Order Found With Order Id : {order_id}"



    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })




#---------------------------------------------------------- ADD TO ORDER ------------------------------------------------------------------------
def add_to_order(parameters: dict , session_id : str  ):
    Model_name  = parameters["ModelNames"]
    print(Model_name)

    if len(Model_name) >  1 :
        fulfillment_text = "Sorry I didn't understand. Can you please specify Brand name clearly !"
    else:
        new_item = Model_name

        if session_id in inprogress_orders:
            pass
            current_items = inprogress_orders[session_id]
            current_items.append(new_item[0])
            inprogress_orders[session_id] = current_items
        else:
            inprogress_orders[session_id] = new_item

    order_str = extract.get_items(inprogress_orders[session_id])
    fulfillment_text = f"So far you have , {order_str}. Do you need anything else?"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


#---------------------------------------------------------- GET  ORDER ID  ------------------------------------------------------------------------
def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
    else:
        order = inprogress_orders[session_id]

        order_id = save_to_db(order)
        if order_id == -1:
            fulfillment_text = "Sorry, I couldn't process your order due to a backend error. " \
                               "Please place a new order again"
        else:
            fulfillment_text = f"Awesome. We have placed your order. " \
                               f"Here is your order id # {order_id}. "

    # Delete The Processed Order :
    del inprogress_orders[session_id]

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def save_to_db(order: list):
    next_order_id = db.get_next_order_id()
    print(order)
    # Insert individual items
    for item in order:
        rcode = db.insert_order_item(item,next_order_id)
        if rcode == -1:
            return -1

    # Now insert order tracking status
    db.insert_order_tracking(next_order_id, "in progress")
    return next_order_id




# From The Data Base Fetching The Required Order_id Status :

def get_order_status(order_id) :
    cursor = db.cnx.cursor()

    query = f"SELECT status FROM orderstracking WHERE order_id = {order_id}"

    # excuting  the  query
    cursor.execute(query)

    # Fetching the results
    result = cursor.fetchone()

    # Making the cursor Close :
    cursor.close()

    if result:
        return  result[0]
    else :
        return  None


