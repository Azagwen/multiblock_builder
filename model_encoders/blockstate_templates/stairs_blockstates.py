import json


def encode_blockstate(namespace: str, model: str, model_inner: str, model_outer: str):
    return json.dumps(
        {
            "variants": {
                "facing=east,half=bottom,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=east,half=bottom,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}"
                },
                "facing=east,half=bottom,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=east,half=bottom,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}"
                },
                "facing=east,half=bottom,shape=straight": {
                    "model": f"{namespace}:block/{model}"
                },
                "facing=east,half=top,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=east,half=top,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=east,half=top,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=east,half=top,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=east,half=top,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=top,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=top,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=north,half=top,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=top,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=north,half=top,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=south,half=bottom,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}"
                },
                "facing=south,half=bottom,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=bottom,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}"
                },
                "facing=south,half=bottom,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=bottom,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=top,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=top,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=south,half=top,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=top,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=south,half=top,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=top,shape=inner_left": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=top,shape=inner_right": {
                    "model": f"{namespace}:block/{model_inner}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=west,half=top,shape=outer_left": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=top,shape=outer_right": {
                    "model": f"{namespace}:block/{model_outer}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=west,half=top,shape=straight": {
                    "model": f"{namespace}:block/{model}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                }
            }
        },
        indent=4
    )
