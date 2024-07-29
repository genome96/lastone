#!/bin/bash

git clone https://github.com/magnific0/wondershaper.git
cd wondershaper
make install
cd
rm -rf wondershaper
cd
cat > /home/re_otm <<-END
7
END

service cron restart > /dev/null 2>&1

rm -f /root/set-br.sh
