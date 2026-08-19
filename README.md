# fossil
Compatibility tool for Unreal Engine games running old engine versions. Created for [Skyfear](https://store.steampowered.com/app/814330/Skyfear/), but could be copied and used for other Unreal Engine games, or any game with a compatibility issue that can be solved through environment variables.

### Why
Skyfear was made in a source-compiled version of Unreal Engine 4.21, which does not support a change made by Intel on their SHA references to OpenSSL in newer CPUs. There are two articles about this here, https://dovetailgames.freshdesk.com/en/support/solutions/articles/80000968751-intel-10th-gen-cpus-causing-crashes-on-older-ue4-games, https://www.intel.com/content/www/us/en/developer/articles/troubleshooting/openssl-sha-crash-bug-requires-application-update.html, and I've included .pdf copies of these articles in this repository in case the original pages are gone someday. Reasons why I cannot fix this in the game engine itself are complicated, Skyfear is very intertwined with the 4.21 version and changing that would be months-a year of work.

### Solution
The solution was a script that generates a compatible environment to straighten out any issues like this before running the game. `launcher.py` creates a shell session where the environment variable(s) are corrected, and runs the game through that. This happens non-destructively, so the **neither the game nor user's system require permenant changes.** When you close the game, the environment goes with it and there are no system-wide changes to worry about.

Worth mentioning that the environment variable changes can be done manually by the user, but 1) this would be permanent, 2) hoping every customer follows instructions precisely is not safe. A lone modder might be game for doing it manually, but I made this to have a binary launcher so the general audience has an automatic solution. Plus it's nice to have non-destructive compatibility.

### Use / development
Feel free to use this to  
- ensure your game runs if using an older Unreal Engine version
- fix somebody else's game that is no longer maintained by its developer/publisher

The recommendation is to copy `Source/`, modify to suit your game's needs, then use the build script to make a binary to ship with your game. Have Steam's launch target be your built tool, which should point to your game. Just please rename all Skyfear mentions with your own game. Name it whatever you want, it's *your* launcher now. Please keep the license & source link in `launcher.py`.

If you are interested in contributing, please see [Contributing](CONTRIBUTING.md) and [Security](SECURITY.md).

Also, works in Proton, tested.

---

[See games made by Protoria Studios](https://store.steampowered.com/search/?developer=Protoria%20Studios)

![](https://protoriastudios.com/Skyfear_Screenshot02.png)