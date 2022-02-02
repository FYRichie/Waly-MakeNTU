import json
import sys
from typing import Dict, List, Union

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Missing file directory for preprocessing or file directory for saving processed data")
        print("Usage:\npython3 annotation_preprocess.py <file load path> <file save path>")
        exit(0)

    load_path = sys.argv[1]
    save_path = sys.argv[2]
    with open(load_path, "r") as origin_file:
        raw_data = json.load(origin_file)
        target: List[Dict[str, Union[str, int, List]]] = []
        for img in raw_data["images"]:
            target.append({
                "file_name": img["file_name"],
                "width": img["width"],
                "height": img["height"],
                "label": []
            })

        for label in raw_data["annotations"]:
            target[label["image_id"]]["label"].append({
                "category_id": label["category_id"],
                "category_discription": raw_data["categories"][label["category_id"]]["name"],
                "bbox": label["bbox"]
            })

        with open(save_path, "w+") as new_file:
            new_file.write(json.dumps(target))