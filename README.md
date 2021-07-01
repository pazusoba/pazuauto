# pazuauto
This is the ultimate goal for pazusoba, solving the puzzle and performing the solution. `scrcpy` is used to mirror and control my Android devices. For iOS devices, `Dell Mobile Connect` can be used. `Wormhole` is another alternative and is quite good but it is paid.

For Android, there will be a standalone app to performance the automation on the device without a computer. Check out [pazusoba-android](https://github.com/HenryQuan/pazusoba-android).

### Projects
- [pazusoba](https://github.com/HenryQuan/pazusoba), the core algorithm
- [pazulove](https://github.com/HenryQuan/pazulove), machine learning
- [pazuauto](https://github.com/HenryQuan/pazuauto), automation
- [pazuflata](https://github.com/HenryQuan/pazuflata), pazusoba with Flutter
- [pazusoba-android](https://github.com/HenryQuan/pazusoba-android), pazusoba and automation on Android

## Supported system
- Windows
- Mac OS
- Linux, maybe (manual adjustment)

#### Scrcpy
It might be a good idea to reduce the bit rate and resolution so that it won't affect the performance of your device. The solver only needs to take a screenshot of it so it doesn't need to be too high resolution. The board is recognised by colour so it should work for all games.
~~~shell
$ scrcpy.cmd -b 1M -m 512
~~~

### Supported games
- Puzzle & Dragons (パズドラ)
- Puzzle & Dragons Battle (パズドラバトル)
- Puzzle & Dragons Z (パズドラZ)
- Puzzle & Dragons Mario (パズドラマリオ)
- Puzzle & Dragons X (パズドラクロス)

Last three games are supported if you play them on your device with [`citra`](https://citra-emu.org/) emulator not on the 3DS. Yes, I own all three games and am playing them again at the moment. 

## Setup
***The automation project should only be used for education purpose.*** `DO NOT` use it for any other purposes nor am I liable for anything you do.

It is recommended to use `virtualenv` inside `automation/` and run `pip install -r requirements.txt` to install everything.

You also need `pazusoba` binary and place it in `automation/`. 

# Extra
- [All orb styles](https://pad.protic.site/resource/orb-skins/)
- [Template Matching with Multiple Objects](https://docs.opencv.org/4.2.0/d4/dc6/tutorial_py_template_matching.html)
- [Wormhole website](https://www.er.run/), not sponsored

**Special thanks to my OP `Cody 大先輩` for helping me with opencv.**
