import argparse
import json
from str2speech.speaker import Speaker

def main():
    parser = argparse.ArgumentParser(description="Process podcast generation arguments.")
    parser.add_argument("--host_voice", default="bf_emma", help="The voice ID for the host.")
    parser.add_argument("--guest_voice", default="af_heart", help="The voice ID for the guest.")
    parser.add_argument("--input_file", required=True, help="The path to the input JSON file.")

    args = parser.parse_args()

    host_voice = args.host_voice
    guest_voice = args.guest_voice
    input_file = args.input_file

    s = Speaker("kokoro")

    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
            print(f"Successfully loaded data from {input_file}")

            if isinstance(data, list):
                print("Data is a list of objects.")
                i = 0
                for item in data:
                    if isinstance(item, dict) and "role" in item and "content" in item:
                        role = item["role"]
                        content = item["content"]
                        print(f"Role: {role}, Content: {content}")
                        s.text_to_speech(content, f"{i}.wav", host_voice if role == "host" else guest_voice)
                        i += 1
                    else:
                        print(f"Warning: Invalid item format found: {item}")
            else:
                print("Error: Input JSON file does not contain a list of objects.")

    except FileNotFoundError:
        print(f"Error: Input file not found: {input_file}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {input_file}")
    except Exception as e:
        print(f"An unexpected error occurred while reading {input_file}: {e}")
    

if __name__ == '__main__':
    main()
