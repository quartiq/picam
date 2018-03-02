#!/bin/sh -ex

SDK_URL=ftp://ftp.princetoninstruments.com/Public/Software/Official/PICam/Picam_SDK.run

wget $SDK_URL -c -O Picam_SDK.run
sh Picam_SDK.run --target Picam_SDK --noexec

for lib in libpicam.so libpiac.so libpicc.so libpida.so libpidi.so; do
  ln -sf $(basename Picam_SDK/pi/runtime/${lib}.?.?.?) Picam_SDK/pi/runtime/${lib}.0
done

ln -sf $(basename Picam_SDK/pi/misc/libftd2xx.so.?.?.?) Picam_SDK/pi/misc/libftd2xx.so
