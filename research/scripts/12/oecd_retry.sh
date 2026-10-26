#!/bin/bash
# Retries OECD SDMX downloads (rate-limited 429) every 90 s, up to 25 attempts each.
D=research/data/raw/12/oecd
O="https://sdmx.oecd.org/public/rest/data"
H="Accept: application/vnd.sdmx.data+csv; charset=utf-8"
declare -a NAMES=(sha_tot waiting am)
declare -a URLS=(
"$O/OECD.ELS.HD,DSD_SHA@DF_SHA,/.A.EXP_HEALTH.PT_B1GQ+USD_PPP_PS..._T._T._T._T._T.?startPeriod=2004"
"$O/OECD.ELS.HD,DSD_HEALTH_PROC@DF_WAITING,/all?startPeriod=2004"
"$O/OECD.ELS.HD,DSD_HEALTH_STAT@DF_AM,/all?startPeriod=2004"
)
for i in "${!NAMES[@]}"; do
  n=${NAMES[$i]}; u=${URLS[$i]}
  for a in $(seq 1 25); do
    code=$(curl -s -m 300 -A "research-script" -H "$H" -o "$D/$n.csv" -w "%{http_code}" "$u")
    echo "$(date +%H:%M:%S) $n attempt $a -> $code $(wc -c < $D/$n.csv)" >> $D/download_log.txt
    if [ "$code" = "200" ]; then echo "$u" >> $D/urls_ok.txt; break; fi
    if [ "$code" = "404" ]; then break; fi
    sleep 90
  done
done
