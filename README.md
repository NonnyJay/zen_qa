## Zen Technical Assessment ##
# Instruction on how to use and run the project

This is the Zen Technical Assessment repo for the role of a Quality Assurance Engineer.

In this project, an automated script is written to test the Individual current account features on [Zen](https://www.zenithbank.com/).

The Selenium Script has two main branch listed below, the last branch `refactor` holds same code as in the `master` branch:

- `Vanilla`: This script was written in plain selenium alone and can work on 'chrome browser' alone. 
- `Master`: This scripts combines the Selenium and Unittest Framework. And execute on both Chrome and Edge browser to showcase multi-browser testing.

`## Note:` WebDriver manager was use for this project. This is to ensure version dependency issues between your Chrome/Edge Browser and the browser driver can be smoothly manager by it and still allows the project runs when there is a browser update on your device. To read more about  the  WebDriver manager for Selenium on Python and how it is used visit [WebDriverManager](https://pypi.org/project/webdriver-manager/). 



## Prerequisites

* Desktop Computer.
* Git: <a href="https://git-scm.com/downloads" target="_blank">Download and install Git</a> for your system. 
* Code editor: You can <a href="https://code.visualstudio.com/download" target="_blank">download and install VS code</a> here.
* Python version between 3.9 and above. But for 100% stability use can the exact version this project was written on 3.9.5 Check the current version using:
```bash
#  Mac/Linux/Windows 
python --version
```
You can download a specific release version from <a href="https://www.python.org/downloads/" target="_blank">here</a>.

* Python package manager - PIP 19.x or higher. PIP is already installed in Python 3 >=3.4 downloaded from python.org . However, you can upgrade to a specific version, say 24.0, using the command:
```bash
#  Mac/Linux/Windows Check the current version
pip --version
# Mac/Linux
pip install --upgrade pip==24.0
# Windows
python -m pip install --upgrade pip==24.

pip install virtualenv
```
> **Note** - If we do not mention the specific version of a package, then the default latest stable package will be installed.

* Terminal
   * Mac/Linux users can use the default terminal.
   * Windows users can use either the GitBash terminal or WSL. 
* Selenium 4 and WebDriverManger 4 and above:
   


## Initial setup

### I strong advise you use a 'virtualenv' so as not to temper with your other environment dependencies.

1. Fork the <a href="https://github.com/NonnyJay/zen_qa" target="_blank">Zen QA Github repo</a> to your Github account.
1. Locally clone your forked version to begin working on the project.
```bash
git clone https://github.com/NonnyJay/zen_qa.git
cd zen_qa/
```
1. These are the files relevant for the current project:
```bash
. 
├── README.md
├── zen.py
├── requirements.txt

```

     
## Project Steps

To run the the project involves several steps after successful cloning, Do the below in the same folder the clone project is on:

1. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

2. **Install the dependencies:**
```
pip install -r requirements.txt
```

3. **Run the script:**
```
py zen.py

or

python3 app.py
```

4. **Verify on the Browser**<br>

For more detail about each of these steps, see the project lesson.
