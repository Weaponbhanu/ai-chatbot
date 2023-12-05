import re    
import random   

class rulebot():
    
    negative_responses=("no", "nope", "nah", "naw", "not a chance", "sorry")

    exit_commands=("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions=("How can I assist you?",
                      "What can i do for you?",
                      "How can I help?",
                      "I am because of you.Tell me your matter?",
                      "May I know your area of concern.PLease!"
                      
                       )                               

    def _init_(self): 
         self.alienbabble= { "resume_building_intent": r".*\s*resume",     #keywords to quick response
                             "answer_why_hire_intent": r".\s*hire\s*",
                             "about_yourself": r".\s*yourself\s*",
                             "packages": r".\s*packages\s*",
                             "eligibility": r".\s*eligibility\s*",
                             "Interview_tips_intent":r".\s*interview\s*",
                             "Internship_intent":r".\s*internship\s*",
                             "students_CGPA_intent":r".\s*CGPA\s*",
                             "staff_recruitment_intent":r".\s*staff recruitment\s*",
                             "staff_salary_intent:":r".\s*salary *\s",
                             "current_vacany_intent":r".\s*vacancy\s*",
                          } 
    def greet(self):     #greeting the guest
        print("Welcome to DAV University")
        self.name=input("what is  your name?\n")
        will_help=input(
            f"hi {self.name},i am rule bot")
        if will_help  in self.negative_responses:
           print("FEEDBACK! are important for RULEBOT growth..(type \"Quit!\" if you dont want to")
           feedback=input("Write here plz")
           if feedback=="Quit":
              print("ok,Have a great earth day!")
           else: 
               print("Bie,to see you again")
        return 
        self.name1=input("who are you? student/recruiter/staff\n")
        will_help1=input("My pleasure to have you here")
        if will_help1  in self.negative_responses:
            print("FEEDBACK! are important for RULEBOT growth..(type \"Quit!\" if you dont want to")
            feedback=input("Write here plz")
            if feedback=="Quit":
               print("ok,Have a great earth day!")
            else: 
                print("Bie,to see you again")
           
        return 
        self.chat()
        
    def make_exit(self,reply): # to exit the RULEBOT based on negative responses 
        for command in self.exit_commands:
            if reply==command:
                print("FEEDBACK! are important for RULEBOT growth..(type \"Quit!\" if you dont want to")
                feedback=input("Write here plz")
                if feedback=="Quit":
                   print("ok,Have a great earth day!")
                else: 
                    print("Bie,to see you again")
                
            return True
    def chat(self):  # defining the chat function
        reply=input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply=input(self.match_reply(reply)) #calling match_reply function
  
               
    def match_reply(self, reply):   # to collect the right response by matching intent from dictationary defined above
           for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match=re.match(regex_pattern, reply)
            if found_match and intent=="resume_building_intent":
                return self.resume_building_intent()
            elif found_match and intent=="answer_why_hire_intent":
                return self.answer_why_hire_intent()
            elif found_match and intent=="about_yourself":
               return self.about_yourself()
            elif found_match and intent=="packages":
               return self.packages()
            elif found_match and intent=="eligibility":
              return self.eligibility()
            elif found_match and intent=="Interview_tips_intent":
               return self.Interview_tips_intent()
            elif found_match and intent=="Internship_intent":
               return self.Internship_intent()
            elif found_match and intent=="students_CGPA_intent":
               return self.students_CGPA_intent()
            elif found_match and intent=="staff_recruitment_intent":
              return self.staff_recruitment_intent()
            elif found_match and intent=="staff_salary_intent":
             return self.staff_salary_intent()
            elif found_match and intent=="current_vacany_intent":
              return self.current_vacany_intent()
            if not found_match :
             return self.no_match_intent()
 # defining the intent functions        
    def resume_building_intent(self):
       responses=( """You can use this criteria:
                      1.Review the job description
                      2.Select a formatt
                      3.Add your contact information
                      4.Include your professional summary
                      5.Provide relevant work experience
                      6.Include your educational background
                      7.Highlight your skills""")
       return (responses) 
    def answer_why_hire_intent(self):
      print("You can use this from my side")
      responses= ("""I should be hired for this role because of my relevant skills,
                  experience, and passion for the industry.
                  I've researched the company and can add value to its growth.
                  My positive attitude, work ethics, and long-term goals align with the job requirements, making me a committed and valuable asset to the company./n""",
                 """ You should hire me because I have the qualifications, experience, and attitude to contribute to your company. 
                 I am a quick learner, adaptable, and possess excellent communication and problem-solving skills.
                 Furthermore, I am passionate about this field and eager to contribute to your team's success/n""",
                
      return random.choice(responses)
    def about_yourself(self):
        print("Tell me about yourself. You’ll hear these four fairly unassuming words at the beginning of almost any job interview. So,here are some tips for you")
        responses=("""Hey [recruiter name],My name’s [name]. I completed my [qualifying course or training] in [year] and have [x] years of experience working as [relevant position]. While working for [previous company’s name],
                 I developed [soft and hard skills], which I think will apply well to this role.
                   I’ve also been hoping to work on my [ambitions], and I know I’d get the opportunity to do so at [this company] since you value [insert value]. 
                   I look forward to telling you more about my qualifications throughout this call and thank you in advance for your time.\n""",
                
        return random.choice(responses)
    def packages(self):
        responses=("""Average MNC Group fresher salary in India is ₹2.8 Lakhs for less than 1 year of experience. 
                   fresher salary at MNC Group India ranges between ₹2.3 Lakhs to ₹5.3 Lakhs. 
                   According to our estimates it is 10% less than the average fresher Salary in Investment Banking / Venture Capital / Private Equity Companies.\n""",
                   
            )
        return responses
    def eligibility(self):
        responses=("""a majority of companies require a minimum 60 per cent aggregate, 
                   a few companies accept 50 per cent aggregate also in class 10th and 12th, depending on the job role and overall profile of the candidate\n"""
            )
        return (responses)
    def Interview_tips_intent(self):
         print("I got you Buddy! Here are some tips for you")
         responses=("""1.Be prepared: Research the company and practice your answers. 
                       2.Be on time: Try to arrive 10–15 minutes early. 
                       3.Dress professionally: Dress for the job or company. 
                       4.Be polite: Greet the interviewer with a handshake and a smile. 
                       5.Be confident: Be positive and authentic. 
                       6.Be a good listener: Don't talk too much. 
                       7.Ask questions: Have some prepared and ask relevant questions. 
                       8.Make a good impression: Leave a positive first impression. 
                       9.Thank the interviewer: Thank them for their time\n""")
         return (responses)
  
        return responses
    def no_match_intent(self):
       responses =("Please tell me more.\n", "Tell me morel\n", "Why do you say that?\n", 
                   "I see. Can you elaborate?\n", 
                   "Interesting. Can you tell me more?\n",
                   "I see. How do you think?\n", "Why?\n",
                   "How do you think I feel when you say that?\n")
       return random.choice(responses)      
   
alienbot=rulebot()   #creating of instances
alienbot.greet()     #calling the function