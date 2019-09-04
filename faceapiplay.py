import requests

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'abcdXXXXXXXXXXXXX',
}

image_url = 'https://saitestblob.blob.core.windows.net/testcontainer/rkface.jpg'
detectfaceapi_url = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/detect'
createpersongroup_url = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/persongroups/mainbu'
createperson_url = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/persongroups/mainbu/persons'

body = {
    "name": "mainbunm",
    "recognitionModel": "recognition_02"
}


detectionparams = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'recognitionModel':'recognition_02',
    'detectionModel':'detection_02',
    'returnRecognitionModel':'true'
}

def detectFace():
    try:
        response = requests.post(detectfaceapi_url, params=detectionparams, headers=headers, json={"url": image_url})
        faces = response.json()
        print(faces)
    except Exception as e:
        print(e)

def createPersonGroup():
    try:
        response = requests.put(createpersongroup_url,headers=headers,json=body)
        #resp = response.read()
        print(response.content)
    except Exception as e:
       print("[Errno {0}] {1}".format(e.errno, e.strerror))


def deletePersonGroup():
    try:
        response = requests.delete(createpersongroup_url,headers=headers)
        #resp = response.read()
        print(response.content)
    except Exception as e:
       print("[Errno {0}] {1}".format(e.errno, e.strerror))

#{'personId': '4270e6cf-5ec1-4605-867d-879c8126f504'}
def createPerson(strpersonName):
    try:
        response = requests.post(createperson_url, headers=headers, json={"name": strpersonName })
        faces = response.json()
        print(faces)
    except Exception as e:
        print(e)

#{'persistedFaceId': '0f31e390-17fc-4ee7-b325-60068f1e9c15'}
def addFace(strpersonGrp, strpersonID):
    try:
        addFaceUrl= "https://centralindia.api.cognitive.microsoft.com/face/v1.0/persongroups/" + strpersonGrp + "/persons/" +  strpersonID + "/persistedFaces?detectionModel=detection_02"
        response = requests.post(addFaceUrl, headers=headers, json={"url": image_url})
        faces = response.json()
        print(faces)
    except Exception as e:
        print(e)

def trainPersonGroup(strPersonGrpId):
    try:
        trainFaceUrl= "https://centralindia.api.cognitive.microsoft.com/face/v1.0/persongroups/" + strPersonGrpId + "/train"
        response = requests.post(trainFaceUrl, headers=headers, json={})
    except Exception as e:
        print(e)

def identifyFace(strPersonGrpId,tempFaceId):
    try:
        identifyFaceUrl= "https://centralindia.api.cognitive.microsoft.com/face/v1.0/identify"
        response = requests.post(identifyFaceUrl, headers=headers, json={"PersonGroupId": strPersonGrpId, "faceIds": [ tempFaceId ], "maxNumOfCandidatesReturned": 1, "confidenceThreshold": 0.5 })
        faces = response.json()
        print(faces)
    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    #createPersonGroup()
    #detectFace()
    #[{'faceId': '67f78894-30f4-470c-8ceb-e3af43bb35fe', 'faceRectangle': {'top': 366, 'left': 558, 'width': 285, 'height': 399}, 'recognitionModel': 'recognition_02'}]
    #deletePersonGroup()
    #createPerson("RK")
    #addFace("mainbu","4270e6cf-5ec1-4605-867d-879c8126f504")
    #trainPersonGroup("mainbu")
    identifyFace("mainbu","67f78894-30f4-470c-8ceb-e3af43bb35fe")

