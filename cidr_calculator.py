def get_cidr():
    user_input = input("Please enter your CIDR\n")
    ip_addr, prefix = user_input.split("/")
    return ip_addr, int(prefix)


def main():
    ip_addr, prefix = get_cidr()
    total_ips = 2 ** (32 - prefix)


if __name__ == "__main__":
    main()
