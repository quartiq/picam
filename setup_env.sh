PICAM_SDK=$(pwd)/Picam_SDK

LD_LIBRARY_PATH=${PICAM_SDK}/pi/runtime
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${PICAM_SDK}/pi/misc
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${PICAM_SDK}/pleora/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${PICAM_SDK}/pleora/lib/genicam/bin/Linux64_x64
LD_PRELOAD=$(pwd)/interceptor/interceptor.so
export LD_LIBRARY_PATH LD_PRELOAD

GENICAM_ROOT_V2_4=${PICAM_SDK}/pleora/lib/genicam
GENICAM_LOG_CONFIG_V2_4=${PICAM_SDK}/pleora/lib/genicam/log/config/DefaultLogging.properties
GENICAM_CACHE_V2_4=${HOME}/.config/Pleora/genicam_cache_v2_4
export GENICAM_ROOT_V2_4 GENICAM_LOG_CONFIG_V2_4 GENICAM_CACHE_V2_4

PICAM_TMP=${HOME}/.local/tmp
export PICAM_TMP
