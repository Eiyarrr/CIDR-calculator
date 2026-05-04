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


def main():
    ip_addr, prefix = get_cidr()

    total_ips = 2 ** (32 - prefix)
    subnet_mask = get_subnet_mask(prefix)


if __name__ == "__main__":
    main()
