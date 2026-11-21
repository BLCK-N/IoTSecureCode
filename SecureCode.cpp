#include "SecureCode.h"

bool check_secure_code(const char* device_id, const char* private_key) {
  const char* secret_code = XOR("77gsrs7q4x4th9q2dfppv6kh");
  char gen_key[33];
  clear_data(gen_key, 33);
  for (unsigned char i = 0; i < 4; i++) {
    unsigned char j;
    for (j = 0; j < 2; j++) {
      gen_key[i * 8 + j] = device_id[i * 2 + j];
    }
    for (unsigned char k = 0; k < 6; k++) {
      gen_key[i * 8 + j + k] = secret_code[i * 6 + k];
    }
  }

  char md5_data[33];
  gen_md5(gen_key, md5_data);
  return strcmp(md5_data, private_key) == 0;
}

void gen_md5(const char* data, char* md5_data) {
  MD5 md5;
  md5.add(data, strlen(data));
  strcpy(md5_data, md5.getHash().c_str());
}
void clear_data(char* data, unsigned char len) {
  for (unsigned char i = 0; i < len; i++) {
    data[i] = '\0';
  }
}