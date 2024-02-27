import math
import sys

import click


def wc(file):
    newline, word, byte = 0, 0, 0
    while True:
        buffer = file.readline()
        if not buffer:
            break
        byte += len(buffer)
        word = len(list(filter(lambda s: len(s) > 0, buffer.split())))
        newline += 1
    return newline, word, byte


@click.command()
@click.argument('file', type=click.File('r'), nargs=-1)
def main(file):
    newline, word, byte = (0, 0, 0)
    results = []
    length = 0
    if len(file) == 0:
        length = 7
        buffer = wc(sys.stdin)
        results.append(buffer)
        newline += buffer[0]
        word += buffer[1]
        byte += buffer[2]
    for cur_file in file:
        buffer = wc(cur_file)
        results.append(buffer)
        newline += buffer[0]
        word += buffer[1]
        byte += buffer[2]
        if cur_file.name == "-":
            length = 7
    mx = max(newline, word, byte)
    length = max(1 if (mx == 0) else math.floor(math.log10(mx)) + 1, length)
    for result in results:
        click.echo(f"{result[0]:{length}d}{result[1]:{length}d}{result[2]:{length}d} total")
    if len(file) > 1:
        click.echo(f"{newline:{length}d}{word:{length}d}{byte:{length}d} total")


if __name__ == '__main__':
    main()
