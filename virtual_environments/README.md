# Virtual environments

<p align="center">
  <img src="../figures/virtual_environments.png" width="300">
</p>

In these exercises we are going to be looking at how we can use `conda` to control dependencies when we are working on
python projects. `conda` is a so called environment manager that that helps you make sure that the dependencies of
different projects do not cross-contaminate each other. Many of you may already have `conda` installed, but most people
have never actually used it.

The workflow presented in these exercises for managing dependencies are as follow

* Use `conda` to create environments
* Use `pip` to install packages in that environment

It is most likely not the optimal way of doing things but where conda shines over other dependency managers is that it
support all three major operating systems (Windows, OS, Linux) the best. Therefore, it is a great tool for teaching
about virtual environments.

In the future you may be interested in trying out other environment managers. We can recommend
[venv](https://docs.python.org/3/library/venv.html), [pipenv](https://pipenv.pypa.io/en/latest/),
[poetry](https://python-poetry.org/) and [pdm](https://python-poetry.org/) as excellent alternatives to `conda`.

## Exercises

1. Download and install `conda`. You are free to either install full `conda` or the much simpler version `miniconda`.
   The core difference between the two packages is that `conda` already comes with a lot of packages that you would
   normally have to install with `miniconda`. The downside is that `conda` is an much larger package which can be a
   huge disadvantage on smaller devices.

2. Start a terminal or command prompt an type in `conda help` which should show you the help page for the different
   commands that you can use with conda. If this does not work you probably need to set some system variable to
   [point to the conda installation](https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10)

3. First important `conda` command is `create` that will create a new environment

   ```bash
   conda create -n "my_environment" python=3.11
   ```

   Execute the command

4. Afterwards activate the environment.

5. After entering the environment, what `pip` command you execute to get an list of all the dependencies already
   installed in the environment?

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

7. The way we usually communicate to other people the requirements needed to run our python applications/scripts are
   called `requirement.txt` files. These files are a simple list of dependencies with the format

   ```txt
   dependency1==X.Y.Z
   dependency2==X.Y.Z
   ```

   Where X.Y.Z is the particular version of that package. Construct a `requirements.txt` file containing the
   dependencies you just installed to run the script.

8. When you think you have managed to create the file, lets test that it works. Execute these three commands:

   ```
   conda create -y -n "newenv" python=3.11 & conda activate newenv & pip install -r requirements.txt & python simple_classifier.py
   ```

   We here use the `&` is used to combine multiple commands into one line. Make sure you understand the 4 things this
   one line does. If it completes without errors, congratulations on creating your first reproduceabile virtual
   environment.

6. Hopefully you will be using multiple environment in the future and forget from time to time what you called them.
   Which `conda` commando gives you a list of all the environments that you have created?

7. Finally, make sure you also know how to delete unused environments as these can fill up your laptop. Figure out the
   command to remove the `newenv` environment created in the previous exercise.
