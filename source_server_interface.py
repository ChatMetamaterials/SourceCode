import requests
import json
import ast


server_url = "http://43.159.130.228/"

def greetings():
    message = "Thanks for using local ChatMetamaterial API source code communicator:\n"
    print (message)
    return

def write_json_to_txt(data, filename):
    try:
        json_str = json.dumps(data, indent=4)
        with open(filename, 'w') as file:
            file.write(json_str)
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


def classification_API_local_calling (Input, Image = ""):
    function_link = "openAi/classification"
    url = server_url+function_link
    params = {"userInput": Input,
              "image": Image}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def basic_cells_API_local_calling (Input, Image = ""):
    function_link = "openAi/basic/cells"
    url = server_url+function_link
    params = {"userInput": Input,
              "image": Image}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def deformation_recognition_API_local_calling (Input, Image = ""):
    function_link = "openAi/deformation/recognition"
    url = server_url+function_link
    params = {"userInput": Input,
              "image": Image}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def research_innovation_API_local_calling (Input, Image = ""):
    function_link = "openAi/research/innovation"
    url = server_url+function_link
    params = {"userInput": Input,
              "image": Image}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def universal_metamaterials_API_local_calling (Input, Type):
    function_link = "openAi/special/agents"
    url = server_url+function_link
    if (Type == "damage programmable"):
        whichone = 0
    elif (Type == "irrational"):
        whichone = 1
    elif (Type == "gyroid"):
        whichone = 2
    else:
        return "ERROR: the current architecture is not supported yet."
    params = {"userInput": Input,
              "whichOne": whichone}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def universal_product_API_local_calling (Input, Type, Image):
    function_link = "openAi/design/shoe"
    url = server_url+function_link
    if (not Type == "Shoe sole"):
        return "ERROR: the current product is not supported yet."
    params = {"userInput": Input,
              "image": Image}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def multi_single_cells_algorithms(metadata_basic_cells):
    url = "http://43.159.130.228/metadata/multi/single/cells"
    input_data = {"singleCellDataList": metadata_basic_cells}
    response = requests.post(url, json=input_data)
    data = response.json()
    return data

def deformation_pattern_generation_algorithms(metadata_deformation):
    url = "http://43.159.130.228/metadata/deformation/pattern"
    input_data = {"deformation": metadata_deformation}
    response = requests.post(url, json=input_data)
    data = response.json()
    return data

def research_innovation_generation_algorithms(metadata_research_innovation):
    url = "http://43.159.130.228/metadata/research/innovation"
    input_data = {"researchInnovation": metadata_research_innovation}
    response = requests.post(url, json=input_data)
    data = response.json()
    return data

def architecture_data_algorithms(structure_metadata):
    url = "http://43.159.130.228/metadata/materials/lines"
    input_data = {"metadata": structure_metadata}
    response = requests.post(url, json=input_data)
    data = response.json()
    return data

def extended_architecture_data_algorithms(structure_metadata, Type):
    url = "http://43.159.130.228/metadata/lines/special/agents"
    if (Type == "damage programmable"):
        whichone = 0
    elif (Type == "irrational"):
        whichone = 1
    elif (Type == "gyroid"):
        whichone = 2
    else:
        return "ERROR: the current architecture is not supported yet."
    input_data = {"metadataSpecial": structure_metadata,
                  "indicator": whichone}
    response = requests.post(url, json=input_data)
    data = response.json()
    return data

def extract_data_txt (filename):
    with open(filename, "r") as file:
        content = file.read()
    data_dict = json.loads(content)
    data = data_dict["data"]
    return data

def extract_data_json (json_data):
    data = json_data["data"]
    return data

greetings()