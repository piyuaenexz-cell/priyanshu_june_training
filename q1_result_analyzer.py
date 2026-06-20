def analyze_result(name, roll, marks):
   
    total = sum(marks)
    average = total / 5
    
   
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
        
    print("Student: " + name )
    print("Roll: " + str(roll) )
    print("Total: " + str(round(total, 1)))
    print("Average: " + str(round(average, 1)))
    print("grade: " + grade)
    
    # subjects below 40
    failed_subs = []
    index = 1  
    for score in marks:
      if score < 40:
         failed_subs.append("Subject " + str(index))
      index += 1  

            
    # Print the failing subjects row
    if failed_subs:
      print("Subjects below 40:", end=" ")
      for sub in failed_subs:
        print(sub, end=" ")
      print() 

# Getting student profile details
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

# Getting marks using a list

marks = [float(x) for x in input("Enter 5 subject marks separated by spaces: ").split()]

# --- Execute Function ---
analyze_result(name, roll, marks)
