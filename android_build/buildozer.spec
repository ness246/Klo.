[app]

# (str) Title of your application
title = Klo.

# (str) Package name
package.name = klotski

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ness246

# (str) Source code where the main.py live
source.dir = ..

# (str) Main entry point - buildozer main_android.py'yi main.py olarak kopyalayacak
android.entrypoint = org.kivy.android.PythonActivity

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,ttf,ogg,wav

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"]([^'"]+)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# Note: pygame2 for Android compatibility (pygame2 is recommended for mobile)
requirements = python3,pygame2,sdl2_image,sdl2_mixer,sdl2_ttf,android

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
presplash.filename = %(source.dir)s/logo.png

# (str) Icon of the application
icon.filename = %(source.dir)s/logo.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash animation using Lottie format.
# See https://lottie-files.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect, Synfig, etc.
#presplash.lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/logo.png
#icon.adaptive_background.filename = %(source.dir)s/logo.png

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android SDK version to use
#android.sdk = 20

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT executable (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) The entry point for the Android application.
# Default is ok for Kivy-based apps
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_compiled_libs =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display the filter or not
#android.logcat_pid_only = False

# (str) Android entry point, default is ok for Kivy-based apps
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Android AppCompat
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_compiled_libs =

#
# Python for android (p4a) specific
#

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to which the last last filtering of logs should be written
#p4a.log_filter = 

# (str) The directory in which your python-for-android dist will be built, defaults to `../python-for-android/dist`
#p4a.b dist_dir =

# (str) python-for-android recipe to use, defaults to python3
#p4a.recipe = python3

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

# (bool) Whether or not to sign the code
ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team that signed your certificate
#ios.codesign.developer_team = <hexstring>  # Team or User ID

# (list) List of iOS URL schemes to handle (e.g. myapp://)
#ios.url_schemes =

# (str) iOS application source code directory
ios.source_dir = .

# (str) iOS App Name
#ios.appname = MyApp

# (str) iOS Entry point (default ok for Kivy-based apps)
#ios.entrypoint = main_android.py

#
# Buildozer
#

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Directory in which buildozer should download all the non-built dependencies
#buildozer.download_dir = ./packages

# (str) Path to directory where buildozer should store non-built and non-downloaded dependencies
#buildozer.global_download_dir = ~/.buildozer/downloads

# (str) Path to local download directory (if not specified, within the download_dir)
#buildozer.local_download_dir = ~/.buildozer/downloads/local

# (str) Override directory where buildozer should unpack pre-built dependencies
#buildozer.unpack_dir = ~/.buildozer

# (str) Set custom build directory
#buildozer.build_dir = ./.buildozer

# (list) Paths to other buildozer spec files to include
#buildozer.includes =

# (str) Android packaging tool to use
# Can be 'apk', 'aab' or 'aar'
android.packaging.tool = apk

# (str) Android packaging format to use
# Can be 'gradle', 'ant' or 'none'
android.packaging.format = gradle

# (list) Java files to compile and bind
#android.java_files =

# (list) Java source directories
#android.java_src_dirs =

# (list) AAR libraries to add
#android.add_aars =

# (list) Assets folders to add
android.add_assets = assets,levels

# (str) Asset folder to add (if empty, will be the main source.dir/assets)
#android.add_assets = 

# (list) Additional files to copy into the assets folder
android.add_src =

# (str) Android main program entry point (default ok for Kivy-based apps)
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Android AppCompat
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the main_android.py file)
# Android entry point - main_android.py will be copied and renamed to main.py during build

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_compiled_libs =

