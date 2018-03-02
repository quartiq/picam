#define _GNU_SOURCE
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <dlfcn.h>

#define PREFIX "/var/run/pits/"

int open(const char *pathname, int flags, ...) {
  va_list va;
  va_start(va, flags);
  mode_t mode = va_arg(va, mode_t);
  va_end(va);

  static int (*libc_open)(const char *, int, ...);
  if(!libc_open) {
    libc_open = dlsym(RTLD_NEXT, "open");
    if(!libc_open) {
      abort();
    }
  }

  if(!strncmp(pathname, PREFIX, strlen(PREFIX))) {
    const char *new_prefix = getenv("PICAM_TMP");
    if(!new_prefix) {
      new_prefix = PREFIX;
    }

    size_t new_pathname_len = strlen(new_prefix) +
                              strlen(&pathname[strlen(PREFIX)]);
    char *new_pathname = calloc(1, new_pathname_len + 1);
    strcat(new_pathname, new_prefix);
    strcat(new_pathname, &pathname[strlen(PREFIX)]);

    int result = libc_open(new_pathname, flags, mode);

    free(new_pathname);

    return result;
  } else {
    return libc_open(pathname, flags, mode);
  }
}
