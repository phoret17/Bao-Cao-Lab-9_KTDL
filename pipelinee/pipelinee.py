import sys
import os

def run_ex1():
    os.system("python Excercise-1/main.py")

def run_ex2():
    os.system("python Excercise-2/main.py")

def run_ex3():
    os.system("python Excercise-3_cách2/main.py")  # hoặc cách_2 nếu bạn dùng cách đó

def run_ex4():
    os.system("python Excercise-4/main.py")

def run_ex5():
    os.system("python Excercise-5/main.py")

if __name__ == "__main__":
    print("🏁 Running Full Pipeline")
    run_ex1()
    run_ex2()
    run_ex3()
    run_ex4()
    run_ex5()
    print("✅ All done!")
