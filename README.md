# APIFuzz

APIFuzz is a API (java api/native api) fuzzing test tool based on dynamic binary instrumentation. 

## Project Structure

Introduction of some files and directories

- `README.md`: basic information about APIFuzz
- `Api_Fuzzing_01.py`: the api fuzzing demo example
- `sample`: sample folder which including a api fuzzing test demp apk and fuzzing test python and JavaScript scripts.
- `tool`: which involve some test assistance tool, eg, collect all class method running app 
- `pkg `:  which involve a APIFuzz source and wheel building scripts

## Instruction

### STEP 1:  Prepare for the Environment

install the fuzz demo app in android device(real machine or android simulator)

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
python Api_Fuzzing_01.py

```
