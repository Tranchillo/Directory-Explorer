import os

def list_directory(directory, indent=""):
    try:
        items = os.listdir(directory)
        report = ""
        
        # Ordina gli elementi alfabeticamente
        items.sort()
        
        for item in items:
            path = os.path.join(directory, item)
            
            if os.path.isdir(path):
                report += f"{indent}|-- {item}/\n"
                # Esplora ricorsivamente la sottodirectory
                report += list_directory(path, indent + "    ")
            else:
                report += f"{indent}|-- {item}\n"
                
        return report
    except Exception as e:
        return f"{indent}|-- [Errore: {str(e)}]\n"

def main():
    # Usa la directory corrente dove si trova lo script
    main_directory = os.getcwd()

    # Crea il report
    report = f"Struttura completa della directory: {main_directory}\n"
    report += list_directory(main_directory)

    # Nome del file di output
    output_file = "struttura_directory.txt"

    # Salva il report
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report completo generato in '{output_file}'")

if __name__ == "__main__":
    main()
