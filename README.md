# APIFuzz

APIFuzz is a API (java api/native api) fuzzing test tool based on dynamic binary instrumentation. ----> can found more issues than api interface fuzzing tool based on source code level,
it is based on real operation scenarios, multiple modules interact with each other (e.g. business logic) 

## Project Structure

Introduction of some files and directories

- `README.md`: basic information about APIFuzz
- `apk`: some demo apks
- `sample`: sample folder which including some samples file fuzzing test android java api / native api which are some test python and JavaScript scripts.
- `tool`: which involve some test assistance tool, eg, collect all class method running app, get function/method para.
- `pkg `:  which involve a APIFuzz source and wheel building scripts

## Instruction

### STEP 1:  Prepare for the Environment

install the fuzz demo apps in android device(real machine or android simulator)--->get from apk folder

install adb sdk tool on your test PC

install python3 env in your PC.

### STEP 2:  Build APIFuzz wheel package and install it.

git clone the your in your PC and open a command shell

Run:

```
cd pkg
python setup.py bdist_wheel
cd dist
pip install ApiFuzz-1.0.0-py3-none-any.whl
```

### STEP 3: Run the demo fuzzing test

open a command shell
Run:

```
cd sample
python Api_Fuzzing_01.py # running a android api fuzzing
python Api_Fuzzing_02.py # running a native api fuzzing

```
