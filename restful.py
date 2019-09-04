import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'db349972687b4646XXXXXXXXX',
}

params = urllib.parse.urlencode({
})


body = {
    "name": "mainbu",
    "recognitionModel": "recognition_02"
}

bodyurl = {
    "url": "https://saitestblob.blob.core.windows.net/testcontainer/rkface.jpg"
}

def createPersonGroup():
    try:
        conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        
        conn.request("PUT", "/face/v1.0/persongroups/mainbu/persons?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def detectFace():
    try:
        conn = http.client.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&recognitionModel=recognition_02&returnRecognitionModel=true&detectionModel=detection_02 %s %s" %body, %headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print(e)

# Main method.
if __name__ == '__main__':
    #createPersonGroup()
    detectFace()
