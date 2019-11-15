"""
os 모듈의 변수와 함수들
"""
import os

# CWD: Current Working Directory(현재 작업 디렉토리/폴더)
print(os.getcwd())

# 절대 경로(absolute path):
#  시스템의 루트(root)부터 전체 디렉토리 경로를 표시하는 방법
#  C:\dev\lab-python\lec07_file (Windows)
#  /Users/user/Documents (MacOS 또는 Linux)
# 상대 경로(relative path):
#  현재 작업 디렉토리(cwd)를 기준으로 경로를 표시하는 방법
#  .(현재 디렉토리), ..(상위 디렉토리)
#  ..\lec06_class\inheritance01.py
#  C:\dev\lab-python\lec06_class\inheritance01.py
