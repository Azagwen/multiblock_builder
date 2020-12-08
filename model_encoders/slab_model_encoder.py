import json
from model_encoders.utils import \
    ModelEncoder, \
    write_json, \
    blocks_model_path, \
    block_items_model_path, \
    blockstates_model_path


class EncodeSlabModel(ModelEncoder):

    def __init__(
            self,
            namespace: str,
            path: str,
            model_name: str,
            texture: str,
            is_tex_vanilla: bool,
            double_slab_path: str
    ):
        self.double_slab_path = double_slab_path
        super().__init__(namespace, path, model_name, texture, is_tex_vanilla)

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

    def encode_slab_bottom_model(self):
        return self.encode_generic_model("slab")

    def encode_slab_top_model(self):
        return self.encode_generic_model("slab_top")

    def encode_slab_item_model(self):
        return json.dumps(
            {
                "parent": f"{self.namespace}:block/{self.full_path}_slab"
            },
            indent=4
        )

    def encode_blockstates(self):
        if self.is_tex_vanilla:
            namespace = "minecraft"
            path = self.model_name
        else:
            namespace = self.namespace
            path = f"{self.double_slab_path}/{self.model_name}"

        return json.dumps(
            {
                "variants": {
                    "type=bottom": {
                        "model": f"{self.namespace}:block/{self.full_path}_slab"
                    },
                    "type=double": {
                        "model": f"{namespace}:block/{path}"
                    },
                    "type=top": {
                        "model": f"{self.namespace}:block/{self.full_path}_slab_top"
                    }
                }
            }
        )

    def write_slab_models(self):
        if self.path == "":
            model_path = blocks_model_path
        else:
            model_path = f"{blocks_model_path}/{self.path}"

        write_json(
            path=model_path,
            file_name=f"{self.model_name}_slab",
            content=self.encode_slab_bottom_model()
        )
        write_json(
            path=model_path,
            file_name=f"{self.model_name}_slab_top",
            content=self.encode_slab_top_model()

        )

    def write_slab_item_model(self):
        write_json(
            path=block_items_model_path,
            file_name=f"{self.model_name}_slab",
            content=self.encode_slab_item_model()
        )

    def write_slab_blockstate(self):
        write_json(
            path=blockstates_model_path,
            file_name=f"{self.model_name}_slab",
            content=self.encode_blockstates()
        )
