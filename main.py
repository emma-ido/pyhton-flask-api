from flask import *
import json, time


app = Flask(__name__)

@app.route('/', methods=["GET"])
def home_page():
    data_set = {"Page": "Home", "Message": "Successfully loaded the Home page", "Timestamp": time.time()}
    json_dump = json.dumps(data_set);

    return json_dump

# /permissions?code=<number>
@app.route('/permissions', methods=["GET"])
def permissions_page():
    user_query = str(request.args.get("code"))
    #binary = convertToBinary(int(user_query))
    #data_set = {"Page": "Home", "Message": f'Successfully got the request for {user_query}', "Timestamp": time.time(), "Binary":f'{binary}'}
    
    data_set = {}
    if(len(user_query) == 3):
        data_set = getPermissions(user_query);
    json_dump = json.dumps(data_set);

    return json_dump


@app.route('/parity', methods=["GET"])
def parity_page():
    #user_query = request.args.getlist("parity")
    g = list(request.args.to_dict().values())
    g = xor(g)
    return str(g)


def xor(arg):
	j = int(arg[0])
	for i in arg:
		j = int(i) ^ j
		print(j)
	return j

def convertToBinary(num):
    num = int(num)
    binary = ""
    while(num != 0):
        binary = str(num % 2) + binary
        num = num//2
        #print("Here: ", num)
    while(len(binary) < 3):
        binary = "0" + binary
    return binary

def getPermissions(code):
    groups = {"owner":[], "group":[], "other":[]}
    j = 0;
    for i in groups:
        binary = convertToBinary(code[j])
        groups[i] = getPem(binary)
        j = j + 1;
    return groups

def getPem(binary):
    if(len(str(binary)) != 3):
        return []
    permissions = [];
    if(binary[0] == "1"):
        permissions.append("read")
    if(binary[1] == "1"):
        permissions.append("write")
    if(binary[2] == "1"):
        permissions.append("execute")
    return permissions


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



