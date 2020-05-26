
def iterate_json(json_object):
    for url,response in json_object.items():
        app.add_url_rule(url,response["endpoint"],func,methods=['GET','POST'])

config_file = open("../configuration.json")
json_object = json.load(config_file)
config_file.close()
iterate_json(json_object)
