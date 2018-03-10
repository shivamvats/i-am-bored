# i-am-bored
Mantra: *Keep it simple.*

Set up a list of goals divided into small bite-sized portions that you want to achieve. Whenever you are bored `i-am-bored` will give you one of those bits to do.

## Setup
* Run
```
ln -s /path/to/i-am-bored.py /path/to/bin
chmod +x i-am-bored.py
```

## Usage

`i-am-bored` - Runs one of the available routines randomly.  
`i-am-bored list` - Print the list of available routines.  
`i-am-bored run 1` - Run a specific routine.  

## Current Status
*  `i-am-bored` command can be typed and used from anywhere.
* Currenly a few routines including coding questions and interesting blogs are
  available. Every time you type `i-am-bored` one of these tasks is randomly
chosen and opened for you.

## To do
* Set up infrastructure to divide a big task into chunks.
* Some way to track and update progress.
* Progress tracking can be integrated with routinizer so that both are updated
  with progress on tasks.
* Improve command-line use- add options to view available tasks and choose one
  of them.
* Review the code- make it more extensible and easy to update.
