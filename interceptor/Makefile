.PHONY: all clean

all:
	$(CC) -Wall -fPIC -O2 -shared -ldl -o interceptor.so interceptor.c

clean:
	rm -f interceptor.so
