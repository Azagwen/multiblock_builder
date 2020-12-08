from model_encoders.full_block_model_encoder import EncodeFullBlockModel
from model_encoders.stairs_model_encoder import EncodeStairsModel
from model_encoders.slab_model_encoder import EncodeSlabModel
from model_encoders.wall_model_encoder import EncodeWallModel
from model_encoders.utils import \
    output_path, \
    models_path, \
    blocks_model_path, \
    block_items_model_path, \
    blockstates_model_path, \
    colors

import os


def create_dir(path: str):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"[Notice] {path} already exists !")


class WriteFiles:

    def __init__(self, namespace: str, path: str, model_name: str, texture: str, is_tex_vanilla: bool, parent_model: int, double_slab_path: str):
        self.namespace = namespace
        self.model_name = model_name
        self.texture = texture
        self.is_tex_vanilla = is_tex_vanilla
        self.parent_model = parent_model
        self.path = path
        self.double_slab_path = double_slab_path

    def write_json_files(self):
        pm = self.parent_model
        encode_full_block = EncodeFullBlockModel(
            self.namespace,
            self.path,
            self.model_name,
            self.texture,
            self.is_tex_vanilla)
        encode_stairs = EncodeStairsModel(
            self.namespace,
            self.path,
            self.model_name,
            self.texture,
            self.is_tex_vanilla)
        encode_slab = EncodeSlabModel(
            self.namespace,
            self.path,
            self.model_name,
            self.texture,
            self.is_tex_vanilla,
            self.double_slab_path)
        encode_wall = EncodeWallModel(
            self.namespace,
            self.path,
            self.model_name,
            self.texture,
            self.is_tex_vanilla)

        # Write models
        if pm == 0:
            encode_full_block.write_block_model()
            encode_full_block.write_block_item_model()
            encode_full_block.write_block_blockstate()
        elif pm == 1:
            encode_stairs.write_stairs_models()
            encode_stairs.write_stairs_item_model()
            encode_stairs.write_stairs_blockstate()
        elif pm == 2:
            encode_slab.write_slab_models()
            encode_slab.write_slab_item_model()
            encode_slab.write_slab_blockstate()
        elif pm == 3:
            encode_wall.write_wall_models()
            encode_wall.write_wall_item_model()
            encode_wall.write_wall_blockstate()


def create_output_dirs(special_model_path: str):
    create_dir(output_path)
    create_dir(models_path)
    create_dir(blocks_model_path)
    create_dir(block_items_model_path)
    create_dir(blockstates_model_path)
    try:
        os.makedirs(f"{blocks_model_path}/{special_model_path}")
    except FileExistsError:
        print(f"[Notice] {blocks_model_path}/{special_model_path} already exists !")


def create_colored_block_models(
        namespace: str,
        block_name: str,
        model_path: str,
        is_tex_vanilla: bool,
        block_type: int,
        double_slab_path: str
):
    for color in colors:
        name = block_name
        if color == "":
            model_name = name
        else:
            model_name = f"{color}_{name}"

        file_writer = WriteFiles(
            namespace=namespace,
            path=model_path,
            model_name=model_name,
            texture=model_name,
            is_tex_vanilla=is_tex_vanilla,
            parent_model=block_type,
            double_slab_path=double_slab_path
        )
        file_writer.write_json_files()
