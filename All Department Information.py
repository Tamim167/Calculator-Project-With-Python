#Project no-2
#Made By TAMIM
print("Welcome To My New Project ")
name=(input("Enter Your Name :"))
roll=int(input("Enter Your Roll Here :"))
print("Welcome To My Project :",name)
a=(input("Press Enter To  Start :"))
Computer=("Computer science is the study of computers and computational systems. It is a broad field which includes everything from the algorithms that make up software to how software interacts with hardware to how well software is developed and designed. Computer scientists use various mathematical algorithms, coding procedures, and their expert programming skills to study computer processes and develop new software and systems.")
Civil=("Civil engineering is the professional practice of designing and developing infrastructure projects. This can be on a huge scale, such as the development of nationwide transport systems or water supply networks, or on a smaller scale, such as the development of individual roads or buildings.")
Electrical=("Electrical engineering is an engineering discipline concerned with the study, design, and application of equipment, devices, and systems which use electricity, electronics, and electromagnetism.")
Mechanical=("Mechanical engineering is the study of physical machines that may involve force and movement. It is an engineering branch that combines engineering physics and mathematics principles with materials science, to design, analyze, manufacture, and maintain mechanical systems.")
Textile=("Textile engineering is an area of engineering that uses scientific and engineering principles to produce or improve textile products, such as apparel, upholstery or materials for medical devices.")
Marine=("Marine Engineering is the discipline that deals with matters related to the design, innovation, construction and maintenance of seagoing vessels and navigation equipment. Marine Engineering focuses primarily on the development and production of internal systems of boats, ships, or submarines.")
Architectural=("Architectural engineering or architecture engineering, also known as building engineering, is an engineering discipline that deals with the engineering systems - such as structural, mechanical, electrical, lighting, environmental, climate control, telecommunications, security, and other technologies used in buildings.")
print("Press 1 For Computer Science And Engineering Information.  \nPrees 2 For Civil Technology Information. \nPress 3 For Electrical Engineering Information. \nPress 4 For Mechanical Engineering Information. \nPress 5 For  Textile Engineering Information. \nPress 6 For Marine Engineering Information. \nPress 7 For Architectural Engineering Information. ")
choice=int(input("Enter your choice from= 1-7 :"))

if choice ==1:
    print("Computer Science And Engineering :")
    print(Computer)
    print("Thanks For Reading")
elif choice ==2:
    print("Civil Technology :")
    print(Civil)
elif choice ==3:
    print("Electrical Engineering :")
    print(Electrical)
    print("Thanks For Reading")
elif choice ==4:
    print("Mechanical Engineering :")
    print(Mechanical)
    print("Thanks For Reading")
elif choice ==5:
    print("Textile Engineering :",)
    print(Textile)
    print("Thanks For Reading")
    print
elif choice ==6:
    print("Marine Engineering :")
    print(Marine)
    print("Thanks For Reading")
elif choice ==7:
    print("Architectural Engineering :")
    print(Architectural)
    print("Thanks For Reading")
else:
    print("Invalid choice")
    print("Try Again")
    
