# TilePipe Aseprite templates

[Check out the original video](https://www.youtube.com/watch?v=6YWbSjnG4oI) if you want to learn how to use [TilePipe2](https://aleksandrbazhin.itch.io/tilepipe2) and with this repository.

## Lazy?
Don't feel like manually change colors of the template? Don't worry, I've got you.

> Assuming [Python 3.12](https://www.python.org/downloads/) or higher is installed on your system.

### Setup Virtual Environment
Initialize your virtual environment
```sh
> python -m venv venv
```
Then activate your virtual environment for windows or for unix.

**Windows**
```sh
> .\venv\Scripts\activate
```
**Unix**
```sh
> source venv/bin/activate
```

Make sure you have [pip-tools](https://pypi.org/project/pip-tools/) installed.
```sh
> pip install pip-tools
```

Compile the `requirements.txt` file.
```sh
> pip-compile -o requirements.txt pyproject.toml
```

After compiling the requirements, install them
```sh
> pip install -r requirements.txt
```

Your environment is now ready to go

## What now?
I know, I know, that was a lot of effort ;)

Open `colors.py` and find `TRANSPILE` variable. It's an array with dictionary items.
Each object in the array represents a new texture. A new output. A new file basically.
Each object has key and values. The key (left variable) represents the color in the template.
The value of the dicationary represents the new color we would like to change it is.
Please note, each color has to be a [hex](https://www.color-hex.com/) color with one exception "`transparent`".

Once you have configured your colors, simply run
```sh
> python convert.py
```

Enjoy your new assets. You can give them a final touch as done in the [video](https://www.youtube.com/watch?v=6YWbSjnG4oI).

## Known Issues.
- As of today (26-07-2024) [TilePipe2](https://aleksandrbazhin.itch.io/tilepipe2) doesn't seem to support godot4 exports.

## Credits
- 25PartAsymTemplate -> [Echo in a Void](https://github.com/TheDoorworlds)
- TilePipe2 -> [Aleksandr Bazhin](https://github.com/aleksandrbazhin)
- Convert Script -> [undeƒined](https://github.com/0x78f1935)
