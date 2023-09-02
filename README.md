This is a simple weather forecast project built with termux in mobile which sends you the weather via email.


# Introduction: 

You can change the `youremail@.com`, `yourpassword`, `recipient@gmail.com`, `city`   in the code to your respective email address, password, recipient email and city.

# Installation:

To run the script, you'll need Python 3 installed on your system. You can install it according to your specific operating system or desktop environment.

For example I use Linux mint in my pc and termux in my mobile so the command to install python3 in them is:

## Debian/Ubuntu-based systems:

```
sudo apt update
sudo apt install python3
```

`
## Termux:

If you are using termux in android:
```
pkg install python3
```


After installing python3 if you don't have the package manager 'pip' you can install it using this command in the terminal

```
sudo apt-get install python3-pip
```


## Libraries 

Install these libraries:

```
pip3 install requests
pip3 install smtplib
pip3 install schedule
```

These libraries may already be present in the 'pip' make sure if its there using the above commands. 

```
pip3 install smtplib                                                                     
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement smtplib (from versions: none)
ERROR: No matching distribution found for smtplib

```

If you get it this means that smtplib is not an external package to be downloaded using pip it's actually a part of python's standard library.


# Getting the API key:

I used an api key from this site [https://openweathermap.org/].

You can also get your key by following these steps:

1. Visit the OpenWeatherMap website at [https://openweathermap.org/].
    
2.  Sign up for a free account by clicking on the "Sign Up" or "Join" button on the top right corner of the homepage.
    
3. After signing up, log in to your OpenWeatherMap account.
    
4. Once logged in, navigate to the "API keys" section, usually found in your account settings or profile.
    
5. Generate a new API key by clicking on the appropriate button or link. You may be asked to specify the type of API key you need, such as a "Free" or "Basic" plan key.
    
6. The generated API key will be displayed on the screen. Make sure to copy and securely store this key as you will need it to access OpenWeatherMap's API services.


# Execution:

Run this in the terminal:

```
python3 weather_notification.py
```

If this command prints to the next line at the scheduled time you'll get the email. 

# Running in the background:

If you want to the kill the terminal but want to receive the email use this command:

```
nohup python3 weather_notification.py &
```

The `nohup` command stands for "no hang up." It's used in Unix-like operating systems (including Linux) to run a command or a script in such a way that it can continue running even after you log out or close the terminal session.

`nohup` also redirects the standard output (stdout) and standard error (stderr) streams of the command or script to a file called `nohup.out` in the current directory. This allows you to capture any output or error messages generated by the process.

When you run a command with `nohup`, it can be started in the background (using the `&` symbol) so that you can continue using the terminal for other tasks. 

