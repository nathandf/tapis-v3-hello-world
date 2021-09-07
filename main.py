import json

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

    print(json.dumps(output))

if __name__ == "__main__":
    main()
