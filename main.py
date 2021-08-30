import json, os
from datetime import datetime

data_filename = "./data/data.txt"
output_filename="./output/" + datetime.now().isoformat() + ".txt"

output = {
    "lineCount": 0,
    "charCount": 0
}

def main() -> None :
    file = open( "./data/data.txt", "r")
    for line in file:
        output["lineCount"] += 1
        output["charCount"] += len(line)
    file.close()

    save_output(output)

def save_output(data: dict) -> None :
    json_string = json.dumps(data)
    file = open( output_filename, "w" )
    file.write(json_string)
    file.close()

    with open( output_filename, "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
