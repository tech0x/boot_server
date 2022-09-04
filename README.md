
0. Default server network 10.0.3.0/24 and main server must have ip 10.0.3.11 (for backup boot server by default used ip 10.0.3.240)
0. Default password for boot image is "DefaultPassword"

1. Change if needed ip and boot logic src/local.ipxe and build ipxe boot loader with new settings ./docker-compose -f ipxe.yaml up --build
2. Setup dhcpd config etc/dhcp
3. Place public rsa key for ssh auth app/id_rsa.pub
4. Place boot config in app/templates mac.boot
5. Place run config in app/templates mac.config
6. Run ./docker-compose up --build
