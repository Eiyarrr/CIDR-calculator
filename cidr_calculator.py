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
    return 256 / 2**bits_remaining


def main():
    ip_addr, prefix = get_cidr()

    total_ips = 2 ** (32 - prefix)
    usable_hosts = get_usable_hosts(prefix)
    subnet_mask = get_subnet_mask(prefix)
    block_size = get_block_size(prefix)

    print(total_ips)
    print(subnet_mask)
    print(usable_hosts)
    print(block_size)


if __name__ == "__main__":
    main()
