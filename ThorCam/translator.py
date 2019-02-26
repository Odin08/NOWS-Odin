from ctypes import *
import time
import os
import sys
import platform
import tempfile
import re

if sys.version_info >= (3, 0):
    import urllib.parse


ximc_dir = os.path.join("C:", os.sep, "Program Files", "XILab", "ximc-2.10.5", "ximc")
ximc_package_dir = os.path.join(ximc_dir, "crossplatform", "wrappers", "python")
sys.path.append(ximc_package_dir)  # add ximc.py wrapper to python path

if platform.system() == "Windows":
    arch_dir = "win64" if "64" in platform.architecture()[0] else "win32"
    libdir = os.path.join(ximc_dir, arch_dir)
    os.environ["Path"] = libdir + ";" + os.environ["Path"]  # add dll

try:
    from pyximc import *
    from pyximc import lib
except ImportError as err:
    print(
        "Can't import pyximc module. The most probable reason is that you changed the relative location of the testpython.py and pyximc.py files. See developers' documentation for details.")
    exit()
except OSError as err:
    print(
        "Can't load libximc library. Please add all shared libraries to the appropriate places. It is decribed in detail in developers' documentation. On Linux make sure you installed libximc-dev package.\nmake sure that the architecture of the system and the interpreter is the same")
    exit()


def test_get_position(device_id):
    x_pos = get_position_t()
    lib.get_position(device_id, byref(x_pos))
    return x_pos.Position, x_pos.uPosition


def test_move(device_id, distance, udistance):
    lib.command_move(device_id, distance, udistance)


def test_wait_for_stop(device_id, interval):
    lib.command_wait_for_stop(device_id, interval)


def test_set_speed(device_id, speed):
    mvst = move_settings_t()
    lib.get_move_settings(device_id, byref(mvst))
    mvst.Speed = int(speed)
    lib.set_move_settings(device_id, byref(mvst))


def test_set_microstep_mode_256(device_id):
    eng = engine_settings_t()
    lib.get_engine_settings(device_id, byref(eng))
    eng.MicrostepMode = MicrostepMode.MICROSTEP_MODE_FRAC_256
    lib.set_engine_settings(device_id, byref(eng))


def follow_home(device_id):
    lib.command_homezero(device_id)
    print('Im home')

def main():
    lib.set_bindy_key(os.path.join(ximc_dir, "win32", "keyfile.sqlite").encode("utf-8"))

    probe_flags = EnumerateFlags.ENUMERATE_PROBE + EnumerateFlags.ENUMERATE_NETWORK
    enum_hints = b"addr=192.168.0.1,172.16.2.3"

    devenum = lib.enumerate_devices(probe_flags, enum_hints)
    print("Device enum handle: " + repr(devenum))
    print("Device enum handle type: " + repr(type(devenum)))

    dev_count = lib.get_device_count(devenum)
    print("Device count: " + repr(dev_count))

    controller_name = controller_name_t()
    for dev_ind in range(0, dev_count):
        enum_name = lib.get_device_name(devenum, dev_ind)
        result = lib.get_enumerate_device_controller_name(devenum, dev_ind, byref(controller_name))
        if result == Result.Ok:
            print("Enumerated device #{} name (port name): ".format(dev_ind) + repr(enum_name) + ". Friendly name: " + repr(
                controller_name.ControllerName) + ".")

    open_name = None
    if len(sys.argv) > 1:
        open_name = sys.argv[1]
    elif dev_count > 0:
        open_name = lib.get_device_name(devenum, 1)  # Если ось 1, тогда единица, если ось 2, тогда 0
    elif sys.version_info >= (3, 0):
        tempdir = tempfile.gettempdir() + "/testdevice.bin"
        if os.altsep:
            tempdir = tempdir.replace(os.sep, os.altsep)
        uri = urllib.parse.urlunparse(urllib.parse.ParseResult(scheme="file",
                                                               netloc=None, path=tempdir, params=None, query=None,
                                                               fragment=None))
        open_name = re.sub(r'^file', 'xi-emu', uri).encode()

    if not open_name:
        exit(1)

    if type(open_name) is str:
        open_name = open_name.encode()

    print("\nOpen device " + repr(open_name))
    device_id = lib.open_device(open_name)
    print("Device id: " + repr(device_id))
    test_set_microstep_mode_256(device_id)
    st = 2.56
    print('size of step = ', st, 'mkm')
    return device_id

def pos(l):
    l = float(l)
    l = l * 1e3 / 2.56
    return int(l)



def end():
    print("\nClosing")
    lib.close_device(byref(cast(device_id, POINTER(c_int))))
    print("Done")