find . | cpio --create --format='newc' | gzip -9 > ../initrd.new
