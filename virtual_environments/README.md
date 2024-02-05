# Virtual environments

<p align="center">
  <img src="../figures/virtual_environments.png" width="200">
</p>

Python is a great programming language and this is mostly due to its vast ecosystem of packages. No matter what you want
to do, there is probably a package that can get you started. Just try to remember when the last time you wrote a program
only using the [Python standard library](https://docs.python.org/3/library/index.html). Probably never. For this reason,
we need a way to install third-party packages and this is where
[package managers](https://en.wikipedia.org/wiki/Package_manager) come into play.

You have probably already used `pip` for the longest time, which is the default package manager for Python. `pip` is
great for beginners but it is missing one essential feature that you will need as a developer or data scientist:
*virtual environments*. Virtual environments are an essential way to make sure that the dependencies of different
projects do not cross-contaminate each other. As a naive example, consider project A requires `torch==1.3.0` and
project B requires `torch==2.0`, then 

```bash
cd project_A  # move to project A
pip install torch==1.3.0  # install old torch version
cd ../project_B  # move to project B
pip install torch==2.0  # install new torch version
cd ../project_A  # move back to project A
python main.py  # try executing main script from project A
```

will mean that even though we are executing the main script from project A's folder, it will use `torch==2.0` instead of
`torch==1.3.0` because that is the last version we installed because in both cases `pip` will install the package into
the same environment, in this case, the global environment. Instead, if we did something like:

```bash
cd project_A  # move to project A
python -m venv env  # create a virtual environment in project A
source env/bin/activate  # activate that virtual environment
pip install torch==1.3.0  # Install the old torch version into the virtual environment belonging to project A
cd ../project_B  # move to project B
python -m venv env  # create a virtual environment in project B
source env/bin/activate  # activate that virtual environment
pip install torch==2.0  # Install new torch version into the virtual environment belonging to project B
cd ../project_A  # Move back to project A
source env/bin/activate  # Activate the virtual environment belonging to project A
python main.py  # Succeed in executing the main script from project A
```

then we would be sure that `torch==1.3.0` is used when executing `main.py` in project A because we are using two
different virtual environments. In the above case, we used the [venv module](https://docs.python.org/3/library/venv.html)
which is the built-in Python module for creating virtual environments. `venv+pip` is arguably a good combination
but when working on multiple projects it can quickly become a hassle to manage all the different
virtual environments yourself, remembering which Python version to use, which packages to install and so on.

For this reason, several package managers have been created that can help you manage your virtual environments and
dependencies, with some of the most popular being:

* [conda](https://docs.conda.io/en/latest/)
* [pipenv](https://pipenv.pypa.io/en/latest/)
* [poetry](https://python-poetry.org/)
* [pipx](https://pipx.pypa.io/stable/)
* [hatch](https://hatch.pypa.io/latest/)
* [pdm](https://pdm.fming.dev/latest/)

In these exercises, we are going to be looking at how we can use `conda` to control dependencies when we are working on
python projects. Many of you may already have `conda` installed, but most people have never actually used it. The 
workflow presented in these exercises for managing dependencies are as follows

* Use `conda` to create environments
* Use `pip` to install packages in that environment

It is most likely not the optimal way of doing things but where conda shines over other dependency managers is that it 
supports all three major operating systems (Windows, OS, Linux) the best. Therefore, it is a great tool for teaching
about virtual environments. Additionally, many local compute clusters in universities only allow you to work on the
cluster if you use virtual environments through conda.

## Exercises

1. Download and install `conda`. You are free to either install full `conda` or the much simpler version `miniconda`.
    The core difference between the two packages is that `conda` already comes with a lot of packages that you would
    normally have to install with `miniconda`. The downside is that `conda` is a much larger package which can be a
    huge disadvantage on smaller devices.

2. Start a terminal or command prompt and type in `conda help` which should show you the help page for the different
    commands that you can use with conda. If this does not work you probably need to set some system variable to
    [point to the conda installation](https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10)

3. The first important `conda` command is `create` which will create a new environment

    ```bash
    conda create -n "my_environment" python=3.11
    ```

    Execute the command. What does the `-n` flag do? What does the `python=3.11` flag do?

    <details><summary>Solution!</summary> 
    The `-n` flag is used to specify the name of the environment and the `python=3.11` flag is used to specify the 
    version of python that should be installed in the environment. In general, you can call `conda create --help` to get
    information about the different flags you can use with the `create` command.
    </details>

4. Afterward, use the `conda activate` command to activate the environment.

5. After entering the environment, what `pip` command should you execute to get a list of all the dependencies already
    installed in the environment?

    <details><summary>Solution!</summary> `pip freeze` </details>

6. We are now ready to install some dependencies. Try to get the script `simple_classifier.py` running. Essentially,
    you need to iteratively call

    ```bash
    python simple_classifier.py
    ```

    and

    ```bash
    pip install <missing-package>
    ```

   Until the script runs.

7. The way we usually communicate to other people the requirements needed to run our Python applications/scripts are
    called `requirement.txt` files. These files are a simple list of dependencies with the format

    ```txt
    dependency1==X.Y.Z
    dependency2==X.Y.Z
    ```

    Where X.Y.Z is the particular version of that package. Construct a `requirements.txt` file containing the
    dependencies you just installed to run the script. Remember to specify the exact version you have used!

8. We are often interested in listing only the bare minimum necessary to run our code in the `requirements.txt` file.
    If you have written more than 2 dependencies in the last exercise, you have too many. Try figuring out what
    two are strictly necessary to get the application running?

9. When you think you have managed to create the file, let's try to test that it works. Execute these four commands:

    ```bash
    conda create -y -n "newenv" python=3.11
    conda activate newenv
    pip install -r requirements.txt
    python simple_classifier.py
    ```

    Make sure you understand what the four commands does. If it completes without errors, congratulations on creating 
    your first reproducible virtual environment.

10. Hopefully, you will be using multiple environments in the future and forget from time to time what you call them.
    Which `conda` commando gives you a list of all the environments that you have created? Hint: look at this
    [conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

    <details><summary>Solution!</summary> `conda env list` </details>

11. Finally, make sure you also know how to delete unused environments as these can fill up your laptop. Figure out the
    command to remove the `newenv` environment created in the previous exercise.

    <details><summary>Solution!</summary> `conda env remove -n newenv` </details>
