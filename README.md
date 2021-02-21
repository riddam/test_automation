# Test Automation

These test scripts are written in pytest-bdd to test
following [dummy website](https://mystifying-beaver-ee03b5.netlify.app/)

Table of content
-------------------

- [Installation](#Installation)
- [Execution](#Execution)

## Installation

### Assumption:

- Web drivers are installed(please refer "driver-scripts" directory for linux shell scripts)
- Python and virtualenv are installed

Activate virtual environment:

```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

Install package requirements:

```shell
$ pip3 install -r requirements.txt
```

## Execution

Execute test cases using following command:

```shell
/test_automation$ pytest -s --driver=chrome --html=report.html --junitxml=report.xml -m sort
```

where all arguments are optional    
-s: shortcut for --capture=no   
--driver: default is firefox; supported value: chrome  
--html: to generate test report in html format   
--junitxml: To create result files which can be read by Jenkins or other CI tools    
-m: allowed tags/markers(web,sort, filter, filtersort)
