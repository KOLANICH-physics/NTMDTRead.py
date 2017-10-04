#!/usr/bin/env bash
apt-get update

if ! $(apt-get -y install gnupg-curl); then
  apt-get -y install gnupg1-curl
fi;
apt-get install -y apt-transport-https

echo "deb https://dl.bintray.com/kaitai-io/debian_unstable jessie main" >> /etc/apt/sources.list.d/kaitai.list
apt-key adv --keyserver hkps://keyserver.ubuntu.com --recv 8756C4F765C9AC3CB6B85D62379CE192D401AB61
apt-get update
apt-get install -y kaitai-struct-compiler

#git clone --depth=1 https://github.com/kaitai-io/kaitai_struct_formats.git "$KAITAI_STRUCT_ROOT/formats"
ksc --help
apt-get install -y kaitai-struct-compiler

#git clone --depth=1 https://github.com/kaitai-io/kaitai_struct_formats.git "$KAITAI_STRUCT_ROOT/formats"
ksc --help
