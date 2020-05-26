import json
import flask
from flask import request, jsonify, Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SERVER_NAME"] = "127.0.0.1:1024"
responseJsonDir = '../responseJsonResources/'
responseHtmlDir = '../responseHtmlResources/'

def func():
    global json_object
    response = Response()
    url = request.path

    if("responseJsonFileName" in json_object[url]):
        global responseJsonDir
        responseJsonFilePath = responseJsonDir + json_object[url]["responseJsonFileName"]
        responseJsonFile = open(responseJsonFilePath)
        responseJson = json.load(responseJsonFile)
        responseHtmlFile.close()
        response.set_data(str(responseJson))

    if("html" in json_object[url]):
        global responseHtmlDir
        responseHtmlFilePath = responseHtmlDir + json_object[url]["html"]
        responseHtmlFile = open(responseHtmlFilePath)
        responseHtml = responseHtmlFile.read()
        responseHtmlFile.close()
        response.set_data(str(responseHtml))

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
        app.add_url_rule(url,response["endpoint"],func,methods=['GET','POST'])


config_file = open("../configuration.json")
json_object = json.load(config_file)
config_file.close()
iterate_json(json_object)

app.run()
