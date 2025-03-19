import sys
import sha3


def normalize(address: str):
    if (address.startswith("0x")):
        address = address[2:]
    return address, address.lower()


def is_valid_eip_55(address: str, checksum: str, normalized_address: str):
    final_address = ""

    for key, value in enumerate(address):
        if int(checksum[key], 16) > 7:
            final_address += value.upper()
        else:
            final_address += value

    return final_address == address


def main(address: str):
    address, normalized_address = normalize(address)
    assert len(address) == 40, "Not a valid ethereum address"
    keccak = sha3.keccak_256()
    keccak.update(normalized_address.encode())
    checksum = keccak.hexdigest()[:40]

    if is_valid_eip_55(address, checksum, normalized_address):
        print("valid")
    else:
        print("invalid!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} address")
        exit(0)

    main(sys.argv[1])
