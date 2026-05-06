def get_cidr():
    user_input = input("Please enter your CIDR\n")
    ip_addr, prefix = user_input.split("/")
    return ip_addr, int(prefix)


def get_subnet_mask(prefix):
    subnet_mask = ""
    bits_remaining = prefix % 8
    full_octects = int(prefix / 8)

    for _ in range(full_octects):
        subnet_mask += "255."

    inverse_remaining = 8 - bits_remaining
    subnet_mask += str(256 - 2**inverse_remaining)

    for _ in range(3 - full_octects):
        subnet_mask += ".0"

    return subnet_mask


def get_usable_hosts(prefix):
    # could skip check for `== 32` and return abs()
    if prefix == 32:
        return 1

    return 2 ** (32 - prefix) - 2


def get_block_size(prefix):
    bits_remaining = prefix % 8
    block_size = 256 / 2**bits_remaining
    return int(block_size)


def get_network_addr(ip_addr, block_size):
    split_ip = ip_addr.split(".")
    # integer division followed by multiplication gives the first element of the block
    last_octect = int(int(split_ip[3]) / block_size) * block_size
    network_addr = ""
    for i in range(3):
        network_addr += split_ip[i] + "."
    network_addr += str(last_octect)
    return network_addr


def main():
    ip_addr, prefix = get_cidr()

    total_ips = 2 ** (32 - prefix)
    usable_hosts = get_usable_hosts(prefix)
    subnet_mask = get_subnet_mask(prefix)
    block_size = get_block_size(prefix)
    network_addr = get_network_addr(ip_addr, block_size)

    print("Total IPs:       " + str(total_ips))
    print("Subnet mask:     " + str(subnet_mask))
    print("Usable hosts:    " + str(usable_hosts))
    print("Block size:      " + str(block_size))
    print("Network Addr:    " + str(network_addr))


if __name__ == "__main__":
    main()
