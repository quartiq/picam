.PHONY: all clean

all:
	$(CC) -Wall -fPIC -shared -ldl -o interceptor.so interceptor.c

clean:
	rm -f interceptor.so
