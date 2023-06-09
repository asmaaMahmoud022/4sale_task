from flask import Flask, jsonify, request
app = Flask(__name__)
app.config['SECRET_KEY']='XXXXXXX'

from mailjet_rest import Client

api_key = 'REPLACE_YOUR_KEY'
api_secret = 'REPLACE_YOUR_SECRET'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

@app.route('/service')
def service():
    return 'Notification Service',200

@app.route('/sendEmail',methods=["POST"])
def sendEmail():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json
        name = body["name"]
        email = body["email"]
        data = {
  'Messages': [
    {
      "From": {
        "Email": "REPLACE_YOUR_EMAIL",
        "Name": "asmaa"
      },
      "To": [
        {
          "Email":email,
          "Name": name
        }
      ],
      "Subject": "Greetings from asmaa",
      "TextPart": "Welcome to the Tutorial",
      "HTMLPart": f"<h3>Dear {name}",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
        mailjet.send.create(data=data)
        return jsonify({"Accepted":202}),202
    else:
        return jsonify({"Bad Request":400}),400
        
if __name__ == '__main__':
	app.run(debug=True)