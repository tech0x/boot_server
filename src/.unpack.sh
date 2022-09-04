mkdir -p $1
cd $1
cpio -id < ../$2
