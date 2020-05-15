# from doUtils.sgInstance import SG

import os
import sys
import time

sys.path.insert(0, r"\\server\manager\centralizeTools\python")

try:
    import shotgun_api3
except Exception as e:
    raise

sg = shotgun_api3.Shotgun("https://do-vfx.shotgunstudio.com",
                          script_name="uploadRV",
                          api_key="tdziowv!nqkzgdh2tnFeruajw",
                          http_proxy="sg.do-vfx.com:3128")

while True:

    print("scan starting")

    try:
        # filters = [["created_at", "in_calendar_month", -1]]
        filters = [["created_at", "in_calendar_day", 0]]

        fields = ["sg_path_to_movie", "sg_uploaded_movie"]

        verData = sg.find("Version", filters, fields)

        for ver in verData:

            if not ver["sg_uploaded_movie"]:
                print(ver)

                path = ver["sg_path_to_movie"]
                version = ver["id"]
                print(os.path.isfile(path))

                if os.path.isfile(path):
                    sg.upload("Version", version, path, "sg_uploaded_movie")
                    print("%s upload success!!!" % path)
    except:
        continue

    print("scan completed; updated nothing")
    print("sleeping 10s until next scan")
    time.sleep(10)
