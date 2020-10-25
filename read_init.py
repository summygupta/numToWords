import json

def get_init_config():
	with open("./init.json") as json_file:
		json_object = json.load(json_file)
		path_object = dict()
		path_object["ALLOWED_HOSTS"] = json_object["ALLOWED_HOSTS"]
		return path_object