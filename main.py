def main():
    input_file = input('input file path: ')

    with open(input_file, 'r') as f:
        comp_input = f.read()


    comp_input = comp_input.replace('func', '[f]')
    comp_input = comp_input.replace(' ', '')
    comp_input = comp_input.replace('\n', '')

    comp_output = ''

    print(comp_input)

    return


if __name__ == '__main__':
    main()
