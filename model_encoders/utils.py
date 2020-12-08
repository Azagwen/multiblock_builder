# Path names
output_path = "output"
models_path = f"{output_path}/models"
blocks_model_path = f"{models_path}/block"
block_items_model_path = f"{models_path}/item"
blockstates_model_path = f"{output_path}/blockstates"

colors = [
    "",
    "white",
    "orange",
    "magenta",
    "light_blue",
    "yellow",
    "lime",
    "pink",
    "gray",
    "light_gray",
    "cyan",
    "purple",
    "blue",
    "brown",
    "green",
    "red",
    "black"
]


def write_json(path: str, file_name: str, content: str):
    try:
        file = open(f"{path}/{file_name}.json", "x")
        file.write(content)
        file.close()
        print(f"[Created] {path}/{file_name}.json")
    except FileExistsError:
        file = open(f"{path}/{file_name}.json", "w")
        file.write(content)
        file.close()
        print(f"[Overwritten] {path}/{file_name}.json")


class ModelEncoder:
    def __init__(self, namespace: str, path: str, model_name: str, texture: str, is_tex_vanilla: bool):
        self.namespace = namespace
        self.model_name = model_name
        self.texture = texture
        self.is_tex_vanilla = is_tex_vanilla
        self.path = path

        if path == "":
            self.full_path = model_name
        else:
            self.full_path = f"{path}/{model_name}"
