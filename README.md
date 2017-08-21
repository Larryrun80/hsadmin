# HSFramework
a general flask framework, integrated flask with some always-used modules

### About HSFramework
Flask is a well-known microframework and this is great, for you can choose your favorite modules to creat your project, and it's very flexible to organize your the structure yourselves.


But in using Flask, we found its not very convenant to create new project, for it's too "micro" and we should build an advance framework everytime.


So HSFramework is such a project: it's base on Flask, but intergarted some always-used modules, and provide a recommanded organization of your project. HSFrameword is aiming to help your create your project more quickly.


And, thanks Robert Picard for writing <[Explore Flask](https://exploreflask.com/en/latest/index.html)>, HSFramework learned lots of things from this article.


At last, we using PEP8 and PEP 257 to format our code.


### How to start
1. git clone to any folder you like;
2. [optional] change the name of folder "project" to your project name if you like;
3. [optional] if you did step 2, remind to modify the first line of run.py, change "project" to your project name, too. It should be the same as project folder name;
4. modify "instance/default.py", change the SECRET_KEY and other settings if you like
5. python run.py and enjoy