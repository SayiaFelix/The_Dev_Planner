# The_Dev_Planner

#### By 
* Sayia F Lucas (https://github.com/SayiaFelix/)
* Gamaliel Sirengo  
* Caren Chepkorir 
* Christine Nkatha
* Joyce Njoroge
* 
## Description
This is a web application that helps developers plan out their day and keep track of their various tasks. The dev planner helps you keep track of your tasks and deadlines.Starting a bootcamp can be overwhelming,the dev planner has resources that can help you get started in your journey as a developer.

## live link


## Running the Application
* Install virtual environment using `$ python -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:
* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:
* $ chmod a+x start.sh
* $ ./start.sh
  

## Technologies used
* Python
* Flask
* Boostrap
* HTML
* CSS


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On first page** | Get the landing page, Select between signup or login|
| Select SignUp| **Email**,**Username**,**Password**,**confirm-password** | Go to login|
| Select Login | **Username** and **password** |Go to the dashboard, adds a new task, get resources|
| select Weekly tasks |  **Adds weekly tasks** | Display the user's weekly tasks|
| Select profile| **Edit bio** |displays edited bio|


### License
*MIT LICENSE*
Copyright (c) 2022 **The_Dev_Planner**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.