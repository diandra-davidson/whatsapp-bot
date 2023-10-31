from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a message
    if 'search' in str(body).lower():
        query = str(body).split(":", 1)[1].strip(" ")
        resp.message(f"-- Top 5 Results for '{query}' --")
        for result in search(query, num_results=5):
            resp.message(result)
    return str(resp )

if __name__ == "__main__":
    app.run(debug=True)