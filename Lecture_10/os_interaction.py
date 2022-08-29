import os
import sys
import platform
import json


def system():
    system_data = {
        'System Name': os.name.upper(),
        'Operation System': f"{platform.system()}, {sys.platform}",
        'Version': platform.version(),
        'Edition': platform.win32_edition(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'System Version': sys.version,
    }

    print('#' * 10, 'System Name', '#' * 10)
    print(os.name.upper())
    print()
    print('#' * 10, 'Operation System', '#' * 10)
    print(f"{platform.system()}, {sys.platform}")
    print('ver.', platform.version())
    print(platform.win32_edition(), 'Edition')
    print()
    print('#' * 10, 'Machine', '#' * 10)
    print(platform.machine())
    print()
    print('#' * 10, 'Processor', '#' * 10)
    print(platform.processor())
    print()
    print('#' * 10, 'System Version', '#' * 10)
    print(sys.version)

    with open("os_report.json", "w") as report:
        json.dump(system_data, report)


system()
