import flask
from flask import Flask, Response, request, jsonify
import json

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
responseJsonDir = './responseJsonResources/'
responseHtmlDir = './responseHtmlResources/'
configurationFilePath = './configuration.json'

def func():
    global json_object
    response = Response()
    url = request.path

    if("responseJsonFileName" in json_object[url]):
        global responseJsonDir
        responseJsonFilePath = responseJsonDir + json_object[url]["responseJsonFileName"]
        responseJsonFile = open(responseJsonFilePath)
        responseJson = json.load(responseJsonFile)
        responseJsonFile.close()
        response.set_data(json.dumps(responseJson))

    if("html" in json_object[url]):
        global responseHtmlDir
        responseHtmlFilePath = responseHtmlDir + json_object[url]["html"]
        responseHtmlFile = open(responseHtmlFilePath)
        responseHtml = responseHtmlFile.read()
        responseHtmlFile.close()
        response.set_data(str(responseJson))

        
    if("headers" in json_object[url]):
        print("in headers ...")
        headers = json_object[url]["headers"]
        print(type(headers))
        print(str(headers))
        for header,value in headers.items():
            response.headers[header] = value

    return response


def iterate_json(json_object):
    for url,response in json_object.items():
        app.add_url_rule(url,response["endpoint"],func,methods=['GET','POST','DELETE'])


config_file = open(configurationFilePath)
json_object = json.load(config_file)
config_file.close()
iterate_json(json_object)

# app.run()
