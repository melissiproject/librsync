all :
	mkdir -p build
	gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.6 -c _librsyncmodule.c -o build/_librsyncmodule.o
	gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions build/_librsyncmodule.o -lrsync -o build/_librsync.so
clean :
	rm -rf build
