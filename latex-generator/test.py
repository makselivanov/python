from latex_generator import latex_generator_for_table, latex_generator_for_images


def main():
    test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    image_path = "./artifacts/images/sadcat.png"
    tex_string = f"""\\documentclass{{article}}
\\usepackage{{graphicx}}
\\graphicspath{{ {{./images/}} }}

\\begin{{document}}
{latex_generator_for_table(test_list)}
{latex_generator_for_images(image_path)}
\\end{{document}}
    """
    with open("../artifacts/table.tex", "w") as file:
        file.writelines(tex_string)


if __name__ == '__main__':
    main()
