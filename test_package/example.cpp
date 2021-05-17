#include <iostream>
#include <libvault/VaultClient.h>

int main(void)
{
  Vault::HttpErrorCallback httpErrorCallback = [&](std::string err) {
    std::cout << "Everything is fine, curl timed out" << std::endl;
  };

  Vault::Token token{"example_token"};
  Vault::TokenStrategy tokenStrategy{token};

  Vault::Config config = Vault::ConfigBuilder().build();
  Vault::Client vaultClient{config, tokenStrategy, httpErrorCallback};
  std::cout << "Client created succesfully with token : " << vaultClient.getToken() << std::endl;

  Vault::KeyValue kv{vaultClient, Vault::KeyValue::Version::v1};
  Vault::Path key{"hello"};
  Vault::Parameters parameters(
      {
          {"foo","world"},
          {"baz","quux"},
          {"something", "something else"},
      }
  );

  kv.create(key, parameters);
}