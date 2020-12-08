import json
from model_encoders.blockstate_templates.stairs_blockstates import encode_blockstate as e_bs
from model_encoders.utils import \
    ModelEncoder, \
    write_json, \
    blocks_model_path, \
    block_items_model_path, \
    blockstates_model_path


class EncodeStairsModel(ModelEncoder):

    def encode_generic_model(self, parent_model):
        if self.is_tex_vanilla:
            namespace = "minecraft"
        else:
            namespace = self.namespace

        return json.dumps(
            {
                "parent": f"minecraft:block/{parent_model}",
                "textures": {
                    "bottom": f"{namespace}:block/{self.texture}",
                    "top": f"{namespace}:block/{self.texture}",
                    "side": f"{namespace}:block/{self.texture}"
                }
            },
            indent=4
        )

    def encode_stairs_model(self):
        return self.encode_generic_model("stairs")

    def encode_inner_stairs_model(self):
        return self.encode_generic_model("inner_stairs")

    def encode_outer_stairs_model(self):
        return self.encode_generic_model("outer_stairs")

    def encode_stairs_item_model(self):
        return json.dumps(
            {
                "parent": f"{self.namespace}:block/{self.full_path}_stairs"
            },
            indent=4
        )

    def encode_blockstates(self):
        return e_bs(
            namespace=self.namespace,
            model=f"{self.full_path}_stairs",
            model_inner=f"{self.full_path}_stairs_inner",
            model_outer=f"{self.full_path}_stairs_outer"
        )

    def write_stairs_models(self):
        if self.path == "":
            model_path = blocks_model_path
        else:
            model_path = f"{blocks_model_path}/{self.path}"

        write_json(
            path=model_path,
            file_name=f"{self.model_name}_stairs",
            content=self.encode_stairs_model()
        )
        write_json(
            path=model_path,
            file_name=f"{self.model_name}_stairs_inner",
            content=self.encode_inner_stairs_model()

        )
        write_json(
            path=model_path,
            file_name=f"{self.model_name}_stairs_outer",
            content=self.encode_outer_stairs_model()
        )

    def write_stairs_item_model(self):
        write_json(
            path=block_items_model_path,
            file_name=f"{self.model_name}_stairs",
            content=self.encode_stairs_item_model()
        )

    def write_stairs_blockstate(self):
        write_json(
            path=blockstates_model_path,
            file_name=f"{self.model_name}_stairs",
            content=self.encode_blockstates()
        )
