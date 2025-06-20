#advanced #virtual-env #venv #project-isolation #dependencies

# 📘 Day 21 - Virtual Environment

[<< Day 20](../20_Day_Web_scraping/20_web_scraping.md) | [Day 22 >>](../22_Day_Python_web/22_python_web.md)



- [📘 Day 21](#-day-21)
  - [Setting up Virtual Environments](#setting-up-virtual-environments)
  - [💻 Exercises: Day 23](#-exercises-day-23)

# 📘 Day 21

## Setting up Virtual Environments

To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, we will access only packages which are specific for that project. Open your terminal and install virtualenv

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

Inside the 30DaysOfPython folder create a flask_project folder.

After installing the virtualenv package go to your project folder and create a virtual env by writing:

For Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

For Windows:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

I prefer to call the new project venv, but feel free to name it differently. Let us check if the the venv was created by using ls (or dir for windows command prompt) command.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

Let us activate the virtual environment by writing the following command at our project folder.

For Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
Activation of the virtual environment in Windows may very on Windows Power shell and git bash. 

For Windows Power Shell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

For Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

After you write the activation command, your project directory will start with venv. See the example below.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

Now, lets check the available packages in this project by writing pip freeze. You will not see any packages.

We are going to do a small flask project so let us install flask package to this project.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Now, let us write pip freeze to see a list of installed packages in the project:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

When you finish you should dactivate active project using _deactivate_.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

The necessary modules to work with flask are installed. Now, your project directory is ready for a flask project. You should include the venv to your .gitignore file not to push it to github.

## 💻 Exercises: Day 21

1. Create a project directory with a virtual environment based on the example given above.

🎉 CONGRATULATIONS ! 🎉

[<< Day 20](../20_Day_Web_scraping/20_web_scraping.md) | [Day 22 >>](../22_Day_Python_web/22_python_web.md)
