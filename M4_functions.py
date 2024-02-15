# nested dictionaries
# 2/1/24
# CSC121 M4Pro
# Jahan p

'''FUNCTIONS '''
def display_content(student_list):
    '''pass list and print each item in the list (Key and value) '''
    #iterate through list 
    for item in student_list:
        #iterate through nested dictionary
            for key in item:
                print(key,":", item[key])
                #print items in the courses list
            print()
            print()


def display_menu():
    print("1)Display student registry")
    print("2) Dislay course roster") #display all students in a certain class
    print("3) Display student based on major")
    print("4) Display student by on ID")
    print("5) Exit the program")


#Display all students first and last name attched to a specific course 
def display_roster (student_list, course_class):
    #create an empty list to hold students
        SIC = []
        for item in student_list:
            for course in (item["courses"]): #this is a list
                if course ==course_class:
                    SIC.append(item["firstName"]+ " " + item["lastName"])
        return SIC

def getMajor(student_list, major):
    my_list = []
    for student in student_list: #student is a dictionary
        this_major = student["major"]
        if this_major == major:
            my_list.append(student["firstName"] + " " + student["lastName"])
    return my_list


def getID(student_list,stuID ):
    stuID_list = []
    for student in student_list: #student is a dictionary
        this_stuID = student["stuID"]
        if this_stuID == stuID:
            stuID_list.append(student["firstName"] + " " + student["lastName"])
    return stuID_list


def getStudentReg():
    students = [ {"stuID":"1201", 'firstName':'Sarah', 'lastName':'Spadling', 'major':'Programming', 'courses':["MAT143-Math","ENG111-English","CIS115-Intro to Programming","CSC121-Python"]},

               {"stuID":"1202", 'firstName':'James', 'lastName':'Spalding', 'major':'Psychology', 'courses':["MAT243-Math","ENG211-English","PSY101-Intro to Psychology","ETH101-Intro to Ethics"]},

               {"stuID":"1203", 'firstName':'John', 'lastName':'Spalding', 'major':'Programming', 'courses':["MAT143-Math","ENG111-English","CIS115-Intro to Programming","CSC121-Python"]},

               {"stuID":"1204", 'firstName':'Rayliee', 'lastName':'Craston', 'major':'Biology', 'courses':["MAT143-Math","ENG111-English","BIO101-Intro to Biology","ICE101-Ice Skating"]},

               {"stuID":"1205", 'firstName':'Carter', 'lastName':'Craston', 'major':'Chemistry', 'courses':["MAT343-Math","ENG211-English","ETH101-Intro to Ethics","HIS201-American History"]},

               {"stuID":"1206", 'firstName':'Brodiey', 'lastName':'Craston', 'major':'Physics', 'courses':["MAT143-Math","ENG111-English","PHY101-Intro to Physics","ICE101-Ice Skating"]},

               {"stuID":"1207", 'firstName':'Caera', 'lastName':'Mikkelsen', 'major':'Art History', 'courses':["MAT243-Math","ENG211-English","HIS168-Religious History","HIS190-Intro to Art History"]},

               {"stuID":"1208", 'firstName':'Sophiah', 'lastName':'Mikkelsen', 'major':'Economics', 'courses':["MAT143-Math","ENG111-English","ETH101-Intro to Ethics","BUS121-Market Basics"]},

               {"stuID":"1209", 'firstName':'Scott', 'lastName':'Scott', 'major':'Programming', 'courses':["MAT143-Math","ENG111-English","CIS115-Intro to Programming","CSC121-Python"]},

               {"stuID":"1301", 'firstName':'Sean', 'lastName':'Lean', 'major':'Education', 'courses':["MAT343-Math","ENG311-English","ETH101-Intro to Ethics","EDU201-Adolescent Education"]},

               {"stuID":"1302", 'firstName':'Emily', 'lastName':'Mikkelsen', 'major':'Graphic Design', 'courses':["ART320-Botanical Design","ASB353-Death and Dying","GRA323-Technology for Design","GRA345-Design Rhetoric"]},

               {"stuID":"1303", 'firstName':'Porter', 'lastName':'Parker', 'major':'Psychology', 'courses':["MAT143-Math","ENG111-English","PSY101-Intro to Psychology","ETH101-Intro to Ethics"]},

               {"stuID":"1304", 'firstName':'Crete', 'lastName':'Crate', 'major':'Occult Studies', 'courses':["MAT143-Math","ENG111-English","ETH101-Intro to Ethics","HIS168-Religious History"]},

               {"stuID":"1305", 'firstName':'Parker', 'lastName':'Peter', 'major':'Education', 'courses':["MAT243-Math","ENG211-English","ETH101-Intro to Ethics","EDU201-Adolescent Education"]},

               {"stuID":"1306", 'firstName':'Orhum', 'lastName':'Sorhum', 'major':'Programming', 'courses':["MAT343-Math","ENG211-English","CIS215-Advanced Programming","CSC221-Advanced Python"]},

               {"stuID":"1307", 'firstName':'Durham', 'lastName':'Sorhum', 'major':'Culinary Arts', 'courses':["MAT143-Math","ENG211-English","CUL201-Sous Basics","CUL221-Kitchen Cleaning"]},

               {"stuID":"1308", 'firstName':'Werhum', 'lastName':'Sorhum', 'major':'Business', 'courses':["MAT243-Math","ENG211-English","ETH101-Intro to Ethics","BUS221-Market Practices"]},

               {"stuID":"1309", 'firstName':'Merhum', 'lastName':'Sorhum', 'major':'Politics', 'courses':["MAT243-Math","ENG211-English","ETH101-Intro to Ethics","HIS201-American History"]},

               {"stuID":"1401", 'firstName':'Lerhum', 'lastName':'Sorhum', 'major':'Programming', 'courses':["MAT243-Math","ENG211-English","CIS215-Advanced Programming","CSC221-Advanced Python"]},

               {"stuID":"1402", 'firstName':'Seurem', 'lastName':'Sorhum', 'major':'Engineering', 'courses':["MAT343-Math","ENG211-English","ETH101-Intro to Ethics","EGI321-Mechanical Engineering"]}
               ]
    return students
