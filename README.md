## mac-attrs v0.1.0

mac-attrs is a fun, little web app that evaluates the attributes of a MAC address.


## Python dependencies

mac-attrs requires Python and the pip package.  It also requires the following packages.

- [macaddress](https://github.com/critical-path/macaddress)
- [random-mac](https://github.com/critical-path/random-mac)
- flask
- gunicorn


## Front-end dependencies

mac-attrs requires Bootstrap.  While it only uses Bootstrap's CSS files, the JS files and their dependencies (jQuery and Popper) are included for the sake of completeness.


## Installing mac-attrs

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command.

```bash
$ sudo pip install .
```


## Prepping mac-attrs

If you have never used mac-attrs before, then start by running the `prep-mac-attrs.sh` script, which will fetch files and make a classifier.  (random-mac, one of the dependencies referenced above, requires this classifier.)

Do not forget to toggle the script's `x` bit first.

```bash
$ chmod +x prep-mac-attrs.sh
$ ./prep-mac-attrs.sh
```


## Using mac-attrs

1. Run `gunicorn` with the `--bind` option.

```bash
$ gunicorn bind 127.0.0.1:8080 "mac_attrs:make_app()"
```

2. Point your browser to the web app.
