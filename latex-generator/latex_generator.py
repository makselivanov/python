def row_to_string(row):
    return " & ".join(list(map(str, row)))


def generate_latex_string_for_table(table: list[list]) -> str:
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


def latex_generator_for_table(table: list[list]) -> str:
    template = """\\documentclass{{article}}
\\begin{{document}}
    {}
\\end{{document}}
"""

    latex_string_for_table = generate_latex_string_for_table(table)

    final_latex_string_for_document = template.format(latex_string_for_table)
    return final_latex_string_for_document
