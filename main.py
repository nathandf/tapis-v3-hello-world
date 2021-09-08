import os
import json

output = {
    "lineCount": 0,
    "charCount": 0
}

def main() -> None :
    
    print("\n\n")
    print(os.getcwd(), "\n")
    print(os.listdir(), "\n")
    print(os.environ)
    print("\n\n")

    file = open( "./data/data.txt", "r")
    for line in file:
        output["lineCount"] += 1
        output["charCount"] += len(line)
    file.close()

    print(json.dumps(output))

if __name__ == "__main__":
    main()
