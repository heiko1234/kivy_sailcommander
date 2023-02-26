# kivy_sailcommander


This is a small sail commando learning app.

![sailcommando_logo](./sailcommander/assets/logos/SAIL_Commander.png)


# Install

The Repo is created with poetry.

```dash

# create virtual environment
python -m venv .venv

# poetry
python -m pip install --upgrade pip

python -m pip install poetry

# poetry update and install of packages

poetry update --lock -vvv

poetry install

```



## MDApp Design

https://m3.material.io/
https://m3.material.io/components


https://github.com/kivymd/KivyMD/wiki/

Chips:
https://github.com/kivymd/KivyMD/wiki/Components-Chip


ICONs:
https://pictogrammers.com/library/mdi/
# https://pictogrammers.com/library/mdi/   # ICONs


## Links


https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#minimal-app

https://kivymd.readthedocs.io/en/1.1.1/getting-started/




## Screens of the App

The App contains 2 Screens.






# To make an android app

[Here](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04-de) a link to make buildozer work on ubuntu.

Install `javac` see [here](https://stackoverflow.com/questions/66853462/how-to-install-javac-on-linux-mint).

```dash

# for Ubuntu
sudo apt-get install openjdk-8-jdk

# check version
javac -version   
# javac 1.8.0_352

```

Be sure libssl-dev and java is up-to-date on your machine. it cause strange errors like not installing sdk-tools on the machine or not establishing ssl download conections.

```dash

sudo apt-get update

sudo apt-get install libssl-dev

java -version #1.8

sudo apt install default-jre

java -verion #11.8

```

In case sdk-tools get not installed, do it manually, but there is a deeper problem.

https://stackoverflow.com/questions/59330223/sdkmanager-not-installed

Install buildozer in the virtual environment with poetry

```dash

poetry add buildozer

poetry add cython

# do not miss to add `.buildozer` to  .gitignore  file

```
It will be automatically installed, if all is up-to-date.

Optional:

Install [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager)


Download the latest "command line tools only" package from the Android Studio downloads page and unzip the package.
Move the unzipped cmdline-tools directory into a new directory of your choice, such as android_sdk. This new directory is your Android SDK directory.

Add the unzipped files to your .venv or .buildozer/android/app/plattform/android-sdk/tools/....


## Config buildozer

Required if something goes wrong.


Download the SDK manager here: wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip (run this on your command line in your buildozer directory)

Then you unzip it with the command: $ unzip sdk-tools-linux-3859397.zip

when you see a tools directory you have successfully installed sdkmanager

Create a .spec file with 
```dash 
buildozer init
```

Then edith your .spec (buildozer.spec) file(in your kivy app folder) line 112 with the path where you unzipped your SDK file

andriod.sdk_path = (Your file path) eg /home/freezy/buildozer/




```dash

# buildozer.spec  file: 
# line 127
# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =
android.sdk_path = /home/heiko/Repos/kivy/kivy_health_repo/kivy_health/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager.sh

# copy unzipped downloaded sdkmanager into the folder android-sdk/tools/bin/...
# problem solved with update libssl-dev

```


# Work with buildozer

Following the description [here](https://realpython.com/mobile-app-kivy-python/)

```dash

# to make it testable

buildozer init

buildozer -v android debug

```

When running buildozer to create the android related files they will show up in the new created `bin` folder.


![bin_apk](./assets/bin_apk.png)




# How to deploy on Android

Install the android debug bridge for deploying the apk file to your mobile for test reasons.

[Here](https://www.youtube.com/watch?v=pzsvN3fuBA0) is a video for this.

[Troubleshooting](https://www.youtube.com/watch?v=We45D_TjKdc) video for adb connections.

```dash

# install linux tools
sudo apt install android-tools-adb
sudo apt install android-tools-fastboot


# install android debug bridge (adb)
sudo apt install adb


# connect to device
adb connect 192.168.0.158:5555  # works not for me

# to list all connections
adb devices

sudo adb kill-server
sudo adb start-server

adb devices

# my list of devices
# 222be3df
# 29477c1e

# switch to dir of bin
cd ./bin

adb -s 29477c1e install sailcommander-0.1-arm64-v8a_armeabi-v7a-debug.apk

# for error logging
adb -s 29477c1e logcat *:S python:D   


```


![adb_devices](./assets/adb_devices.png)





# All on Mobil

![login](./assets/app_on_mobil.png)

![on_app](./assets/heal_login.png)

![logo_on_app](./assets/screenshoot_on_mobil.png)









