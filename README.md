# MLOps for data scientists

<p align="center">
  <img src="figures/4topics.png" width="300">
</p>

This repository contains a small introduction to *machine learning operations* (MLOps) for data scientists. The four
core topics covered are:

* [Virtual environments](https://github.com/SkafteNicki/ku_devops/tree/main/virtual_environments)
* [Version control](https://github.com/SkafteNicki/ku_devops/tree/main/version_control)
* [Code testing](https://github.com/SkafteNicki/ku_devops/tree/main/code_testing)
* [Experiment tracking](https://github.com/SkafteNicki/ku_devops/tree/main/experiment_tracking)

When doing the exercises, do maximize your MLOps/DevOps experience you should priorities:

1. Make yourself familiar with running commands in the terminal. The terminal can be a scary place, but it is an
   essential skill to be able to run commands without relying on a graphical interface. If you want good introduction
   to using the shell, I highly recommend the first two lectures from
  [this MIT course](https://missing.csail.mit.edu/).
2. Only use scripts e.g. no notebooks for these exercises. Notebooks have their benefits but the fact is that developing
   software in the *real world* is done in scripts. Therefore make sure that whenever you are writing code for the
   exercises do this in `.py` scripts. If you feel like you miss the interactiveness of notebooks when working with
   script I can highly recommend giving [ipython](https://ipython.org/) a spin.
3. Get a good code editor. If you do not have one, I can highly recommend
   [Visual Studio Code](https://code.visualstudio.com/) that are a lightweight editor, but through extensions can
   become really powerfull. Otherwise, I also recommend [PyCharm](https://www.jetbrains.com/pycharm/).

Why should a data scientist care of MLOps? Because MLOps provide processes and tools for creating *reproducible*
experiments at scale when working with any kind of machine learning models. Being able secure that your experiments
are reproducible are important in the context of the scientific method:

<p align="center">
  <img src="figures/scientific_method.jpg" width="300">
  <br>
  <a href="https://www.australianenvironmentaleducation.com.au/education-resources/what-is-the-scientific-method/"> Image credit </a>
</p>

Without reproducibility the method breaks at the experimental stage, as non-reproduceable experiments will most likely
lead to different results and thereby different conclusions on the initial hypothesis.

For a much more complete set of material on this topic, see [this course](https://skaftenicki.github.io/dtu_mlops/)
which goes over the near complete pipeline of designing, modeling and deploying machine learning applications.
