# Fossil: Skyfear Compatibility Launcher
# Written by telekrex @ Protoria Studios LLC
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A binary script designed to establish a
# safe, compatibile environment, in which
# to run Skyfear on Windows (works with
# proton as well). Details and reasons for
# this are in the README.txt that should be
# included if you're reading this source
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import modules we need
import os, sys, subprocess

VAR_NAME = "OPENSSL_ia32cap" # is the name of the variable we need to look for
VAR_VALUE = "~0x200000200000000" # is the value it needs to be to be compatible
GAME_EXE = "SKYFEAR.exe" # is the Skyfear game client file we want to run

def game_exists(path):
    # simple function that executes
    # checking if GAME_EXE exists in
    # the given path, and returning
    # True or False
    return os.path.isfile(path)

def launch_game(path):
    # function that attempts to run
    # the game in a newly created
    # environment after setting values
    #
    # first we copy the host's existing
    # environment and assign it to the
    # variable "env",
    env = os.environ.copy()
    # then we set the environment variable
    # VAR_NAME to the value of VAR_VALUE,
    # which we defined after imports,
    env[VAR_NAME] = VAR_VALUE
    try:
        # attempt to create a process that runs
        # the game (given as a path, which should
        # be the full path to the game client),
        # with the newly modified environment
        subprocess.run([path], env=env)
    except Exception as e:
        # if anything fails, we should get an
        # error printed to the terminal window
        print("Error launching game:", e)

def main():
    # print some pretty text on screen because
    print("/// Skyfear Compatibility Launcher")
    print("/// Source code: https://github.com/Protoria-Studios/skyfear-launch-script")
    # just looks nice and professional and provides a link to learn about the software

    # set a variable game_path to the current working directory that this
    # software is running in, which should be Skyfear's install location
    game_path = os.path.join(os.getcwd(), GAME_EXE)

    # check if the Skyfear game client
    # exists in the game_path path,
    if not game_exists(game_path):
        print("Game client not found.")
        # if not, we exit this main() function
        # and thus close the script
        return

    # if we are here, game client was found ok;
    # now we check if the operating system environment has
    # the value we need in the variable we are concerned about:
    if os.environ.get(VAR_NAME) != VAR_VALUE:
        # if the value of that variable is not the desired value,
        # (defined at the start of the script) then we call the
        # function to set it to the desired value
        print(f"Setting env var {VAR_NAME}...")
        os.environ[VAR_NAME] = VAR_VALUE

    # now we attempt to launch the game client
    # using the function we defined to do so
    # in the new environment
    print("Starting game client...")
    launch_game(game_path)

if __name__ == "__main__":
    main()
