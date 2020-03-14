from ctypes import cdll

lib = cdll.LoadLibrary("../target/release/libembed.so")

lib.process()
lib.process_not_pub()

print("done from Python!")

