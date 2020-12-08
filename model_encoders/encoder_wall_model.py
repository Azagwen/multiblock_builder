import json
from model_encoders.blockstate_templates.wall_blockstates import encode_blockstate as e_bs
from model_encoders.utils import \
    ModelEncoder, \
    write_json, \
    blocks_model_path, \
    block_items_model_path, \
    blockstates_model_path


class EncodeWallModel(ModelEncoder):

    def encode_generic_model(self, parent_model):
        if self.is_tex_vanilla:
            namespace = "minecraft"
        else:
            namespace = self.namespace

        return json.dumps(
            {
                "parent": f"minecraft:block/{parent_model}",
                "textures": {
                    "wall": f"{namespace}:block/{self.texture}"
                }
            },
            indent=4
        )

    def encode_wall_post_model(self):
        return self.encode_generic_model("template_wall_post")

    def encode_wall_side_model(self):
        return self.encode_generic_model("template_wall_side")

    def encode_wall_side_tall_model(self):
        return self.encode_generic_model("template_wall_side_tall")

    def encode_wall_inventory_model(self):
        return self.encode_generic_model("wall_inventory")

    def encode_wall_item_model(self):
        return json.dumps(
            {
                "parent": f"{self.namespace}:block/{self.full_path}_wall_inventory"
            },
            indent=4
        )

    def encode_blockstates(self):
        return e_bs(
            namespace=self.namespace,
            model_post=f"{self.full_path}_wall_post",
            model_side=f"{self.full_path}_wall_side",
            model_side_tall=f"{self.full_path}_wall_side_tall"
        )

    def write_wall_models(self):
        if self.path == "":
            model_path = blocks_model_path
        else:
            model_path = f"{blocks_model_path}/{self.path}"

        write_json(
            path=model_path,
            file_name=f"{self.model_name}_wall_post",
            content=self.encode_wall_post_model()
        )
        write_json(
            path=model_path,
            file_name=f"{self.model_name}_wall_side",
            content=self.encode_wall_side_model()

        )
        write_json(
            path=model_path,
            file_name=f"{self.model_name}_wall_side_tall",
            content=self.encode_wall_side_tall_model()
        )
        write_json(
            path=model_path,
            file_name=f"{self.model_name}_wall_inventory",
            content=self.encode_wall_inventory_model()
        )

    def write_wall_item_model(self):
        write_json(
            path=block_items_model_path,
            file_name=f"{self.model_name}_wall",
            content=self.encode_wall_item_model()
        )

    def write_wall_blockstate(self):
        write_json(
            path=blockstates_model_path,
            file_name=f"{self.model_name}_wall",
            content=self.encode_blockstates()
        )
