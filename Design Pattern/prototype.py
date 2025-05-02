# Goal:
# You want to clone an object instead of creating it from scratch every time.
# Use Case:
# Imagine you're building a resume builder. Creating a resume from scratch each time is costly. So you keep a prototype resume and clone it when needed.

import copy

class Resume:
    def __init__(self, name, experience, skills):
        self.name = name
        self.experience = experience
        self.skills = skills

    def show_resume(self):
        print(f"Name : {self.name}")
        print(f"Total experience : {self.experience}")
        print(f"Skills : {self.skills}")

    def clone(self):
        return copy.deepcopy(self)
    

my_resume = Resume("Manish", "2 Years", ["python", "Django", "Postgresql", "javascript", "node.js"])
my_resume.show_resume()

mukesh = my_resume.clone()
mukesh.name = "mukesh"
mukesh.skills.append("Dockrik")
mukesh.experience = "1 years"
mukesh.show_resume()        
