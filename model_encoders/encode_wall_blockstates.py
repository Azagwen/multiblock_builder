import json


def encode_blockstate(namespace: str, model_post: str, model_side: str, model_side_tall: str):
    return json.dumps(
        {
            "multipart": [
                {
                    "when": {
                        "up": "true"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_post}"
                    }
                },
                {
                    "when": {
                        "north": "low"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side}",
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "east": "low"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side}",
                        "y": 90,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "south": "low"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side}",
                        "y": 180,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "west": "low"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side}",
                        "y": 270,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "north": "tall"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side_tall}",
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "east": "tall"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side_tall}",
                        "y": 90,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "south": "tall"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side_tall}",
                        "y": 180,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "west": "tall"
                    },
                    "apply": {
                        "model": f"{namespace}:block/{model_side_tall}",
                        "y": 270,
                        "uvlock": True
                    }
                }
            ]
        }
    )
