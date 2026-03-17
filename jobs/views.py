from django.shortcuts import render, redirect
from .models import Job
from .agent import analyze_job

def home(request):
    """
    Main dashboard showing analyzed jobs.
    """
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def analyze_job_view(request):
    """
    View to handle job description submission and AI analysis.
    """
    if request.method == 'POST':
        description = request.POST.get('description')
        user_skills = request.POST.get('user_skills')
        
        # Analyze using the AI agent
        try:
            analysis = analyze_job(description, user_skills)
            
            # Create a job entry with dummy metadata for the demo
            # In a real app, you'd scrape title/company from the description or URL
            job = Job.objects.create(
                title=request.POST.get('title', 'Analyzed Job'),
                company=request.POST.get('company', 'Unknown Company'),
                description=description,
                url=request.POST.get('url', 'http://example.com'),
                ai_summary=analysis['summary'],
                match_score=analysis['match_score'],
                skills_found=analysis['skills_found']
            )
            return redirect('home')
        except Exception as e:
            # Handle API errors or parsing issues
            return render(request, 'jobs/analyze.html', {'error': str(e)})
            
    return render(request, 'jobs/analyze.html')
