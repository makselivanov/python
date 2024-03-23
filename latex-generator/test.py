from latex_generator import latex_generator_for_table


def main():
    test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lines = latex_generator_for_table(test_list)
    with open("../artifacts/table.tex", "w") as file:
        file.writelines(lines)


if __name__ == '__main__':
    main()
