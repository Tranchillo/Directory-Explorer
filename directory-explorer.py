import os

def list_directory(directory, indent="", skip_dirs=None):
    try:
        # Elenco delle directory da saltare
        if skip_dirs is None:
            skip_dirs = []

        items = os.listdir(directory)
        report = ""

        # Ordina gli elementi alfabeticamente
        items.sort()

        for item in items:
            path = os.path.join(directory, item)
            
            # Salta le directory specificate
            if os.path.isdir(path) and item in skip_dirs:
                report += f"{indent}|-- {item}/ [Saltato]\n"
                continue
            
            if os.path.isdir(path):
                report += f"{indent}|-- {item}/\n"
                # Esplora ricorsivamente la sottodirectory
                report += list_directory(path, indent + "    ", skip_dirs)
            else:
                report += f"{indent}|-- {item}\n"

        return report
    except Exception as e:
        return f"{indent}|-- [Errore: {str(e)}]\n"

def main():
    # Usa la directory corrente dove si trova lo script
    main_directory = os.getcwd()

    # Directory da saltare
    skip_dirs = ["venv"]

    # Crea il report
    report = f"Struttura completa della directory: {main_directory}\n"
    report += list_directory(main_directory, skip_dirs=skip_dirs)

    # Nome del file di output
    output_file = "struttura_directory.txt"

    # Salva il report
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report completo generato in '{output_file}'")

if __name__ == "__main__":
    main()
