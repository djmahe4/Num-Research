import math
import matplotlib.pyplot as plt
import matplotlib
from datetime import date,timedelta
import datetime
from matplotlib import dates
import streamlit as st
import pandas as pd

def days_since_birth(date_of_birth):
    """Calculates the number of days since birth considering leap years"""
    today = date.today()
    # Extract year, month, day from the provided date of birth string
    year, month, day = map(int, date_of_birth.split("-"))

    # Create a date object representing the date of birth
    birth_date = date(year, month, day)

    # Calculate the difference between today and date of birth in days
    time_delta = today - birth_date
    return time_delta.days


def calculate_bhagyank(date_of_birth):
    """Calculates Bhagyank from date of birth"""
    year, month, day = map(int, date_of_birth.split("-"))
    sum = 0
    for i in str(day):
        sum = sum + int(i)
    if sum > 9:
        sum1 = 0
        for i in str(sum):
            sum1 = sum1 + int(i)
        sum = sum1
    for i in str(month):
        sum = sum + int(i)
    if sum > 9:
        sum2 = 0
        for i in str(sum):
            sum2 = sum2 + int(i)
        sum = sum2
    for i in str(year):
        sum = sum + int(i)
    if sum > 9:
        sum3 = 0
        for i in str(sum):
            sum3 = sum3 + int(i)
        sum = sum3
    if sum > 9:
        sum4 = 0
        for i in str(sum):
            sum4 = sum4 + int(i)
        sum = sum4
    return sum
    # return (day + month + (year % 100) + (year // 100)) % 9 + 1  # Ensure Bhagyank is 1-9


def calculate_naamank(name):
    aldict = {'a': 1, 'j': 1, 's': 1, 'b': 2, 'k': 2, 't': 2, 'c': 3, 'l': 3, 'u': 3, 'd': 4, 'm': 4, 'v': 4, 'e': 5, 'n': 5, 'w': 5, 'f': 6, 'o': 6, 'x': 6, 'g': 7, 'p': 7, 'y': 7, 'h': 8, 'q': 8, 'z': 8, 'i': 9, 'r': 9}
    """Calculates Naamank (sum of numerological letter values)"""
    name_sum = 0
    for letter in name.lower().strip():
        if letter != " ":
            number = aldict.get(letter, 0)  # Initialize number with 0 if letter not found
            name_sum += number

    while name_sum > 9:
        sum_digits = 0
        for digit in str(name_sum):
            sum_digits += int(digit)
        name_sum = sum_digits
    if name_sum +3>9:
      name_sum=name_sum-3
    else:
      name_sum=name_sum+3
    return name_sum
def calculate_moolank(date_of_birth):
  """Calculates Moolank from date of birth"""
  year, month, day = map(int, date_of_birth.split("-"))
  sum=0
  for i in str(day):
    sum=sum+int(i)
  if sum>9:
      sum1 = 0
      for i in str(sum):
          sum1 = sum1 + int(i)
      sum=sum1
  #return sum
  return sum

def combine_numbers( moolank,bhagyank, naamank):
    """Combines Moolank, Bhagyank, and Naamank with Fibonacci offset (not scientific)"""
    #combined = (moolank * 3 + bhagyank * 2 + normalized_naamank)  # / 6
    combined= moolank+(bhagyank*naamank)
    print('{}*{}+{}={}'.format(bhagyank, naamank, moolank, combined))
    typ=-9.81
    if combined<=9:
        combined = bhagyank * naamank
        print("Alternate {}*{}={}".format(bhagyank,naamank,combined))
        typ=+9.81
    return combined ,typ#if moolank> else ValueError # - fibonacci_offset, fibonacci_sequence

def combine_numbers2( moolank,bhagyank, naamank,st):
    """Combines Moolank, Bhagyank, and Naamank with Fibonacci offset (not scientific)"""
    #combined = (moolank * 3 + bhagyank * 2 + normalized_naamank)  # / 6
    #combined= moolank+(bhagyank*naamank)
    combined = bhagyank + (moolank * naamank)
    #print('{}*{}+{}={}'.format(bhagyank, naamank, moolank, combined))
    print('{}+({}*{})={}'.format(bhagyank, moolank,naamank, combined))
    st.write('{}+({}*{})={}'.format(bhagyank, moolank,naamank, combined))
    typ= +9.81
    #if combined<=9:
            #combined = bhagyank * naamank
            #print("Alternate {}*{}={}".format(bhagyank,naamank,combined))
        #combined = moolank + (bhagyank * naamank)
        #print('{}*{}+{}={}'.format(bhagyank, naamank, moolank, combined))
        #typ= -9.81
    return combined ,typ


def biorhythm_chart(days, combined):
    """Generates biorhythm chart using Fibonacci sequences (not scientific)"""
    biorhythm_data = []
    # for cycle, factor in zip(cycles, fibonacci_scaling_factors):
    # fibonacci_values = [f * factor for f in fibonacci_sequence[:cycle]]
    biorhythm_data.append([math.sin(2 * math.pi * i / combined) for i in range(days - 15, days + 15)])

    return biorhythm_data[0]


def plot_biorhythm_chart(combined_points, dates,st, cycle_label="Combined"):
  """Plots the biorhythm chart with dates using matplotlib.pyplot."""

  if len(combined_points) != len(dates):
    raise ValueError("Combined points and dates lists must have the same length.")
  #fig,ax=plt.subplots()
  fig=plt.figure(figsize=(10, 6))
  plt.plot(combined_points, label=cycle_label)

  # Customize x-axis labels with numbers (optional)
  plt.xticks(range(len(combined_points)))  # Use data point indices

  # Add dates below the x-axis (optional, adjust spacing as needed)
  plt.xticks(range(len(combined_points)), [d for d in dates], rotation=45, ha='right', va='bottom', fontsize=8)

  plt.xlabel("Day")  # Adjust label if needed
  plt.ylabel("Biorhythm Level")
  plt.title("Biorhythm Chart (not scientific)")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()  # Adjust spacing to avoid overlapping labels
  #plt.show()
  st.pyplot(fig)
def get_date_range(days_before=15, days_after=14):
  """
  Finds today's date and a range of dates before and after in dd-mm-yyyy format.

  Args:
      days_before (int, optional): Number of days before today (default: 15).
      days_after (int, optional): Number of days after today (default: 14).

  Returns:
      list: A list of strings representing the dates in dd-mm-yyyy format.
  """
  today = date.today()
  date_range = []

  # Add date 15 days before today
  #date_range.append(today - timedelta(days=days_before))
  for i in range(-15, days_after +1):
    date_range.append(today - timedelta(days=i))
  formatted_dates = [date.strftime("%d-%m-%Y") for date in date_range]

  return formatted_dates

# Get the date range
date_list = get_date_range()

st.title("Numerology app!")
#while True:
name = st.text_input("Enter name: ",key=1)
    #if name!="":
        #break
#while True:
date_of_birth = st.text_input("Enter date of birth (YYYY-MM-DD): ",key=2)
pts=st.radio("Previous match points?",['Yes','No'])
    #if date_of_birth!="":
        #break
if st.button("Run Prediction"):
# Get user input
    # Calculate Moolank, Bhagyank, and Naamank

    bhagyank = calculate_bhagyank(date_of_birth)
    moolank = calculate_moolank(date_of_birth)
    naamank = calculate_naamank(name)

    print(f"Bhagyank: {bhagyank}")
    print(f"Naamank: {naamank}")
    print("Moolank:",moolank)
    st.write(f"Bhagyank: {bhagyank}")
    st.write(f"Naamank: {naamank}")
    st.write("Moolank:",moolank)

    # Biorhythm chart parameters (adjust as needed)
    # cycles = [23, 28, 33]  # Physical,
    comb,typ = combine_numbers2( moolank,bhagyank, naamank,st)
    days = days_since_birth(date_of_birth)
    bio = biorhythm_chart(days, comb)
    #print(bio)
    print("-"*58)
    st.write("-"*58)
    today = datetime.date.today()
    st.write("Today        =", today.strftime("%d%b%Y"))
    st.write("Age in days  =", days)
    st.write("-"*58)
    print("-"*58)
    di={}
    for i,date in enumerate(date_list):
        di.update({date:bio[i]})
    #print(di)
    # Print table header
    print("Date \t\t|\t\tValue")
    print("-" * 30)  # Separator line

    # Loop through the dictionary and print each date-value pair
    for date, value in di.items():
      print(f"{date} \t|\t {value:.4f}")
    new=pd.DataFrame(di.items(),columns=["Date","Values"])
    st.table(new)
    #plot_biorhythm_chart(bio, date_list)
    ck=15 #ck should be set to 15 by default
    #if st.button("Continue?"):

    if pts=='Yes':
        try:
            prev = st.text_input("Enter points:",key=3)
            if prev!="":
                print(f"{bio[ck]:.4f}")
                print(f"Predicted points:{int((bio[ck]*typ)+prev)}")
        except ValueError:
            print(f"{bio[ck]:.4f}")
            print(f"x+ points:{int(bio[ck] * typ)}")
    if bio[ck-1]==bio[ck+1]:
        st.write("Warning!! Prediction may fail!")
    #if st.button("Continue"):
    #print(bio)
    ls=[abs(round(ele,4)) for ele in bio[:-(ck+1):-1]]
    print(ls)
    mx=max(ls)
    ln=0
    found=False
    while ln < len(ls):
        last = ls[ln]
        try:
            if ls[ln - 1] == mx and ln>=0:
                found = True
                #ln += 1
                #continue
            elif ls[ln + 1] == mx:
                found = True
                #ln += 2
                #continue
                ln+=1
        except IndexError:
            print("Passed {}".format(ls[ln]))
            st.write("Passed {}".format(ls[ln]))
            #pass
        if ls[ln]==mx:
            found=True
            #ln+=1
            #continue
        if found:
            print(ls[ln])
            ln = ln + 2
        else:
            print("Not found {}".format(ls[ln]))
            st.write("Not found {}".format(ls[ln]))
            ln = ln + 1

    if last == ls[-1]:
        print("Great..")
        st.write("Great..")
    else:
        print("Flop :(")
        st.write("Flop :(")
    for i in ls[-4:]:
        if ls[-4:].count(i)>1:
            print("Pipe!")
            st.write("Pipe!")
            break
    plot_biorhythm_chart(list(di.values()), list(di.keys()),st)
#if st.button("Rerun.."):
    #st.rerun()
