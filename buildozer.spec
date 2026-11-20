[app]
title = Afed SOS
package.name = afedsos
package.domain = org.afed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0

requirements = python3,kivy==2.3.0,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_ADVERTISE,BLUETOOTH_CONNECT,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,MODIFY_AUDIO_SETTINGS,WAKE_LOCK,FOREGROUND_SERVICE,POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 26b
android.accept_sdk_license = True
android.archs = arm64-v8a

p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
