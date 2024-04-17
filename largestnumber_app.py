import streamlit as stl

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def main():
    stl.title("Find the Largest Number")

    stl.write("Enter three numbers below:")

    num1 = stl.number_input("Enter the first number:", value=0)
    num2 = stl.number_input("Enter the second number:", value=0)
    num3 = stl.number_input("Enter the third number:", value=0)

    if stl.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        stl.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
