#!/bin/bash

#make bin-x86_64-efi/ipxe.efi EMBED=local.ipxe
make -j4 -l4  bin/ipxe.kpxe EMBED=local.ipxe DEBUG=scsi,iscsi
