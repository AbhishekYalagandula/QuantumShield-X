#include <openssl/rsa.h>
#include <openssl/aes.h>
#include <openssl/sha.h>

void encrypt()
{
    RSA_generate_key(2048, RSA_F4, NULL, NULL);

    AES_encrypt(nullptr, nullptr, nullptr);

    SHA1(nullptr, 0, nullptr);
}