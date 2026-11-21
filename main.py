import argparse
import hashlib

# python3 main.py --id 00752901 --name WL-001
# Result:
#define DEVICE_NAME "WL-001"
#define PRIVATE_KEY "a051adffd887ec1e7395bd760546f112"


def gen_device_key(device_id):
    # example:
    # device_id = "00E0C0DB" // 8 characters
    # secret_code = "77gsrs7q4x4th9q2dfppv6kh" // 24 characters
    # gen_key = [00][77gsrs][E0][7q4x4t][C0][h9q2df][DB][ppv6kh] // 36 characters
    # return public_key == md5(gen_key)
    secret_code = "77gsrs7q4x4th9q2dfppv6kh"
    gen_key = ""
    for i in range(0, 4):
        gen_key += (
            device_id[i * 2 : i * 2 + 2] + secret_code[i * 6 : i * 6 + 6]
        )
    private_key = hashlib.md5(gen_key.encode("utf-8")).hexdigest()
    return device_id, gen_key, private_key


def check_device_id_exist(filename, device_id):
    try:
        with open(filename, "r") as f:
            for line in f:
                if device_id in line:
                    return True
        return False
    except FileNotFoundError:
        return False


def main(device_id, device_name):
    device_id, gen_key, private_key = gen_device_key(device_id)
    # name = device_name + "-" + private_key[-4:].upper()
    # #define DEVICE_NAME "WL-001"
    #define PRIVATE_KEY "adf1ad18326aade806ecd1ce4d781643"
    
    # device_name = "CB-001" => device_number = 1
    device_number = int(device_name.split("-")[1])
    print(f"#if DEVICE == {device_number}")
    print(f"#define DEVICE_NAME \"{device_name}\"")
    print(f"#define PRIVATE_KEY \"{private_key}\"")
    print("#endif")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--id", type=str, help="Device ID")
    args.add_argument("--name", type=str, help="Device Name")

    device_id = args.parse_args().id
    device_name = args.parse_args().name

    main(device_id, device_name)