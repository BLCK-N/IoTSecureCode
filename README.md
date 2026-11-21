# Secure Code for IoT device

## Generate `private_key` from `device_id` and `secret_code`

- Device ID: `device_id = [12] [34] [56] [78]` (8 characters)

- Secret Code: `secret_code = [xiht7s] [65s6r3] [hd489c] [qr5rg9]` (24 characters)

- Generate key: `key = [12][xiht7s] [34][65s6r3] [56][hd489c] [78][qr5rg9]` (32 characters)

- Private key: `private_key = md5(key)` (33 characters)

## Code test

- File `tools/main.cpp`
