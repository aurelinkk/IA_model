import json
import shutil
import os

# Chemin du dossier source des images
image_source_folder = r"C:\Users\aurel\Documents\Stage\code\GARBAGE\test"

# Chemin du dossier de destination des images
image_destination_folder = r"C:\Users\aurel\Documents\Stage\code\GARBAGE\test\images"

# Chemin du fichier d'annotations d'entrée et de sortie
input_file = "_annotations.coco.json"
output_file = "annotations_subset.coco.json"

# Nombre maximal d'annotations à récupérer
max_annotations = 200

# Charger les données depuis le fichier d'entrée
with open(input_file, "r") as f:
    data = json.load(f)

# Extraire les 200 premières annotations
subset_data = {
    "info": data["info"],
    "licenses": data["licenses"],
    "categories": data["categories"],
    "images": data["images"][:max_annotations],
    "annotations": [annotation for annotation in data["annotations"] if annotation["id"] < max_annotations]
}

# Créer le dossier de destination s'il n'existe pas
if not os.path.exists(image_destination_folder):
    os.makedirs(image_destination_folder)

# Copier les images dans le dossier de destination
for image_info in subset_data["images"]:
    image_filename = image_info["file_name"]
    image_source_path = os.path.join(image_source_folder, image_filename)
    image_destination_path = os.path.join(image_destination_folder, image_filename)
    shutil.copyfile(image_source_path, image_destination_path)

# Écrire les données extraites dans le fichier de sortie
with open(output_file, "w") as f:
    json.dump(subset_data, f, indent=4)

print("Les 200 premières annotations ont été extraites avec succès dans", output_file)
print("Les images correspondantes ont été copiées dans", image_destination_folder)
