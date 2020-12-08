import json
from model_encoders.utils import \
    ModelEncoder, \
    write_json, \
    blocks_model_path, \
    block_items_model_path, \
    blockstates_model_path


class EncodeFullBlockModel(ModelEncoder):

    def encode_full_block_model(self):
        if self.is_tex_vanilla:
            namespace = "minecraft"
        else:
            namespace = self.namespace

        return json.dumps(
            {
                "parent": "minecraft:block/cube_all",
                "textures": {
                    "all": f"{namespace}:block/{self.texture}"
                }
            },
            indent=4
        )

    def encode_block_item_model(self):
        return json.dumps(
            {
                "parent": f"{self.namespace}:block/{self.full_path}"
            },
            indent=4
        )

    def encode_blockstates(self):
        return json.dumps(
            {
                "variants": {
                    "": {
                        "model": f"{self.namespace}:block/{self.full_path}"
                    }
                }
            },
            indent=4
        )

    def write_block_model(self):
        if self.path == "":
            model_path = blocks_model_path
        else:
            model_path = f"{blocks_model_path}/{self.path}"

        write_json(
            path=model_path,
            file_name=self.model_name,
            content=self.encode_full_block_model()
        )

    def write_block_item_model(self):
        write_json(
            path=block_items_model_path,
            file_name=self.model_name,
            content=self.encode_block_item_model()
        )

    def write_block_blockstate(self):
        write_json(
            path=blockstates_model_path,
            file_name=self.model_name,
            content=self.encode_blockstates()
        )
