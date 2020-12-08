from model_encoders.model_writer import create_output_dirs, create_colored_block_models

full_block = 0
stairs = 1
slabs = 2
wall = 2


def quit_check(input_text: str):
    quit_command = "quit"
    if input_text.lower() == quit_command:
        quit()


while True:

    namespace = input("Namespace: ")
    quit_check(namespace)
    block_name = input("Block Name: ")
    quit_check(block_name)
    model_path = input("Model Path: ")
    quit_check(model_path)
    van_tex = input("Use vanilla Texture ? (True/False): ")
    quit_check(van_tex)
    block_type = input("""Block Type :
0 - full block
1 - stairs
2 - slab
3 - wall
>""")
    quit_check(block_type)
    double_slab_path = input("Double Slab Model Path (used for Type 2): ")
    quit_check(double_slab_path)

    if van_tex == "False":
        is_texture_vanilla = False
    else:
        is_texture_vanilla = True

    create_output_dirs(model_path)
    create_colored_block_models(
        namespace=namespace,
        block_name=block_name,
        model_path=model_path,
        is_tex_vanilla=is_texture_vanilla,
        block_type=int(block_type),
        double_slab_path=double_slab_path
    )

    print("")
