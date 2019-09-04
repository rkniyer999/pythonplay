from flask import Flask, jsonify, request,json

app = Flask(__name__) 

# This method is used to retrieve the details of registered Visitor from the DB
@app.route('/getVisitorDetails/<int:visId>',methods=['GET'])
def getVisitorDetails(visId):
    return jsonify({'about': visId})


# This method is used to retrieve the details of registered Visitor from the DB
@app.route('/registerVisitor',methods=['POST'])
def registerVisitorDetails():
    #if(request.method()=='POST'):
    visitordetailsJson = request.json
    visitordetailsJsonstr= json.dumps(visitordetailsJson)
    print(type(visitordetailsJsonstr))
    parsed_json = json.loads(visitordetailsJsonstr)
    print(parsed_json['company'])
    #print(visitordetailsJson)
    return jsonify(request.json)


def identifyVisitor():
    # Get the Image
    # Pass the image & get the face ID
    # Invoke Identify and return the faceID
    return "aa"

def registerFaceAPI():
    return ""






