import os.path


def row_to_string(row):
    return " & ".join(list(map(str, row)))


def latex_generator_for_table(table: list[list]) -> str:
    max_len = max(map(len, table))
    template = """\\begin{{center}}
    \\begin{{tabular}} {}
        {}    
    \\end{{tabular}}
\\end{{center}}"""
    parameter_for_column_size = ["{"] + ["c" for _ in range(max_len)] + ["}"]
    string_for_parameter = " ".join(parameter_for_column_size)
    rows_list = list(map(row_to_string, table))
    table_string = " \\\\\n".join(rows_list)
    final_latex_string_for_table = template.format(string_for_parameter, table_string)
    return final_latex_string_for_table


def latex_generator_for_images(image_path: str) -> str:
    file_name_with_extension = os.path.basename(image_path)
    file_name = os.path.splitext(file_name_with_extension)[0]
    image_template = f"\\includegraphics{{ {file_name} }}"
    return image_template
