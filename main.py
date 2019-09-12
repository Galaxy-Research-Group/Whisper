# Implementing Chirp, information for it can be found:
# https://developers.chirp.io

from chirpsdk import ChirpConnect, CallbackSet
import os
os.path.expanduser('~/.chirprc')

chirp = ChirpConnect()
chirp.start(send=True, receive=True)

# Sending data
identifier = 'hello'
payload = bytearray([ord(ch) for ch in identifier])
chirp.send(payload, blocking=True)


# Receiving data
class Callbacks(CallbackSet):
    def on_received(self, payload, channel):
        if payload is not None:
            identifier = payload.decode('utf-8')
            print('Received: ' + identifier)
        else:
            print('Decode failed')


chirp.set_callbacks(Callbacks())

# Stop processing data
chirp.stop()
