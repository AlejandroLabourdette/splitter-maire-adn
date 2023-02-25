import argparse
import sys


def arg_parser() -> argparse.ArgumentParser:
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help="path to the file where is written the dna sequence")
    argParser.add_argument("-s", "--sequence", help="path to the file where is written the subsequence to match in the dna sequence")
    argParser.add_argument("-o", "--output", help="path to the file where the output should be stored")

    return argParser

def get_files_paths(parser: argparse.ArgumentParser, argv: list[str]):
    args = parser.parse_args(argv)
    if args.input == None or args.sequence == None:
        print('Arguments --input and --sequence should be included in the command. Please execute python3 main.py -h to see more information.')
        sys.exit(2)
    return args

def get_positions_found(dna: str, seq: str) -> list[int]:
    seq_len = len(seq)
    positions_found = []
    last_position = 0
    while True:
        position_found = dna.find(seq, last_position)
        if position_found == -1:
            break
        positions_found.append(position_found)
        last_position = position_found + seq_len
    return positions_found

def get_subsequences(dna: str, seq: str) -> list[int]:
    return dna.split(seq)
    
def compute_weight(sequence: str) -> float:
    sum = 0
    for c in sequence:
        if c == 'a':
            sum += 313.2
        elif c == 'c':
            sum += 289.2
        elif c == 'g':
            sum += 329.2
        elif c == 't':
            sum += 304.2
        else:
            print('Caracter inesperado en la secuencia de adn: ' + c)
            sys.exit(2)
    return sum

def main(argv: list[str]):
    parser = arg_parser()
    args = get_files_paths(parser, argv)

    dna = open(args.input, "r").read()
    seq = open(args.sequence, "r").read()
    seq_len = len(seq)

    positions_found = get_positions_found(dna, seq)
    subsequences = get_subsequences(dna, seq)

    output_file = open(args.output, "w")
    output_file.write("Se encontraró la secuencia " + str(len(positions_found)) + " veces.\n")
    
    positions_str = ""
    for i in positions_found:
        positions_str += " (" + str(i) + "," + str(i+seq_len) + ") "    
    output_file.write("    Posiciones: {" + positions_str + "} \n\n")


    output_file.write("La secuencia de ADN se dividió en " + str(len(positions_found)+1) + " subsecuencias.\n")
    for i in range(len(subsequences)):
        output_file.write("    Subsecuencia "+str(i+1)+":\n")
        output_file.write("        Peso:  " + str(compute_weight(subsequences[i])) + " g/mol \n")
        output_file.write("        Representación:  " + subsequences[i] + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])