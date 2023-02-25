dna_file = "cgtcgggggggggggggggggggtttttttttttaaaaaaaaaaaaaaaa"
match_file = "gt"

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
    return sum

def main():
    dna = dna_file
    seq = match_file
    seq_len = len(seq)

    positions_found = get_positions_found(dna, seq)
    subsequences = get_subsequences(dna, seq)

    print("Se encontraró la secuencia " + str(len(positions_found)) + " veces.\n")
    
    positions_str = ""
    for i in positions_found:
        positions_str += " (" + str(i) + "," + str(i+seq_len) + ") "    
    print("    Posiciones: {" + positions_str + "} \n\n")


    print("La secuencia de ADN se dividió en " + str(len(positions_found)+1) + " subsecuencias.\n")
    for i in range(len(subsequences)):
        print("    Subsecuencia "+str(i+1)+":\n")
        print("        Peso:  " + str(compute_weight(subsequences[i])) + " g/mol \n")
        print("        Representación:  " + subsequences[i] + "\n")

if __name__ == "__main__":
    main()