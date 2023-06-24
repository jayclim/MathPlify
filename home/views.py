from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import ProblemForm
from .models import GeneratedProblem, Problem, User
import requests
import json
import google.generativeai as palm
from dotenv import load_dotenv
import os
load_dotenv()
palm.configure(api_key=os.environ.get('PALM_API'))

# text = "\text { Find the inverse of } f(x)=\frac{8-7 x}{6}"
# prompt = "You are a math assistant who is helping a student create more practice problems given a word problem. The word problem is: " + text + " The student wants to create a practice problem that is similar to the word problem that test the same ideas and concepts needed to solve the original problem. List 10 practice problems that are similar to the word problem and write them in a python list format."




# Create your views here.

def index(request):
    if request.method == 'POST' and request.user.is_authenticated:
        if request.POST.get('isImage') == 'true':
            form = ProblemForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    uploaded_img = form.save(commit=False)
                    uploaded_img.image_data = form.cleaned_data['image'].file.read()
                    uploaded_img.user = request.user
                    r = requests.post("https://api.mathpix.com/v3/text",
                        files={"file": uploaded_img.image_data},
                        data={
                        "options_json": json.dumps({
                            "math_inline_delimiters": ["\\(", "\\)"],
                            "rm_spaces": True,
                            "formats": ["text", "data", "html"],
                            
                        })
                        },
                        headers={
                            "app_id": os.environ.get('MATHPIX_APP'),
                            "app_key": os.environ.get('MATHPIX_API')
                        }
                    )
                    response = r.json()
                    latex = response['text']
                    uploaded_img.latex = latex
                    uploaded_img.save()
                    return JsonResponse({'success':True, 'extracted':latex, 'problem_id': uploaded_img.id}, safe=False)
                except Exception as e:
                    return JsonResponse({'success':False, 'extracted':"", 'error':e}, safe=False)
            else:
                return JsonResponse({'success':False, 'extracted':""}, safe=False)
        else:
            try:
                latex = repr(request.POST.get('latex'))
                completion = palm.generate_text(
                    model="models/text-bison-001",
                    prompt=get_prompt(latex),
                    temperature=0,
                    # The maximum length of the response
                    # max_output_tokens=2000,
                )
                response = completion.result
                # remove empty lines
                problems = [i.strip() for i in response.split('```') if len(i.strip()) > 0]
                for p in problems:
                    tmp = GeneratedProblem(problem=Problem.objects.get(id=request.POST['problem_id']), generated=p.strip())
                    tmp.save()
                return JsonResponse({'success':True, 'problems':problems}, safe=False)
            except Exception as e:
                tmp = GeneratedProblem(problem=Problem.objects.get(id=request.POST['problem_id']))
                return JsonResponse({'success':False, 'problems':"", 'error':e}, safe=False)

    else:
        form = ProblemForm()
        # Page from the theme 
        return render(request, 'pages/index.html', {
            'form': form,
            'nums': (User.objects.count(), Problem.objects.count(), GeneratedProblem.objects.count()),
        })
        
def problems(request):
    if request.user.is_authenticated:
        # tmp = []
        # for problem in Problem.objects.all():
        #     tmp.append((problem, problem.generated_problems))
            
        return render(request, 'pages/problems.html', {
            'problems': Problem.objects.all(),
        })
    return redirect('login')

def get_prompt(text):
    return "You are a math assistant who is helping a student create more practice problems given a LaTeX equation. The LaTeX equation is: " + text + " The student wants to create a practice problem that is similar to the original LaTeX equation that test the same ideas and concepts needed to solve the original problem. Problems should be formatted exactly the same as the original problem. All problems should have different numbers. List 10 practice problems that are similar to the original LaTeX equation and write each new problem in LaTeX format. Do not number each problem. Most importantly, seperate each problem with three backticks."