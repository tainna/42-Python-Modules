

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        arquivo = open("ancient_fragment.txt")
    
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    
    arq = arquivo.read()

    print(f"Data: {arq}")

    arquivo.close
    print("\nData recovery complete. Storage unit disconnected.")

except FileNotFoundError:
    print("Error: File not found")
pass