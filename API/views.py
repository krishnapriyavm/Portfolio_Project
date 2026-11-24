from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse


# Create your views here.

class AboutView(View):
    def get(self, request):
        data = {
            "ID" : 1,
            "Full Name" : "Krishnapriya V M",
            "Professional Title" : "Python Django React Fullstack intern",
            "Bio" : "A passionate developer building scalable applications",
            "Date of Birth" : "02/07/2005",
            "Email" : "krishnapriyavm8@gmail.com",
            "Contact Number" : 9778123485,
            "Location" : "Kothamangalam",
            "GitHub URL" : "https://github.com/krishnapriyavm",
            "LinkedIn URL" : "https://linkedin.com/krishnapriyavm"
        }
        return JsonResponse(data)
    
class EducationView(View):
    def get(self, request):
        data = {
            "ID" : 1,
            "Institution" : "Luminar",
            "Course" : "Python fullstack",
            "University" : "MGU",
            "Location" : "Kochi",
            "Starting Year" : "August 2026",
            "Ending Year" : "January 2027",
            "CGPA" : 7.5,
            "Description" : "Completed python full stack development"
        }
        return JsonResponse(data)
class ProjectsView(View):
    def get(self, request):
        data = [
            {
            "ID" : 1,
            "Project Title" : "Elora",
            "Short Description" : "Plant shopping system",
            "Long Description" : "Plant shopping system where anyone can sell and buy plants",
            "Technologies used" : ["PHP", "MySQL", "HTML", "CSS", "JavaSript"],
            "Live URL" : "https://project.elora.com",
            "GitHUb URL" : "https://github.com/krishnapriyavm",
            "Featured Status" : True
        },
            {
            "ID" : 2,
            "Project Title" : "COHUB",
            "Short Description" : "Hostel room allocation system",
            "Long Description" : "Hostel room allocation system with AI matching roommate compatibility",
            "Technologies used" : ["Python Django", "SqlLite", "HTML", "CSS", "JavaScript"],
            "Live URL" : "https://project.cohub.com",
            "GitHUb URL" : "https://github.com/krishnapriyavm",
            "Featured Status" : True
        }
            ]
        
        return JsonResponse(data, safe=False)
    
# In order to allow non-dict objects to be serialized set the safe parameter to False.

class SkillsView(View):
    def get(self, request):
        data = [
            {
                "ID": 1,
                "Skill Name": "Python",
                "Category": "Programming Language",
                "Proficiency Level": "Beginner",
                "Years of Experience": 2
            },
            {
                "ID": 2,
                "Skill Name": "Django",
                "Category": "Backend",
                "Proficiency Level": "Beginner",
                "Years of Experience": 1
            },
            {
                "ID": 3,
                "Skill Name": "React",
                "Category": "Frontend",
                "Proficiency Level": "Intermediate",
                "Years of Experience": 1
            }
        ]

        return JsonResponse(data, safe=False)