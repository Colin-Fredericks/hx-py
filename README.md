# HX-PY: HarvardX Python Grading Library

This project collects the python grading functions that have been used in various HX courses and puts them all in one place so that they're easier to implement.

## Currently Working On...

Nothing in particular.

## How to Implement HXPY in your course

Put `python_lib.zip` in your Files & Uploads. Leave it zipped. Do _not_ unzip it first.

You should be able to call functions from that library as demonstrated in the XML_Example file, basically like this:

```
from python_lib import HXFileName

HXFileName.nameOfFunction(options, moreoptions)
```

## Currently Available Graders

```
HXGraders
  multiTextResponseGrader(ans, options) - for text-logging problems
  qualtricsSurveyGrader(ans, options) - for grading Qualtrics surveys
  textResponseGrader(ans, options) - for text-logging problems
  videoWatchGrader(ans, grading) - for video watch problems
  matchingAGrader(ans, right_answer, partial_credit, feedback) - for accessible matching problems
  rangeGuessGrader(ans, options) - for range guessing problems
  getRangeGuesserParams(options) - also for range guessing problems, just not the grader
```

## Currently Available Other Function

```
simpleFunctions
  returnTrue() - just to make sure things are working

JSBridge
  insertJavascript() - just to make sure things are working
  JSAlert() - it console.logs whatever you put into it. Just a proof-of-concept.
```

## Currently Available Tools

All other tools have been moved to the new [hx-util](https://github.com/Colin-Fredericks/hx-util) repository.
