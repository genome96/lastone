#!/bin/bash

clear
G='\e[1;32m'
Y='\e[0;33m'
C='\e[1;36m'
O='\e[1;37;46m'
W='\e[1;37m'
N='\e[0m'
FILE="/usr/local/bin/ws-stunnel"
BACKUP_FILE="${FILE}.bak"

if [ ! -f "$BACKUP_FILE" ]; then
    cp "$FILE" "$BACKUP_FILE"
fi

clear
echo -e " $C—————————————————————————————————————————$N"
echo -e " $O         UBAH RESPON HTTP/1.1 101        $N"
echo -e " $C—————————————————————————————————————————$N"
echo
echo -e " ${Y}Masukkan teks baru ${G}!!!${N}"
read -rp " $(echo -e "${C}---> : ${N}")" teksmu
echo -e " ${Y}Masukkan warna contoh: cyan ${G}!!!${N}"
read -rp " $(echo -e "${C}---> : ${N}")" warnamu

# Baris yang akan diganti
OLD_LINE="RESPONSE = 'HTTP/1.1"
# Baris baru pengganti dengan escape karakter yang diperlukan
NEW_LINE="RESPONSE = 'HTTP/1.1 101 <b><font color=${warnamu}>${teksmu}</font></b>\\r\\nUpgrade: websocket\\r\\nConnection: Upgrade\\r\\nSec-WebSocket-Accept: foo\\r\\n\\r\\n'"

# Escape baris baru untuk digunakan dalam sed
NEW_LINE_ESCAPED=$(echo "$NEW_LINE" | sed 's/[&/\]/\\&/g')

# Menggunakan sed untuk mengganti baris yang mengandung OLD_LINE dengan NEW_LINE_ESCAPED
sed -i "\|^${OLD_LINE}|c\\${NEW_LINE_ESCAPED}" "$FILE"

systemctl restart ws-stunnel
clear
if [[ $warnamu == "red" ]]; then
	warna='\e[1;31m'
elif [[ $warnamu == "green" ]]; then
	warna='\e[1;32m'
elif [[ $warnamu == "yellow" ]]; then
        warna='\e[1;33m'
elif [[ $warnamu == "blue" ]]; then
        warna='\e[1;34m'
elif [[ $warnamu == "magenta" ]]; then
        warna='\e[1;35m'
elif [[ $warnamu == "cyan" || $warnamu == "aqua" ]]; then
        warna='\e[1;36m'
elif [[ $warnamu == "white" ]]; then
        warna='\e[1;37m'
fi
baru="${warna}${teksmu}${N}"
echo
echo -e " ${G}DONE!!!${N}"
echo -e " Respon ${W}HTTP/1.1 101 ${baru} ${W}Sudah aktif${N}"
echo -e "${W} Silahkan konekkan SSH.nya untuk dites!!!${N}"
