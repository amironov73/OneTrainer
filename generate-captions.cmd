@echo off

if L%1L == LL exit

rem venv\Scripts\accelerate.exe launch scripts\generate_captions.py --model WD14_VIT_2  --include-subdirectories --sample-dir %1
rem venv\Scripts\accelerate.exe launch scripts\generate_captions.py --model BLIP  --include-subdirectories --sample-dir %1
venv\Scripts\accelerate.exe launch scripts\generate_captions.py --model BLIP2  --include-subdirectories --sample-dir %1
