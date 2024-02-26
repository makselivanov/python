import click


@click.command()
@click.argument('file', type=click.File('r'), default="-")
def main(file):
    index = 0
    while True:
        line = file.readline()
        if not line:
            break
        index += 1
        click.echo(f"{index:6d}\t{line}", nl=False)


if __name__ == '__main__':
    main()
