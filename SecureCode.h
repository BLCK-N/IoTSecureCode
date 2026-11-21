#ifndef SecureCode_h
#define SecureCode_h

#include <Arduino.h>

#include "Obfuscation.h"
#include "md5.h"

bool check_secure_code(const char* device_id, const char* private_key);

void gen_md5(const char* data, char* md5_data);

void clear_data(char* data, unsigned char len);

#endif