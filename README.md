# personalClipboard
Python personal clipboard
Works in linux/debian, with python3.
Modules needed: pyperclip and tkinter.

Update options in conf/options_conf.conf file, separated by a semicolon ";".

To create a shortcut command use:

echo "alias personalClipboard='nohup python3 personalClipboard/clipboard.py &'" >> .bashrc 2>&1

...then restart linux console.
